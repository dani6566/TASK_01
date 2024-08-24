import streamlit as st   #Web development
import numpy as np   # np mean,random...
import pandas as pd  #Read csv, df manipulation
import time      #To simulate a real time date,time loop
import plotly.express as px #Interactive charts
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

Data_benin = pd.read_csv("../data/benin-malanville.csv")
Data_sier = pd.read_csv("../data/sierraleone-bumbuna.csv")
Data_togo = pd.read_csv("../data/togo-dapaong_qc.csv")


Select_Country = "Benin"

st.title("Solar Radiation Measurement Data Dashboard")

# Sidebar for navigation
st.sidebar.title("Navigation")
analysis_type = st.sidebar.selectbox("Select Analysis", ["", "Correlation", "Wind", "Temperature", "Histograms", "Z-Score", "Bubble Chart", "Data Cleaning"])
Select_Country = st.sidebar.selectbox("Select Country", ["Benin", "Sierraleone","Togo"])
st.sidebar.markdown("## Parameters")
selected_month = st.sidebar.slider("Select Month", 1, 12, 6)

if analysis_type == "Time Series":
    st.header("Time Series Analysis")

if Select_Country == "Benin":
    # Convert 'Timestamp' to datetime
    Data_benin['Timestamp'] = pd.to_datetime(Data_benin['Timestamp'])

    # Additional preprocessing steps as needed
    Data_benin['Year'] = Data_benin['Timestamp'].dt.year
    Data_benin['Month'] = Data_benin['Timestamp'].dt.month
    Data_benin['Day'] = Data_benin['Timestamp'].dt.day
    Data_benin['Hour'] = Data_benin['Timestamp'].dt.hour
    

    # Filter data by selected month
    df_month = Data_benin[Data_benin['Month'] == selected_month]

    # Plot GHI, DNI, DHI, and Tamb over time
    fig, ax = plt.subplots(figsize=(14, 7))
    df_month.set_index('Timestamp')[['GHI', 'DNI', 'DHI', 'Tamb']].plot(ax=ax)
    ax.set_title(f'Solar Irradiance and Temperature for Month {selected_month}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    st.pyplot(fig)

    if analysis_type == "Correlation":
        st.header("Correlation Analysis")

    # Calculate and plot heatmap for correlations
    corr = Data_benin[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

    # Pair plots for relationships
    st.subheader("Pair Plot Analysis")
    fig = sns.pairplot(Data_benin[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']])
    st.pyplot(fig)

    if analysis_type == "Wind":
        st.header("Wind Analysis")

        # Polar plot for wind direction and speed
        st.subheader("Wind Direction and Speed")
        fig = px.scatter_polar(Data_benin, r="WS", theta="WD", color="WSgust", 
                            title="Wind Speed and Direction", 
                            color_continuous_scale=px.colors.sequential.Plasma)
        st.plotly_chart(fig)
    if analysis_type == "Temperature":
        st.header("Temperature Analysis")

        st.subheader("Impact of Relative Humidity on Temperature Readings")
        fig = px.scatter(Data_benin, x="RH", y="TModA", color="GHI", size="WS",
                        title="Temperature vs. Humidity")
        st.plotly_chart(fig)
    if analysis_type == "Histograms":
        st.header("Histograms")

        variable = st.sidebar.selectbox("Select Variable", Data_benin.select_dtypes(include='number').columns)
        fig, ax = plt.subplots(figsize=(10, 6))
        Data_benin[variable].hist(bins=20, ax=ax)
        ax.set_title(f'Distribution of {variable}')
        st.pyplot(fig)
    if analysis_type == "Z-Score":
        st.header("Z-Score Analysis")

        
    if analysis_type == "Bubble Chart":
        st.header("Bubble Chart Analysis")

        fig = px.scatter(Data_benin, x="GHI", y="Tamb", size="WS", color="RH", 
                        title="GHI vs. Temperature with Wind Speed and Humidity",
                        hover_data=["BP"])
        st.plotly_chart(fig)
    if analysis_type == "Data Cleaning":
        st.header("Data Cleaning")

        st.subheader("Handle Missing Values")
        df_cleaned = Data_benin.dropna(subset=['Comments'])
        st.write(f"Original Data Size: {Data_benin.shape[0]} rows")
        st.write(f"Cleaned Data Size: {df_cleaned.shape[0]} rows")
        st.write("Cleaned data by removing rows with missing 'Comments' values.")

if Select_Country == "Togo":
    Data_togo['Timestamp'] = pd.to_datetime(Data_togo['Timestamp'])

    # Additional preprocessing steps as needed
    Data_togo['Year'] = Data_togo['Timestamp'].dt.year
    Data_togo['Month'] = Data_togo['Timestamp'].dt.month
    Data_togo['Day'] = Data_togo['Timestamp'].dt.day
    Data_togo['Hour'] = Data_togo['Timestamp'].dt.hour
        
    # Filter data by selected month
    df_month = Data_togo[Data_togo['Month'] == selected_month]

    # Plot GHI, DNI, DHI, and Tamb over time
    fig, ax = plt.subplots(figsize=(14, 7))
    df_month.set_index('Timestamp')[['GHI', 'DNI', 'DHI', 'Tamb']].plot(ax=ax)
    ax.set_title(f'Solar Irradiance and Temperature for Month {selected_month}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    st.pyplot(fig)

    if analysis_type == "Correlation":
        st.header("Correlation Analysis")

    # Calculate and plot heatmap for correlations
    corr = Data_togo[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

    # Pair plots for relationships
    st.subheader("Pair Plot Analysis")
    fig = sns.pairplot(Data_togo[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']])
    st.pyplot(fig)

    if analysis_type == "Wind":
        st.header("Wind Analysis")

        # Polar plot for wind direction and speed
        st.subheader("Wind Direction and Speed")
        fig = px.scatter_polar(Data_togo, r="WS", theta="WD", color="WSgust", 
                            title="Wind Speed and Direction", 
                            color_continuous_scale=px.colors.sequential.Plasma)
        st.plotly_chart(fig)
    if analysis_type == "Temperature":
        st.header("Temperature Analysis")

        st.subheader("Impact of Relative Humidity on Temperature Readings")
        fig = px.scatter(Data_togo, x="RH", y="TModA", color="GHI", size="WS",
                        title="Temperature vs. Humidity")
        st.plotly_chart(fig)
    if analysis_type == "Histograms":
        st.header("Histograms")

        variable = st.sidebar.selectbox("Select Variable", Data_togo.select_dtypes(include='number').columns)
        fig, ax = plt.subplots(figsize=(10, 6))
        Data_togo[variable].hist(bins=20, ax=ax)
        ax.set_title(f'Distribution of {variable}')
        st.pyplot(fig)
    if analysis_type == "Z-Score":
        st.header("Z-Score Analysis")

        
    if analysis_type == "Bubble Chart":
        st.header("Bubble Chart Analysis")

        fig = px.scatter(Data_togo, x="GHI", y="Tamb", size="WS", color="RH", 
                        title="GHI vs. Temperature with Wind Speed and Humidity",
                        hover_data=["BP"])
        st.plotly_chart(fig)
    if analysis_type == "Data Cleaning":
        st.header("Data Cleaning")

        st.subheader("Handle Missing Values")
        df_cleaned = Data_togo.dropna(subset=['Comments'])
        st.write(f"Original Data Size: {Data_benin.shape[0]} rows")
        st.write(f"Cleaned Data Size: {df_cleaned.shape[0]} rows")
        st.write("Cleaned data by removing rows with missing 'Comments' values.")

if Select_Country == "Sierraleone":
    Data_sier['Timestamp'] = pd.to_datetime(Data_sier['Timestamp'])

    # Additional preprocessing steps as needed
    Data_sier['Year'] = Data_sier['Timestamp'].dt.year
    Data_sier['Month'] = Data_sier['Timestamp'].dt.month
    Data_sier['Day'] = Data_sier['Timestamp'].dt.day
    Data_sier['Hour'] = Data_sier['Timestamp'].dt.hour
        
    # Filter data by selected month
    df_month = Data_sier[Data_sier['Month'] == selected_month]

    # Plot GHI, DNI, DHI, and Tamb over time
    fig, ax = plt.subplots(figsize=(14, 7))
    df_month.set_index('Timestamp')[['GHI', 'DNI', 'DHI', 'Tamb']].plot(ax=ax)
    ax.set_title(f'Solar Irradiance and Temperature for Month {selected_month}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    st.pyplot(fig)

    if analysis_type == "Correlation":
        st.header("Correlation Analysis")

    # Calculate and plot heatmap for correlations
    corr = Data_sier[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

    # Pair plots for relationships
    st.subheader("Pair Plot Analysis")
    fig = sns.pairplot(Data_sier[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']])
    st.pyplot(fig)

    if analysis_type == "Wind":
        st.header("Wind Analysis")

        # Polar plot for wind direction and speed
        st.subheader("Wind Direction and Speed")
        fig = px.scatter_polar(Data_sier, r="WS", theta="WD", color="WSgust", 
                            title="Wind Speed and Direction", 
                            color_continuous_scale=px.colors.sequential.Plasma)
        st.plotly_chart(fig)
    if analysis_type == "Temperature":
        st.header("Temperature Analysis")

        st.subheader("Impact of Relative Humidity on Temperature Readings")
        fig = px.scatter(Data_sier, x="RH", y="TModA", color="GHI", size="WS",
                        title="Temperature vs. Humidity")
        st.plotly_chart(fig)
    if analysis_type == "Histograms":
        st.header("Histograms")

        variable = st.sidebar.selectbox("Select Variable", Data_sier.select_dtypes(include='number').columns)
        fig, ax = plt.subplots(figsize=(10, 6))
        Data_sier[variable].hist(bins=20, ax=ax)
        ax.set_title(f'Distribution of {variable}')
        st.pyplot(fig)
    if analysis_type == "Z-Score":
        st.header("Z-Score Analysis")

        
    if analysis_type == "Bubble Chart":
        st.header("Bubble Chart Analysis")

        fig = px.scatter(Data_sier, x="GHI", y="Tamb", size="WS", color="RH", 
                        title="GHI vs. Temperature with Wind Speed and Humidity",
                        hover_data=["BP"])
        st.plotly_chart(fig)
    if analysis_type == "Data Cleaning":
        st.header("Data Cleaning")

        st.subheader("Handle Missing Values")
        df_cleaned = Data_sier.dropna(subset=['Comments'])
        st.write(f"Original Data Size: {Data_benin.shape[0]} rows")
        st.write(f"Cleaned Data Size: {df_cleaned.shape[0]} rows")
        st.write("Cleaned data by removing rows with missing 'Comments' values.")

