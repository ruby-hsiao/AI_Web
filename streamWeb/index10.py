import streamlit as st

st.title("計數器範例")
count = 0
count1 = 0

# no cookie
increment = st.button("Increment")
if increment:
    count += 1

st.write("Count=", count)

# with session
names:dict = {'allice':23}
if 'robert' not in st.session_state:
    st.session_state['robert'] = 30

st.write(f":red-background[dict:{st.session_state}], :blue[value:{st.session_state.robert}]")

st.markdown("---")

# with cookie in calculator
if 'count1' not in st.session_state:
    st.session_state.count1 = 0

increment1 = st.button("Increment1")
if increment1:
    st.session_state.count1 += 1

st.write(f":red[Count1=]", {st.session_state.count1})