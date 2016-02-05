# load stringr package
library(stringr)
source("fitness_functions.R")

population_size		<-	100
genome_size 		<-	18
simulation_length	<-	2000
mu		        	<- 	0.001

# fitness function
# compute_fitness    <-  CAC_count
# compute_fitness    <-  communication_fixed_target
compute_fitness    <-  communication_random_target


generate_population <-  function(population_size, genome_size) {
    # generate initial population with random strings
    population <- matrix(rep(0,population_size*genome_size), population_size, genome_size)
    for (i in 1:population_size) {
        new_member <- sample(c('A','G','C','U'), size=genome_size, replace=TRUE)
        population[i,] <- new_member
    }

    return(population)
}

simulate_evolution <- function(population) {

    # compute fitness
    fitness <- compute_fitness(population)
    # print(fitness)

    av_fitness <- rep(0, simulation_length)
    av_fitness[1] <- mean(fitness)

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
    }

    # plot average fitness
    ymax <- av_fitness[simulation_length]+2
    generation <- seq(1,simulation_length,1)
    plot(generation, av_fitness, type="l",ann=FALSE, ylim=c(0,ymax))
    title(main="Average population fitness", xlab="Generation", ylab="Fitness")

    return(population)
}

# run the function
population <- generate_population(population_size, genome_size)
population <- simulate_evolution(population)
