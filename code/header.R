
library(readxl)    
library(lubridate)
library(tidyverse)
library(data.table)
library(plyr)
library(ggplot2)
library(tidyr)
library(stringr)
library(data.table)
library(epiDisplay)
library(survival)
library(survminer)
library(qwraps2)
library(table1)
library(fBasics)
library(comorbidity)
library(gtsummary)
library(glmnet)
library(BeSS)
library(dummies)
library(hash)



##### ------------ Settings ------------
setwd(root_dir)

data_dir <- paste(root_dir, "/../data/", sep = "") # for input data files.
output_dir <- paste(root_dir, "/../outputs/", sep = "") # for output files.
##### end Settings

pvalue <- function(x, ...) {
  y <- unlist(x)
  g <- factor(rep(1:length(x), times=sapply(x, length)))
  if (is.numeric(y)) {
    p <- t.test(y ~ g)$p.value
  } else {
    p <- chisq.test(table(y, g))$p.value
  }
  c("", sub("<", "&lt;", format.pval(p, digits=3, eps=0.001)))
}


