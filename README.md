# Retail Sales Analytics

## Project Overview

This project analyzes retail sales data to identify trends in sales, profitability, customers, products, regions, and shipping performance.

The project uses the Superstore dataset and combines Python data analysis with an interactive Streamlit dashboard.

## Business Questions

* How are sales and profit changing over time?
* Which product categories and sub-categories perform best?
* Which regions and customer segments are most profitable?
* Which products generate losses?
* How are discounts associated with profitability?
* What are the monthly sales trends?
* How long does it take to ship orders?

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook
* Streamlit
* Git & GitHub

## Key Results

* **Total Sales:** $2.30M
* **Total Profit:** $286.4K
* **Profit Margin:** 12.47%
* **Total Orders:** 5,009
* **Average Order Value:** $458.61
* **Total Quantity Sold:** 37,873

### Key Findings

* Technology generated the highest total sales and profit.
* Copiers were the highest-profit sub-category.
* The West region had the highest profit margin.
* 2018 was the strongest year for sales.
* Tables generated significant sales but produced a loss.
* Higher discount levels were associated with lower profit margins.
* September through December were the strongest sales months.
* Standard Class was the most common shipping mode.

## Dashboard

The Streamlit dashboard provides:

* Interactive region, category, segment, and date filters
* KPI cards
* Sales by category
* Profit by region
* Monthly sales trends
* Sales vs. profit trends
* Top sub-categories by profit
* Filtered data download

## Business Recommendations

1. Review pricing and discount strategies for heavily discounted products.
2. Investigate the profitability of the Tables sub-category.
3. Focus on high-performing Technology products.
4. Analyze low-margin regions to identify pricing or cost issues.
5. Prepare inventory and staffing for the strong September–December sales period.

## Project Structure

```text
Retail-Sales-Analytics/
│
├── data/
│   └── Superstore.csv
│
├── notebooks/
│   └── Retail_Sales_Analysis.ipynb
│
├── dashboard/
│
├── images/
│
├── sql/
│
├── app.py
├── README.md
└── .gitignore
```

## How to Run the Dashboard

Activate the virtual environment:

```bash
source venv/bin/activate
```

Run Streamlit:

```bash
streamlit run app.py
```

The dashboard will open in your browser at:

```text
http://localhost:8501
```

## Conclusion

This project demonstrates practical data analytics skills including data cleaning, exploratory analysis, KPI development, business insights, visualization, and interactive dashboard development.
