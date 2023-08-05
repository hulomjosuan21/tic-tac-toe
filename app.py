import streamlit as st

st.set_page_config("Site Error 110",layout='centered',initial_sidebar_state='auto')
def main():
    password = st.text_input("Password",type='password')
    
    if st.button("Proceed",key="btn"):
        if password == "hulom2212004":
            tab1,tab2 = st.tabs(["Video #1","Video #2"])
            with tab1:
                st.video("vid-1.mp4",format='video/mp4')
            with tab2:
                st.video("vid-2.mp4",format='video/mp4')
        else:
            st.error("Wrong password!")

if __name__ == '__main__':
    main()
