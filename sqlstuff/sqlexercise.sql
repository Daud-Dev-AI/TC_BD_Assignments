drop database if exists newexample;
create database newexample;
use newexample;

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price DECIMAL(10,2)
);

CREATE TABLE Sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    quantity_sold INT,
    sale_date DATE,
    total_price DECIMAL(10,2),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Products (product_id, product_name, category, unit_price) VALUES
(101, 'Laptop', 'Electronics', 500.00),
(102, 'Smartphone', 'Electronics', 300.00),
(103, 'Headphones', 'Electronics', 30.00),
(104, 'Keyboard', 'Electronics', 20.00),
(105, 'Mouse', 'Electronics', 15.00);

INSERT INTO Sales (sale_id, product_id, quantity_sold, sale_date, total_price) VALUES
(1, 101, 5, '2024-01-01', 2500.00),
(2, 102, 3, '2024-01-02', 900.00),
(3, 103, 2, '2024-01-02', 60.00),
(4, 104, 4, '2024-01-03', 80.00),
(5, 105, 6, '2024-01-03', 90.00),
(6, 105, 8, '2024-02-03', 920.00);

-- Q1 Retrieve all columns from the Sales table
SELECT * FROM Sales;

-- Q2 Retrieve product_name and unit_price from Products table
SELECT product_name, unit_price FROM Products;

-- Q3 Retrieve sale_id and sale_date from Sales
SELECT sale_id, sale_date FROM Sales;

-- Q4 Show sales with total_price greater than 100
SELECT * FROM Sales
WHERE total_price > 100;

-- Q5 Show products only in Electronics category
SELECT * FROM Products
WHERE category = 'Electronics';

-- Q6 Retrieve sale_id and total_price for sales on Jan 3 2024
SELECT sale_id, total_price FROM Sales
WHERE sale_date = '2024-01-03';

-- Q7 Retrieve product_id and product_name where unit_price > 100
SELECT product_id, product_name FROM Products
WHERE unit_price > 100;

-- Q8 Calculate total revenue from all sales
SELECT SUM(total_price) AS total_revenue FROM Sales;

-- Q9 Find average unit_price of products
SELECT AVG(unit_price) AS average_price FROM Products;

-- Q10 Find total quantity sold
SELECT SUM(quantity_sold) AS total_quantity_sold FROM Sales;

-- Q11 Count number of sales per day
SELECT sale_date, COUNT(*) AS sales_count FROM Sales
GROUP BY sale_date;

-- Q12 Find product with highest unit price
SELECT product_name, unit_price FROM Products
WHERE unit_price = (SELECT MAX(unit_price) FROM Products);

-- Q13 Retrieve sale_id, product_id and total_price where quantity_sold > 4
SELECT sale_id, product_id, total_price FROM Sales
WHERE quantity_sold > 4;

-- Q14 Order products by unit_price descending
SELECT product_name, unit_price FROM Products
ORDER BY unit_price DESC;

-- Q15 Round total_price to two decimals
SELECT sale_id, ROUND(total_price,2) AS rounded_total_price FROM Sales;

-- Q16 Find average total_price of sales
SELECT AVG(total_price) AS avg_total_price FROM Sales;

-- Q17 Format sale_date as YYYY-MM-DD
SELECT sale_id, DATE_FORMAT(sale_date,'%Y-%m-%d') AS formatted_date FROM Sales;

-- Q18 Total revenue from Electronics category
SELECT SUM(Sales.total_price) AS electronics_revenue FROM Sales
JOIN Products
ON Products.product_id = Sales.product_id
WHERE Products.category = 'Electronics';

-- Q19 Find products priced between 20 and 600
SELECT product_name, unit_price FROM Products
WHERE unit_price BETWEEN 20 AND 600;

-- Q20 List product_name and category ordered by category
SELECT product_name, category FROM Products
ORDER BY category ASC;

-- INTERMEDIATE LEVEL QUERIES
-- Q1 Total quantity sold for Electronics category
-- Explanation: join tables then sum quantity
SELECT SUM(Sales.quantity_sold) AS electronics_quantity FROM Sales
JOIN Products
ON Sales.product_id = Products.product_id
WHERE Products.category = 'Electronics';

-- Q2 Retrieve product_name and computed total_price
SELECT Products.product_name,
       Sales.quantity_sold * Products.unit_price AS computed_total_price
FROM Sales
JOIN Products
ON Sales.product_id = Products.product_id;

-- Q3 Find most frequently sold product
SELECT Products.product_name,
       COUNT(*) AS times_sold
FROM Sales
JOIN Products
ON Sales.product_id = Products.product_id
GROUP BY Products.product_id, Products.product_name
ORDER BY times_sold DESC
LIMIT 1;

-- Q4 Find products that have not been sold
-- Explanation: LEFT JOIN keeps products even without sales
SELECT Products.product_id, Products.product_name
FROM Products
LEFT JOIN Sales
ON Products.product_id = Sales.product_id
WHERE Sales.product_id IS NULL;

-- Q5 Total revenue per category
-- Explanation: group by category and sum revenue
SELECT Products.category,
       SUM(Sales.total_price) AS category_revenue
FROM Sales
JOIN Products
ON Sales.product_id = Products.product_id
GROUP BY Products.category;

-- Q6 Category with highest average price
-- Explanation: find avg price per category
SELECT category,
       AVG(unit_price) AS avg_unit_price
FROM Products
GROUP BY category
ORDER BY avg_unit_price DESC
LIMIT 1;

-- Q7 Products with total quantity sold greater than 30
-- Explanation: HAVING filters aggregated results
SELECT Products.product_id,
       Products.product_name,
       SUM(Sales.quantity_sold) AS total_quantity
FROM Sales
JOIN Products
ON Sales.product_id = Products.product_id
GROUP BY Products.product_id, Products.product_name
HAVING SUM(Sales.quantity_sold) > 30;

-- Q8 Count sales per month
-- Explanation: extract year and month from date
SELECT YEAR(sale_date) AS year,
       MONTH(sale_date) AS month,
       COUNT(*) AS sales_count
FROM Sales
GROUP BY YEAR(sale_date), MONTH(sale_date)
ORDER BY year, month;

-- Q9 Sales details for products containing 'Smart'
-- Explanation: LIKE pattern search
SELECT Sales.sale_id,
       Sales.product_id,
       Sales.quantity_sold,
       Sales.sale_date,
       Sales.total_price
FROM Sales
JOIN Products
ON Sales.product_id = Products.product_id
WHERE Products.product_name LIKE '%Smart%';

-- Q10 Average quantity sold where unit_price > 100
-- Explanation: filter expensive products then average
SELECT AVG(Sales.quantity_sold) AS avg_quantity
FROM Sales
JOIN Products
ON Sales.product_id = Products.product_id
WHERE Products.unit_price > 100;

-- Q11 Product name and total sales revenue per product
-- Explanation: sum revenue grouped by product
SELECT Products.product_name,
       SUM(Sales.total_price) AS total_revenue
FROM Sales
JOIN Products
ON Sales.product_id = Products.product_id
GROUP BY Products.product_id, Products.product_name;

-- Q12 List all sales with corresponding product names
-- Explanation: join tables to display readable names
SELECT Sales.sale_id,
       Products.product_name,
       Sales.quantity_sold,
       Sales.sale_date,
       Sales.total_price
FROM Sales
JOIN Products
ON Sales.product_id = Products.product_id;

-- Q13 Retrieve the product name and total sales revenue for each product
-- Explanation: JOIN Sales + Products, then SUM(total_price) per product
SELECT p.product_name,
       SUM(s.total_price) AS total_sales_revenue
FROM Sales s
JOIN Products p
ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name;

-- Q14 Rank products based on total sales revenue
-- Explanation: aggregate revenue per product, then RANK() by revenue (MySQL 8+)
SELECT product_name,
       total_sales_revenue,
       RANK() OVER (ORDER BY total_sales_revenue DESC) AS revenue_rank
FROM (
    SELECT p.product_name,
           SUM(s.total_price) AS total_sales_revenue
    FROM Sales s
    JOIN Products p
    ON p.product_id = s.product_id
    GROUP BY p.product_id, p.product_name
) t;

-- Q15 Calculate the running total revenue for each product category
-- Explanation: first get revenue per category per day, then running SUM over time
SELECT category,
       sale_date,
       daily_revenue,
       SUM(daily_revenue) OVER (PARTITION BY category ORDER BY sale_date) AS running_category_revenue
FROM (
    SELECT p.category,
           s.sale_date,
           SUM(s.total_price) AS daily_revenue
    FROM Sales s
    JOIN Products p
    ON p.product_id = s.product_id
    GROUP BY p.category, s.sale_date
) t
ORDER BY category, sale_date;

-- Q16 Categorize sales as "High", "Medium", or "Low" based on total_price
-- Explanation: CASE gives labels based on thresholds
SELECT sale_id,
       total_price,
       CASE
           WHEN total_price >= 1000 THEN 'High'
           WHEN total_price >= 100 THEN 'Medium'
           ELSE 'Low'
       END AS sale_category
FROM Sales;

-- Q17 Identify sales where quantity_sold is greater than the average quantity_sold
-- Explanation: compare each row to AVG(quantity_sold) across all sales
SELECT *
FROM Sales
WHERE quantity_sold > (SELECT AVG(quantity_sold) FROM Sales);

-- Q18 Extract the month and year from sale_date and count sales per month
-- Explanation: group by YEAR and MONTH of sale_date
SELECT YEAR(sale_date) AS sale_year,
       MONTH(sale_date) AS sale_month,
       COUNT(*) AS sales_count
FROM Sales
GROUP BY YEAR(sale_date), MONTH(sale_date)
ORDER BY sale_year, sale_month;

-- Q19 Calculate days between current date and sale_date for each sale
-- Explanation: DATEDIFF returns number of days between two dates
SELECT sale_id,
       sale_date,
       DATEDIFF(CURDATE(), sale_date) AS days_since_sale
FROM Sales;

-- Q20 Identify sales made during weekdays versus weekends
-- Explanation: DAYOFWEEK() returns 1=Sunday ... 7=Saturday in MySQL
SELECT sale_id,
       sale_date,
       CASE
           WHEN DAYOFWEEK(sale_date) IN (1, 7) THEN 'Weekend'
           ELSE 'Weekday'
       END AS day_type
FROM Sales;

-- Advanced Questions
-- Q1 List top 3 products by revenue contribution percentage
SELECT p.product_id, p.product_name, SUM(s.total_price) AS total_product_revenue, 
(100 * sum(s.total_price) / (SELECT SUM(total_price) FROM Sales)) AS contribution_perct
FROM Sales s
JOIN Products p ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
ORDER BY contribution_perct DESC
LIMIT 3;

-- Q2 Write a query to create a view named Total_Sales that displays the total 
-- sales amount for eachproduct along with their names and categories.
CREATE VIEW Total_Sales AS
SELECT
p.product_id,
p.product_name,
p.category,
SUM(s.total_price) AS total_sales_amount
FROM Products p
LEFT JOIN Sales s ON s.product_id = p.product_id
GROUP BY p.product_id, p.product_name, p.category;

-- Q3 Display products that have greater than avg quantity sold across all products
SELECT p.product_id, p.product_name, p.category, p.unit_price 
FROM Products p
JOIN Sales s on s.product_id = p.product_id
GROUP BY p.product_id, p.product_name, p.category, p.unit_price
HAVING sum(s.quantity_sold) > (
	SELECT avg(total_qty) 
    FROM (
		SELECT SUM(quantity_sold) AS total_qty
        FROM Sales
        GROUP BY product_id
    ) x
);

-- Q4 Explain the significance of indexing in SQL databases and provide example that improves performance
-- ANS: Indexing creates a fast lookup structure 
-- that reduces full table scans, improving read performance (but adds overhead on inserts/updates).
-- Example index can be applied on date column as people would want to query by date a lot. Consider:
-- CREATE INDEX idx_sales_sale_date on Sales(sale_date);

-- Q5 Foreign Key constraint addition to sales referencing product_id;
-- ANS: Already added but if needed to be added later on, this would be used:
ALTER TABLE Sales
ADD CONSTRAINT fk_product_id
FOREIGN KEY (product_id) REFERENCES Products(product_id);

-- Q6 Create a view Top_Products listing top 3 products sold
CREATE OR REPLACE VIEW Top_Products AS
	SELECT p.product_id, p.product_name, sum(s.quantity_sold) as total_sold
    FROM Sales s
    JOIN Products p ON p.product_id = s.product_id
    GROUP BY p.product_id, p.product_name
    ORDER BY total_sold DESC
    LIMIT 3;

-- Q7 Implement transaction that deducts quantity_sold from Products when
-- a sale in Sales table is made, ensure committment or rollback
-- ANS: Introducing inventory column in Products table to allow for deductions.
ALTER TABLE Products
ADD COLUMN Inventory int NOT NULL default 0;

START TRANSACTION;


