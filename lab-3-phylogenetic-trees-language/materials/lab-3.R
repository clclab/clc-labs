# library for str_count
library(stringr)
source("auxiliary_functions.R")

population_size		<-	100
genome_size 		<-	50
simulation_length	<-	1000
mu		        	<- 	0.001

# fitness function
compute_fitness    <-  CAC_count
# compute_fitness    <-  communication_fixed_target
# compute_fitness    <-  communication_random_target
# compute_fitness    <-  sending_random_target


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

    # compute fitness and population diversity
    fitness <- compute_fitness(population)

    av_fitness <- rep(0, simulation_length)
    av_fitness[1] <- mean(fitness)

    diversity <- rep(0, simulation_length)
    diversity[1] <- compute_diversity(population)

    # simulate evolution
    for (j in 2:simulation_length) {
        # print(paste("simulation round",j))

        # generate children. 
        population_children <- population[sample(population_size, size=population_size, replace=TRUE, prob=fitness/sum(fitness)),]

        # mutation childrn
        population <- mutate_population_fast(population_children)

        # recompute fitness
        fitness <- compute_fitness(population)

        # add to list with average fitness
        av_fitness[j] <- mean(fitness)
        diversity[j] <- compute_diversity(population)
    }

    # plot average fitness and population diversity
    par(mfrow=c(1,2))
    ymax <- av_fitness[simulation_length]+2
    generation <- seq(1,simulation_length,1)
    plot(generation, av_fitness, type="l",ann=FALSE, ylim=c(0,ymax))
    title(main="Average population fitness", xlab="Generation", ylab="Fitness")
    plot(generation, diversity, type="l",ann=FALSE)
    title(main="Population diversity", xlab="Generation", ylab="Number of distinct phenotypes")

    return(population)
}

# Generate population and simulate evolution, store population members in the mean time
population <- generate_population(population_size, genome_size)
population <- simulate_evolution(population)
