# fitness functions

CAC_count <- function(population) {
    # fitness function based on number of
    # occurences of substring CAC
    fitness <- rep(0,population_size)
    for (i in 1:population_size) {
        fitness[i] <- str_count(population[i], "CAC")
    }
    return(fitness)
}

target_R <- matrix(rep(0,9),3,3)
diag(target_R) <- 1
target_S <- matrix(rep(0,9),3,3)
diag(target_S) <- 1
target_agent = list(R=target_R, S=target_S)

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

    population_size = length(population)
    fitness <- rep(0, population_size)
    for (i in 1:population_size) {
        random_agent <- sample(population_matrices, size=1)[[1]]
        fitness[i] <- compute_success(population_matrices[[i]], random_agent)
    }

    return(fitness)
}

compute_success <- function(agent1, agent2) {
    # agents are characterized by a list
    # containing S and R matrix
    product <- agent1$S %*% t(agent2$R) + t(agent1$S) %*% agent2$R
    fitness <- sum(diag(product))
    return(fitness)
}

get_population_matrices <- function(population) {
    # generate a list of S and R matrices
    # corresponding to the population's genomes
    # matrices = sapply(population_matrices, FUN=get_matrix)
    matrices <- list()
    for (i in 1:length(population)) {
        matrices[[i]] <- get_matrix(population[i])
    }

    return(matrices)
}

get_matrix <- function(genome) {
    # generate S and R matrix for genome
    
    # replace A, G, C and U by 3, 2, 1 and 0
    genome <- gsub("A",3,genome); genome <- gsub("G",2,genome)
    genome <- gsub("C",1,genome); genome <- gsub("U",0,genome)

    # convert to vector
    genome_vec <- as.numeric(strsplit(genome, "")[[1]])

    # create two matrices
    S <- normalise(matrix(genome_vec[1:9],3,3))
    R <- normalise(matrix(genome_vec[10:18],3,3))

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

mutate_population <- function(population) {
    # choose number of elements to change
    N_change <- rbinom(genome_size*population_size, 1, mu)
 
    # generate indices of elements to change
    indices <- sample(genome_size*population_size, N_change)

    # generate vector representations
    population_vec <- matrix(rep(0, genome_size*population_size), population_size, genome_size)
    for (i in 1:population_size) {
        population_vec[i,] <- strsplit(population[i],"")[[1]]
    }

    # change elements
    for (index in indices) {
        row <- ceiling(index/genome_size)
        # print("row")
        # print(row)
        column <- index %% genome_size
        # print("column")
        # print(column)
        distr <- mutation_matrix[match(population_vec[row, column], alphabet),]
        population_vec[row, column] <- population_vec[row, column]
    }

    mutated_population <- rep(0, population_size)
    for (i in 1:population_size) {
        mutated_member <- population_vec[i,]
        mutated_population[i] <- paste(mutated_member, collapse='')
    }

    return(mutated_population)
}

population <- c(rep(1,10))
for (i in 1:10) {
    population[i] <- paste(sample(c("A","G","C","U"),size=18, replace=TRUE), collapse="")
}

