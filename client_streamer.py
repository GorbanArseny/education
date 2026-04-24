print('spark_reader_for_streaming')
import sys
import io
import socket
import select
import threading
import queue
import random
import time
import warnings
role='reader'
host ='localhost'
port = 9998

import findspark
findspark.init() 
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Эта команда находит Spark и добавляет его в Python path
import findspark
findspark.init() 

# Create Spark session
spark = (SparkSession.builder 
    .appName("main_session") # имя сесии
    # .config("spark.executor.memory", "2g") # память экзекьютеров в гигабайтах
    .master("local[*]") 
    .getOrCreate()
          )

# Читаем поток из TCP сокета
lines = spark.readStream \
    .format("socket") \
    .option("host", host)\
    .option("port", port)\
    .load()

print("Streaming source configured")
#-------------------------------------------------------------
warnings.filterwarnings("ignore") # отключение предупреждений

# "ignore" — полностью игнорировать предупреждение
# "default" — вывести предупреждение только в первый раз
# "error" — превратить предупреждение в исключение
# "always" — всегда выводить предупреждение
# "module" — выводить предупреждение только один раз в модуле
# "once" — выводить предупреждение только один раз (на уровне интерпретатора)
#---------------------------------------------------------------------
# Трансформация данных
words = lines.select(F.explode(F.split(lines.value, " ")).alias("word"))

# добавление времени
words_with_time = words.withColumn("timestamp", F.current_timestamp())

# Агрегация данных в 10-minute windows
windowed_counts = (words_with_time
    # .withWatermark('timestamp', '30 seconds')\
    .groupBy(
    F.window("timestamp", "10 seconds"),
    "word")\
    .agg(F.count(F.lit('1')).alias('count')))


# Write with checkpointing
query = windowed_counts.writeStream \
    .outputMode("update") \
    .format("console") \
    .option("checkpointLocation", "C:/work_space/my_scripts/streaming/spark_checkpoints/windowed_count") \
    .trigger(processingTime="10 seconds") \
    .start()

query.awaitTermination()
