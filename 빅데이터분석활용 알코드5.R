
#  Homework

# Data Loading
vscores = data.frame(ID = c(1:36),
                     G8 = c(1.75,0.90,0.80,2.42,-1.31,-1.56,1.09,-1.92,-1.61,2.47,-0.95,1.66,2.07,3.30,2.75,2.25,2.08,0.14,
                            0.13,2.19,-0.64,2.02,2.05,1.48,1.97,1.35,-0.56,0.26,1.22,-1.43,-1.17,1.68,-0.47,2.18,4.21,8.26),
                     G9 = c(2.60,2.47,0.93,4.15,-1.31,1.67,1.50,1.03,0.29,3.64,0.41,2.74,4.92,6.10,2.53,3.38,1.74,0.01,
                            3.19,2.65,-1.31,3.45,1.80,0.47,2.54,4.63,-0.36,0.08,1.41,0.80,1.66,1.71,0.93,6.42,7.08,9.55),
                     G10 = c(3.76,2.44,0.40,4.56,-0.66,0.18,0.52,0.50,0.73,2.87,0.21,2.40,4.46,7.19,4.28,5.79,4.12,1.48,0.60,
                             3.27,-0.37,5.32,3.91,3.63,3.26,3.54,1.14,1.17,4.66,-0.03,2.11,4.07,1.30,4.64,6.00,10.24),
                     G11 = c(3.68,3.43,2.27,4.21,-2.22,2.33,2.33,3.04,3.243,5.38,1.82,2.17,4.71,7.46,5.93,4.40,3.62,2.78,
                             3.14,2.736,4.09,6.01,2.49,3.88,5.62,5.24,1.34,2.15,2.62,1.04,1.42,3.30,0.76,4.82,5.65,10.58))

# Test
library(tidyverse)
vscores_df <- data.frame(ID = rep(c(1:36),4), 
                         GROUP = rep(c("G8","G9","G10","G11"),each=36),
                         VALUE = c(vscores$G8,vscores$G9,vscores$G10,vscores$G11)) %>% 
  mutate(ID = as.factor(ID), GROUP = as.factor(GROUP))
ANOVA_MODEL = aov(VALUE ~ GROUP, data=vscores_df)
summary(ANOVA_MODEL)

# Profile Analysis
vscores = vscores[,-1]
C = matrix(c(1, -1,  0,  0,
             0,  1, -1,  0,
             0,  0,  1, -1), ncol = 4, byrow=T)
vscores.ramus = as.data.frame(as.matrix(vscores) %*% t(C))
library(ICSNP)
HotellingsT2(vscores.ramus, test="f")

# Interaction Plot
library(tidyverse)
vscores_df <- data.frame(ID = rep(c(1:36),4), 
                         GROUP = rep(c("G8","G9","G10","G11"),each=36),
                         VALUE = c(vscores$G8,vscores$G9,vscores$G10,vscores$G11)) %>% 
  mutate(ID = as.factor(ID), GROUP = as.factor(GROUP))
with(vscores_df, interaction.plot(x.factor = GROUP, trace.factor = ID, response = VALUE, legend = FALSE))