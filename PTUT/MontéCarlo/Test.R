library(ggplot2)

# méthode "middle square"
middle_square <- function(seed, n) {
  numbers <- numeric(n)  
  current_number <- seed  
  
  for (i in 1:n) {
    squared <- current_number^2  
    str_squared <- sprintf("%08d", squared)  
    middle_digits <- substr(str_squared, nchar(str_squared)/2 - 1, nchar(str_squared)/2 + 2)  
    current_number <- as.numeric(middle_digits)  
    numbers[i] <- current_number / 10000  # Normaliser pour obtenir des valeurs entre 0 et 1
  }  
  
  return(numbers)
}

#  La méthode congruentielle linéaire
linear_congruential_generator <- function(seed, n, a, c, m) {
  numbers <- numeric(n)  
  current_number <- seed  
  
  for (i in 1:n) {
    current_number <- (a * current_number + c) %% m  
    numbers[i] <- current_number / m  
  }  
  
  return(numbers)
}

# Paramètres pour les générateurs
seed <- 7533  
n <- 10000  
a <- 1664525  
c <- 1013904223  
m <- 2^32  

# Génération de nombres pseudo-aléatoires
random_numbers <- linear_congruential_generator(seed, n, a, c, m)

random_numbers <- middle_square(seed, n)

# Regroupement par classes
breaks <- seq(0, 1, by = 0.1)
observed_frequencies <- cut(random_numbers, breaks = breaks, right = FALSE, include.lowest = TRUE)
observed_frequencies_table <- table(observed_frequencies)

# Fréquences attendues pour une distribution uniforme
expected_frequencies <- rep(n / 10, 10)

# Test du khi-deux d'adéquation
chi_squared_test <- function(observed, expected) {
  chi_squared <- sum((observed - expected)^2 / expected)
  df <- length(observed) - 1
  p_value <- 1 - pchisq(chi_squared, df)
  cat("Chi-squared:", chi_squared, "\n")
  cat("Degré de liberté:", df, "\n")
  cat("P-value:", p_value, "\n")
  return(list(chi_squared = chi_squared, df = df, p_value = p_value))
}

result <- chi_squared_test(observed_frequencies_table, expected_frequencies)


ggplot(data = as.data.frame(table(observed_frequencies)), aes(x = observed_frequencies, y = Freq)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  theme_minimal() +
  labs(title = "Distribution des valeurs générées", x = "Intervalle", y = "Fréquence")
