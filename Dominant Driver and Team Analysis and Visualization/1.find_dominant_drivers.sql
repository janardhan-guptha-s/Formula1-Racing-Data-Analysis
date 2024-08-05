-- Databricks notebook source
-- MAGIC %md 
-- MAGIC ###Finding Dominant Driver

-- COMMAND ----------

select * from f1_presentation.calculated_race_results;

-- COMMAND ----------

SELECT driver_name,
      COUNT(1) AS total_races,
       SUM(calculated_points) AS total_points
  FROM f1_presentation.calculated_race_results
GROUP BY driver_name
ORDER BY total_points DESC

-- COMMAND ----------

SELECT driver_name,
       COUNT(1) AS total_races,
       SUM(calculated_points) AS total_points,
       AVG(calculated_points) AS avg_points
  FROM f1_presentation.calculated_race_results
GROUP BY driver_name
HAVING COUNT(1) >= 50
ORDER BY avg_points DESC

-- COMMAND ----------

SELECT driver_name,
       COUNT(1) AS total_races,
       SUM(calculated_points) AS total_points,
       AVG(calculated_points) AS avg_points
  FROM f1_presentation.calculated_race_results
 WHERE race_year BETWEEN 2011 AND 2020
GROUP BY driver_name
HAVING COUNT(1) >= 50
ORDER BY avg_points DESC

-- COMMAND ----------

SELECT driver_name,
       COUNT(1) AS total_races,
       SUM(calculated_points) AS total_points,
       AVG(calculated_points) AS avg_points
  FROM f1_presentation.calculated_race_results
 WHERE race_year BETWEEN 2001 AND 2010
GROUP BY driver_name
HAVING COUNT(1) >= 50
ORDER BY avg_points DESC
