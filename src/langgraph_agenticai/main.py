import streamlit as st
import os

from src.langgraph_agenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():

    """
    Loads and runs the Langgraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model, sets up the graph based on the selected usecase, and displays the output while implementing exception handling for robustness.
    
    """

    #Load UI

    ui = LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: LLM Model should not be initialized.")

    return

user_message = st.chat_input("Enter your message: ")        