# data_visualization.py
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from data_query import duration_to_seconds 

# Display the count label on top of each bar
def add_bar_label(ax):
    for bar in ax.patches:
        ax.annotate(format(bar.get_height(), '.0f'),(bar.get_x() + bar.get_width() / 2, bar.get_height()), ha='center', va='bottom', fontsize=5)

def generate_plots(df, column, title, xlabel, ylabel):
    plt.figure(figsize=(4, 3))  # Increase figure size for better readability
    if column == 'difficulty':
        df[column].dropna().plot(kind='hist', bins=5, color='grey', edgecolor='black', linewidth=0.1)
    elif column == 'duration_seconds':
        df[column].dropna().plot(kind='hist', bins=15, color='grey', edgecolor='black', linewidth=0.1)
        plt.xticks([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420], fontsize=5)
    elif column == 'language' or column == 'source':
        ax = df[column].value_counts().dropna().sort_index().plot(kind='bar', color='grey')
        plt.xticks(rotation=45)
        add_bar_label(ax)
    elif column == 'year':
        df['decade'] = (df['year'] // 10) * 10
        ax = df['decade'].value_counts().sort_index().plot(kind='bar', color='grey')
        # Add 's' to each label on the x-axis
        ax.set_xticklabels([f"{int(label.get_text())}s" for label in ax.get_xticklabels()], rotation=0)
        plt.xticks(rotation=0)
    elif column == 'gender':
        plt.figure(figsize=(5, 3))
        df = df.dropna(subset=[column])
        gender_counts = df[column].value_counts()
        plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    elif column == 'count':
        df.set_index('Date', inplace=True)
        df[column].plot(kind='line', marker='.', color='grey', markersize=0.2)
    
    plt.title(title, fontsize=7, color='black')
    plt.xlabel(xlabel, fontsize=5, color='black')
    plt.ylabel(ylabel, fontsize=5, color='black')
    plt.tick_params(axis='both', which='both', length=1, width=0.5)  # Length and width of ticks
    plt.xticks(fontsize=5)
    plt.yticks(fontsize=5)
    plt.grid(False)  # Disable the background grid lines
    plt.tight_layout()  # Adjust the layout to fit everything nicely

    # Make the outline of the graph thinner
    ax = plt.gca()  # Get the current axes
    ax.spines['top'].set_linewidth(False)  # Thinner top outline
    ax.spines['right'].set_linewidth(False)  # Thinner right outline
    ax.spines['left'].set_linewidth(0.2)  # Thinner left outline
    ax.spines['bottom'].set_linewidth(0.2)  # Thinner bottom outline

    st.pyplot(plt)

def make_plots(tab_df, play_df):
    # Plot 1: Histogram of songs by difficulty level
    generate_plots(tab_df, 'difficulty', 'Songs by Difficulty Level', 'Difficulty Level', 'Number of Songs')

    # Plot 2: Histogram of songs by duration
    tab_df['duration_seconds'] = tab_df['duration'].apply(duration_to_seconds)
    generate_plots(tab_df, 'duration_seconds', 'Songs by Duration', 'Duration(sec)', 'Number of Songs')

    # Plot 3: Bar chart of songs by language
    generate_plots(tab_df, 'language', 'Songs by Language', 'Language', 'Number of Songs')

    # Plot 4: Bar chart of songs by source
    generate_plots(tab_df, 'source', 'Songs by Source', 'Source', 'Number of Songs')

    # Plot 5: Bar chart of songs by decade
    generate_plots(tab_df, 'year', 'Songs by Decade', 'Year', 'Number of Songs')

    # Plot 6: Cumulative line chart of songs played
    generate_plots(get_cummulative_song_count(play_df), 'count', 'Songs Played Over Tuesdays', 'Date', 'Number of Songs')

    # Plot 7: Pie chart of songs by gender
    generate_plots(tab_df, 'gender', 'Songs by Gender', '', '')







def get_cummulative_song_count(play_df):
    date_columns = [col for col in play_df.columns if col.isdigit()]  # Get columns that are dates
    dates = pd.to_datetime(date_columns, format='%Y%m%d', errors='coerce')  # Convert to datetime
    songs_played_counts = [play_df[date].notna().sum() for date in date_columns]  # Count non-NaN values
    # Create a DataFrame for cumulative counts
    cumulative_df = pd.DataFrame({
        'Date': dates,
        'Songs Played': songs_played_counts
    })
    # Sort the DataFrame by Date
    cumulative_df = cumulative_df.sort_values(by='Date').reset_index(drop=True)
    cumulative_df['count'] = cumulative_df['Songs Played'].cumsum()
    # st.dataframe(cumulative_df)
    return cumulative_df



def load_data():
    tab_df = pd.read_csv("D:/SEM 1/MIS41110-Programming for Analytics/Assignment/tabdb.csv")
    play_df = pd.read_csv("D:/SEM 1/MIS41110-Programming for Analytics/Assignment/playdb.csv")    
    return tab_df, play_df


# Run the program
if __name__ == "__main__":
    df1, df2 = load_data()
    # get_cummulative_song_count(df2)
    make_plots(df1, df2)


