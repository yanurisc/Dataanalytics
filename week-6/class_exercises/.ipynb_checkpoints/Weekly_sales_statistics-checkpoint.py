import statistics

def analyze_sales(analyst, region, sales):
    mean   = statistics.mean(sales)
    median = statistics.median(sales)
    mode   = statistics.mode(sales)
    stdev  = statistics.stdev(sales)
    total  = sum(sales)
    high   = max(sales)
    low    = min(sales)
    return mean, median, mode, stdev, total, high, low

analyst = input("Analyst name: ")
region  = input("Region: ")

print("Enter daily sales for 7 days (one per line):")
sales = [float(input(f"  Day {i+1}: $")) for i in range(7)]

print(f"""
======== Weekly Sales Statistics Report ========
Analyst : {analyst}
Region  : {region}
Data    : {sales}
------------------------------------------------
Total revenue : ${total:.2f}
Mean (avg)    : ${mean:.2f}
Median        : ${median:.2f}
Mode          : ${mode:.2f}
Std deviation : ${stdev:.2f}
Highest day   : ${high:.2f}
Lowest day    : ${low:.2f}
================================================
""")