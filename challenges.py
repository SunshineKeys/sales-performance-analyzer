# Day 2: CHALLENGES - SQL Thinking Practice

"""
🎯 INSTRUCTIONS:
These challenges simulate real data analyst interview questions.
Practice thinking in SQL terms even though you're using pandas!

💼 INTERVIEW TIP:
When you solve these, explain your logic out loud:
"I would GROUP BY region and SUM the revenue to get total sales per region"
This is exactly how you'd answer in an interview!
"""

import pandas as pd

df = pd.read_csv("sales_data.csv")

print("=" * 70)
print("DAY 2 CHALLENGES - SQL THINKING")
print("=" * 70)
print("\nOur sales data:")
print(df)

# ============================================
# CHALLENGE 1: SELECT SPECIFIC COLUMNS
# ============================================
print("\n🎯 CHALLENGE 1: Show Only Date and Revenue")
print("-" * 70)
print("Task: Create a DataFrame with just 'date' and 'revenue' columns")
print("SQL equivalent: SELECT date, revenue FROM sales")

# YOUR CODE HERE
date_revenue = df[['revenue', 'date']]
print("date and revenue only:")

# date_revenue = 

#Uncomment to test:
print(date_revenue)

"""
💡 HINT: Use double brackets df[['col1', 'col2']]
"""

# ============================================
# CHALLENGE 2: FILTER BY VALUE
# ============================================
print("\n🎯 CHALLENGE 2: High Revenue Sales")
print("-" * 70)
print("Task: Show only sales where revenue >= 1200")
print("SQL equivalent: SELECT * FROM sales WHERE revenue >= 1200")

# YOUR CODE HERE
high_sales = df[df['revenue'] > 1200]
print("Sales over $1200:")# Uncomment to test:
print(high_sales)

"""
💡 HINT: df[df['column'] >= value]
"""

# ============================================
# CHALLENGE 3: FILTER BY CATEGORY
# ============================================
print("\n🎯 CHALLENGE 3: West Region Only")
print("-" * 70)
print("Task: Show all sales from the West region")
print("SQL equivalent: SELECT * FROM sales WHERE region = 'West'")

# YOUR CODE HERE
west_sales = df[df['region'] == 'West']
print("\nWest region sales:")

# Uncomment to test:
print(west_sales)

"""
💡 HINT: df[df['column'] == 'value']
"""

# ============================================
# CHALLENGE 4: SUM AGGREGATION
# ============================================
print("\n🎯 CHALLENGE 4: Total Revenue")
print("-" * 70)
print("Task: Calculate the total revenue across all sales")
print("SQL equivalent: SELECT SUM(revenue) FROM sales")

# YOUR CODE HERE
total_revenue = df['revenue'].sum()
# Uncomment to test:
print(f"Total revenue: ${total_revenue}")

"""
💡 HINT: df['column'].sum()
"""

# ============================================
# CHALLENGE 5: GROUP BY WITH SUM
# ============================================
print("\n🎯 CHALLENGE 5: Revenue by Product")
print("-" * 70)
print("Task: Calculate total revenue for each product")
print("SQL equivalent: SELECT product, SUM(revenue) FROM sales GROUP BY product")

# YOUR CODE HERE
revenue_by_product = df.groupby('product')['revenue'].sum()
# Uncomment to test:
print(revenue_by_product)

"""
💡 HINT: df.groupby('column')['value_column'].sum()
"""

# ============================================
# CHALLENGE 6: COUNT BY CATEGORY
# ============================================
print("\n🎯 CHALLENGE 6: Sales Count by Region")
print("-" * 70)
print("Task: How many sales happened in each region?")
print("SQL equivalent: SELECT region, COUNT(*) FROM sales GROUP BY region")

# YOUR CODE HERE
sales_per_region = df.groupby('region')['revenue'].size()

# Uncomment to test:
print(sales_per_region)

"""
💡 HINT: df.groupby('column').size()
"""

# ============================================
# CHALLENGE 7: AVERAGE CALCULATION
# ============================================
print("\n🎯 CHALLENGE 7: Average Revenue by Region")
print("-" * 70)
print("Task: Calculate the average revenue for each region")
print("SQL equivalent: SELECT region, AVG(revenue) FROM sales GROUP BY region")

# YOUR CODE HERE
avg_by_region = df.groupby('region')['revenue'].mean()

# Uncomment to test:
print(avg_by_region)

"""
💡 HINT: df.groupby('column')['value'].mean()
"""

# ============================================
# CHALLENGE 8: SORTING
# ============================================
print("\n🎯 CHALLENGE 8: Sort by Revenue (Highest First)")
print("-" * 70)
print("Task: Show all sales sorted by revenue, highest to lowest")
print("SQL equivalent: SELECT * FROM sales ORDER BY revenue DESC")

# YOUR CODE HERE
sorted_sales = df.sort_values('revenue', ascending=False)

# Uncomment to test:
print(sorted_sales)

"""
💡 HINT: df.sort_values('column', ascending=False)
"""

# ============================================
# CHALLENGE 9: MULTIPLE CONDITIONS
# ============================================
print("\n🎯 CHALLENGE 9: East Region, Product A Only")
print("-" * 70)
print("Task: Show sales that are BOTH in East region AND for Product A")
print("SQL: SELECT * FROM sales WHERE region = 'East' AND product = 'A'")

# YOUR CODE HERE
east_product_a = df[(df['region'] == 'East') & (df['product'] == 'A')]

# Uncomment to test:
print(east_product_a)

"""
💡 HINT: df[(df['col1'] == 'val1') & (df['col2'] == 'val2')]
Don't forget parentheses!
"""

# ============================================
# CHALLENGE 10: FILTER THEN AGGREGATE
# ============================================
print("\n🎯 CHALLENGE 10: Total Revenue for Product B")
print("-" * 70)
print("Task: What's the total revenue for Product B only?")
print("SQL: SELECT SUM(revenue) FROM sales WHERE product = 'B'")

# YOUR CODE HERE
product_b_revenue = df[df['product'] == 'B']['revenue'].sum()

# Uncomment to test:
print(f"Product B total revenue: ${product_b_revenue}")

"""
💡 HINT: 
1. Filter: df[df['product'] == 'B']
2. Sum: ['revenue'].sum()
Can chain them: df[df['product'] == 'B']['revenue'].sum()
"""

# ============================================
# CHALLENGE 11: TOP N RESULTS
# ============================================
print("\n🎯 CHALLENGE 11: Top 3 Sales by Revenue")
print("-" * 70)
print("Task: Show the 3 highest-revenue sales")
print("SQL equivalent: SELECT * FROM sales ORDER BY revenue DESC LIMIT 3")

# YOUR CODE HERE
top_3_sales = df.sort_values('revenue', ascending=False).head(3)
print("\nTop 3 highest revenue sales:")

# Uncomment to test:
print(top_3_sales)

"""
💡 HINT: 
1. Sort descending: .sort_values('revenue', ascending=False) 
2. Take top 3: .head(3)
Chain them together!
"""

# ============================================
# CHALLENGE 12: MULTIPLE AGGREGATIONS
# ============================================
print("\n🎯 CHALLENGE 12: Multiple Stats by Product")
print("-" * 70)
print("Task: For each product, show total revenue, average revenue, and count")
print("SQL: SELECT product, SUM(revenue), AVG(revenue), COUNT(*)")
print("     FROM sales GROUP BY product")

# YOUR CODE HERE
product_stats = df.groupby('product')['revenue'].agg(['sum', 'mean', 'count'])

# Uncomment to test:
print(product_stats)

"""
💡 HINT: Use .agg(['sum', 'mean', 'count'])
df.groupby('product')['revenue'].agg(['sum', 'mean', 'count'])
"""

# ============================================
# CHALLENGE 13: PERCENTAGE CALCULATION
# ============================================
print("\n🎯 CHALLENGE 13: Region Revenue Percentages")
print("-" * 70)
print("Task: What percentage of total revenue came from each region?")
print("This is common in business analysis!")

# YOUR CODE HERE
# Steps:
# 1. Get total revenue by region
# 2. Get overall total
# 3. Calculate percentage: (region_total / overall_total) * 100
total_by_region = df.groupby('region')['revenue'].sum()
overall_total = df['revenue'].sum()
revenue_percentages = (total_by_region / overall_total) * 100
# Uncomment to test:
print(revenue_percentages)

"""
💡 HINT:
total_by_region = df.groupby('region')['revenue'].sum()
overall_total = df['revenue'].sum()
percentages = (total_by_region / overall_total) * 100
"""

# ============================================
# CHALLENGE 14: COMPLEX FILTERING
# ============================================
print("\n🎯 CHALLENGE 14: Find High-Value Sales in Specific Regions")
print("-" * 70)
print("Task: Show sales where revenue > 1000 AND region is East OR West")
print("SQL: SELECT * FROM sales")
print("     WHERE revenue > 1000 AND (region = 'East' OR region = 'West')")

# YOUR CODE HERE
complex_filter = df[(df['revenue'] > 1000) & ((df['region'] == 'East') | (df['region'] == 'West'))]

# Uncomment to test:
print(complex_filter)

"""
💡 HINT:
revenue_filter = df['revenue'] > 1000
region_filter = (df['region'] == 'East') | (df['region'] == 'West')
result = df[revenue_filter & region_filter]

Or in one line (harder to read but more concise):
df[(df['revenue'] > 1000) & ((df['region'] == 'East') | (df['region'] == 'West'))]
"""

# ============================================
# CHALLENGE 15: BUSINESS QUESTION (HARDEST!)
# ============================================
print("\n🎯 CHALLENGE 15: Which Product is Best in Each Region?")
print("-" * 70)
print("Task: For each region, show which product had the highest revenue")
print("This requires advanced pandas - try your best!")

# YOUR CODE HERE
# Hint: You'll need .groupby() and .idxmax() or .sort_values()
# This is challenging - don't worry if it takes time!
print("\nBest product by region:")

for region in df['region'].unique():
    region_data = df[df['region'] == region]
    product_revenue = region_data.groupby('product')['revenue'].sum()
    best_product = product_revenue.idxmax()
    best_revenue = product_revenue.max()
    print(f"  {region}: Product {best_product} (${best_revenue})")

"""
💡 ADVANCED HINT:
1. Group by both region AND product: .groupby(['region', 'product'])
2. Sum revenue: ['revenue'].sum()
3. Sort or find max per region
OR
1. Group by region: .groupby('region')
2. Use .apply() with a custom function
This is advanced! Research .idxmax() or .nlargest() if stuck
"""

print("\n" + "=" * 70)
print("🎓 ONCE YOU COMPLETE THESE:")
print("=" * 70)
print("1. You understand SQL-style operations in pandas")
print("2. You can answer 80% of entry-level data analyst interview questions")
print("3. Move to portfolio_project.py to build your sales analyzer")
print("")
print("💼 INTERVIEW READY:")
print("You can now say 'Yes, I know SQL' and back it up with examples!")
print("=" * 70)
