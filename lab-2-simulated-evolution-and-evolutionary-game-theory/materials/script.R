# load stringr package
library(stringr)
source("fitness_functions.R")

population_size		<-	100
genome_size 		<-	100
simulation_length	<-	100
mu		        	<- 	0.1

# fitness function
# compute_fitness    <-  CAC_count
# compute_fitness    <-  communication_fixed_target
compute_fitness    <-  communication_random_target


simulate_evolution <- function() {
    # generate initial population with random strings
    population <- rep(0,population_size)        # generate empty string
    for (i in 1:population_size) {
        new_member <- sample(c('A','G','C','U'), size=genome_size, replace=TRUE)
        population[i] <- paste(new_member, collapse='')
    }

    # compute fitness
    fitness <- compute_fitness(population)

    av_fitness <- rep(0, simulation_length)
    av_fitness[1] <- mean(fitness)

    # simulate evolution
    for (j in 2:simulation_length) {
        # print(paste("simulation round",j))

        # generate children. 
        population <- sample(population, size=population_size, replace=TRUE, prob=fitness/sum(fitness))

        # mutation children
        population <- mutate_population(population)

        # recompute fitness
        for (i in 1:population_size) {fitness[i] <- str_count(population[i], "CAC")}

        # add to list with average fitness
        av_fitness[j] <- mean(fitness)
    }

    # plot average fitness
    ymax <- av_fitness[simulation_length]+2
    generation <- seq(1,simulation_length,1)
    plot(generation, av_fitness, type="l",ann=FALSE, ylim=c(0,ymax))
    title(main="Average population fitness", xlab="Generation", ylab="Fitness")
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
        column <- index %% population_size
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

# run the function
simulate_evolution()
