import pandas as pd

# Detailed dictionary of actual waste items
waste_library = {
    "Plastic": [
        "PET Water Bottle", "HDPE Milk Jug", "PP Yogurt Tub", "PVC Pipe", "LDPE Grocery Bag",
        "Plastic Cutlery", "Shampoo Bottle", "Detergent Container", "Bubble Wrap", "Plastic Straw",
        "Takeaway Container", "Medicine Bottle", "Plastic Crate", "Toy Bricks", "Cling Film",
        "Lotion Pump", "Plant Pot", "Plastic Folder", "Contact Lens Case", "Toothbrush"
    ],
    "Paper": [
        "Cardboard Box", "Newspaper", "Glossy Magazine", "Office Paper", "Envelope",
        "Paper Bag", "Egg Carton", "Cereal Box", "Phone Book", "Post-it Note",
        "Greeting Card", "Paperback Book", "Toilet Paper Roll", "Juice Carton", "Shoe Box",
        "Flyer", "Paper Straw", "Receipt", "Wrapping Paper", "Cardboard Tube"
    ],
    "Metal": [
        "Aluminum Soda Can", "Steel Food Tin", "Aluminum Foil", "Copper Wiring", "Brass Fitting",
        "Metal Utensil", "Paper Clip", "Paint Can", "Aerosol Spray", "Bottle Cap",
        "Key", "Curtain Rod", "Staples", "Metal Hanger", "Cookie Tin",
        "Baking Sheet", "Iron Nail", "Soda Tab", "Jar Lid", "Aluminum Tray"
    ],
    "Organic": [
        "Banana Peel", "Apple Core", "Coffee Grounds", "Eggshells", "Grass Clippings",
        "Tea Bag", "Orange Rind", "Vegetable Scraps", "Bread Crust", "Chicken Bone",
        "Dead Leaves", "Nut Shells", "Pizza Crust", "Potato Skin", "Used Napkin",
        "Hair Trimmings", "Corn Husk", "Fruit Pit", "Wilted Flower", "Rice"
    ],
    "E-Waste": [
        "AA Battery", "Smartphone", "Laptop Charger", "Broken Earbuds", "LED Bulb",
        "USB Drive", "Old Mouse", "Keyboard Key", "Circuit Board", "Remote Control",
        "Power Strip", "CPU Fan", "Tablet Screen", "Router", "Digital Watch",
        "Camera Lens", "VCR Tape", "Hard Drive", "Calculator", "Floppy Disk"
    ],
    "Glass": [
        "Wine Bottle", "Beer Bottle", "Jam Jar", "Perfume Bottle", "Glass Vial",
        "Drinking Glass", "Glass Plate", "Broken Window Panes", "Glass Candle Holder", "Medicine Jar",
        "Olive Oil Bottle", "Glass Bowl", "Spice Jar", "Sauce Bottle", "Glass Ornament",
        "Cosmetic Jar", "Glass Pitcher", "Baby Food Jar", "Coffee Carafe", "Glass Bead"
    ],
    "Landfill": [
        "Greasy Pizza Box", "Styrofoam Cup", "Used Diaper", "Ceramic Shard", "Mirror Glass",
        "Cigarette Butt", "Vacuum Bag", "Treated Wood", "Plastic Laminated Paper", "Cat Litter",
        "Potato Chip Bag", "Candy Wrapper", "Dirty Sponge", "Rubber Band", "Old Textile Rag",
        "Single-use Face Mask", "Gauze", "Latex Glove", "Ballpoint Pen", "Thermal Receipt"
    ]
}

# Configuration for environmental logic
config = {
    "Plastic": {"score": 85, "carbon": 150, "disposal": "Recycling Bin"},
    "Paper": {"score": 95, "carbon": 220, "disposal": "Recycling Bin"},
    "Metal": {"score": 100, "carbon": 300, "disposal": "Metal Bin"},
    "Organic": {"score": 100, "carbon": 80, "disposal": "Compost Bin"},
    "E-Waste": {"score": 65, "carbon": 900, "disposal": "E-Waste Center"},
    "Glass": {"score": 100, "carbon": 180, "disposal": "Glass Bin"},
    "Landfill": {"score": 0, "carbon": -50, "disposal": "Trash Bin"}
}

data_rows = []
counter = 1

# Generate 300 items by cycling through the library and adding detail
while counter <= 300:
    for cat, items in waste_library.items():
        if counter > 300: break
        
        # Select item and add variety
        base_item = items[(counter // 7) % len(items)]
        size = ["Small", "Large", "Medium", "Crushed", "Empty"][(counter % 5)]
        item_name = f"{size} {base_item}"
        
        data_rows.append({
            "Item_ID": counter,
            "Item_Name": item_name,
            "Category": cat,
            "Recyclability_Score": config[cat]["score"],
            "Carbon_Saved_g": config[cat]["carbon"],
            "Disposal_Method": config[cat]["disposal"],
            "Smart_Recommendation": f"Ensure this {cat} item is clean before disposal."
        })
        counter += 1

# Create and Export
df = pd.DataFrame(data_rows)
df.to_csv('ecovision_waste_db.csv', index=False)
print("Success! Created 'ecovision_waste_db.csv' with 300 unique items.")