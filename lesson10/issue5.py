import streamlit as st

st.subheader("BMI值計算")
st.divider()
st.latex('BMI值計算公式: BMI = 體重(公斤)/身高^2(公尺^2)')
st.latex('例如：一個52公斤的人，身高是155公分，則BMI為:')
st.markdown('''<h6 style="color:blue;text-align:center">\
            52(公斤) / 1.552 ( 公尺<sup>2</sup> ) = 21.6</h6>''',
            unsafe_allow_html=True)

st.markdown('<h6 style="color:orange;text-align:center">體重正常範圍為 BMI = 18.5～24</h6>',
            unsafe_allow_html=True)

st.markdown('<hr style="border:0;margin:0 auto;width:80%;border-top:2px dotted blue">',
            unsafe_allow_html=True)

st.write("<h6 style='color:purple;text-align:center'>快看看自己的BMI是否在理想範圍吧!</h6>", unsafe_allow_html=True)

def clear():
    st.session_state.height = 100.0
    st.session_state.weight = 30.0

with st.form('bmi_form', border=False):
    h = st.slider(':green[選擇身高(cm)]', min_value=100.0, max_value=199.0, key='height')
    w = st.number_input(':green[選擇體重(kg)]', min_value=30.0, max_value=200.0, key='weight')

    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
    with col1:
        submitted = st.form_submit_button("BMI計算")
    
    with col2:

        if submitted:
            st.session_state.bmi = round((w / (h/100) **2), 1)

            if st.session_state.bmi < 18.5:
                result = "體重過輕"  
            elif st.session_state.bmi < 24:
                result = "正常範圍"
            elif st.session_state.bmi < 27:
                result = "過重"
            elif st.session_state.bmi < 30:
                result = "輕度肥胖"		
            elif st.session_state.bmi < 35:
                result = "中度肥胖"
            else:
                result = "重度肥胖"
            
            st.session_state.bmi_result = f"您的BMI是: {st.session_state.bmi}, 狀態:{result}"
            st.write(f"#### :orange[{st.session_state.bmi_result}]", unsafe_allow_html=True)
        
    with col3:
        cleared = st.form_submit_button("清除", on_click=clear)


    
    col4, col5, col6 = st.columns(3)
    with col4:
    st.text("")

    with col5:
    st.text("身體質量指數(BMI)(kg/m2)")

    with col6:
    st.text("腰圍(cm)")






