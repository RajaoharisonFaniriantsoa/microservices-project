CREATE TABLE IF NOT EXISTS sales_data (
    id SERIAL PRIMARY KEY,
    product VARCHAR(50) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    sale_date DATE NOT NULL
);