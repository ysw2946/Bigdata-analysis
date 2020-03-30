weight = read.csv("C:/Users/ysw29/Downloads/ExamFile/Bodyweight.csv", header=T)
weight = weight[,-1]
print(weight)

C = matrix(c(1, -1, 0, 0, 0,
             0, 1, -1, 0, 0,
             0, 0, 1, -1, 0,
             0, 0, 0, 1, -1), ncol = 5,byrow=T)
ad.weight = as.data.frame(as.matrix(weight) %*% t(C))

library(ICSNP)
HotellingsT2(ad.weight, test="f")

library(tidyverse)
weight_p <- data.frame(ID = rep(c(1:27),5), 
                     G = rep(c("w0","w1","w2","w3","w4"),each=27),
                     P = c(weight$w0,weight$w1,weight$w2,weight$w3,weight$w4)) %>% 
  mutate(ID = as.factor(ID), G = as.factor(G))
with(weight_p, interaction.plot(x.factor = G, trace.factor = ID, response = P, legend = FALSE))