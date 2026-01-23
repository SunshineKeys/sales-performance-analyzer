# Day 2: PORTFOLIO PROJECT - Sales Performance Analyzer
# Build an executive dashboard for stakeholders

import pandas as pd

# ============================================
# LOAD DATA
# ============================================
df = pd.read_csv("sales_data.csv")

print("=" * 70)
print("SALES PERFORMANCE ANALYZER - EXECUTIVE DASHBOARD")
print("=" * 70)

# ============================================
# SECTION 1: EXECUTIVE SUMMARY
# ============================================
print("\n📊 EXECUTIVE SUMMARY")
print("-" * 70)

# Total revenue across ALL sales
total_revenue = df['revenue'].sum()

# Number of transactions
total_transactions = len(df)

# Average sale value
average_sale = df['revenue'].mean()

# Date range
earliest_date = df['date'].min()
latest_date = df['date'].max()

# Print formatted output
print(f"Total Revenue: ${total_revenue:,.0f}")
print(f"Total Transactions: {total_transactions}")
print(f"Average Sale Value: ${average_sale:,.2f}")
print(f"Data Period: {earliest_date} to {latest_date}")

# ============================================
# SECTION 2: REGIONAL PERFORMANCE
# ============================================
print("\n🌍 REGIONAL PERFORMANCE ANALYSIS")
print("-" * 70)

# Calculate stats
region_stats = df.groupby('region')['revenue'].agg(['sum', 'count', 'mean'])

# Get total for percentages
total_revenue = df['revenue'].sum()

# Print formatted output for each region
for region in region_stats.index:
    revenue_sum = region_stats.loc[region, 'sum']
    count = region_stats.loc[region, 'count']
    avg = region_stats.loc[region, 'mean']
    percentage = (revenue_sum / total_revenue) * 100

    print(f"\nRegion: {region}")
    print(f"  Total Revenue: ${revenue_sum:,.0f} ({percentage:.1f}%)")
    print(f"  Transactions: {int(count)}")
    print(f"  Avg Sale Value: ${avg:,.2f}")

# ============================================
# SECTION 3: PRODUCT PERFORMANCE
# ============================================
print("\n📦 PRODUCT PERFORMANCE ANALYSIS")
print("-" * 70)

# Calculate stats
product_stats = df.groupby('product')['revenue'].agg(['sum', 'count', 'mean'])

# Get total and overall average for percentages
total_revenue = df['revenue'].sum()
overall_avg = df['revenue'].mean()

# Print formatted output for each product
for product in product_stats.index:
    revenue_sum = product_stats.loc[product, 'sum']
    count = product_stats.loc[product, 'count']
    avg = product_stats.loc[product, 'mean']
    percentage = (revenue_sum / total_revenue) * 100

    # Performance indicator
    if avg > overall_avg * 1.2:
        performance = "🟢 Strong"
    elif avg < overall_avg * 0.8:
        performance = "🔴 Needs attention"
    else:
        performance = "🟡 Average"

    print(f"\nProduct {product}:")
    print(f"  Total Revenue: ${revenue_sum:,.0f} ({percentage:.1f}%)")
    print(f"  Transactions: {int(count)}")
    print(f"  Avg Sale Value: ${avg:,.2f}")
    print(f"  Performance: {performance}")

# ============================================
# SECTION 4: CROSS-ANALYSIS (PIVOT TABLE)
# ============================================
print("\n🔍 REGIONAL PRODUCT BREAKDOWN")
print("-" * 70)

print("\n🔄 REGIONAL × PRODUCT ANALYSIS")
print("-" * 70)

# Create the pivot table
revenue_pivot = df.pivot_table(
    values='revenue',
    index='region',
    columns='product',
    aggfunc='sum',
    fill_value=0
)

print("Revenue by Region and Product:")
print(revenue_pivot)
print()

# Find best product per region
print("Top product in each region:")
for region in revenue_pivot.index:
    best_product = revenue_pivot.loc[region].idxmax()
    best_revenue = revenue_pivot.loc[region].max()
    print(f"  {region}: Product {best_product} (${best_revenue:,.0f})")

# ============================================
# SECTION 5: TIME-BASED ANALYSIS
# ============================================
print("\n📅 SALES TIMELINE")
print("-" * 70)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Sort by date
sales_by_date = df.sort_values('date')

# Print chronological sales
print("Chronological sales:")
for _, row in sales_by_date.iterrows():
    print(f"  {row['date'].strftime('%b %d')}: Product {row['product']} ({row['region']}) - ${row['revenue']:,.0f}")

# Extract month for grouping
df['month'] = df['date'].dt.month
df['month_name'] = df['date'].dt.strftime('%B')

# Calculate revenue by month
monthly_revenue = df.groupby('month_name')['revenue'].sum().sort_values(ascending=False)

print("\nSales by Month:")
for month, revenue in monthly_revenue.items():
    print(f"  {month}: ${revenue:,.0f}")

# Find best month
best_month = monthly_revenue.idxmax()
best_revenue = monthly_revenue.max()
print(f"\nHighest revenue month: {best_month} (${best_revenue:,.0f})")

# ============================================
# SECTION 6: KEY INSIGHTS & RECOMMENDATIONS
# ============================================
print("\n💡 KEY INSIGHTS")
print("-" * 70)

# 1. Top performing region
top_region = region_stats['sum'].idxmax()
top_region_revenue = region_stats.loc[top_region, 'sum']
top_region_pct = (top_region_revenue / total_revenue) * 100

print(f"\n🎯 Top Region: {top_region}")
print(f"   Generates ${top_region_revenue:,.0f} ({top_region_pct:.1f}% of total revenue)")

# 2. Top performing product
top_product = product_stats['sum'].idxmax()
top_product_revenue = product_stats.loc[top_product, 'sum']
top_product_pct = (top_product_revenue / total_revenue) * 100

print(f"\n🎯 Top Product: Product {top_product}")
print(f"   Generates ${top_product_revenue:,.0f} ({top_product_pct:.1f}% of total revenue)")

# 3. Identify gaps
print("\n⚠️  Performance Gaps:")
for region in revenue_pivot.index:
    for product in revenue_pivot.columns:
        if revenue_pivot.loc[region, product] == 0:
            print(f"   Product {product} has ZERO sales in {region} region")

# 4. Performance variance
highest_sale = df['revenue'].max()
lowest_sale = df['revenue'].min()
avg_sale = df['revenue'].mean()

print(f"\n📊 Sale Value Analysis:")
print(f"   Highest sale: ${highest_sale:,.0f}")
print(f"   Lowest sale: ${lowest_sale:,.0f}")
print(f"   Average sale: ${avg_sale:,.2f}")
print(f"   Variance: ${highest_sale - lowest_sale:,.0f} gap between high and low")

# 5. Strategic recommendations
print("\n🎯 STRATEGIC RECOMMENDATIONS:")

print(f"\n1. Double down on {top_region} region and Product {top_product}")
print(f"   These drive {top_region_pct + top_product_pct:.1f}% of revenue combined")

# Recommendation 2: Address gaps
zero_sales = []
for region in revenue_pivot.index:
    for product in revenue_pivot.columns:
        if revenue_pivot.loc[region, product] == 0:
            zero_sales.append(f"Product {product} in {region}")

if zero_sales:
    print(f"\n2. Investigate why these combinations have zero sales:")
    for item in zero_sales:
        print(f"   - {item}")

# Recommendation 3: Best product per region
print("\n3. Region-specific product focus:")
for region in revenue_pivot.index:
    best_product = revenue_pivot.loc[region].idxmax()
    best_revenue = revenue_pivot.loc[region].max()
    print(f"   {region}: Focus on Product {best_product} (proven ${best_revenue:,.0f} performer)")

# ============================================
# BONUS: ADVANCED ANALYSIS
# ============================================
print("\n🔬 ADVANCED METRICS (BONUS)")
print("-" * 70)

# 1. Market share by region
print("\n1️⃣ Product Market Share by Region:")
for product in df['product'].unique():
    product_data = df[df['product'] == product]
    product_total = product_data['revenue'].sum()

    if product_total > 0:
        print(f"\nProduct {product} (Total: ${product_total:,.0f}):")
        for region in df['region'].unique():
            region_revenue = product_data[product_data['region'] == region]['revenue'].sum()
            market_share = (region_revenue / product_total) * 100
            print(f"  {region}: ${region_revenue:,.0f} ({market_share:.1f}%)")

# 2. Growth analysis
df['month_num'] = df['date'].dt.month
first_half = df[df['month_num'] <= 3]['revenue'].sum()
second_half = df[df['month_num'] > 3]['revenue'].sum()
growth_rate = ((second_half - first_half) / first_half) * 100 if first_half > 0 else 0

print(f"\n2️⃣ Growth Analysis:")
print(f"  First half: ${first_half:,.0f}")
print(f"  Second half: ${second_half:,.0f}")
print(f"  Growth: {growth_rate:+.1f}% {'📈' if growth_rate > 0 else '📉' if growth_rate < 0 else '➡️'}")

# 3. Revenue concentration
top_2_sales = df.nlargest(2, 'revenue')['revenue'].sum()
concentration = (top_2_sales / total_revenue) * 100

print(f"\n3️⃣ Revenue Concentration:")
print(f"  Top 2 sales: ${top_2_sales:,.0f} ({concentration:.1f}% of total)")
print(f"  {'⚠️ HIGH concentration' if concentration > 50 else '✅ Well-distributed'}")

# 4. Forecast
monthly_avg = total_revenue / df['month_num'].nunique()

print(f"\n4️⃣ Revenue Forecast:")
print(f"  Monthly average: ${monthly_avg:,.2f}")
print(f"  Next month projection: ${monthly_avg:,.2f}")

# 5. Rankings
print(f"\n5️⃣ Performance Rankings:")
print("\nTop Regions:")
for i, (region, row) in enumerate(region_stats.sort_values('sum', ascending=False).iterrows(), 1):
    print(f"  #{i} {region}: ${row['sum']:,.0f}")

print("\nTop Products:")
for i, (product, row) in enumerate(product_stats.sort_values('sum', ascending=False).iterrows(), 1):
    print(f"  #{i} Product {product}: ${row['sum']:,.0f}")

# ============================================
# EXPORT RESULTS
# ============================================
print("\n💾 EXPORT ANALYSIS")
print("-" * 70)

# 1. Export key metrics to CSV
metrics_summary = {
    'Metric': [
        'Total Revenue',
        'Total Transactions',
        'Average Sale Value',
        'Top Region',
        'Top Product',
        'Highest Month'
    ],
    'Value': [
        f'${total_revenue:,.0f}',
        len(df),
        f'${df["revenue"].mean():,.2f}',
        top_region,
        f'Product {top_product}',
        best_month
    ]
}

metrics_df = pd.DataFrame(metrics_summary)
metrics_df.to_csv('sales_metrics.csv', index=False)
print("✅ Exported: sales_metrics.csv")

# 2. Export regional performance
region_stats.to_csv('regional_performance.csv')
print("✅ Exported: regional_performance.csv")

# 3. Export product performance
product_stats.to_csv('product_performance.csv')
print("✅ Exported: product_performance.csv")

# 4. Export pivot table
revenue_pivot.to_csv('region_product_matrix.csv')
print("✅ Exported: region_product_matrix.csv")

# 5. Create executive summary report
with open('executive_summary.txt', 'w') as f:
    f.write("=" * 70 + "\n")
    f.write("SALES PERFORMANCE ANALYSIS - EXECUTIVE SUMMARY\n")
    f.write("=" * 70 + "\n\n")

    f.write("KEY METRICS\n")
    f.write("-" * 70 + "\n")
    f.write(f"Total Revenue: ${total_revenue:,.0f}\n")
    f.write(f"Total Transactions: {len(df)}\n")
    f.write(f"Average Sale Value: ${df['revenue'].mean():,.2f}\n")
    f.write(f"Data Period: {df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}\n\n")

    f.write("TOP PERFORMERS\n")
    f.write("-" * 70 + "\n")
    f.write(f"Best Region: {top_region} (${top_region_revenue:,.0f}, {top_region_pct:.1f}%)\n")
    f.write(f"Best Product: Product {top_product} (${top_product_revenue:,.0f}, {top_product_pct:.1f}%)\n")
    f.write(f"Best Month: {best_month} (${best_revenue:,.0f})\n\n")

    f.write("STRATEGIC RECOMMENDATIONS\n")
    f.write("-" * 70 + "\n")
    f.write(f"1. Focus resources on {top_region} region and Product {top_product}\n")
    f.write(f"2. Investigate zero-sales combinations:\n")
    for item in zero_sales[:3]:
        f.write(f"   - {item}\n")
    f.write(f"3. Leverage region-specific strengths:\n")
    for region in revenue_pivot.index:
        best = revenue_pivot.loc[region].idxmax()
        f.write(f"   - {region}: Product {best}\n")

    f.write("\n" + "=" * 70 + "\n")
    f.write("END OF REPORT\n")
    f.write("=" * 70 + "\n")

print("✅ Exported: executive_summary.txt")

print("\n📊 All analysis files saved to project directory!")
print("   Ready for:\n   • Excel analysis (CSV files)\n   • Stakeholder review (TXT report)\n   • Further processing")

print("\n" + "=" * 70)
print("✅ ANALYSIS COMPLETE - READY FOR STAKEHOLDERS")
print("=" * 70)