import pandas as pd

# Adding the "Must-Haves" for a realistic demo
essentials = {
    "Waste_Item": ["Polythene Bag", "Styrofoam Cup", "Bubble Wrap", "Pizza Box", "Disposable Mask"],
    "Category": ["Plastic", "Plastic", "Plastic", "Paper", "Mixed"],
    "Weight_grams": [5, 10, 8, 250, 4],
    "Carbon_Impact_Score": [35, 120, 45, 60, 25],
    "Disposal_Type": ["Plastic Collection", "Trash Bin", "Plastic Collection", "Recycling Bin", "Trash Bin"],
    "Recyclable": ["Yes (Store Drop-off)", "No", "Yes (Store Drop-off)", "Yes", "No"]
}

df = pd.read_csv("ecovision_waste_db.csv")
new_df = pd.concat([df, pd.DataFrame(essentials)], ignore_index=True).drop_duplicates(subset=['Waste_Item'])
new_df.to_csv("ecovision_waste_db.csv", index=False)
print("✅ Essentials added: Polythene, Styrofoam, and more!")