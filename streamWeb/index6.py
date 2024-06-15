import streamlit as st

with st.form('my_form'):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    #每一個form必需要有一個submit button
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

slider_val2 = st.slider("Form slider")
checkbox_val2 = st.checkbox("Form checkbox")

    
st.write("slider", slider_val2, "checkbox", checkbox_val2)

