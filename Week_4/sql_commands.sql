SELECT COUNT (*) FROM de-zoomcamp-2024-410417.dbt_madkadanalyses.fact_fhv_trips

SELECT 
	COUNT(1),
	TIMESTAMP_TRUNC(pickup_datetime, MONTH) AS year_month,
  service_type
FROM de-zoomcamp-2024-410417.dbt_madkadanalyses.fact_trips
GROUP BY 2,3

SELECT 
	COUNT(1),
	TIMESTAMP_TRUNC(pickup_datetime, MONTH) AS year_month,
  service_type
FROM de-zoomcamp-2024-410417.dbt_madkadanalyses.fact_trips
GROUP BY 2,3
