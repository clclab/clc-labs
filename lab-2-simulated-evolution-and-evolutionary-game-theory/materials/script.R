# load stringr package
library(stringr)

# generate random strings
x = paste(sample(c('A','G','C','U'), size=10, replace=TRUE), collapse='')

simulate_evolution <- function(size_population=100, size_individual=100, sim_length=100, mu=0) {

    # generate initial population with random strings
    population <- rep(0,size_population)        # generate empty string
    for (i in 1:size_population) {
        population[i] <- paste(sample(c('A','G','C','U'), size=size_individual, replace=TRUE), collapse='')
    }

    # compute fitness
    fitness <- rep(0,size_population)
    for (i in 1:size_population) {fitness[i] <- str_count(population[i], "CAC")}

    av_fitness = rep(0, sim_length)
    av_fitness[1] <- mean(fitness)

    # simulate evolution
    for (j in 2:sim_length) {

        # generate children. 
        for (i in 1:size_population) {
            population = sample(population, size=size_population, replace=TRUE, prob = fitness/sum(fitness))

            # mutation children
        }

        # recompute fitness
        for (i in 1:size_population) {fitness[i] <- str_count(population[i], "CAC")}

        # add to list with average fitness
        av_fitness[j] <- mean(fitness)
    }

    # plot average fitness
    generation = seq(1,100,1)
    plot(generation, av_fitness, type="l",ann=FALSE)
    title(main="Average population fitness", xlab="Generation", ylab="Fitness")
}

simulate_evolution(size_population=100, size_individual=100, sim_length=100, mu=0)
