import streamlit as st
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(page_title="Calculating Intrinsic Value using Discounted Cash Flow Method", layout="wide")
st.title("Calculating Intrinsic Value using Modified Ben Graham Method")

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
    st.write("Formula Share Intrinsic Value = EPS*(EPS0+M*G)*A/Y")
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
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
form = st.form("my-form")
g05 = form.slider(label="Predicted Average Growth Rate Per Year for the next five years in %", min_value = 0.00, max_value = 100.00, step =.05, format ="%.2f")
#st.write("Predicted Growth Rate for the sixth to ninth years")
eps = form.number_input("Earnings Per Share (EPS)",   step =.01, format ="%.2f")
aaa_c = form.slider(label="Current Yield Per Year of AAA corporate bonds in the country in %", min_value = 1.00, max_value = 100.00, step =.05, format ="%.2f")
aaa_30 = form.slider(label="Average Yield Per Year of AAA corporate bonds for last 30 years in the country in %", min_value = 0.00, max_value = 100.00, step =.05, format ="%.2f")
eps_0 = form.number_input("Earnings Per Share (EPS) of a zero growth company in the country (Eg: India - 10 ) ",   step =.01, format ="%.2f")
#st.write("Enterprise Values (in millions)")
m =  form.selectbox(label="Multiplication Factor - Select 1 for a country growing at less that 4 percentage GDP else 2", options=(1,2), index = 0 )
sp = form.number_input("Share Price",   step =.01, format ="%.2f")
fs = form.slider(label="Factor of Safety in %", min_value = 0.00, max_value = 100.00, step =.05, format ="%.2f")

calculate = form.form_submit_button("Calculate")
if calculate:
    bg_calculate_intrinsic_value()

refresh = form.form_submit_button("Refresh  ")
if refresh:
    #clear_input_fields()
    #st.write("Refresh2 button click is working")
    #st.write(st.session_state)
    streamlit_js_eval(js_expressions="parent.window.location.reload()")
    
