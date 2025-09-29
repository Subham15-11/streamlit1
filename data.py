import streamlit as st
import pandas as pd

st.title("Play with Data")

file = st.file_uploader("Upload your file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

    st.subheader("Data Summary")
    st.write(df.describe())
    
if file:
    st.subheader("Column Selection")
    columns = st.multiselect("Select columns to display", df.columns.tolist())
    if columns:
        st.dataframe(df[columns])

if file:
    st.subheader("Filter Data")
    filter_column = st.selectbox("Select column to filter", df.columns.tolist())
    unique_values = df[filter_column].unique().tolist()
    selected_value = st.selectbox("Select value to filter by", unique_values)
    filtered_df = df[df[filter_column] == selected_value]
    st.dataframe(filtered_df)