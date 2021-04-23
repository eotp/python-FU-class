lower_ci = xbar - me
upper_ci = xbar + me

(print("We are {}% confident that the true weight of chicken is between {} and {} grams.".
       format((1-alpha)*100, lower_ci, upper_ci)))