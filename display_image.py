import streamlit as st
import json

with open("subset_dataset.json") as f:
    subset_dataset = json.load(f)

number = st.selectbox("Select a number", range(len(subset_dataset["url"])))

st.image(subset_dataset["url"][number])

filtered_data = [{"x": entry["x"], "y": entry["y"], "phrase": entry["phrase"]} for entry in subset_dataset['regions'][number]]

st.write(filtered_data)