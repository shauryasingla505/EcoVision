# ==========================================================
# EcoVision - Smart Recommendation Engine
# Member 4 | Final Correct Implementation
# ==========================================================

import csv
import random

# ✅ CORRECT DATASET NAME
DATASET_FILE = "ecovision_300_waste_types_enhanced.csv"

# ----------------------------------------------------------
# Simulated Disposal / Recycling Centers
# ----------------------------------------------------------

DISPOSAL_CENTERS = [
    {"name": "GreenCycle Hub", "category": "Plastic", "distance": 2.1},
    {"name": "PaperLoop Center", "category": "Paper", "distance": 3.4},
    {"name": "MetalWorks Facility", "category": "Metal", "distance": 4.6},
    {"name": "Urban Compost Facility", "category": "Organic", "distance": 2.8},
    {"name": "E-Waste Safe Center", "category": "E-Waste", "distance": 5.0},
]

# ----------------------------------------------------------
# Compost Tips (for organic waste)
# ----------------------------------------------------------

COMPOST_TIPS = [
    "Separate wet and dry waste",
    "Avoid plastics and metals",
    "Turn compost every 2–3 days",
    "Maintain proper moisture level"
]

# ----------------------------------------------------------
# Load Dataset (BOM-safe + clean)
# ----------------------------------------------------------

def load_dataset():
    dataset = []
    try:
        with open(DATASET_FILE, newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                clean_row = {k.strip(): v.strip() for k, v in row.items()}
                dataset.append(clean_row)
    except FileNotFoundError:
        print("❌ ERROR: Dataset file not found.")
        exit()
    return dataset

# ----------------------------------------------------------
# Find Waste Item (partial + case-insensitive)
# ----------------------------------------------------------

def find_item(user_input, dataset):
    user_input = user_input.lower().strip()
    for item in dataset:
        if user_input in item["Waste_Item"].lower():
            return item
    return None

# ----------------------------------------------------------
# Simulate AI Confidence (derived from carbon impact)
# ----------------------------------------------------------

def simulate_ai_confidence(carbon_score):
    base = min(float(carbon_score) / 500, 1)
    confidence = round(random.uniform(base - 0.1, base + 0.1), 2)
    return max(0.6, min(confidence, 0.99))

# ----------------------------------------------------------
# Find Nearest Disposal Center (simulated)
# ----------------------------------------------------------

def find_nearest_center(category):
    valid = [
        c for c in DISPOSAL_CENTERS
        if c["category"].lower() == category.lower()
    ]
    if not valid:
        return None
    return min(valid, key=lambda x: x["distance"])

# ----------------------------------------------------------
# Optimization Logic
# ----------------------------------------------------------

def calculate_optimization_score(weight, carbon, distance, confidence):
    score = (
        (float(weight) * 0.2) +
        (float(carbon) * 0.4) +
        ((1 / distance) * 20) +
        (confidence * 10)
    )
    return round(score, 2)

# ----------------------------------------------------------
# Smart Recommendation Engine
# ----------------------------------------------------------

def smart_recommendation(item):
    category = item["Category"]
    weight = item["Weight_grams"]
    carbon = item["Carbon_Impact_Score"]
    recyclable = item["Recyclable"]

    confidence = simulate_ai_confidence(carbon)
    center = find_nearest_center(category)
    distance = center["distance"] if center else 10

    optimization_score = calculate_optimization_score(
        weight, carbon, distance, confidence
    )

    print("\n🔍 ECOVISION – SMART WASTE RECOMMENDATION")
    print("================================================")
    print(f"Waste Item              : {item['Waste_Item']}")
    print(f"Category                : {category}")
    print(f"Recyclable              : {recyclable}")
    print(f"Disposal Method         : {item['Disposal_Type']}")
    print(f"Weight                  : {weight} grams")
    print(f"Carbon Impact Score     : {carbon}")
    print(f"AI Confidence           : {confidence}")

    if center:
        print(f"Nearest Center          : {center['name']}")
        print(f"Distance                : {center['distance']} km")
    else:
        print("Nearest Center          : Not Available")

    if category.lower() == "organic":
        print("\n🌱 Compost Suggestions:")
        for tip in COMPOST_TIPS:
            print(f" - {tip}")

    print(f"\nOptimization Score      : {optimization_score}")

    print("\n🧠 Decision Logic:")
    print("Optimized using carbon impact, waste weight,")
    print("AI confidence, and distance-based scoring.")
    print("================================================\n")

# ----------------------------------------------------------
# MAIN FUNCTION
# ----------------------------------------------------------

def main():
    dataset = load_dataset()

    print("\n♻️ Welcome to EcoVision – Smart Waste Assistant ♻️\n")
    user_input = input("Enter waste item name: ").strip()

    item = find_item(user_input, dataset)

    if not item:
        print("\n❌ Waste item not found in database.")
        print("Tip: Try partial names like: bottle, bag, packet")
        return

    smart_recommendation(item)

# ----------------------------------------------------------
# PROGRAM START
# ----------------------------------------------------------

if __name__ == "__main__":
    main()
