leaf_nodes <- c(0, 0, 0, 0, 0)

transition_probability <- function(state, next_state, gain, loss){

    zero <- 1 - gain
    one <- 1 - loss

    if (state & next_state) { return(one) }
    if (!state & next_state) { return(gain) }
    if (!state & !next_state) { return(zero) }
    if (state & !next_state) { return(loss) }

}

# Node-state sequence is ordered by depth-first tree-traversal
tree_likelihood <- function(ancestor_nodes, leaf_nodes, gain, loss) {

    an <- ancestor_nodes
    ln <- leaf_nodes
    tp <- function(state, next_state) { transition_probability(state, next_state, gain, loss) }

    return (tp(an[1], an[2]) * tp(an[2], an[3]) * tp(an[3], ln[1]) 
                                                * tp(an[3], ln[2])
            * tp(an[1], an[4]) * tp(an[4], an[5]) * tp(an[5], ln[3])
                                                    * tp(an[5], ln[4])
                                * tp(an[4], an[6]) * tp(an[6], ln[5]))
}

calculate_likelihood <- function(gain, loss) {

    n_ancestor_nodes <- 6

    ancestor_nodes <- expand.grid(rep(list(0:1), n_ancestor_nodes))
    rows <- dim(ancestor_nodes)[1]

    # Brute-foce likelihood
    #p <- 0

    #for (row in 1:rows) {
    #    p <- p + tree_likelihood(ancestor_nodes[row,], leaf_nodes, gain, loss)
    #}

    tp <- function(state, next_state) { transition_probability(state, next_state, gain, loss) }
    ln <- leaf_nodes

    # Optimized likelihood calculation
    level_0 <- rep(0, 2)
    for (n1 in 0:1) {
        level_1_a <- rep(0, 2)
        for (n2 in 0:1) {
            level_2 <- rep(0, 2)
            for (n3 in 0:1) {
                level_2[n3+1] <- tp(n2, n3) * tp(n3, ln[1]) * tp(n3, ln[2])
            }
            level_1_a[n2+1] <- sum(level_2) * tp(n1, n2)
        }
        level_1_b <- rep(0, 2)
        for (n4 in 0:1) {
            level_2_a <- rep(0, 2)
            for(n5 in 0:1) {
                level_2_a[n5+1] <- tp(n4,n5) * tp(n5, ln[3]) * tp(n5, ln[4])
            }
            level_2_b <- rep(0, 2)
            for(n6 in 0:1) {
                level_2_b[n6+1] <- tp(n4,n6) * tp(n6, ln[5]) 
            }
            level_1_b[n4+1] <- tp(n1, n4) * sum(level_2_a) * sum(level_2_b)
        }
        level_0[n1+1] <- sum(level_1_a) * sum(level_1_b)
    }

    return(sum(level_0))

}

calculate_likelihood_surface <- function(resolution) {

    gains <- seq(0, 1, length=resolution)
    losses <- seq(0, 1, length=resolution)

    likelihood_surface <- matrix(rep(0.0, resolution**2), resolution, resolution)

    for (gain_index in 1:resolution) {
        for (loss_index in 1:resolution) {
            likelihood_surface[gain_index, loss_index] <- calculate_likelihood(gains[gain_index], losses[loss_index])
        }
    }

    return(likelihood_surface)

}

plot_2d <- function(likelihood_surface) {
    image2D(likelihood_surface, clab="likelihood", ylab="loss", xlab="gain")
}

plot_3d <- function(likelihood_surface) {
    persp3D(z=likelihood_surface, clab="likelihood", ylab="loss", xlab="gain")
}
