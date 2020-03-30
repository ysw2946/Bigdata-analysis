cross <- read.csv("C:/Users/ysw29/Downloads/RTTR.csv", header = T) 
head(cross)

library(tidyverse) 
data1 <- data.frame(sub=1:18, seq = cross[,2]) 
data1 <- mutate(data1, AUC = cross$period1, period = 1) 
data1 <- mutate(data1, formula = if_else(seq == 1, "R", "T")) 
data2 <- data.frame(sub=1:18, seq=cross[,2]) 
data2 <- mutate(data2, AUC = cross$period2, period = 2) 
data2 <- mutate(data2, formula = if_else(seq == 1, "T", "R"))

crossover <- merge(data1, data2, all = T) 
crossover <- select(crossover, sub, seq, formula, period, AUC)

crossover <- crossover %>% mutate(sub = as.factor(sub),
                                  seq = as.factor(seq),
                                  formula = as.factor(formula),
                                  period = as.factor(period))

str(crossover)

library(BE)
BEdata <- with(crossover,data.frame(sub,period,formula,log(AUC)))
names(BEdata) <- c("SUBJ","PRD","TRT","AUC")
BEdata$GRP <- ifelse(crossover$seq ==1, "RT","TR")
be2x2(BEdata,Columns = c("AUC"))
