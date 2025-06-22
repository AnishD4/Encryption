import random
import os

import streamlit as st
from chepy import Chepy

from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(
    page_title="Decryption Detective",
    page_icon="🕵️",
)

ctf_data = [
    ["122 105 126 117 114 125 124 111 117 116", "REVOLUTION", "OCTAL+ROT13"],
    ["68 73 83 67 79 86 69 82 89", "DISCOVERY", "CHARCODE"],
    ["434S4R56454R54494S4R", "CONVENTION", "HEXADECIMAL+ROT13"],
    ["48 49 48 48 48 48 49 49 32 48 49 48 48 49 49 49 49 32 48 49 48 48 49 49 49 48 32 48 49 48 48 48 49 49 48 32 48 49 48 48 49 48 48 49 32 48 49 48 48 48 49 48 48 32 48 49 48 48 48 49 48 49 32 48 49 48 48 49 49 49 48 32 48 49 48 48 48 48 49 49 32 48 49 48 48 48 49 48 49", "CONFIDENCE", "BINARY+CHARCODE"],
    ["eH0ldCNwciV4J3Q=", "INTERACTIVE", "ROT47+BASE64"],
    ["84 82 65 78 83 67 82 73 66 69", "TRANSCRIBE", "CHARCODE"],
    ["UNCCVARFF", "HAPPINESS", "ROT13"],
    ["SU5WSVNJQkxF", "INVISIBLE", "BASE64"],
    ["--. . -. . .-. .- - .. --- -.", "GENERATION", "MORSE"],
    ["``_ `_` `a_ `a_ ``` ``e `_d `ab `ab", "HAPPINESS", "OCTAL+ROT47"],
    ["526B3956546B524256456C5054673D3D", "FOUNDATION", "BASE64+HEXADECIMAL"],
    ["113 122 103 125 107 123 103 117 112 65 107 105 66 122 62 132", "TECHNOLOGY", "BASE32+OCTAL"],
    ["qprzv#~&}s", "BACKGROUND", "ROT47"],
    ["01000110 01001111 01010010 01001101 01001001 01000100 01000001 01000010 01001100 01000101", "FORMIDABLE", "BINARY+ATBASH"],
    ["KEYUURSRKZJEUVTLNRKVOUJ5HU======", "CREATIVITY", "BASE64+BASE32"],
    ["131 156 160 165 166 142 156 141 171 156 144 145", "INNOVATION", "OCTAL+ROT47"],
    ["5468414E4B53484C59", "FORMIDABLE", "CHARCODE+HEXADECIMAL"],
    ["FGEHPGHER", "STRUCTURE", "ROT13"],
    ["414348494556454D454E54", "ACHIEVEMENT", "HEXADECIMAL"],
    ["123 145 156 163 141 164 151 157 156", "SENSATION", "OCTAL+CHARCODE"],
    ["101 154 141 143 153 153 141 142 143 153", "BACKGROUND", "OCTAL+BASE32"],
    ["114 151 147 150 164 156 151 156 147", "LIGHTNING", "OCTAL"],
    ["JBUHW6WDRBQUY4Q=", "MANIPULATE", "BASE32+BINARY"],
    [".11010110 .10101110 ... etc", "COMPARISON", "BINARY+ROT47"],
    ["77 69 67 72 65 78 73 83 77", "MECHANISM", "CHARCODE"],
    ["-- .- -. .. .--. ..- .-.. .- - .", "MANIPULATE", "MORSE"],
    ["EMRAPOHRQ=", "COMPARISON", "BASE32+CHARCODE"],
    ["01000010 01010010 01000001 01001110 01000100", "TRANSCRIBE", "ROT13+BINARY"],
    ["106 117 110 100 97 109 101 110 116", "FOUNDATION", "OCTAL"],
    ["111 156 156 157 166 141 164 151 157 156", "INNOVATION", "OCTAL"],
    ["UINZXOLIRMT", "FORMIDABLE", "ATBASH"],
    ["}%-&@%~{", "LIMITATION", "ROT47"],
    ["103 150 145 155 151 163 164 162 171", "CHEMISTRY", "CHARCODE+BINARY"],
    ["01000100 01001001 01010010 01000101 01000011 01010100 01001001 01001111 01001110", "DIRECTION", "BINARY+HEXADECIMAL"],
    ["544543484E4F4C4F4759", "TECHNOLOGY", "HEXADECIMAL"],
    ["434F4E464944454E4345", "CONFIDENCE", "HEXADECIMAL"],
    ["GAYTAMBRGEYDAIBQGEYDAMJQGAYSAMBRGAYDCMJQGEQDAMJQGAYTAMBREAYDCMBRGAYTAMBAGAYTAMBQGAYDCIBQGEYDCMBRGAYCAMBRGAYDCMBQGEQDAMJQGAYTCMJREAYDCMBQGEYTCMA=", "LIMITATION", "BINARY+BASE32"],
    ["IRCUMSKOJFKEST2O", "DEFINITION", "BASE32"],
    ["126 117 103 101 102 125 114 101 122 131", "VOCABULARY", "OCTAL+ROT13"],
    ["066 065 040 067 066 040 067 061 040 067 071 040 070 062 040 067 063 040 070 064 040 067 062 040 067 067", "ALGORITHM", "CHARCODE+OCTAL"],
    ["NPURIRZRAG", "ACHIEVEMENT", "ROT13"],
    ["103 117 116 106 111 104 105 116 103 105", "CONFIDENCE", "OCTAL"],
    ["ZNAVCHYNGR", "MANIPULATE", "ROT13"],
    ["CBCUCTCTCDCBDCCHCUCT", "CONNECTION", "HEXADECIMAL+ROT47"],
    ["Q09NUEFSSVNPTg==", "COMPARISON", "BASE64"],
    ["123 124 122 125 103 124 125 122 105", "STRUCTURE", "OCTAL"],
    ["01000010 01000001 01000011 01001011 01000111 01010010 01001111 01010101 01001110 01000100", "BACKGROUND", "BINARY"],
    [".- .-- .- .-. . -. . ... ...", "AWARENESS", "MORSE"],
    ["01000001 01010111 01000001 01010010 01000101 01001110 01000101 01010011 01010011", "AWARENESS", "BINARY"],
    ["WVURMRGRLM", "DEFINITION", "ATBASH"]
]


st.markdown("""
<style>
    .stSelectbox, .stTextInput {
        font-size: 1.2rem;
    }
    button, .stButton>button {
        font-size: 1.2rem;
        padding: 0.5rem 2rem;
    }
    .stSuccess, .stError, .stInfo {
        font-size: 1.3rem;
        padding: 1.5rem;
    }
    h1, h2, h3 {
        margin-top: 1rem;
    }
    
    .stAppDeployButton {
            visibility: hidden;
        }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 100% !important;
    }

    .stSelectbox, .stTextInput input, .stTextArea textarea, .stToggleSwitch {
        font-size: 1.4rem !important;
        padding: 1rem !important;
    }

    .stButton button {
        font-size: 1.3rem !important;
        padding: 1rem 2rem !important;
    }

    h1, h2, h3, h4 {
        font-size: 2rem !important;
    }

    .stTextInput, .stSelectbox, .stTextArea {
        width: 100% !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        justify-content: space-between;
        display: flex;
        width: 100%;
    }

    .stTabs [data-baseweb="tab"] {
        flex-grow: 1;
        font-size: 1.2rem;
    }
        .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        width: 100%;
    }

    .stTabs [data-baseweb="tab"] {
        flex: 1;
        text-align: center;
        white-space: nowrap;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 4px 4px 0 0;
        padding: 10px 16px;
        font-weight: 600;
        background-color: #262730;
    }

    .stTabs [aria-selected="true"] {
        background-color: #151820;
    }
</style>
<div style="display: flex; justify-content: center; align-items: center;">
    <img src="https://github.com/AnishD4/Encryption/blob/main/logo.png?raw=true" style="width: 800px;" />
</div>

""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### Cipher Tools")
    st.markdown("Transform your text using multiple cipher algorithms")
with col2:
    st.markdown("### CTF Challenge")
    st.markdown("Test your decryption skills with cipher puzzles")
with col3:
    st.markdown("### AI Analysis")
    st.markdown("Let AI detect which cipher was used")

tab1, tab2, tab3 = st.tabs(["Encrypt/Decrypt", "CTF Challenge", "AI Analyze"])

options = ["base64", "Morse", "Hexadecimal", "ROT13", "Binary", "Atbash", "Octal", "Charcode", "base32", "ROT47"]
with tab1:
    selected = st.selectbox("Which cipher would you like to encode/decode?", options)

    txt = st.text_input("Enter the input you want decode/encode:")
    encode = st.toggle("Encode or Decode")
    if encode:
        st.write("Mode: **Encoding**")
    else:
        st.write("Mode: **Decoding**")
    res = "Error"
    match selected:
        case "base64":
            if encode:
                res = Chepy(txt).to_base64()
            else:
                res = Chepy(txt).from_base64()
        case "Morse":
            if encode:
                res = Chepy(txt).to_morse_code()
            else:
                res = Chepy(txt).from_morse_code()
        case "Hexadecimal":
            if encode:
                res = Chepy(txt).to_hex()
            else:
                res = Chepy(txt).from_hex()
        case "ROT13":
            res = Chepy(txt).rot_13()
        case "Binary":
            if encode:
                res = Chepy(txt).to_binary()
            else:
                res = Chepy(txt).from_binary()
        case "Atbash":
            if encode:
                res = Chepy(txt).atbash_encode()
            else:
                res = Chepy(txt).atbash_decode()
        case "Octal":
            if encode:
                res = Chepy(txt).to_octal()
            else:
                res = Chepy(txt).from_octal()
        case "Charcode":
            if encode:
                res = Chepy(txt).to_charcode()
            else:
                res = Chepy(txt).from_charcode()
        case "base32":
            if encode:
                res = Chepy(txt).to_base32()
            else:
                res = Chepy(txt).from_base32()
        case "ROT47":
            res = Chepy(txt).rot_47

    res = str(res)
    if res:
        res = "Result: **" + res + "**"
        st.success(res)

with tab2:
    st.header("CTF Challenge")
    st.write("Test your cipher decoding skills with a decoding challenge!")

    if "ctf_challenge" not in st.session_state:
        st.session_state.ctf_challenge = None
        st.session_state.user_solved = False

    if st.button("Get New Challenge"):
        st.session_state.ctf_challenge = random.choice(ctf_data)
        st.session_state.user_solved = False
        st.session_state.revealed = False

    if st.session_state.ctf_challenge:
        encrypted_text, answer, method = st.session_state.ctf_challenge

        st.write(f"**Encrypted text:** `{encrypted_text}`")
        st.write(f"**Hint:** This was encoded using {method}")

        ans = st.text_input("Your solution:", key="ctf_solution")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Submit Answer"):
                if ans.upper() == answer.upper():
                    st.success("Correct! You solved it!")
                    st.session_state.user_solved = True
                else:
                    st.error("You are incorrect. Try again!")

        with col2:
            if st.button("Reveal Answer"):
                st.session_state.revealed = True

        if "revealed" in st.session_state and st.session_state.revealed:
            st.info(f"The answer is: **{answer}**")

with tab3:
    st.header("AI Cipher type detector")
    st.write("Enter a encoded string and an AI will evaluate your text and tell you what cipher it was encoded with")

    inp = st.text_input("Enter your encoded string:")
    if inp:
        st_placeholder = st.empty()
        st_placeholder.markdown("**Thinking...**")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction="You are a cipher identification assistant. When given an encoded string, analyze it and return only the name(s) of the cipher or encoding method(s) used, in the order you believe they were applied. Focus primarily on the following types: base64, Morse, Hexadecimal, ROT13, Binary, Atbash, Octal, Charcode, base32, and ROT47, but include others if clearly identifiable. Do not provide explanations, decoding, or any additional text—only output the list of cipher names in order in this format: cipher1+cipher2+cipher3... . If unsure, output unsure."),
            contents="User Input:" + inp
        )
        st_placeholder.empty()
        output = response.text
        if output.lower() == "unsure":
            st.error("**The AI has analyzed patterns in your encoded string but it was not able to identify any valid ciphers**")
        else:
            st.success("The AI has analyzed patterns in your encoded string and has identified the most likely cipher(s) it was encoded with to be: **"+output+"**")



st.markdown("""
<div style="background-color: rgba(151, 166, 195, 0.05); 
           padding: 15px; border-radius: 8px; margin-top: 30px; text-align: center;">
    <p style="margin: 0; font-size: 14px; color: #6c757d;">
        Decryption Detective | Built by Srikar, Anish, and Sayuon using Streamlit and Chepy
    </p>
</div>
""", unsafe_allow_html=True)