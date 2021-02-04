## read the data
data <- read.table("household_power_consumption.txt", stringsAsFactors= F, header = T, sep =";",na.strings = "?")

## convert dates and times
data$Time <- strptime(paste(data$Date, data$Time, sep = " "), format = "%d/%m/%Y %H:%M:%S")
data[, 1] <- as.Date(data$Date, format = "%d/%m/%Y")

## getting the subset
data <- data[format(data$Date, "%Y-%m-%d") == "2007-02-01" | format(data$Date, "%Y-%m-%d") == "2007-02-02" ,]

## plotting plot2.png
png(filename = "plot2.png")
plot(data$Time, data$Global_active_power, type = "l", xlab= "", ylab = "Global Active Power (kilowatts)")
dev.off()
