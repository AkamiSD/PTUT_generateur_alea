library(ggplot2)

library(ggforce)

von_neumann_generator <- function(seed, n) {
  numbers <- numeric(n)
  current_number <- seed
  for (i in 1:n) {
    squared <- current_number^2
    str_squared <- sprintf("%08d", squared)
    middle_digits <- substr(str_squared, nchar(str_squared)/2 - 1, nchar(str_squared)/2 + 2)
    current_number <- as.numeric(middle_digits)
    numbers[i] <- current_number
  }
  return(numbers)
}

generate_points <- function(seed, nombre_de_points) {
  random_numbers <- von_neumann_generator(seed, 2 * nombre_de_points)
  points <- data.frame(
    x = (random_numbers[seq(1, length(random_numbers), 2)] %% 10000) / 5000 - 1,
    y = (random_numbers[seq(2, length(random_numbers), 2)] %% 10000) / 5000 - 1
  )
  points$inside <- ifelse(points$x^2 + points$y^2 <= 1, "inside", "outside")
  return(points)
}

approximate_pi <- function(points) {
  4 * sum(points$inside == "inside") / nrow(points)
}

seed <- 5678
nombre_de_points <- 1000
points <- generate_points(seed, nombre_de_points)
pi_approx <- approximate_pi(points)

ggplot() +
  geom_point(data = points, aes(x = x, y = y, colour = inside), alpha = 0.5) +
  geom_circle(aes(x0 = 0, y0 = 0, r = 1), linetype = "dashed", color = "blue") +
  coord_fixed() +
  xlim(c(-1, 1)) + ylim(c(-1, 1)) +
  labs(title = paste("Approximation de PI avec Von Neumann: ", round(pi_approx, 4))) +
  theme_minimal() +
  theme(legend.position = "none")


