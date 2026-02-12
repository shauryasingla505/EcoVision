import streamlit as st
import csv
import difflib

DATA_FILE = "waste_data.csv"

# Default category mappings
DEFAULT_MAPPING = {
    "paper": "newspaper",
    "plastic": "plastic bottle",
    "glass": "glass bottle",
    "metal": "aluminum can"
}

# Load dataset
@st.cache_data
def load_data():
    waste_db = {}
    with open(DATA_FILE, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["Waste_Item"].strip().lower()
            waste_db[name] = row
    return waste_db

waste_db = load_data()
waste_items = list(waste_db.keys())


def find_suggestion(user_input):
    matches = difflib.get_close_matches(user_input, waste_items, n=1, cutoff=0.4)
    return matches[0] if matches else None


# ------------------ UI ------------------
st.set_page_config(page_title="EcoVision Waste Finder", page_icon="♻️")

st.title("♻️ EcoVision Waste Finder")

user_input = st.text_input("Enter waste item", "")

if user_input:
    user_input = user_input.lower().strip()

    # 1. Direct mapping
    if user_input in DEFAULT_MAPPING:
        user_input = DEFAULT_MAPPING[user_input]

    # 2. Direct match
    if user_input in waste_db:
        item = waste_db[user_input]

        st.success("Waste item found!")
        st.write("### Result")
        st.write(f"**Waste Item:** {item['Waste_Item']}")
        st.write(f"**Category:** {item['Category']}")
        st.write(f"**Weight (g):** {item.get('Weight_g', 'N/A')}")
        st.write(f"**Carbon Score:** {item.get('Carbon_Score', 'N/A')}")
        st.write(f"**Disposal Type:** {item.get('Disposal_Type', 'N/A')}")
        st.write(f"**Recyclable:** {item.get('Recyclable', 'N/A')}")

    else:
        suggestion = find_suggestion(user_input)

        if suggestion:
            st.warning(f"Did you mean **{suggestion}**?")
            if st.button("Yes, show result"):
                item = waste_db[suggestion]
                st.write("### Result")
                st.write(f"**Waste Item:** {item['Waste_Item']}")
                st.write(f"**Category:** {item['Category']}")
                st.write(f"**Weight (g):** {item.get('Weight_g', 'N/A')}")
                st.write(f"**Carbon Score:** {item.get('Carbon_Score', 'N/A')}")
                st.write(f"**Disposal Type:** {item.get('Disposal_Type', 'N/A')}")
                st.write(f"**Recyclable:** {item.get('Recyclable', 'N/A')}")
        else:
            st.error("Item not found in database.")
