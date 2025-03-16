import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


df = pd.read_csv("data.csv")


if "FinalAmount" not in df.columns:
    st.error("Error: 'FinalAmount' column is missing in the dataset!")
    st.stop()


df["Date"] = pd.to_datetime(df["Date"])


df["FinalAmount"].fillna(df["FinalAmount"].median(), inplace=True)


st.title("📊 Customer Purchase Behavior Analysis")


st.write("### Sample Data", df.head())


total_sales = df["FinalAmount"].sum()
st.metric(label="💰 Total Sales", value=f"${total_sales:,.2f}")


fig = px.line(df, x="Date", y="FinalAmount", title="📈 Sales Trend Over Time")
st.plotly_chart(fig)


st.write("### 🏷 Customer Segmentation")
customer_data = df.groupby("CustomerID").agg({"FinalAmount": "sum", "Date": "count"})
customer_data.columns = ["TotalSpend", "PurchaseCount"]
kmeans = KMeans(n_clusters=3, random_state=42)
customer_data["Cluster"] = kmeans.fit_predict(customer_data)

fig2 = px.scatter(
    customer_data, x="TotalSpend", y="PurchaseCount", 
    color=customer_data["Cluster"].astype(str),
    title="📌 Customer Segmentation (K-Means Clustering)"
)
st.plotly_chart(fig2)


st.write("### 🏆 Top 10 Customers by Spending")
top_customers = df.groupby("CustomerID")["FinalAmount"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_customers)


st.write("### 📦 Sales Breakdown by Category")
category_sales = df.groupby("Category")["FinalAmount"].sum().sort_values(ascending=False)
st.bar_chart(category_sales)


df["DayOfYear"] = df["Date"].dt.dayofyear
X = df[["DayOfYear"]]
y = df["FinalAmount"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

st.metric(label="📊 Prediction MAE", value=f"{mae:.2f}")


fig3 = px.histogram(df, x="FinalAmount", nbins=30, title="🎯 Purchase Amount Distribution", marginal="box")
st.plotly_chart(fig3)

st.success("✅ Analysis Complete!")
