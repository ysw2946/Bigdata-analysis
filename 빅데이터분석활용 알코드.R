library(tidyverse)
Michelson1 = scan(file="C:/Users/ysw29/Downloads/Velocity/Michelson1.dat")
Michelson2 = scan(file="C:/Users/ysw29/Downloads/Velocity/Michelson2.dat")
Newcomb1 = scan(file="C:/Users/ysw29/Downloads/Velocity/Newcomb1.dat")
Newcomb2 = scan(file="C:/Users/ysw29/Downloads/Velocity/Newcomb2.dat")
Newcomb3 = scan(file="C:/Users/ysw29/Downloads/Velocity/Newcomb3.dat")

data <- data.frame(Experiment = c(rep("Michelson1", length(Michelson1)),
                                  rep("Michelson2", length(Michelson2)),
                                  rep("Newcomb1", length(Newcomb1)),
                                  rep("Newcomb2", length(Newcomb2)),
                                  rep("Newcomb3", length(Newcomb3))),
                   value = c(Michelson1, Michelson2, Newcomb1, Newcomb2, Newcomb3))
data
data %>% ggplot(aes(x=Experiment, y=value)) + 
  geom_boxplot() + 
  scale_x_discrete(limits=c("Michelson1","Newcomb1","Newcomb2","Newcomb3","Michelson2")) +
  theme(axis.title=element_blank(),axis.ticks.x=element_blank())
