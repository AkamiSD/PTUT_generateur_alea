#générateur middle_square
middle_square <- function(seed, n) {
  numbers <- numeric(n)  
  current_number <- seed  
  
  for (i in 1:n) {
    squared <- current_number^2  
    str_squared <- sprintf("%08d", squared)  # Convertir en chaîne et ajouter des zéros au début pour obtenir au moins 8 chiffres
    middle_digits <- substr(str_squared, nchar(str_squared)/2 - 1, nchar(str_squared)/2 + 2)  # Extraire les 4 chiffres du milieu
    current_number <- as.numeric(middle_digits)  
    numbers[i] <- current_number  
  }
  
  return(numbers)
}
  
seed <- 7533    
n <- 10000   
random_numbers <- middle_square(seed, n)


chi_squared_test <- function(observed, expected) {
  chi_squared <- sum((observed - expected)^2 / expected)
  df <- length(observed) - 1
  p_value <- 1 - pchisq(chi_squared, df)
  cat("Chi-squared:", chi_squared, "\n")
  cat("Degrees of freedom:", df, "\n")
  cat("P-value:", p_value, "\n")
  return(list(chi_squared = chi_squared, df = df, p_value = p_value))
}

observed_frequencies <- table(random_numbers)

expected_frequency <- n / length(observed_frequencies)

expected_frequencies <- rep(expected_frequency, length(observed_frequencies))


result <- chi_squared_test(observed_frequencies, expected_frequencies)




# générateur congruentiel linéaire:

linear_congruential_generator <- function(seed, n, a, c, m) {
  numbers <- numeric(n)  
  current_number <- seed  
  
  for (i in 1:n) {
    current_number <- (a * current_number + c) %% m  # Formule du générateur congruentiel linéaire
    numbers[i] <- current_number / m # Normalisation pour obtenir des nombres entre 0 et 1 
  }
  
  return(numbers)
}

# Paramètres du générateur congruentiel linéaire
seed <- 12345  
n <- 10000  
a <- 1664525  
c <- 1013904223  
m <- 2^32  

random_numbers <- linear_congruential_generator(seed, n, a, c, m)



# partie graphe dix barre histograme (valeur générer entre 0 et 9):

# Générateur middle_square_generator
middle_square_generator <- function(seed_ms, n) {
  numbers <- numeric(n)
  current_number <- seed_ms
  
  for (i in 1:n) {
    squared <- current_number^2
    str_squared <- sprintf("%08d", squared)
    middle_digits <- substr(str_squared, nchar(str_squared)/2 - 1, nchar(str_squared)/2 + 2)
    current_number <- as.numeric(middle_digits)
    numbers[i] <- current_number %% 10  # Restreindre les nombres entre 0 et 9
  }
  
  return(numbers)
}

# Générateur congruentiel linéaire (LCG)
linear_congruential_generator <- function(seed_lcg, n, a, c, m) {
  numbers <- numeric(n)
  current_number <- seed
  
  for (i in 1:n) {
    current_number <- (a * current_number + c) %% m
    numbers[i] <- current_number %% 10  # Restreindre les nombres entre 0 et 9
  }
  
  return(numbers)
}

# Paramètres des générateurs
seed_ms <- 7533
seed_lcg <- 5567

n <- 10000  
a <- 16807
c <- 0

m <- 2^31-1

# Générer les nombres pseudo-aléatoires
random_numbers_middle_square <- middle_square_generator(seed, n)
random_numbers_lcg <- linear_congruential_generator(seed, n, a, c, m)

# Créer les histogrammes


x_breaks <- seq(-0.5, 9.5, by = 1)
 
# Histogramme pour le générateur middle_square_generator
hist(random_numbers_middle_square, breaks = x_breaks, main = "Distribution des nombres générés (middle_square_generator)", xlab = "Valeurs", ylab = "Fréquence", col = "skyblue", xaxt = "n")
axis(1, at = 0:9, labels = 0:9)

# Histogramme pour le générateur LCG
hist(random_numbers_lcg, breaks = x_breaks, main = "Distribution des nombres générés (LCG)", xlab = "Valeurs", ylab = "Fréquence", col = "lightgreen", xaxt = "n")
axis(1, at = 0:9, labels = 0:9)

