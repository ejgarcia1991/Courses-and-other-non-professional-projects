library(ggplot2)
NEI <- readRDS("./data/summarySCC_PM25.rds")
SCC <- readRDS("./data/Source_Classification_Code.rds")

# How have emissions from motor vehicle sources changed from 1999-2008 in Baltimore City?
# Searching for ON-ROAD type in NEI for motor vehicles

filterNEI <- NEI[NEI$fips=="24510",  ]
filterNEI <- NEI[NEI$type=="ON-ROAD", ]

aggregatedTotalByYear <- aggregate(Emissions ~ year, filterNEI, sum)

png("plot5.png", width=840, height=480)
g <- ggplot(aggregatedTotalByYear, aes(factor(year), Emissions))
g <- g + geom_bar(stat="identity") +
  xlab("year") +
  ylab(expression('Total PM2.5 Emissions')) +
  ggtitle('Total Emissions from motor vehicle in Baltimore City from 1999 to 2008')
print(g)
dev.off()
