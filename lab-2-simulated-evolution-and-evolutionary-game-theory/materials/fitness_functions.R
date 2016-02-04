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
