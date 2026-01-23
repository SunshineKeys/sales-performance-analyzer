# Day 2: SQL Thinking with Pandas - LEARN BY DOING
# Master the operations that show up in EVERY data analyst interview

"""
🎯 LEARNING OBJECTIVES FOR DAY 2:
By the end of this lesson, you will understand:
1. How SQL and pandas are related (spoiler: they're very similar!)
2. SELECT operations (choosing specific columns)
3. WHERE filtering (conditional logic)
4. GROUP BY with aggregations (SUM, AVG, COUNT, MAX, MIN)
5. ORDER BY sorting
6. How to chain multiple operations together

💼 WHY THIS MATTERS:
SQL is tested in ~80% of data analyst interviews.
Even if the job uses Python, they'll ask SQL questions.
Good news: if you know pandas, you basically know SQL!

💊 CPHT CONNECTION:
SQL is like querying a pharmacy database:
"Show me all prescriptions (SELECT) for Medicaid patients (WHERE) 
grouped by drug name (GROUP BY) sorted by quantity (ORDER BY)"
"""

import pandas as pd

# ============================================
# LESSON 1: SQL vs PANDAS - THEY'RE SIBLINGS!
# ============================================
print("=" * 70)
print("DAY 2: SQL THINKING WITH PANDAS")
print("=" * 70)

# Load sales data
df = pd.read_csv("sales_data.csv")

print("\n📊 Our Sales Data:")
print(df)

"""
🧠 SQL AND PANDAS CHEAT SHEET:

SQL OPERATION          |  PANDAS EQUIVALENT
-----------------------|------------------------------------
SELECT col1, col2      |  df[['col1', 'col2']]
WHERE col > 100        |  df[df['col'] > 100]
GROUP BY category      |  df.groupby('category')
ORDER BY col           |  df.sort_values('col')
COUNT(*)               |  df.groupby('col').size()
SUM(revenue)           |  df.groupby('col')['revenue'].sum()

💡 KEY INSIGHT:
If you can do it in pandas, you can explain it in SQL terms during interviews!
Interviewers love hearing: "In SQL, this would be a GROUP BY with SUM aggregation."
"""

# ============================================
# LESSON 2: SELECT - CHOOSING COLUMNS
# ============================================
print("\n\n🔍 LESSON 2: SELECT - CHOOSING SPECIFIC COLUMNS")
print("-" * 70)

# SQL: SELECT product, revenue FROM sales
# Pandas: Select just product and revenue columns
product_revenue = df[['product', 'revenue']]
print("Products and revenue only:")
print(product_revenue)

"""
🧠 BRACKET SYNTAX:
- Single brackets df['column'] → Returns a Series (1 column)
- Double brackets df[['col1', 'col2']] → Returns a DataFrame (multiple columns)

💊 CPHT CONNECTION:
Like pulling just patient name and drug name from a prescription,
ignoring all the other fields (address, DOB, insurance, etc.)
"""

# Select all columns except one
# SQL: SELECT date, product, region FROM sales (excluding revenue)
columns_to_keep = ['date', 'product', 'region']
df_subset = df[columns_to_keep]
print("\nAll columns except revenue:")
print(df_subset)

# ============================================
# LESSON 3: WHERE - FILTERING WITH CONDITIONS
# ============================================
print("\n\n🎯 LESSON 3: WHERE - CONDITIONAL FILTERING")
print("-" * 70)

# SQL: SELECT * FROM sales WHERE revenue > 1000
# Pandas: Filter for high-value sales
high_value = df[df['revenue'] > 1000]
print("Sales over $1000:")
print(high_value)

"""
🧠 COMPARISON OPERATORS:
==  equal to
!=  not equal to
>   greater than
<   less than
>=  greater than or equal
<=  less than or equal

💡 COMMON MISTAKE:
Use == for equality, not =
✅ df[df['status'] == 'Active']
❌ df[df['status'] = 'Active']  # This will crash!
"""

# SQL: SELECT * FROM sales WHERE region = 'East'
# Pandas: Filter by region
east_sales = df[df['region'] == 'East']
print("\nEast region sales:")
print(east_sales)

# SQL: SELECT * FROM sales WHERE product IN ('A', 'B')
# Pandas: Filter for multiple values
products_ab = df[df['product'].isin(['A', 'B'])]
print("\nProducts A and B only:")
print(products_ab)

"""
🧠 WHAT IS .isin()?
Checks if a value is in a list
Like asking: "Is this prescription for Drug A, Drug B, or Drug C?"

💊 CPHT CONNECTION:
.isin(['Medicare', 'Medicaid', 'Cash']) 
= "Show me prescriptions for these 3 insurance types"
"""

# ============================================
# LESSON 4: COMBINING CONDITIONS (AND/OR)
# ============================================
print("\n\n🔗 LESSON 4: COMBINING CONDITIONS")
print("-" * 70)

# SQL: SELECT * FROM sales WHERE region = 'East' AND revenue > 1200
# Pandas: Multiple conditions with &
east_high = df[(df['region'] == 'East') & (df['revenue'] > 1200)]
print("East region with revenue > $1200:")
print(east_high)

"""
🧠 LOGICAL OPERATORS:
&  AND - both conditions must be True
|  OR  - at least one condition must be True
~  NOT - inverts the condition

⚠️ CRITICAL: Always use parentheses!
✅ df[(condition1) & (condition2)]
❌ df[condition1 & condition2]  # This breaks!
"""

# SQL: SELECT * FROM sales WHERE region = 'East' OR region = 'West'
# Pandas: OR logic
east_or_west = df[(df['region'] == 'East') | (df['region'] == 'West')]
print("\nEast OR West regions:")
print(east_or_west)

# SQL: SELECT * FROM sales WHERE NOT region = 'South'
# Pandas: NOT logic
not_south = df[~(df['region'] == 'South')]
print("\nAll regions EXCEPT South:")
print(not_south)

"""
💊 CPHT CONNECTION:
Combined conditions = complex prescription queries:
"Show me controlled substances (AND) for Medicare patients (AND) filled today"
You've done this logic in your head hundreds of times!
"""

# ============================================
# LESSON 5: GROUP BY - THE MOST POWERFUL OPERATION
# ============================================
print("\n\n📊 LESSON 5: GROUP BY - AGGREGATIONS")
print("-" * 70)

"""
GROUP BY is THE CORE of data analysis.
It answers questions like:
- "What's the total revenue per region?"
- "How many sales per product?"
- "What's the average order value by month?"

💊 CPHT CONNECTION:
Every pharmacy report you've seen uses GROUP BY:
- "Prescriptions per doctor" = GROUP BY doctor, COUNT
- "Revenue per insurance type" = GROUP BY insurance, SUM
- "Average wait time by hour" = GROUP BY hour, AVG
"""

# SQL: SELECT region, SUM(revenue) FROM sales GROUP BY region
# Pandas: Total revenue by region
revenue_by_region = df.groupby('region')['revenue'].sum()
print("Total revenue by region:")
print(revenue_by_region)

"""
🧠 SYNTAX BREAKDOWN:
df.groupby('region')      ← Group rows by region
  ['revenue']             ← Focus on revenue column
  .sum()                  ← Add up all values in each group

This creates a Series with region as the index and total revenue as values.
"""

# SQL: SELECT product, COUNT(*) FROM sales GROUP BY product
# Pandas: Count sales per product
sales_per_product = df.groupby('product').size()
print("\nNumber of sales per product:")
print(sales_per_product)

"""
🧠 AGGREGATION FUNCTIONS:
.sum()    - Add up all values
.mean()   - Calculate average
.count()  - Count non-null values
.size()   - Count all rows (including nulls)
.min()    - Find minimum
.max()    - Find maximum
.std()    - Standard deviation

💡 WHEN TO USE WHAT:
- .size() = "How many rows?" (like COUNT(*) in SQL)
- .count() = "How many non-null values?" (like COUNT(column) in SQL)
- Usually, you want .size() for simple counting!
"""

# SQL: SELECT region, AVG(revenue) FROM sales GROUP BY region
# Pandas: Average revenue by region
avg_revenue = df.groupby('region')['revenue'].mean()
print("\nAverage revenue by region:")
print(avg_revenue)

# SQL: SELECT product, MAX(revenue) FROM sales GROUP BY product
# Pandas: Highest sale for each product
max_by_product = df.groupby('product')['revenue'].max()
print("\nHighest sale per product:")
print(max_by_product)

# ============================================
# LESSON 6: MULTIPLE AGGREGATIONS AT ONCE
# ============================================
print("\n\n🎯 LESSON 6: MULTIPLE AGGREGATIONS")
print("-" * 70)

# SQL: SELECT region, SUM(revenue), AVG(revenue), COUNT(*) 
#      FROM sales GROUP BY region
# Pandas: Multiple stats at once
region_stats = df.groupby('region')['revenue'].agg(['sum', 'mean', 'count'])
print("Multiple statistics by region:")
print(region_stats)

"""
🧠 WHAT IS .agg()?
Applies multiple aggregation functions at once.
Returns a DataFrame with one column per function.

💼 INTERVIEW TIP:
When asked "How would you analyze sales by region?" say:
"I'd group by region and calculate total revenue, average revenue, 
and number of sales to get a complete picture."

This shows you think about multiple metrics, not just one!
"""

# ============================================
# LESSON 7: ORDER BY - SORTING RESULTS
# ============================================
print("\n\n📈 LESSON 7: ORDER BY - SORTING")
print("-" * 70)

# SQL: SELECT * FROM sales ORDER BY revenue DESC
# Pandas: Sort by revenue, highest first
df_sorted = df.sort_values('revenue', ascending=False)
print("Sales sorted by revenue (highest first):")
print(df_sorted)

"""
🧠 SORTING:
.sort_values('column')              ← Sorts ascending (A to Z, low to high)
.sort_values('column', ascending=False)  ← Sorts descending (Z to A, high to low)

💊 CPHT CONNECTION:
Like sorting prescriptions by:
- Fill date (oldest first for priority)
- Price (highest first to flag expensive meds)
- Patient name (alphabetical for organization)
"""

# Sort by multiple columns
# SQL: SELECT * FROM sales ORDER BY region, revenue DESC
# Pandas: Sort by region, then revenue within each region
df_multi_sort = df.sort_values(['region', 'revenue'], ascending=[True, False])
print("\nSorted by region, then revenue within region:")
print(df_multi_sort)

# ============================================
# LESSON 8: CHAINING OPERATIONS (ADVANCED!)
# ============================================
print("\n\n🔗 LESSON 8: CHAINING OPERATIONS")
print("-" * 70)

"""
THIS IS WHERE YOU LEVEL UP!
Chain multiple operations to answer complex questions in one go.

💼 INTERVIEW GOLD:
Being able to chain operations shows advanced pandas skills.
Most entry-level candidates can't do this fluently!
"""

# Question: "What's the total revenue for Product A in the East region?"
# SQL: SELECT SUM(revenue) FROM sales 
#      WHERE product = 'A' AND region = 'East'
# Pandas: Chain filter → select column → aggregate
result = df[(df['product'] == 'A') & (df['region'] == 'East')]['revenue'].sum()
print(f"Total revenue for Product A in East region: ${result}")

"""
🧠 WHAT JUST HAPPENED?
1. df[(df['product'] == 'A') & (df['region'] == 'East')]  ← Filter
2. ['revenue']                                            ← Select column
3. .sum()                                                 ← Aggregate

Read it left to right: "Filter data, grab revenue column, sum it up"
"""

# Question: "Show the top 3 highest-revenue sales"
# SQL: SELECT * FROM sales ORDER BY revenue DESC LIMIT 3
# Pandas: Sort → take top N
top_3 = df.sort_values('revenue', ascending=False).head(3)
print("\nTop 3 highest revenue sales:")
print(top_3)

# Question: "What's the average revenue for sales over $1000, by region?"
# SQL: SELECT region, AVG(revenue) FROM sales 
#      WHERE revenue > 1000 GROUP BY region
# Pandas: Filter → group → aggregate
high_value_avg = df[df['revenue'] > 1000].groupby('region')['revenue'].mean()
print("\nAverage revenue for high-value sales (>$1000) by region:")
print(high_value_avg)

"""
🧠 OPERATION ORDER:
1. Filter (WHERE) comes first
2. Group (GROUP BY) comes second  
3. Aggregate (SUM/AVG/COUNT) comes last
4. Sort (ORDER BY) comes after everything

This is the same order as SQL! Learn this pattern and you're golden.
"""

# ============================================
# PUTTING IT ALL TOGETHER: REAL ANALYSIS
# ============================================
print("\n\n" + "=" * 70)
print("🎯 REAL-WORLD ANALYSIS EXAMPLE")
print("=" * 70)

"""
Business Question:
"Which region generated the most revenue, and how does it compare to others?"
"""

print("\n📊 ANALYSIS: Revenue by Region")
print("-" * 70)

# Step 1: Calculate total revenue by region
total_revenue = df.groupby('region')['revenue'].sum().sort_values(ascending=False)
print("Total revenue by region (sorted):")
print(total_revenue)

# Step 2: Calculate percentage of total
overall_total = df['revenue'].sum()
revenue_percentage = (total_revenue / overall_total * 100).round(1)
print("\nPercentage of total revenue:")
print(revenue_percentage)

# Step 3: Find the winner
top_region = total_revenue.index[0]
top_revenue = total_revenue.iloc[0]
print(f"\n🏆 Winner: {top_region} region with ${top_revenue} ({revenue_percentage.iloc[0]}% of total)")

# Step 4: Additional insights
num_sales_by_region = df.groupby('region').size()
avg_sale_by_region = (total_revenue / num_sales_by_region).round(2)
print("\nAverage sale value by region:")
print(avg_sale_by_region)

print("\n💡 INSIGHT:")
print(f"The {top_region} region leads in total revenue, but check average sale value")
print("to see if it's due to volume or higher-value transactions.")

print("\n" + "=" * 70)
print("✅ DAY 2 COMPLETE!")
print("=" * 70)

"""
🎓 WHAT YOU LEARNED TODAY:
✅ SQL and pandas are similar (learn one, know both!)
✅ SELECT = df[['columns']]
✅ WHERE = df[df['condition']]
✅ GROUP BY = df.groupby('column')['value'].sum()
✅ ORDER BY = df.sort_values('column')
✅ How to chain operations for complex analysis
✅ How to answer business questions with data

🚀 NEXT STEPS:
1. Go to challenges.py and practice these operations
2. Build your sales analyzer in portfolio_project.py
3. Study the SQL/pandas comparison chart above

💼 INTERVIEW PREP:
When asked "Do you know SQL?" you can now say:
"Yes! I've worked extensively with pandas, which uses SQL-like operations.
I'm comfortable with SELECT, WHERE, GROUP BY, and aggregations. I can
translate business questions into queries and chain operations for
complex analysis."

Then give examples from your projects! 🎯
"""
