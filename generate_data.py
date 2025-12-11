
import pandas as pd
import numpy as np
import random
import time
from datetime import datetime, timedelta

def generate_data(num_users=1000, num_products=500, num_transactions=100000):
    print(f"Generating data: {num_users} users, {num_products} products, {num_transactions} transactions...")
    
    # 1. Generate Products
    categories = ['Electronics', 'Home', 'Clothing', 'Books', 'Sports']
    products = []
    for i in range(1, num_products + 1):
        products.append({
            'product_id': i,
            'category': random.choice(categories),
            'price': round(random.uniform(10, 1000), 2)
        })
    df_products = pd.DataFrame(products)
    df_products.to_csv('products.csv', index=False)
    print(f"Saved products.csv ({len(df_products)} rows)")

    # 2. Generate Transactions
    # Simulate a "Big Data" stream with timestamps
    data = []
    start_date = datetime(2024, 1, 1)
    
    user_ids = np.random.randint(1, num_users + 1, num_transactions)
    product_ids = np.random.randint(1, num_products + 1, num_transactions)
    ratings = np.random.randint(1, 6, num_transactions) # 1 to 5 stars
    
    # Vectorized date generation for speed
    timestamps = [start_date + timedelta(days=random.randint(0, 365)) for _ in range(num_transactions)]
    
    df_transactions = pd.DataFrame({
        'user_id': user_ids,
        'product_id': product_ids,
        'rating': ratings,
        'timestamp': timestamps
    })
    
    # Add some noise (nulls/duplicates) to make cleaning necessary
    # 1. Duplicate some rows
    df_transactions = pd.concat([df_transactions, df_transactions.sample(n=int(num_transactions * 0.01))])
    
    df_transactions.to_csv('transactions.csv', index=False)
    print(f"Saved transactions.csv ({len(df_transactions)} rows)")

if __name__ == "__main__":
    # Generate enough data to be significant but fast to run
    generate_data(num_users=5000, num_products=1000, num_transactions=200000)
