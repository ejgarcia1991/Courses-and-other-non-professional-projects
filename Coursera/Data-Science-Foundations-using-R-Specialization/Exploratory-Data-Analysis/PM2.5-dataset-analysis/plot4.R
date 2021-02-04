library(ggplot2)

NEI <- readRDS("./data/summarySCC_PM25.rds")
SCC <- readRDS("./data/Source_Classification_Code.rds")

# Across the United States, how have emissions from coal combustion-related sources changed from 1999-2008?

# fetch all NEIxSCC records with Short.Name (SCC) Coal
# merge the two data sets 
mergedData <- merge(NEI, SCC, by="SCC")
coalMatches  <- grepl("coal", mergedData$Short.Name, ignore.case=TRUE)
mergedData <- mergedData[coalMatches, ]

aggregatedTotalByYear <- aggregate(Emissions ~ year, mergedData, sum)



png("plot4.png", width=640, height=480)
g <- ggplot(aggregatedTotalByYear, aes(factor(year), Emissions))
g <- g + geom_bar(stat="identity") +
  xlab("year") +
  ylab(expression('Total PM2.5 Emissions')) +
  ggtitle('Total Emissions from coal sources from 1999 to 2008')
print(g)
dev.off()
