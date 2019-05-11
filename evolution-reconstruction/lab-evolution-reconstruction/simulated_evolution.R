#####################################################################
# Lab section on simulated evolution
#
# Contributors
# - Basitaan van der Weij (bjvanderweij)
# - Dieuwke Hupkes (dieuwkehupkes)
# - Marianne de Heer Kloots (mdhk)
# 
# Last updated: 26 October 2018
#####################################################################

# library for str_count
library(stringr)
source("auxiliary_functions.R")

population_size		<-	100
genome_size 		<-	50
simulation_length	<-	1000
mu		        	<- 	0

# Function to generate new population
generate_population <-  function(population_size, genome_size) {
    # generate initial population with random strings
    population <- matrix(rep(0,population_size*genome_size), population_size, genome_size)
    for (i in 1:population_size) {
        new_member <- sample(c('A','G','C','U'), size=genome_size, replace=TRUE)
        population[i,] <- new_member
    }

    return(population)
}

# Function to simulate evolution
simulate_evolution <- function(population) {

    # compute fitness
    fitness <- CAC_count(population)

    av_fitness <- rep(0, simulation_length)
    av_fitness[1] <- mean(fitness)

    # simulate evolution
    for (j in 2:simulation_length) {

        # generate children by sampling from the population according to fitness
        population_children <- population[sample(population_size, size=population_size, replace=TRUE, prob=fitness/sum(fitness)),]

        # mutate children
        population <- mutate_population_fast(population_children)

        # recompute fitness
        fitness <- CAC_count(population)

        # add to list with average fitness
        av_fitness[j] <- mean(fitness)
    }

    # plot average fitness
    ymax <- av_fitness[simulation_length]+2
    generation <- seq(1,simulation_length,1)
    par(mfrow=c(1,1))
    plot(generation, av_fitness, type="l", ann=FALSE, ylim=c(0,ymax))
    title(main="Average population fitness", xlab="Generation", ylab="Fitness")

    return(population)
}

# Generate population and simulate evolution
population <- generate_population(population_size, genome_size)
population <- simulate_evolution(population)
