import streamlit as st
from streamlit_app.pages import ai_agent, documentation

def main():
    st.set_page_config(
        page_title="Agent IA Éducatif",
        page_icon="🤖",
        layout="wide"
    )
    
    st.sidebar.title("🤖 Agent IA Éducatif")
    
    # Navigation
    page = st.sidebar.radio(
        "Choisir une page:",
        ["Agent IA", "Documentation"]
    )
    
    if page == "Agent IA":
        ai_agent.show()
    elif page == "Documentation":
        documentation.show()

if __name__ == "__main__":
    main()