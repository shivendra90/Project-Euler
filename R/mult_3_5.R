# Calculates sum of al multiples of 3
# and 5 by normal iteration

multiples_3_5 = c()

for (i in 1:1000) {

    if ((i+1) %% 3 == 0) {
        multiples_3_5 <- multiples_3_5 + (i+1)
    }

    if ((i+1) %% 5 == 0) {
        multiples_3_5 <- multiples_3_5 + (i+1)
    }
    return(sum(multiples_3_5))
}
