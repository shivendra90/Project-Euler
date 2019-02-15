# Calculates sum of al multiples of 3
# and 5 by normal iteration

value <- 999

mult_3_5 <- function(x) {

    multiples_3_5 <- 0
    for (i in 1 : x) {
        if (i %% 3 == 0 | i %% 5 == 0) {
            multiples_3_5 <- multiples_3_5 + i # Appends every multiple
        }
    }
    return(sum(multiples_3_5))
}

# Another way
sum(unique(c(seq(3, 999, 3), seq(5, 99, 5))))
