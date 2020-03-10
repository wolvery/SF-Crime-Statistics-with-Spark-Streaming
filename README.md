# SF-Crime-Statistics-with-Spark-Streaming

## Project Overview
In this project, you will be provided with a real-world dataset, extracted from Kaggle, on San Francisco crime incidents, and you will provide statistical analyses of the data using Apache Spark Structured Streaming. You will draw on the skills and knowledge you've learned in this course to create a Kafka server to produce data, and ingest data through Spark Structured Streaming.

## Development Environment
You may choose to create your project in the workspace we provide here, or if you wish to develop your project locally, you will need to set up your environment properly as described below:

* Spark 2.4.3
* Scala 2.11.x
* Java 1.8.x
* Kafka build with Scala 2.11.x
* Python 3.6.x or 3.7.x

Environment Setup (Only Necessary if You Want to Work on the Project Locally on Your Own Machine)
## For Macs or Linux:
Download Spark from https://spark.apache.org/downloads.html. Choose "Prebuilt for Apache Hadoop 2.7 and later."
Unpack Spark in one of your folders (I usually put all my dev requirements in /home/users/user/dev).
Download binary for Kafka from this location https://kafka.apache.org/downloads, with Scala 2.11, version 2.3.0. Unzip in your local directory where you unzipped your Spark binary as well. Exploring the Kafka folder, you’ll see the scripts to execute in bin folders, and config files under config folder. You’ll need to modify zookeeper.properties and server.properties.
Download Scala from the official site, or for Mac users, you can also use brew install scala, but make sure you download version 2.11.x.
Run below to verify correct versions:
* java -version
* scala -version
Make sure your ~/.bash_profile looks like below (might be different depending on your directory):
* export SPARK_HOME=/Users/dev/spark-2.4.3-bin-hadoop2.7
* export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home
* export SCALA_HOME=/usr/local/scala/
* export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SCALA_HOME/bin:$PATH
## For Windows:
Please follow the directions found in this helpful StackOverflow post: https://stackoverflow.com/questions/25481325/how-to-set-up-spark-on-windows

## Execution Snapshots
<img src="Screenshot from 2020-03-10 20-13-01.png"/>
<img src="Screenshot from 2020-03-10 20-13-07.png"/>
<img src="Screenshot from 2020-03-10 20-13-33.png"/>

## Questions
* How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
I have changed maxOffsetPerTrigger and threads allocated but did not change the throughput. I believe it is because of the small potion of data.

* What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
I have checked spark.default.parallelism to 48 and maxOffsetsPerTrigger to some diferent values. It did increase the consumption of memory.
