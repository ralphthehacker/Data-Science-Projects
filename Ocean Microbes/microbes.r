## Reads the CSV file containing the microbial file
microbes <- read.csv(file = "/Users/ralphblanes/PycharmProjects/Data-Science-Projects/Ocean Microbes/seaflow_21min.csv",head = T,sep = ',')
# Plots populations
ggplot(data = microbes,aes(x = pe, y = chl_small,color = pop))+geom_point()
#Creating an r formula
measurements <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
# Training a decision tree
model <- rpart(measurements,method = 'class',data = train)
#Making predictions
predictions <- predict(model,test)
accuracy <- sum(test==predictions)/nrow(test)
table(pred = predictions, true = test)

#Creating a random Forest
model <- randomForest(measurements,data = train)
#Calculating the accuracy of the random forest
predictions <- predict(model,test)
accuracy <- sum(test$pop==predictions)/nrow(test)
table(pred = predictions, true = test$pop)

#Creating a SVM
model<-model <- svm(measurements,data = train)
predictions <- predict(model,test)
svm_accuracy <- sum(test$pop==predictions)/nrow(test)
table(pred = predictions, true = test$pop)


#Doing a sanity check on the data
#fsc_small, fsc_perp, fsc_big, pe, chl_small, chl_big
ggplot(data = microbes,aes(x = time, y = fsc_small,color = pop))+geom_point()
ggplot(data = microbes,aes(x = time, y = fsc_perp,color = pop))+geom_point()
#Found it, fsc_big is not continuous

ggplot(data = microbes,aes(x = time, y = fsc_big,color = pop))+geom_point()
#Found it
ggplot(data = microbes,aes(x = time, y = pe,color = pop))+geom_point()
ggplot(data = microbes,aes(x = time, y = chl_small,color = pop))+geom_point()
ggplot(data = microbes,aes(x = time, y = chl_big,color = pop))+geom_line()

#Cleaning dataset from anomaly
new_microbes <- subset(microbes, file_id != 208)

