import pandas as pd
import plotly.express as px

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("ecovision_waste_db.csv")

print("\nDataset Loaded Successfully!")
print(df.head())

# -----------------------------
# 1️⃣ Most Common Waste Type
# -----------------------------
most_common = df["Material"].value_counts().reset_index()
most_common.columns = ["Material", "Count"]

print("\nMost Common Waste Type:")
print(most_common.iloc[0])

fig1 = px.bar(
    most_common,
    x="Material",
    y="Count",
    title="Most Common Waste Type Distribution"
)
fig1.show()


# -----------------------------
# 2️⃣ Daily Waste Trend
# -----------------------------
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    daily_trend = df.groupby(df["Date"].dt.date).size().reset_index(name="Waste_Count")

    fig2 = px.line(
        daily_trend,
        x="Date",
        y="Waste_Count",
        title="Daily Waste Trend"
    )
    fig2.show()
else:
    print("\n⚠ No 'Date' column found. Daily trend cannot be generated.")


# -----------------------------
# 3️⃣ Recycling Efficiency %
# -----------------------------
total_items = len(df)
recycled_items = len(df[df["Disposal_Type"] == "Recycling Bin"])

recycling_efficiency = (recycled_items / total_items) * 100

print(f"\nRecycling Efficiency: {recycling_efficiency:.2f}%")

fig3 = px.pie(
    names=["Recycled", "Other"],
    values=[recycled_items, total_items - recycled_items],
    title="Recycling Efficiency Breakdown"
)
fig3.show()


print("\nAnalytics Execution Complete.")
