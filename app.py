# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (in your case from Google Colab or local environment)
anime_df = pd.read_csv('Anime.csv')

# Create a Streamlit app
st.title('Anime Dataset Analysis')

# Add a selectbox to choose the type of analysis
analysis_type = st.selectbox('Choose an analysis type', ['Exploratory Data Analysis (EDA)', 'Data Visualization'])

# Perform the chosen analysis
if analysis_type == 'Exploratory Data Analysis (EDA)':
    st.write(anime_df.head())  # Show the first few rows of the dataset
    st.write(anime_df.shape)   # Show the shape of the dataset
    st.write(anime_df.columns) # Show the columns of the dataset
    st.write(anime_df.dtypes)  # Show the data types of each column
    st.write(anime_df.describe())  # Show summary statistics

elif analysis_type == 'Data Visualization':
    st.subheader('Top 10 Anime Based on Rating')
    
    # Get top 10 anime based on rating
    top_anime = anime_df.nlargest(10, 'Rating')
    
    # Create a bar plot for the top 10 anime
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='Rating', y='Name', data=top_anime, ax=ax)
    ax.set_title('Top 10 Anime Based on Rating')
    ax.set_xlabel('Rating')
    ax.set_ylabel('Anime Name')
    
    # Display the plot in Streamlit
    st.pyplot(fig)