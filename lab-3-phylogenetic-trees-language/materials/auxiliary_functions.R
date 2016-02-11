# Auxiliary functions

# library for sets
library(sets)

# alpabet
alphabet <- c("A","G","U","C")

# target matrices if fixed target is used
target_R <- matrix(c(1,0,0,0,1,0,0,0,1),3,3)
target_S <- matrix(c(1,0,0,0,1,0,0,0,1),3,3)
target_agent = list(R=target_R, S=target_S)

CAC_count <- function(population) {
    # fitness function based on number of
    # occurences of substring CAC
    fitness <- rep(0,population_size)
    for (i in 1:population_size) {
        population_member <- paste(population[i,], collapse='')
        fitness[i] <- str_count(population_member, "CAC")
    }
    return(fitness)
}

communication_fixed_target <- function(population) {
    # get S and R matrices
    population_matrices <- get_population_matrices(population)

    # compute fitness
    fitness <- sapply(population_matrices, FUN=compute_success, agent2=target_agent)

    return(fitness)
}

communication_random_target <- function(population) {
    # get S and R matrices
    population_matrices <- get_population_matrices(population)

    population_size = dim(population)[1]
    fitness <- rep(0, population_size)
    for (i in 1:population_size) {
        random_agent <- sample(population_matrices, size=1)[[1]]
        fitness[i] <- compute_success(population_matrices[[i]], random_agent)
    }

    return(fitness)
}

sending_random_target <- function(population) {
    # get S and R matrices
    population_matrices <- get_population_matrices(population)

    population_size = dim(population)[1]
    fitness <- rep(0, population_size)
    for (i in 1:population_size) {
        random_agent <- sample(population_matrices, size=1)[[1]]
        fitness[i] <- compute_receiving_success(population_matrices[[i]], random_agent)
    }

    return(fitness)
}

compute_success <- function(agent1, agent2) {
    # agents are characterized by a list
    # containing S and R matrix
    product <- agent1$S %*% agent2$R + agent1$S %*% agent2$R
    fitness <- sum(diag(product))
    return(fitness)
}

compute_receiving_success <- function(agent1, agent2) {
    # agents are characterized by a list
    # containing S and R matrix
    product <- agent1$S %*% agent2$R
    fitness <- sum(diag(product))
    return(fitness)
}

get_population_matrices <- function(population) {
    # generate a list of S and R matrices
    # corresponding to the population's genomes
    # matrices = sapply(population_matrices, FUN=get_matrix)
    matrices <- list()
    for (i in 1:dim(population)[1]) {
        matrices[[i]] <- get_matrix(population[i,])
    }

    return(matrices)
}

get_matrix <- function(genome) {
    # generate S and R matrix for genome
    
    # replace A, G, C and U by 3, 2, 1 and 0
    genome[genome=="A"] = 3; genome[genome=="G"] = 2;
    genome[genome=="C"] = 1; genome[genome=="U"] = 0;
    genome <- as.numeric(genome)

    # create two matrices
    S <- normalise(matrix(genome[1:9],3,3))
    R <- normalise(matrix(genome[10:18],3,3))

    comm_system <- list(S=S, R=R)

    return(comm_system)
}

normalise <- function(comm_matrix) {
    # normalise such that the rows add up to one
    rowsum <- rowSums(comm_matrix)

    # normalise
    matrix_norm <- comm_matrix/rowsum

    # replace NaNs
    matrix_norm[is.nan(matrix_norm)] <- 1/3

    return(matrix_norm)
}

# Mutation function

alphabet <- c("A","G","U","C")
mutation_matrix <- matrix(rep(1/3,16),4,4)
diag(mutation_matrix) <- 0

mutate_population_fast <- function(population) {
    # choose number of elements to change
    N_change <- rbinom(1, genome_size*population_size, prob=mu)
 
    # generate indices of elements to change
    indices <- sample(genome_size*population_size, size=N_change)

    # change elements
    for (index in indices) {
        row <- ceiling(index/genome_size)
        column <- index %% genome_size + 1
        distr <- mutation_matrix[match(population[row, column], alphabet),]
        population[row, column] <- sample(alphabet, size=1, prob=distr)
    }

    return(population)
}

# compute how many different individuals there are in a population
compute_diversity <- function(population) {
    s = set()
    for (i in 1:nrow(population)) {
         s <- set_union(set(population[i,]), s)
    }
    return(length(s))
}

# construct a tree from a population using a parent matrix
reconstruct_tree <- function(parent_matrix) {
    D <- nrow(parent_matrix)    # maximum depth tree
    N <- ncol(parent_matrix)    # population size
    N_cur <- N                  # cur population size
    cur_depth <- 0              # cur depth tree

    children_indices <- seq(1,N,1)
    # children <- lapply(as.character(seq(1,N,1)),FUN=as.list)
    children <- as.character(seq(1,N,1))

    # while (N_cur > 1 && cur_depth < D) {
    while (cur_depth < D) {
        # create an empty list of population size to group children
        # under the right parent (index)
        parents <- vector("list",N)
        has_children <- rep(0,N)
        # cat(paste("\n\n\ncurrent depth", cur_depth))

        # loop over the children by looping over their indices
        child_index <- 1
        for (child in children_indices) {
            parent <- parent_matrix[D-cur_depth,child]  # find index of parent in prev generation
            child <- children[[child_index]]
            # print("parent found:"); print(parent)
            cur_children_parent <- parents[[parent]]    # check if parent already is assigned children
            cur_number_children <- has_children[parent] # check number of children for parent
            if (cur_number_children == 0 && cur_depth > 0) {
                parents[[parent]] <- children[[child_index]]        # assign child to parent
            } else if (cur_number_children == 0) {
                parents[[parent]] <- list(children[child_index])    # assign list with child to parent
            } else if (cur_depth == 0) {
                parents[[parent]][[cur_number_children+1]] <- child   # add child to cur children
            } else if (cur_number_children == 1) {
                parents[[parent]] <- list(cur_children_parent, child)
            } else {
                parents[[parent]][[cur_number_children+1]] <- child
            }
            
            has_children[parent] <- has_children[parent] + 1        # increase children for parent

            # child_counter <- child_counter + 1
            # print("print parents after adding next child"); print(capture.output(dput(parents)))
            child_index <- child_index + 1
        }
        # print("parents:") print(capture.output(dput(parents)))
        nulls <- sapply(parents, FUN=is.null)       # check which prev population members didn't have children
        # print("compute for all parents whether they are nulls"); print(nulls)
        children_indices <- seq(1,N,1)[!nulls]   # get the indices of the parents, set children to them
        children <- parents[!nulls]
        # print("children"); print(capture.output(dput(children)))
        N_cur <- length(children_indices)
        cur_depth <- cur_depth + 1
    }
    if (N_cur > 1) {
        print("Disconnected tree")
        # list(children)
    } else {
        return(children)
    }
}

# print a nested_list in tree form
print_tree <- function(nested_list) {
    str_repr <- paste(capture.output(dput(nested_list)),collapse='')
    # print(str_repr)
    str_repr <- gsub("[\r\n]","",str_repr)
    # print(str_repr)
    # print("\n\n\n")
    str_repr <- gsub('\"',"",str_repr)
    # print(str_repr)
    # print("\n\n\n")
    str_repr <- gsub('list',"",str_repr)
    # print(str_repr)
    # print("\n\n\n")
    str_repr <- paste(str_repr, ";")
    # print(str_repr)
    # print("\n\n\n")
    str_repr <- gsub(' ',"",str_repr)
    return(str_repr)
}

# p_matrix <- matrix(c(2,1,3,2,5,3,1,2,3,1,5,2,2,1,2,1,1,4),3,6)
# tree <- reconstruct_tree(p_matrix)
# print(print_tree(tree))

# print(print_tree(list(list("a","b"), list(list("c","d"), list("e","f")))))
