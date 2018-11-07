#!/usr/bin/env Rscript

##install.packages('RcppCNPy')
##library('RcppCNPy')
## Segfault
#fmat <- npyLoad('output.npy')

x <- read.csv('output.csv')

##install.packages('data.table')

x <- as.matrix(data.table::fread('output.csv'))
x <- as.matrix(x)

xp <- Matrix::Matrix(x, sparse=T)
saveRDS(xp, 'output.rds')
