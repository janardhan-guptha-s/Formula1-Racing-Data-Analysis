# Databricks notebook source
v_result = dbutils.notebook.run("1.Ingest_circuits_file", 0, {"p_data_source": "Ergast API", "p_file_date": "2021-03-21"})
v_result

# COMMAND ----------

v_result = dbutils.notebook.run("2.Ingest_race_file", 0, {"p_data_source": "Ergast API", "p_file_date": "2021-03-21"})

# COMMAND ----------


v_result = dbutils.notebook.run("3.ingest_constructors_file", 0, {"p_data_source": "Ergast API", "p_file_date": "2021-03-21"})

# COMMAND ----------

v_result = dbutils.notebook.run("4.ingect_driver.json file", 0, {"p_data_source": "Ergast API", "p_file_date": "2021-03-21"})

# COMMAND ----------

v_result = dbutils.notebook.run("5.ingest_results_file.json", 0, {"p_data_source": "Ergast API",, "p_file_date": "2021-03-21"})

# COMMAND ----------

v_result = dbutils.notebook.run("6.ingest_pit_stops_file", 0, {"p_data_source": "Ergast API",, "p_file_date": "2021-03-21"})

# COMMAND ----------

v_result = dbutils.notebook.run("7.ingest_lap_times_file", 0, {"p_data_source": "Ergast API", "p_file_date": "2021-03-21"})

# COMMAND ----------

v_result = dbutils.notebook.run("8.ingest_qualifying_file", 0, {"p_data_source": "Ergast API"})

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT race_id,count(1)
# MAGIC FROM f1_processed.results
# MAGIC GROUP BY race_id
# MAGIC ORDER BY race_id DESC;

# COMMAND ----------


