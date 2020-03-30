gunData <- c(20.2, 26.2, 23.8, 22.0, 22.6, 22.9, 23.1, 22.9, 21.8, 24.1, 26.9, 24.9, 23.5, 24.6, 25.0, 22.9, 23.7, 23.5, 14.2, 18.0, 12.5, 14.1, 14.0, 13.7, 14.1, 12.2, 12.7, 16.2, 19.1, 15.4, 16.1, 18.1, 16.0, 16.1, 13.8, 15.1) 
method <- factor(rep(1:2, each = 18)) 
group <- factor(rep(rep(1:3, each = 3), times = 4)) 
team <- factor(rep(1:3, times = 12)) 
canonloading <- data.frame(gunData, method, group, team) 
str(canonloading)
library(EMSaov) 
result <- EMSanova(gunData ~ method + group + team, type = c("F", "F", "R"), 
                                   nested = c(NA, NA, "G"), data=canonloading)