library(ggplot2)


NEI <- readRDS("./data/summarySCC_PM25.rds")
SCC <- readRDS("./data/Source_Classification_Code.rds")

# Compare emissions from motor vehicle sources in Baltimore City with emissions from motor 
# vehicle sources in Los Angeles County, California (fips == "06037"). 
# Which city has seen greater changes over time in motor vehicle emissions?

# 24510 is Baltimore, 06037 is LA CA
# Searching for ON-ROAD type in NEI for motor vehicles
filterNEI <- NEI[(NEI$fips=="24510"|NEI$fips=="06037"),  ]
filterNEI <- NEI[NEI$type=="ON-ROAD",]

aggregatedTotalByYearAndFips <- aggregate(Emissions ~ year + fips, filterNEI, sum)
aggregatedTotalByYearAndFips$fips[aggregatedTotalByYearAndFips$fips=="24510"] <- "Baltimore, MD"
aggregatedTotalByYearAndFips$fips[aggregatedTotalByYearAndFips$fips=="06037"] <- "Los Angeles, CA"

png("plot6.png", width=1040, height=480)
g <- ggplot(aggregatedTotalByYearAndFips, aes(factor(year), Emissions))
g <- g + facet_grid(. ~ fips)
g <- g + geom_bar(stat="identity")  +
  xlab("year") +
  ylab(expression('Total PM2.5 Emissions')) +
  ggtitle('Total Emissions from motor vehicle in Baltimore City vs Los Angeles, CA 1999-2008')
print(g)
dev.off()
