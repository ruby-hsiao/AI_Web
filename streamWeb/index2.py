import streamlit as st

#Layout and containter
col1, col2 = st.columns(2)

col1.title("This is column 1")
col1.header("Col1 - header")
col1.subheader("Col1 - subheader")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")