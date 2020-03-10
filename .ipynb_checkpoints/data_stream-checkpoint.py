import logging
import json
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as psf


# TODO Create a schema for incoming resources
schema = StructType([
    StructField('crime_id', IntegerType(), True), 
    StructField('original_crime_type_name', StringType(), True), 
    StructField('report_date', TimestampType(), True), 
    StructField('call_date', TimestampType(), True), 
    StructField('offense_date', TimestampType(), True), 
    StructField('call_time', StringType(), True), 
    StructField('call_date_time', TimestampType(), True), 
    StructField('disposition', StringType(), True), 
    StructField('address', StringType(), True), 
    StructField('city', StringType(), True), 
    StructField('state', StringType(), True), 
    StructField('agency_id', IntegerType(), True), 
    StructField('address_type', StringType(), True), 
    StructField('common_location', StringType(), True)
])

def run_spark_job(spark):

    # TODO Create Spark Configuration
    # Create Spark configurations with max offset of 200 per trigger
    # set up correct bootstrap server and port
    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "udacity.police.department.calls") \
        .option("startingOffsets", "earliest") \
        .load()
        

    # Show schema for the incoming resources for checks
    df.printSchema()

    # TODO extract the correct column from the kafka input resources
    # Take only value and convert it to String
    kafka_df = df.selectExpr(" cast (value as STRING)")

    service_table = kafka_df\
        .select(psf.from_json(psf.col('value'), schema).alias("DF"))\
        .select("DF.*")

    distinct_table = service_table.select("call_date_time", "original_crime_type_name", "disposition")
    agg_df = distinct_table \
            .withWatermark("call_date_time", "60 minutes") \
            .groupBy(psf.window(distinct_table.call_date_time, "10 minutes", "5 minutes"), psf.col("original_crime_type_name"))\
            .count() 

   
    query = agg_df \
            .writeStream \
            .outputMode('complete') \
            .format('console') \
            .start()                                                                                                                 
                                                                                                                                     

    # TODO attach a ProgressReporter
    query.awaitTermination()

    radio_code_json_filepath = "radio_code.json"
    radio_code_df = spark.read.json(radio_code_json_filepath)

    # clean up your data so that the column names match on radio_code_df and agg_df
    # we will want to join on the disposition code

    radio_code_df = radio_code_df.withColumnRenamed("disposition_code", "disposition")

    join_query = agg_df.join(radio_code_df, "disposition") \
        .writeStream \
        .format("console") \
        .queryName("join") \
        .start()


    join_query.awaitTermination()


if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    spark = SparkSession \
        .builder \
        .master("local") \
        .appName("KafkaSparkStructuredStreaming") \
        .getOrCreate()

    logger.info("Spark started")

    run_spark_job(spark)

    spark.stop()
