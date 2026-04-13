import pandas as pd

DATA = pd.read_csv("data.csv")

# إنشاء ملف csv يحتوي على عدد مرات استخدام كل وسيلة دفع 
def payment_methods_counts():
    popular_methods = DATA["payment method"].value_counts()
    popular_methods.to_csv("reports/payment_methods_counts.csv", header=True)

# إنشاء ملف csv يحتوي على إجمالي ومتوسط ووسيط المبيعات لكل موقع
def cities_sales():
    total_sales = DATA.groupby("location")["sales"].sum()
    average_sales = DATA.groupby("location")["sales"].mean()
    median_sales = DATA.groupby("location")["sales"].median()
    sales_summary = pd.DataFrame({
        "Total Sales": total_sales,
        "Average Sales": average_sales,
        "Median Sales": median_sales
    })
    sales_summary.to_csv("reports/cities_sales.csv", header=True)

# تنفيذ جميع المهمات 
payment_methods_counts()
cities_sales()
