import pandas as pd
import streamlit as st
import plotly.express as px

from module_18.main1 import total_books, unique_titles, average_rating, average_price

books_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title("Best selling books analysis")
st.write("This app checks the best selling books of amazon")


st.sidebar.header("Add new book data")
with st.sidebar.form("book_form"):
    new_name = st.text_input("Books Name")
    new_author = st.text_input("Author Name")
    new_user_rating = st.sidebar("User_ratings" , 0.0 , 5.0,0.0,0.1)
    new_reviews = st.number_input("Reviews" , min_value=0 , max_value=10 , step=1)
    new_price = st.number_input("Price" , min_value=0 , step=1)
    new_year = st.number_input("Year" , min_value=2009 , max_value=2025, step=1)
    new_genre = st.selectbox("Genre" , books_df['Genre'].unique())
    submit_button = st.form_submit_button(label="Add a book")

if submit_button:
    new_data = {
        "Name": new_name,
        "Author": new_author,
        "User Ratings": new_user_rating,
        "Reviews": new_reviews,
        "Price": new_price,
        "Year": new_year,
        "Genre": new_genre,
    }

    books_df = pd.concat([pd.DataFrame (new_data, index=[0]), books_df], ignore_index=True)
    books_df.to_csv('bestsellers_with_categories_2022_03_27.csv',index=False)
    st.sidebar.success("New book added")

st.subheader("Summary Statistics")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].unique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()


col1, col2, col3, col4 = st.columns (4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", f"{average_rating:.2f}")
co14.metric("Average Price", f"${average_price:.2f}")

st.subheader("Dataset Preview")
st.write(books_df.head())




