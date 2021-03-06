#####################################################################
# Lab section on simulated evolution with ancestry
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
library(ggtree)
source("auxiliary_functions.R")

# parameters of simulation
population_size		<-	100
genome_size 		<-	50
simulation_length	<-	1000
mu		        	<- 	0.005

# Function to generate new population
generate_population <-  function(population_size, genome_size) {
    # generate initial population with random strings
    population <- matrix(sample(c('A','G','C','U'), size=genome_size*population_size, replace=TRUE), population_size, genome_size)
    return(population)
}

# Function to simulate evolution with ancestry
simulate_evolution <- function(population) {

    # initialise
    back_pointers = matrix(rep(0,population_size*(simulation_length-1)), simulation_length-1, population_size) 

    # compute fitness and population diversity
    fitness <- CAC_count(population)

    av_fitness <- rep(0, simulation_length)
    av_fitness[1] <- mean(fitness)

    diversity <- rep(0, simulation_length)
    diversity[1] <- compute_diversity(population)

    # simulate evolution
    for (j in 2:simulation_length) {

        # generate children. 
        indices_children <- sample(population_size, size=population_size, replace=TRUE, prob=fitness/sum(fitness))
        population_children <- population[indices_children,]
        back_pointers[j-1,] <- indices_children

        # mutation childrn
        population <- mutate_population_fast(population_children)

        # recompute fitness
        fitness <- CAC_count(population)

        # store current fitness and diversity
        av_fitness[j] <- mean(fitness)
        diversity[j] <- compute_diversity(population)
    }

    # plot average fitness and population diversity
    par(mfrow=c(1,2))
    ymax <- av_fitness[simulation_length]+2
    generation <- seq(1,simulation_length,1)
    plot(generation, av_fitness, type="l",ann=FALSE, ylim=c(0,ymax))
    title(main="Average population fitness", xlab="Generation", ylab="Fitness")
    plot(generation, diversity, type="l",ann=FALSE,ylim=c(0,population_size))
    title(main="Population diversity", xlab="Generation", ylab="Number of distinct phenotypes")

    results <- list(population=population,parent_matrix=back_pointers)
    par(mfrow=c(1,1))
    return(results)
}

# Generate population and simulate evolution
population <- generate_population(population_size, genome_size)
results <- simulate_evolution(population)
population <- results$population
parent_matrix <- results$parent_matrix
