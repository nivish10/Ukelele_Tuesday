import streamlit as st
import pandas as pd

from data_loader import load_data
from data_query import query_data

def main():

    # Initialize page in session state
    if 'page' not in st.session_state:
        st.session_state.page = 'upload'
    if 'tab_df' not in st.session_state:
        st.session_state.tab_df = None
    if 'play_df' not in st.session_state:
        st.session_state.play_df = None
    if 'request_df' not in st.session_state:
        st.session_state.request_df = None

    # Load data and navigation
    if st.session_state.page == 'upload':
        # Load data
        tab_df, play_df, request_df = load_data()

        # Store data in session state after loading
        if tab_df is not None:
            st.session_state.tab_df = tab_df
        if play_df is not None:
            st.session_state.play_df = play_df
        if request_df is not None:
            st.session_state.request_df = request_df

        # Check if all files have been uploaded before enabling "Next" button
        if st.session_state.tab_df is not None and st.session_state.play_df is not None and st.session_state.request_df is not None:
            if st.button("Next"):
                st.session_state.page = 'filter'
        else:
            st.write("Please upload all required files to proceed.")
    
    elif st.session_state.page == 'filter':
        # Query data
        query_data(st.session_state.tab_df, st.session_state.play_df)
        # if st.button("Next"):
        #         st.session_state.page = 'view'

    # elif st.session_state.page == 'view':
    #     st.title("View Your Data")
        # Plot data
        


# Run the program
if __name__ == "__main__":
    main()