library(tidyverse)
library(here)
library(XML)
library(lubridate)
library(ggmap)
library(geosphere)
options(digits.secs = 3)
options(scipen = 999)

# parse GPX file

parsed <- htmlTreeParse(file = "C:/Users/zool2471/Downloads/Alt_Portsmouth.gpx", useInternalNodes = T)

# get values via via the respective xpath
coords <- xpathSApply(parsed, path = "//trkpt", xmlAttrs)
elev   <- xpathSApply(parsed, path = "//trkpt/ele", xmlValue)
ts_chr <- xpathSApply(parsed, path = "//trkpt/time", xmlValue)

# combine into df
dat_df <- data.frame(
  #ts_POSIXct = ymd_hms(ts_chr, tz = "EST"),
  lat = as.numeric(coords["lat",]), 
  lon = as.numeric(coords["lon",]), 
  elev = as.numeric(elev)
)
head(dat_df)

ggplot(dat_df, aes(x = 1:nrow(dat_df), y = elev)) + 
geom_line(size=2) + 
labs(x = "Time", y = "Elevation [m]") + 
theme_grey(base_size = 14) + theme_classic()
