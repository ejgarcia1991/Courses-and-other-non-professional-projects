---
title: "Codebook"
author: "Eilder Jorge"
date: "2020/6/24"
output: pdf_document
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```
## Data content
This is a filtered tidy dataSet from the UCI HAR repository containing data about smartwrist applications.
It contains the mean and standard deviation of the diferent motions subject realized in one of 6 activities.


## Factor Features
Activity. Is one out of 6: 
1 WALKING
2 WALKING_UPSTAIRS
3 WALKING_DOWNSTAIRS
4 SITTING
5 STANDING
6 LAYING

Subject. It's an unique ID referring to the subject being measured.
Range 1:30
## Numeric Features
The other 86 features represent the numeric mean and standard deviation of each of the actions in each axis in a range of [-1,1].

The values are averaged per subject and activity, leading to a total of 180 rows with mean data for analysis.
 

