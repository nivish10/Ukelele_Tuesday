import streamlit as st
import pandas as pd 

def duration_to_seconds(duration_str):
    try:
        h, m, s = map(int, duration_str.split(':'))
        return h * 3600 + m * 60 + s
    except ValueError:
        return None  # Handle invalid formats gracefully



def filter_data(tab_df, play_df, filters, date_range, year_range, difficulty_range, duration_range):
    # Apply filters to each specified column
    for column, value in filters.items():
        if value != "All" and column in tab_df.columns:
            tab_df = tab_df[tab_df[column] == value]

    # Apply difficulty range filter
    if difficulty_range != "All":
        # Parse the range to get the lower and upper bounds
        lower, upper = map(float, difficulty_range.split('-'))
        tab_df = tab_df[(tab_df['difficulty'] >= lower) & (tab_df['difficulty'] < upper)]

    # Apply year range filter
    if year_range != "All":
        if year_range == "Before 1900":
            tab_df = tab_df[(tab_df['year'] < 1900)]
        else:
            # Parse the range to get the lower and upper bounds
            lower, upper = map(int, year_range.split('-'))
            tab_df = tab_df[(tab_df['year'] >= lower) & (tab_df['year'] < upper)]

    # Apply duration range filter
    tab_df = tab_df[(tab_df['duration_seconds'] >= duration_range[0]) & (tab_df['duration_seconds'] < duration_range[1])]
    
    # Convert the 'date' column to datetime using the specified format
    tab_df['date'] = pd.to_datetime(tab_df['date'].dropna().astype(int).astype(str), format='%Y%m%d', errors='coerce').dt.date
    
    if len(date_range) == 2:
        start_date, end_date = date_range
        tab_df = tab_df[(tab_df['date'] >= start_date) & (tab_df['date'] <= end_date)]
    
    # Calculate the number of times each song was played
    play_df.columns = play_df.columns.str.strip()
    tab_df['play_count'] = tab_df['song'].map(play_df.set_index('song').iloc[:, 1:].notna().sum(axis=1))
    
    return tab_df

def query_data(tab_df, play_df):
    st.title("Filter Your Data")
    tab_df.index = tab_df.index + 1
    # Removing tabber column for data privacy
    tab_df = tab_df.drop('tabber', axis=1)

    if 'duration' in tab_df.columns:
        tab_df['duration_seconds'] = tab_df['duration'].apply(duration_to_seconds)

    # Display columns available for filtering
    st.sidebar.title("Filter by")
    filters = {}
    for column in tab_df.columns:
        print(column, ' -> ', tab_df[column].dtype)
        if tab_df[column].dtype == 'object' and column not in ['duration']:
            # Make all entries in column to camel case
            tab_df[column] = tab_df[column].str.title()
            unique_values = sorted(tab_df[column].dropna().unique())
            selected_value = st.sidebar.selectbox(f"{column}", ["All"] + list(unique_values))
            filters[column] = selected_value

    # Difficulty Filter
    if "difficulty" in tab_df.columns:
        difficulty_range = st.sidebar.selectbox("difficulty", ["All", "0-1", "1-2", "2-3", "3-4", "4-5"])
    
    # Duration Filter (using converted seconds column)
    if "duration_seconds" in tab_df.columns:
        min_duration, max_duration = tab_df['duration_seconds'].min(), tab_df['duration_seconds'].max()
        duration_range = st.sidebar.slider("duration (seconds)", int(min_duration), int(max_duration), (int(min_duration), int(max_duration)))

    # Year Filter
    if "year" in tab_df.columns:
        year_range = st.sidebar.selectbox("year", ["All", "2020-2030", "2010-2020", "2000-2010", "1990-2000", "1980-1990", "1970-1980", "1960-1970", "1950-1960", "1940-1950", "1930-1940", "1920-1930", "1910-1920", "1900-1910", "Before 1900"])
    
    # Date range filter
    date_range = st.sidebar.date_input("Select date range", [])

    # Filter the data based on user input
    filtered_df = filter_data(tab_df, play_df, filters, date_range, year_range, difficulty_range, duration_range)
    
    # Drop duration_seconds column
    # Adding fillna for future empty year data
    filtered_df.loc[:, 'year'] = filtered_df['year'].fillna('Unknown').astype(str)
    st.dataframe(filtered_df.drop('duration_seconds', axis=1))


# def load_data():
#     tab_df = pd.read_csv("D:/SEM 1/MIS41110-Programming for Analytics/Assignment/tabdb.csv")
#     play_df = pd.read_csv("D:/SEM 1/MIS41110-Programming for Analytics/Assignment/playdb.csv")
    
#     return tab_df, play_df


# # Run the program
# if __name__ == "__main__":
#     df1, df2 = load_data()
#     query_data(df1, df2)