import streamlit as st
import time

placeholder = st.empty()

with placeholder:
    for seconds in range(10):
        st.write(f"{seconds} sec have passed.")
        time.sleep(1)
    st.write("^_^ 1 minute over!")

time.sleep(3)
placeholder.empty() #清空

