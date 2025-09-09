import streamlit as st
st.markdown(
    """
    <style>
    .big-heading {
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 40px;
        font-weight;
        text-align: left;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="ZeroOne",   
    page_icon="Favicom.png",  
    layout="wide"              
)

st.markdown(
    """
    <style>
    .image{
        image.align: centre;
    }
    """, 
    unsafe_allow_html=True
)
st.markdown("<div class='image'>Banner3.png</div>", unsafe_allow_html=True)

st.markdown("<div class='big-heading'>ZeroOne</div>", unsafe_allow_html=True)
def text_to_binary(message: str) -> str:
    return ' '.join(format(ord(i), '08b') for i in message)

def binary_to_text(binary: str) -> str:
    try:
        return ''.join([chr(int(b, 2)) for b in binary.split()])
    except Exception:
        return None

st.caption('''Welcome to ZeroOne, This app converts your any message to binary and any binary to text.
           Give it a try: ''')

user_input = st.text_area("Enter text or binary")

if st.button("Convert"):
    if all(ch in "01 " for ch in user_input.strip()):
        result = binary_to_text(user_input)
        if result is None:
            st.error("Invalid binary input!")
        else:
            st.success(f"Text: {result}")
    else:
        result = text_to_binary(user_input)
        st.success(f"Binary: {result}")
st.markdown("---")
st.markdown(
    """
    <style>
    .caption {
       font-family: 'Consolas', 'Courier New', monospace;
       text-align: left;
       color: gray; 
    }
    
    </style>
    """,

    unsafe_allow_html=True
)

st.markdown("<div class='caption'>-Aaradhya Rampuriya</div>", unsafe_allow_html=True)
st.markdown("<div class='caption'>Developer</div>", unsafe_allow_html=True)