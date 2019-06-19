f <- file.choose()
data = read.csv(f,header=TRUE)
summary(data)
library("FactoMineR")
pca = PCA(data[,5:13],scale.unit = TRUE)
data$pc1 <- pca$ind$coord[,1]
data$pc2 <- pca$ind$coord[,2]

corrplot(data[,5:15])

mfa = MFA(data[5:13],group=c(5,4), type=c("s", "c"), ncp=10, name.group=c("obs","logs"))
data$Engagement <- mfa$ind$coord[,1]
data$PhysvsTech <- mfa$ind$coord[,2]
M <- cor(data[,5:17])
library(corrplot)
corrplot(M,type='upper')


if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install("RDRToolbox", version = "3.8")

iso = isomap(data[4:13])
