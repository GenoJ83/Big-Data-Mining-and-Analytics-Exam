from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp

# 1. Justify Big Data (50 words)
"""
Justification:
The Retail Recommendation scenario involves processing high-volume transactional data (millions of rows) with high velocity (real-time purchases). 
Relational databases struggle with such scale and unstructured correlations. 
A Big Data platform like Apache Spark is necessary for distributed processing, enabling scalable collaborative filtering and real-time personalized recommendations.
"""

def run_preprocessing():
    # 2. Tool Selection: PySpark
    print("Initializing Spark Session...")
    spark = SparkSession.builder \
        .appName("RetailRecommendation_Preprocessing") \
        .config("spark.driver.memory", "2g") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    # 3. Data Acquisition (Loaded from generated CSVs)
    print("Loading data...")
    # transactions.csv has a header
    df = spark.read.csv("transactions.csv", header=True, inferSchema=True)
    
    print(f"Initial raw count: {df.count()}")
    df.show(5)

    # 4. Distributed Processing: Cleaning and Transformation
    print("Cleaning data...")
    
    # Remove duplicates
    df_clean = df.dropDuplicates()
    
    # Drop rows with nulls (if any)
    df_clean = df_clean.dropna()

    # Transformation: Ensure timestamp is actual timestamp type
    df_clean = df_clean.withColumn("timestamp", to_timestamp(col("timestamp")))
    
    # Cast user_id and product_id to integer (just in case)
    df_clean = df_clean.withColumn("user_id", col("user_id").cast("integer")) \
                       .withColumn("product_id", col("product_id").cast("integer")) \
                       .withColumn("rating", col("rating").cast("float"))

    print(f"Cleaned count: {df_clean.count()}")
    df_clean.printSchema()
    
    # Save processed data for Part B (optional, or just pass in memory if combined)
    # For this script we just verify it works
    print("Preprocessing complete.")
    
    spark.stop()

if __name__ == "__main__":
    run_preprocessing()
