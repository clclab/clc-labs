
calculate_likelihood <- function(gain, loss) {

    zero = 1 - loss
    one = 1 - gain

    likelihood = zero * zero * zero * gain * gain * one * loss * one * one * one

    return(likelihood)

}

plot_likelihood_surface <- function(resolution) {

    gains <- seq(0, 1, length=resolution)
    losses <- seq(0, 1, length=resolution)

    likelihood_surface <- matrix(rep(0.0, resolution**2), resolution, resolution)

    for (gain in gains) {
        for (loss in losses) {
            likelihood_surface[gain, loss] <- calculate_likelihood(gain, loss)
            print(calculate_likelihood(gain, loss))
        }
    }

    print(likelihood_surface)

    image2D(likelihood_surface, clab="m")

}
