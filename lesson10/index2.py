import requests
from pydantic import BaseModel,Field,RootModel,field_validator,field_serializer
import streamlit as st
import source #匯入module
from source import Root #匯入class

try:
    data_str = source.download_youbike()
except Exception as e:
    st.error(e)
else:    
    root = Root.model_validate_json(data_str)
    data = root.model_dump()
    areas:list[str] = list(set(map(lambda value:value['行政區'], data)))

    option = st.selectbox("請選擇行政區",areas)
    st.write("您選擇:", option)

    def change_area():
        st.write(st.session_state.sarea)

    if 'sarea' not in st.session_state:
        st.session_state.sarea = "淡水區" #default option value

    with st.sidebar:
        option2 = st.selectbox(":orange[請選擇行政區域:]", options=areas, on_change=change_area, key='sarea')
        st.write("您選擇:", option2)

    st.write(st.session_state)

