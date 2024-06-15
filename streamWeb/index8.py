import streamlit as st

# Object notation
selected_value = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# with notation
with st.sidebar:
    radio_value = st.radio(
        "Choose a shipping method",
        ("Standard(5-15 days)","Express(2-3 days)")
        )
    
st.write("way1:", selected_value, radio_value)

# with notation2
with st.sidebar:
    with st.form("abc"):
        selected_value2 = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
            )
        radio_value2 = st.radio(
            "Choose a shipping method",
            ("Standard(5-15 days)","Express(2-3 days)")
            )
        
        st.form_submit_button("確定")
    
st.write("way2:", selected_value2, radio_value2)