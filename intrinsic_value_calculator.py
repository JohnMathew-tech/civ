import streamlit as st
#from streamlit_js_eval import streamlit_js_eval
import pyautogui
from decouple import config

st.set_page_config(page_title="Calculate Intrinsic Value", layout="wide")
st.title("Calculate Intrinsic Value Stock Investing")
DISPLAY = config('DISPLAY') 
st.write(DISPLAY)
refresh = st.button("Refresh")
if refresh:
    try:
        #streamlit_js_eval(js_expressions="parent.window.location.reload()")
        pyautogui.hotkey('f5')
    except:
        st.write("Error in Refreshing. Please try again later")
        
def dcf_calculate_intrinsic_value():
    # Get input field values
    #st.write("Calculate button click is working")
    g05 = input1
    #st.write("g05",str(g05))
    g69 = input2
    #st.write("g69",str(g69))
    ev = input3
    #st.write("ev",str(ev))
    fcf = input4
    #st.write("fcf",str(fcf))
    dr = input5
    #st.write("dr",str(dr))
    fs = input6
    #st.write("fs",str(fs))
    
    

    # Validate input fields
    if not g05 or not g69 or not ev or not fcf or not dr or not fs:
        st.error("All input fields are mandatory")
        return
    # Perform calculations
    y0, y1, y2, y3, y4, y5, y6, y7, y8, y9 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    pv0 = fcf / (1 + dr/100) ** y0
    fcf1 = fcf * (100 + g05) / 100
    pv1 = fcf1 / (1 + dr/100) ** y1
    fcf2 = fcf1 * (100 + g05) / 100
    pv2 = fcf2 / (1 + dr/100) ** y2
    fcf3 = fcf2 * (100 + g05) / 100
    pv3 = fcf3 / (1 + dr/100) ** y3
    fcf4 = fcf3 * (100 + g05) / 100
    pv4 = fcf4 / (1 + dr/100) ** y4
    fcf5 = fcf4 * (100 + g69) / 100
    pv5 = fcf5 / (1 + dr/100) ** y5
    fcf6 = fcf5 * (100 + g69) / 100
    pv6 = fcf6 / (1 + dr/100) ** y6
    fcf7 = fcf6 * (100 + g69) / 100
    pv7 = fcf7 / (1 + dr/100) ** y7
    fcf8 = fcf7 * (100 + g69) / 100
    pv8 = fcf8 / (1 + dr/100) ** y8
    fcf9 = fcf8 * (100 + g69) / 100
    pv9 = fcf9 / (1 + dr/100) ** y9

    tv = ev / fcf
    ev9 = fcf9 * tv
    pvev9 = ev9 / (1 + dr/100) ** y9

    iv = sum([pv0, pv1, pv2, pv3, pv4, pv5, pv6, pv7, pv8, pv9]) + pvev9
    aiv = iv * (100-fs )/ 100
    d = aiv - ev
    ds = d / aiv * 100

    # Display results
    st.markdown("### Results")
    st.write("Predicted Average Growth Rate Per Year for the next five years:",'%.2f'%g05,"%")
    st.write("Predicted Average Growth Rate Per Year for the sixth to ninth years:", '%.2f'%g69, "%")
    st.write("Enterprise Value (in millions):", '%.2f'%ev)
    st.write("Free Cash Flow FCF (in millions):", '%.2f'%fcf)
    st.write("Discount Rate (Expected Average Inflation Per Year for next 10 years):", '%.2f'%dr,"%")
    st.write("Factor of Safety:", '%.2f'%fs,"%")

    st.markdown("### Table")
    table_data = [
        ("Year", "FCF", "Present Value"),
        (str(y0), '%.2f'%fcf, '%.2f'%pv0),
        (str(y1), '%.2f'%fcf1, '%.2f'%pv1),
        (str(y2), '%.2f'%fcf2, '%.2f'%pv2),
        (str(y3), '%.2f'%fcf3, '%.2f'%pv3),
        (str(y4), '%.2f'%fcf4, '%.2f'%pv4),
        (str(y5), '%.2f'%fcf5, '%.2f'%pv5),
        (str(y6), '%.2f'%fcf6, '%.2f'%pv6),
        (str(y7), '%.2f'%fcf7, '%.2f'%pv7),
        (str(y8), '%.2f'%fcf8, '%.2f'%pv8),
        (str(y9), '%.2f'%fcf9, '%.2f'%pv9),
        ("Enterprise Value 9th year", '%.2f'%ev9, '%.2f'%pvev9)
    ]
    st.table(table_data)

    st.write("Intrinsic Value:", '%.2f'%iv)
    st.write("Adjusted Intrinsic Value (after applying factor of safety):", '%.2f'%aiv)
    st.write("Difference:", '%.2f'%d)
    st.write("Discount:", '%.2f'%ds,"%")
def bg_calculate_intrinsic_value():
    # Validate input fields
    if not g05 or not eps or not aaa_c or not aaa_30 or not eps_0 or not m or not sp or not fs:
        st.error("All input fields are mandatory")
        return
    siv = (eps*(eps_0+m*g05)*aaa_30)/aaa_c

    aiv = siv * (100-fs )/ 100
    d = aiv - sp
    ds = d / aiv * 100

    # Display results
    st.markdown("## Results")
    st.write("Predicted Average Growth Rate Per Year for the next five years (G):",'%.2f'%g05,"%")
    st.write("Earnings Per Share (EPS):", '%.2f'%eps)
    st.write("Current Yield Per Year of AAA corporate bonds in the country in % (Y):", '%.2f'%aaa_c,"%")
    st.write("Average Yield Per Year of AAA corporate bonds for last 30 years in the country in % (A):", '%.2f'%aaa_30,"%")
    st.write("Earnings Per Share (EPS0) for zero growth company:", '%.2f'%eps_0)
    st.write("Multiplication Factor (M):", '%.2f'%m)
    st.write("Share Price:", '%.2f'%sp)
    st.write("Factor of Safety:", '%.2f'%fs,"%")
    st.write("Formula for Share Intrinsic Value = EPS*(EPS0+M*G)*A/Y")
    st.write("--------------------------------------------")
    st.write("Intrinsic Value:", '%.2f'%siv)
    st.write("Adjusted Intrinsic Value (after applying factor of safety):", '%.2f'%aiv)
    st.write("Difference:", '%.2f'%d)
    st.write("Discount:", '%.2f'%ds,"%")
# Initialize input fields
#if "input1" not in st.session_state:
    #clear_input_fields()

# Input Fields
#st.write("Predicted Growth Rate for next five years")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .stButton > button {
                color: black;
                background: gray;
                width: 100px;
                height: 50px;
            }
            div.css-keje6w.esravye1 {
                background-color: #EEEEEE;
                border: 5px solid #CCCCCC;
                border-radius: 10px;
            }
            div.css-r421ms.en8akda1 {
                border-width: 0px; 
            }

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
col1, col2= st.columns(2)
with col1.container():
    st.markdown("### Discounted Cash Flow (DCF) Method ") 
    dcf_form = st.form("dcf-form")
    with dcf_form:
        #input1 = form.number_input(label="Predicted Average Growth Rate Per Year for the next five years",  step =1., format ="%.2f")
        input1 = st.slider(label="Predicted Average Growth Rate Per Year for the next five years in %", key="f1", min_value = 0.00, max_value = 100.00, step =.05, format ="%.2f")
        #st.write("Predicted Growth Rate for the sixth to ninth years")
        #input2 = form.number_input("Predicted Average Growth Rate Per Year for the sixth to ninth years",  step =1., format ="%.2f")
        input2 = st.slider(label="Predicted Average Growth Rate Per Year for the sixth to ninth years in %", min_value = 0.00, max_value = 100.00, step =.05, format ="%.2f")
        #st.write("Enterprise Values (in millions)")
        input3 = st.number_input("Enterprise Values (in millions)",   step =.01, format ="%.2f")
        #st.write("Free Cash Flow FCF (in millions)")
        input4 = st.number_input("Free Cash Flow FCF (in millions)",   step =.01, format ="%.2f")
        #st.write("Discount Rate (Expected Average Inflation for next 10 years)")
        #input5 = form.number_input("Discount Rate (Expected Average Inflation for next 10 years)",  step =1., format ="%.2f")
        input5 = st.slider(label="Discount Rate (Expected Average Inflation Per Year for next 10 years) in %", min_value = 0.00, max_value = 100.00, step =.05, format ="%.2f")
        #st.write("Factor of Safety")
        #input6 = form.number_input("Factor of Safety", step =1.,format ="%.2f" )
        input6 = st.slider(label="Factor of Safety in %", min_value = 0.00, max_value = 100.00, step =.05, format ="%.2f")
        calculate = st.form_submit_button("Calculate")
        if calculate:
            try:
                dcf_calculate_intrinsic_value()
            except:
                st.write("Error in calculation. Please try again")
                    
with col2:
    st.markdown("### Modified Ben Graham Method")
    bg_form = st.form("bg-form")
    with bg_form:
        g05 = st.slider(label="Predicted Average Growth Rate Per Year for the next five years in %", min_value = 0.00, max_value = 100.00, step =.05, format ="%.2f")
        #st.write("Predicted Growth Rate for the sixth to ninth years")
        eps = st.number_input("Earnings Per Share (EPS)",   step =.01, format ="%.2f")
        aaa_c = st.slider(label="Current Yield Per Year of AAA corporate bonds in the country in %", min_value = 1.00, max_value = 100.00, step =.05, format ="%.2f")
        aaa_30 = st.slider(label="Average Yield Per Year of AAA corporate bonds for last 30 years in the country in %", min_value = 0.00, max_value = 100.00, step =.05, format ="%.2f")
        eps_0 = st.number_input("Earnings Per Share (EPS) of a zero growth company in the country (Eg: India - 10 ) ",   step =.01, format ="%.2f")
        #st.write("Enterprise Values (in millions)")
        m =  st.selectbox(label="Multiplication Factor - Select 1 for a country growing at less that 4 percentage GDP else 2", options=(1,2), index = 0 )
        sp = st.number_input("Share Price",   step =.01, format ="%.2f")
        fs = st.slider(label="Factor of Safety in %", min_value = 0.00, max_value = 100.00, step =.05, format ="%.2f")
        calculate = st.form_submit_button("Calculate")
        if calculate:
            try:
                bg_calculate_intrinsic_value()
            except:
                st.write("Error in calculation. Please try again")             


    
