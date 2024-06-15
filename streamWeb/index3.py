import streamlit as st
import numpy as np # bar chart

with st.container(border=True, height=None):
    st.write("This is inside the container")
    st.bar_chart(np.random.randn(5,3))

st.write("This is outside the container")