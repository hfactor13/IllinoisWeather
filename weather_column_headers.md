Field Name|Type|Description
-|-|-
id | STRING | The station ID
date | DATE | The date at which the observation was taken.
element | STRING | This is the kind of observation (i.e. average temperature, snowfall, snow depth, wind, etc.). See this URL for more details https://docs.opendata.aws/noaa-ghcn-pds/readme.html#:~:text=SNWD%20%3D%20Snow%20depth%20(mm),temperature%20(tenths%20of%20degrees%20C).
value | FLOAT | The value of the observation varies depending on the element. See this URL https://docs.opendata.aws/noaa-ghcn-pds/readme.html#:~:text=SNWD%20%3D%20Snow%20depth%20(mm),temperature%20(tenths%20of%20degrees%20C).
qflag | STRING | This is the measurement quality flag. The observations that matter are the one's that don't have any failures for the quality assurance check. See this URL https://docs.opendata.aws/noaa-ghcn-pds/readme.html#:~:text=SNWD%20%3D%20Snow%20depth%20(mm),temperature%20(tenths%20of%20degrees%20C).