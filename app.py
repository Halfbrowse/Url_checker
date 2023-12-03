import streamlit as st
import sqlite3
import pandas as pd


def connect_db():
    return sqlite3.connect("admin_panel.db")


def add_entity(data):
    with connect_db() as conn:
        placeholders = ", ".join("?" * len(data))
        conn.execute(f"INSERT INTO Entities VALUES (NULL, {placeholders})", data)


def get_entities_df():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='Entities';"
        )
        if cursor.fetchone():
            # Specify the 'conn' parameter for the connection, and the SQL query to select everything from 'Entities'
            df = pd.read_sql_query("SELECT * FROM Entities", conn)
            return df
        else:
            st.error(
                "The 'Entities' table does not exist. Please run `create_database()` to create it."
            )
            return pd.DataFrame()


st.title("Admin Panel")

with st.form("add_entity"):
    st.subheader("Add New Entity")
    data = [
        st.text_input("Name"),
        st.text_input("Alias"),
        st.text_input("Type"),
        st.text_area("Attribution"),
        st.text_input("Attribution links"),
        st.text_input("Attribution type"),
        st.slider("Attribution confidence 1-5", 1, 5, 3),
        st.text_input("Label"),
        st.text_input("Parent actor"),
        st.text_input("Subsidiary actors"),
        st.text_input("Threat Actor"),
        st.text_input("TTPs"),
        st.text_area("Description of TTPs"),
        st.text_input("Description TTPs Link"),
        st.text_input("Master Narratives"),
        st.text_area("Master Narrative Description"),
        st.text_input("Master Narrative Links"),
        st.text_area("Summary"),
        st.text_input("External links (articles, wikipedia page etc)."),
        st.text_input("Language"),
        st.text_input("Country"),
        st.text_input("Sub-region"),
        st.text_input("Region"),
        st.text_input("Website"),
        st.text_input("Twitter"),
        st.text_input("Twitter ID"),
        st.text_input("Facebook"),
        st.text_input("Threads"),
        st.text_input("YouTube"),
        st.text_input("YouTube ID"),
        st.text_input("TikTok"),
        st.text_input("Instagram"),
        st.text_input("LinkedIn"),
        st.text_input("Reddit"),
        st.text_input("VK"),
        st.text_input("Telegram"),
        st.text_input("Substack"),
        st.text_input("Quora"),
        st.text_input("Patreon"),
        st.text_input("GoFundMe"),
        st.text_input("Paypal"),
        st.text_input("Twitch"),
        st.text_input("Mastadon"),
        st.text_input("Wechat"),
        st.text_input("QQ"),
        st.text_input("Douyin"),
    ]

    submit_entity = st.form_submit_button("Add Entity")
    if submit_entity:
        add_entity(tuple(data))


def bulk_insert_entities(df):
    with connect_db() as conn:
        # Replace spaces with underscores in column names to match the database
        df.columns = [col.replace(" ", "_") for col in df.columns]
        df.to_sql("Entities", conn, if_exists="append", index=False)


st.title("Admin Panel")

# File uploader for CSV
uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file is not None:
    # Can be set to 'ISO-8859-1' if the data has special characters
    df = pd.read_csv(uploaded_file, encoding="utf-8")
    # Perform bulk insert
    bulk_insert_entities(df)
    st.success("CSV data uploaded successfully!")

st.write("Existing Entities:")
entities_df = get_entities_df()
if entities_df is not None:
    st.dataframe(entities_df)
else:
    st.write("No entities found in the database.")
