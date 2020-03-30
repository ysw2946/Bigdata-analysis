boys = read.table("C:/Users/ysw29/Downloads/vscores.dat",header=T)
boys = boys[,-1]

C = matrix(c(1, -1, 0, 0,
             0, 1, -1, 0,
             0, 0, 1, -1), ncol = 4,byrow=T)
ad.boys = as.data.frame(as.matrix(boys) %*% t(C))
library(ICSNP)
HotellingsT2(ad.boys, test="f")

library(tidyverse)
boys_p <- data.frame(ID = rep(c(1:36),4), 
                         G = rep(c("G8","G9","G10","G11"),each=36),
                         P = c(boys$G8,boys$G9,boys$G10,boys$G11)) %>% 
mutate(ID = as.factor(ID), G = as.factor(G))
with(boys_p, interaction.plot(x.factor = G, trace.factor = ID, response = P, legend = FALSE))