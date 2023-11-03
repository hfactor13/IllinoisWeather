Field Name|Type|Description
-|-|-
stn|STRING|Cloud - GSOD NOAA
wban|STRING|WBAN number where applicable--this is the historical "Weather Bureau Air Force Navy" number - with WBAN being the acronym
date|DATE|Date of the weather observations
year|STRING|The year
mo|STRING|The month
da|STRING|The day
temp|FLOAT|Mean temperature for the day in degrees Fahrenheit to tenths. Missing = 9999.9
count_temp|INTEGER|Number of observations used in calculating mean temperature
dewp|FLOAT|Mean dew point for the day in degreesm Fahrenheit to tenths. Missing = 9999.9
count_dewp|INTEGER|Number of observations used in calculating mean dew point
slp|FLOAT|Mean sea level pressure for the day in millibars to tenths. Missing = 9999.9
count_slp|INTEGER|Number of observations used in calculating mean sea level pressure
stp|FLOAT|Mean station pressure for the day in millibars to tenths. Missing = 9999.9
count_stp|INTEGER|Number of observations used in calculating mean station pressure
visib|FLOAT|Mean visibility for the day in miles to tenths. Missing = 999.9
count_visib|INTEGER|Number of observations used in calculating mean visibility
wdsp|STRING|Mean wind speed for the day in knots to tenths. Missing = 999.9
count_wdsp|STRING|Number of observations used in calculating mean wind speed
mxpsd|STRING|Maximum sustained wind speed reported for the day in knots to tenths. Missing = 999.9
gust|FLOAT|Maximum wind gust reported for the day in knots to tenths. Missing = 999.9
max|FLOAT|Maximum temperature reported during the day in Fahrenheit to tenths--time of max temp report varies by country and region, so this will sometimes not be the max for the calendar day. Missing = 9999.9
flag_max|STRING|Blank indicates max temp was taken from the explicit max temp report and not from the 'hourly' data. * indicates max temp was derived from the hourly data (i.e., highest hourly or synoptic-reported temperature)
min|FLOAT|Minimum temperature reported during the day in Fahrenheit to tenths--time of min temp report varies by country and region, so this will sometimes not be the min for the calendar day. Missing = 9999.9
flag_min|STRING|Blank indicates min temp was taken from the explicit min temp report and not from the 'hourly' data. * indicates min temp was derived from the hourly data (i.e., lowest hourly or synoptic-reported temperature)
prcp|FLOAT|Total precipitation (rain and/or melted snow) reported during the day in inches and hundredths; will usually not end with the midnight observation--i.e., may include latter part of previous day. .00 indicates no measurable precipitation (includes a trace). Missing = 99.99 Note: Many stations do not report '0' on days with no precipitation--therefore, '99.99' will often appear on these days. Also, for example, a station may only report a 6-hour amount for the period during which rain fell. See Flag field for source of data
flag_prcp|STRING|A = 1 report of 6-hour precipitation amount B = Summation of 2 reports of 6-hour precipitation amount C = Summation of 3 reports of 6-hour precipitation amount D = Summation of 4 reports of 6-hour precipitation amount E = 1 report of 12-hour precipitation amount F = Summation of 2 reports of 12-hour precipitation amount G = 1 report of 24-hour precipitation amount H = Station reported '0' as the amount for the day (eg, from 6-hour reports), but also reported at least one occurrence of precipitation in hourly observations--this could indicate a trace occurred, but should be considered as incomplete data for the day. I = Station did not report any precip data for the day and did not report any occurrences of precipitation in its hourly observations--it's still possible that precip occurred but was not reported
sndp|FLOAT|Snow depth in inches to tenths--last report for the day if reported more thanonce. Missing = 999.9 Note: Most stations do not report '0' ondays with no snow on the ground--therefore, '999.9' will often appear on these days
fog|STRING|Indicators (1 = yes, 0 = no/not reported) for the occurrence during the day
rain_drizzle|STRING|Indicators (1 = yes, 0 = no/not reported) for the occurrence during the day
snow_ice_pellets|STRING|Indicators (1 = yes, 0 = no/not reported) for the occurrence during the day
hail|STRING|Indicators (1 = yes, 0 = no/not reported) for the occurrence during the day
thunder|STRING|Indicators (1 = yes, 0 = no/not reported) for the occurrence during the day
tornado_funnel_cloud|STRING|Indicators (1 = yes, 0 = no/not reported) for the occurrence during the day