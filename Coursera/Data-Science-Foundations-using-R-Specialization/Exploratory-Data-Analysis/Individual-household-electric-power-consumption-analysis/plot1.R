## read the data
data <- read.table("household_power_consumption.txt", stringsAsFactors= F, header = T, sep =";",na.strings = "?")

## convert dates and times
data$Time <- strptime(paste(data$Date, data$Time, sep = " "), format = "%d/%m/%Y %H:%M:%S")
data[, 1] <- as.Date(data$Date, format = "%d/%m/%Y")

## getting the subset
data <- data[format(data$Date, "%Y-%m-%d") == "2007-02-01" | format(data$Date, "%Y-%m-%d") == "2007-02-02" ,]

## plotting plot1.png
png(filename = "plot1.png")
hist(data$Global_active_power, col = "red", xlab = "Global Active Power (kilowatts)", main ="Global Active Power")
dev.off()
