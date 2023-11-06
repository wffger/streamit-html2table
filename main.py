import streamlit as st
import pyperclip
import funs


col01, col02 = st.columns(2)
with col01:
    column = st.number_input('Set column amount',value=2,min_value=1,format="%i")
with col02:
    delimiter = st.text_input('Set delimiter', value="|", max_chars=3)

col11, col12 = st.columns(2)
with col11:
    st.header("Input")
    txt_input = st.text_area(label="HTML elements to be converted",value="",height=250)

if "default" not in st.session_state:
    st.session_state["default"] = ""
with col12:
    st.header("Ouput")
    txt_output = st.text_area(label="Converted table",value=st.session_state["default"],height=250)


st.write(f"You input {len(txt_input)} characters.")

if st.button('Run'):
    result = funs.apply_rule(column, delimiter, txt_input )
    st.session_state["default"] = result
    st.experimental_rerun()


if st.button('Copy'):
    pyperclip.copy(txt_output)
    st.success('Text copied successfully!')