import streamlit as st

tab1, tab2 = st.tabs(["Session_state", "Call_back"])

def get_bmi_result(bmi) ->str:
    if bmi < 18.5:
        txt = "體重過輕"  
    elif bmi < 24:
        txt = "正常範圍"
    elif bmi < 27:
        txt = "過重"
    elif bmi < 30:
        txt = "輕度肥胖"		
    elif bmi < 35:
        txt = "中度肥胖"
    else:
        txt = "重度肥胖"

    return txt

with tab1:
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

    with st.form('session_bmi_form', border=False):
        h = st.slider(':green[選擇身高(cm)]', min_value=100.0, max_value=199.0, key='height')
        w = st.number_input(':green[選擇體重(kg)]', min_value=30.0, max_value=200.0, key='weight')

        col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
        with col1:
            submitted = st.form_submit_button("BMI計算")
        
        with col2:

            if submitted:
                st.session_state.bmi = round((w / (h/100) **2), 1)

                result = get_bmi_result(st.session_state.bmi)
                
                st.session_state.bmi_result = f"您的BMI是: {st.session_state.bmi}, 狀態:{result}"
                st.write(f"#### :orange[{st.session_state.bmi_result}]", unsafe_allow_html=True)
            
        with col3:
            cleared = st.form_submit_button("清除", on_click=clear)

with tab2:
    st.subheader("BMI值計算2")
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


    def cal_BMI():
        st.session_state.bmi = round((st.session_state.w / (st.session_state.h/100) **2), 1)
    
    with st.form('callback_bmi_form', border=False):
        st.slider(':green[選擇身高(cm)]', min_value=100.0, max_value=199.0, key='h')
        st.number_input(':green[選擇體重(kg)]', min_value=30.0, max_value=200.0, key='w')

        col1, col2 = st.columns([0.2, 0.8])
        with col1:
            submitted = st.form_submit_button(label="BMI計算", on_click=cal_BMI)

        
        with col2:
            if submitted:
                result = get_bmi_result(st.session_state.bmi)
                
                st.session_state.bmi_result = f"您的BMI是: {st.session_state.bmi}, 狀態:{result}"
                st.write(f"#### :orange[{st.session_state.bmi_result}]", unsafe_allow_html=True)

