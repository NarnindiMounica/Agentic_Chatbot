import streamlit as st
import os

from src.langgraph_agenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph_agenticai.LLMs.groq_llm import GroqLLM
from src.langgraph_agenticai.graph.graph_builder import GraphBuilder
from src.langgraph_agenticai.ui.streamlitui.display_result import DisplayResultStreamlit

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


    user_message = st.chat_input("Enter your message: ")  

    if user_message:
        try:

            #configure the LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_models()

            if not model:
                st.error("Error: LLM Model could not be initialized")
                
            #Initialize and set up the graph based on usecase
            usecase = user_input.get("selected_usecase")  

            if not usecase:
                st.error("Error: No use case selected") 

            #graph builder
            graph_builder = GraphBuilder(model)

            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()

            except Exception as e:
                st.error(f"Error: graph setup failed {e}")    

        except Exception as e:
            st.error(f"Error: graph setup failed {e}") 

        return    
