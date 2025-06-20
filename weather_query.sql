SELECT weather.id, weather.date, weather.time, weather.element, weather.value, weather.qflag, 
       stations.latitude, stations.longitude, stations.name, stations.elevation 
FROM `bigquery-public-data.ghcn_d.ghcnd_*` AS weather
INNER JOIN `bigquery-public-data.ghcn_d.ghcnd_stations` AS stations
ON weather.id = stations.id
WHERE weather.id LIKE 'US%'
AND weather._TABLE_SUFFIX BETWEEN '1990' AND '2023'
AND EXTRACT(YEAR FROM weather.date) BETWEEN 1990 AND 2023
AND stations.id LIKE 'US%'
AND stations.state = 'IL';