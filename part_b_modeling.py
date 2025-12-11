from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import col
import time

def run_modeling():
    spark = SparkSession.builder \
        .appName("RetailRecommendation_Modeling") \
        .config("spark.driver.memory", "4g") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    # 1. Load Cleaned Data (Repeating load for independent execution)
    print("Loading data for modeling...")
    df = spark.read.csv("transactions.csv", header=True, inferSchema=True)
    
    # Cast necessary columns
    df = df.withColumn("user_id", col("user_id").cast("integer")) \
           .withColumn("product_id", col("product_id").cast("integer")) \
           .withColumn("rating", col("rating").cast("float"))

    # Split data
    (training, test) = df.randomSplit([0.8, 0.2], seed=42)
    print(f"Training count: {training.count()}, Test count: {test.count()}")

    # 2. Technique Selection: ALS (Alternating Least Squares)
    # Justification: ALS is the standard scalable algorithm for collaborative filtering in Spark.
    
    # 3. Model Scalability & Execution
    print("Training ALS model (Base)...")
    als = ALS(maxIter=5, regParam=0.01, userCol="user_id", itemCol="product_id", ratingCol="rating",
              coldStartStrategy="drop")
    
    start_time = time.time()
    model = als.fit(training)
    train_time = time.time() - start_time
    print(f"Base Model Training Time: {train_time:.2f} seconds")

    # 4. Result Interpretation (Base)
    predictions = model.transform(test)
    evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
    rmse = evaluator.evaluate(predictions)
    print(f"Base Model Root-mean-square error = {rmse:.4f}")

    # 3b. Optimization (Simple Manual Tuning/Grid Search simulation)
    print("\nOptimizing Model (rank=20, maxIter=10)...")
    als_opt = ALS(rank=20, maxIter=10, regParam=0.1, userCol="user_id", itemCol="product_id", ratingCol="rating",
                  coldStartStrategy="drop")
    
    start_time = time.time()
    model_opt = als_opt.fit(training)
    opt_time = time.time() - start_time
    print(f"Optimized Model Training Time: {opt_time:.2f} seconds")
    
    predictions_opt = model_opt.transform(test)
    rmse_opt = evaluator.evaluate(predictions_opt)
    print(f"Optimized Model Root-mean-square error = {rmse_opt:.4f}")
    
    print("\nComparison:")
    print(f"Improvement in RMSE: {rmse - rmse_opt:.4f}")

    # Generate top 3 recommendations for a few users
    print("\nGenerating Top 3 Recommendations for 5 users...")
    userRecs = model_opt.recommendForAllUsers(3)
    userRecs.show(5, truncate=False)

    spark.stop()

if __name__ == "__main__":
    run_modeling()
