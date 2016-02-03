# load stringr package
library(stringr)

population_size		<-	100
genome_size 		<-	100
simulation_length	<-	100
mu		        	<- 	0.5


simulate_evolution <- function(population_size, genome_size, simulation_length, mu) {
    # generate initial population with random strings
    population <- rep(0,population_size)        # generate empty string
    for (i in 1:population_size) {
        population[i] <- paste(sample(c('A','G','C','U'), size=genome_size, replace=TRUE), collapse='')
    }

    # compute fitness
    fitness <- rep(0,population_size)
    for (i in 1:population_size) {fitness[i] <- str_count(population[i], "CAC")}

    av_fitness = rep(0, simulation_length)
    av_fitness[1] <- mean(fitness)

    # simulate evolution
    for (j in 2:simulation_length) {
        print(paste("simulation round",j))

        # generate children. 
        for (i in 1:population_size) {
            population = sample(population, size=population_size, replace=TRUE, prob = fitness/sum(fitness))

            # mutation children
            population = mutate_population(population, population_size, genome_size, mu)
        }

        # recompute fitness
        for (i in 1:population_size) {fitness[i] <- str_count(population[i], "CAC")}

        # add to list with average fitness
        av_fitness[j] <- mean(fitness)
    }

    # plot average fitness
    ymax <- av_fitness[simulation_length]
    generation = seq(1,100,1)
    plot(generation, av_fitness, type="l",ann=FALSE, ylim=c(0,ymax+2))
    title(main="Average population fitness", xlab="Generation", ylab="Fitness")
}

mutate_population <- function(population, population_size, genome_size, mu) {
    # choose number of elements to change
    N_change <- rbinom(genome_length*population_size, 1, mu)

    # generate indices of elements to change
    indices <- sample(genome_length*population_size, N_change)

    # change all strings into lists


    # change elements
    for (index in indices) {
        row <- ceiling(index/genome_length)
        column <- index %% population_size
        # sample new value for character at row, column
    }

    # convert  back into matrix of strings

    return(mutated_population)

mutation_matrix = matrix(rep(1/3,16),4,4)
diag(mutation_matrix) <- 0

# run the function
simulate_evolution(population_size, genome_size, simulation_length, mu)
