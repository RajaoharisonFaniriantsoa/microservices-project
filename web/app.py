from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

# Configuration de la base de données
db_config = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        
        # Récupération des données avec gestion des erreurs
        sales = []
        stats = (0, 0.0, 0.0)  # Valeurs par défaut
        
        try:
            cur.execute("SELECT * FROM sales_data")
            sales = cur.fetchall()
            
            cur.execute("""
                SELECT COUNT(*) as total, 
                       AVG(amount) as avg_amount, 
                       MAX(amount) as max_sale 
                FROM sales_data
            """)
            stats = cur.fetchone() or (0, 0.0, 0.0)
        except psycopg2.Error as e:
            print(f"Database error: {e}")
        
        cur.close()
        conn.close()
        
        return render_template('index.html', sales=sales, stats=stats)
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)