import os
import psycopg2
import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import random

db_config = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

def generate_sales_data():
    """Génère des données de vente aléatoires et les insère dans la base de données"""
    products = ['Ordinateur', 'téléphone', 'Tablet', 'Moniteur', 'Clavier']
    
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sales_data (
            id SERIAL PRIMARY KEY,
            product VARCHAR(50) NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            sale_date DATE NOT NULL
        )
    """)
    
    for i in range(100):
        product = random.choice(products)
        amount = round(random.uniform(100000, 5000000), 2)
        date = datetime.now() - timedelta(days=random.randint(0, 30))
        
        cur.execute(
            "INSERT INTO sales_data (product, amount, sale_date) VALUES (%s, %s, %s)",
            (product, amount, date)
        )
    
    conn.commit()
    cur.close()
    conn.close()

def analyze_data():
    """Analyse les données et affiche des statistiques"""
    conn = psycopg2.connect(**db_config)
    
    df = pd.read_sql("SELECT * FROM sales_data", conn)
    
    print("\n=== Sales Statistics ===")
    print(f"Total sales: {len(df)}")
    print(f"Total revenue: {df['amount'].sum():.2f}MGA")
    print(f"Average sale: {df['amount'].mean():.2f}MGA")
    
    print("\n=== Product Analysis ===")
    product_stats = df.groupby('product')['amount'].agg(['count', 'sum', 'mean'])
    print(product_stats)
    
    print("\n=== Simple Trend Analysis ===")
    df['day_num'] = (df['sale_date'] - df['sale_date'].min()).dt.days
    model = LinearRegression()
    model.fit(df[['day_num']], df['amount'])
    print(f"Trend slope: {model.coef_[0]:.2f} (positive if increasing)")
    
    conn.close()

if __name__ == "__main__":
    print("Data Processor Service Started")
    generate_sales_data()
    analyze_data()
    print("Processing Complete")