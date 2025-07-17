import streamlit as st

# Panggil set_page_config langsung setelah import streamlit
st.set_page_config(
    page_title='Swarm App',
    layout='wide',
    initial_sidebar_state='expanded'
)

import streamlit as st
import eda
import finder

def main():
    with st.sidebar:
    
        # Branding Swarm App
        st.markdown(
            """
            <div style='text-align: center;'>
                <img src='https://huggingface.co/spaces/anismarsela32/swarm-app/resolve/main/src/logo-saja.png'
                    width='150'
                    style='margin-bottom: -30px; margin-top: -10px;' />
            </div>
            <div style="text-align: center; margin-top: -30px;">
                <h2 style='color: #0047AB; margin: 0;'>Swarm App</h2>
                <p style='font-size: 13px; color: gray; margin: 0;'>
                    Discover your ideal smartwatch with AI-powered search and sentiment!
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


        # Navigasi
        menu = ["Smartwatch Finder", "Exploratory Data Analysis"]
        choice = st.selectbox("📂 Select Page", menu)

    # Main content
    if choice == "Smartwatch Finder":
        finder.run()
    elif choice == "Exploratory Data Analysis":
        eda.run()


if __name__ == '__main__':
    main()
