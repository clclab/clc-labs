# Auxiliary functions

# library for sets
suppressWarnings(library(sets))

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
