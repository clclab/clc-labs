# load stringr package
library(stringr)

# generate random strings
x = randomString(maxLenth=10, minLength=10, alphabet=c('A','G','C','U'))

simulate_evolution <- function(size_population=100, size_individual=100, sim_length=100, mu=0) {

    # generate initial population with random strings
    population <- rep(0,size_population)        # generate empty string
    for (i in 1:size_population) {
        population[i] <- randomString(maxLenth=size_individual, minLength=size_individual, alphabet=c('A','G','C','U'))
    }

    fitness <- rep(0,size_population)
        for (i in 1:size_population) {fitness[i] <- str_count(population[i], "CAC")}

    # simulate evolution
    av_fitness = rep(0, sim_length)
    av_fitness[1] <- mean(fitness)
    for (j in 2:sim_length) {

        # generate children. 
        for (i in 1:size_population) {
            # I will have to find out how to use the "random" package
            # on my system

            # mutation children
        }

        # recompute fitness
        for (i in 1:size_population) {fitness[i] <- str_count(population[i], "CAC")}

        # add to list with average fitness
        av_fitness[j] <- mean(fitness)

        # plot average fitness
        generation = seq(1,100,1)
        plot(av_fitness, generation, type="o",ann=false)
        title(main="Average population fitness", xlab="xlab", ylab="ylab")
    }
}
