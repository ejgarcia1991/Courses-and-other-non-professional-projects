library(dplyr)

#Initial Data loading
features <- read.table("UCI HAR Dataset/features.txt", col.names = c("n", "Functions"))
activityLabels <- read.table("UCI HAR Dataset/activity_labels.txt", col.names = c("Code", "Activity"))
trainingSet <- read.table("UCI HAR Dataset/train/X_train.txt", col.names = features$Functions)
trainingLabels <- read.table("UCI HAR Dataset/train/y_train.txt", col.names = c("Code"))
testSet <- read.table("UCI HAR Dataset/test/X_test.txt", col.names = features$Functions)
testLabels <- read.table("UCI HAR Dataset/test/y_test.txt", col.names = c("Code"))
subjectTest <- read.table("UCI HAR Dataset/test/subject_test.txt", col.names = c("Subject"))
subjectTrain <- read.table("UCI HAR Dataset/train/subject_train.txt", col.names = c("Subject"))


#1. Unification of the dataSet
subject <- rbind(subjectTrain,subjectTest)
Y <- rbind(trainingLabels, testLabels)
X <- rbind(trainingSet,testSet)

dataSet <- cbind(Y,subject,X)


#2. Mean and standard deviation for each measurement
dataSet <- dataSet %>% select(Subject, Code, contains("mean"), contains("std"))

#3. Relabeling the Activity variable and converting it to a factor
dataSet$Code <- factor(dataSet$Code, levels = activityLabels$Code ,labels = activityLabels$Activity)
dataSet <- rename(dataSet, "Activity" = "Code")
dataSet$Subject <- as.factor(dataSet$Subject)

#4. Renaming the variables with descriptive variable names
names(dataSet) <- gsub("^t", "Time ", names(dataSet))
names(dataSet) <- gsub("^f", "Frequency ", names(dataSet))
names(dataSet) <- gsub("[Bb]ody", "Body ", names(dataSet))
names(dataSet) <- gsub(".tBody", "Body ", names(dataSet))
names(dataSet) <- gsub("Acc", "Accelerometer ", names(dataSet))
names(dataSet) <- gsub("Gyro", "Gyrometer ", names(dataSet))
names(dataSet) <- gsub("Mag|Magnitude", "Magnitude ", names(dataSet))
names(dataSet) <- gsub(".mean.", "Mean ", names(dataSet))
names(dataSet) <- gsub(".std", "Standard Deviation ", names(dataSet))
names(dataSet) <- gsub("[Jj]erk", "Jerk ", names(dataSet))
names(dataSet) <- gsub("angle", "Angle ", names(dataSet))
names(dataSet) <- gsub("[Gg]ravity", "Gravity ", names(dataSet))


#5.data set with the average of each variable for each activity and each subject
summaryDataSet <- aggregate(dataSet[3:88], by = list(dataSet$Activity,dataSet$Subject), FUN = mean, simplify = T, )
names(summaryDataSet)[1] <- "Activity"
names(summaryDataSet)[2] <- "Subject"

write.table(summaryDataSet,file="summaryDataSet.txt",row.names = FALSE)

