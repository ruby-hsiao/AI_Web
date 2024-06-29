import requests
from pydantic import BaseModel,Field,RootModel,field_validator,field_serializer
import streamlit as st
import source #匯入module
from source import Root #匯入class
import pandas as pd

try:
    data_str = source.download_youbike()
except Exception as e:
    st.error(e)
else:    
    root = Root.model_validate_json(data_str)
    data = root.model_dump()
    areas:list[str] = list(set(map(lambda value:value['行政區'], data)))

    st.title("台北市Youbike各行政區站點資料")
    tableContainer = st.container(border=False)

    display_data = []
    def search(spcific_name):
        for item in data:
            if item['行政區'] == spcific_name:
                display_data.append(item)
        #st.write(display_data)

    def change_area():
        sarea_name = st.session_state.sarea
        filter(search(sarea_name), data)
        
        with tableContainer:
            st.subheader(sarea_name)
            # table display
            #st.table(display_data)
            
            # dataframe
            #st.dataframe(display_data)

            # dataframe
            df1 = pd.DataFrame(data=display_data,
                               columns=['站點名稱','日期時間','地址','總數','可借','可還'])
            st.dataframe(data=df1)

            df2 = pd.DataFrame(display_data,
                               columns=['站點名稱','總數','可借','可還'])

            st.scatter_chart(df2,
                             x='站點名稱',
                             y='總數',
                             size='可借')


    with st.sidebar:
        option2 = st.selectbox(":orange[請選擇行政區域:]", options=areas, on_change=change_area, key='sarea')
        st.write("您選擇:", option2)
        
        

    #st.write(st.session_state)

