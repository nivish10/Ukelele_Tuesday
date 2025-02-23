import streamlit as st
import pandas as pd

def load_data():
    # Upload files and create data frames
    tab_df, play_df, request_df = upload_file()

    # Validate data
    # validate_tab_df(tab_df)
    # validate_play_df(play_df)
    # validate_request_df(request_df)

    return tab_df, play_df, request_df

def upload_file():
    # Sidebar for file uploads
    tabdb_file = st.sidebar.file_uploader("Upload tabdb.csv", type=["csv"])
    playdb_file = st.sidebar.file_uploader("Upload playdb.csv", type=["csv"])
    requestdb_file = st.sidebar.file_uploader("Upload requestdb.csv", type=["csv"])

    st.title("Upload your data files")
    st.write("*Follow this date format for accurate data analysis - YYYYMMDD")

    # Initialize dataframes as None
    tab_df, play_df, request_df = None, None, None

    # Load each file if it’s uploaded
    if tabdb_file is not None:
        tab_df = load_csv(tabdb_file)
        st.write("Tab Data Loaded Successfully!")

    if playdb_file is not None:
        play_df = load_csv(playdb_file)
        st.write("Play Data Loaded Successfully!")

    if requestdb_file is not None:
        request_df = load_csv(requestdb_file)
        st.write("Request Data Loaded Successfully!")

    return tab_df, play_df, request_df

def load_csv(file_path):
    """Loads a CSV file and handles errors."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File {file_path} is empty.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def validate_tab_df(tab_df):
    required_columns_tab = ['song', 'artist', 'year', 'type', 'gender', 'duration', 'language',
                            'tabber', 'source', 'date', 'difficulty', 'specialbooks']
    # if not validate_data(tab_df, required_columns_tab):
    #     st.write("Validation failed for Tab Data")
        
def validate_play_df(play_df):
    required_columns_play = ['song', 'artist']
    # if not validate_data(play_df, required_columns_play):
    #     st.write("Validation failed for Play Data")

def validate_request_df(request_df):
    required_columns_request = ['song', 'artist']
    # if not validate_data(request_df, required_columns_request):
    #     st.write("Validation failed for Request Data")
