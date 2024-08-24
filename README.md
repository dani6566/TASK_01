# Project Overview

  This project involves analyzing solar radiation data, including Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), Diffuse Horizontal Irradiance (DHI), and ambient temperature (Tamb) over time. The goal is to observe patterns, trends, and anomalies in the data and evaluate the impact of environmental conditions on solar radiation components. 
 Tasks: 
    - Data Understanding
    - Exploratory Data Analysis (EDA)
    - Statistical thinking

# Data Description

The dataset contains the following key variables:
- Time: Timestamps of the measurements.
- GHI: Global Horizontal Irradiance (W/m²).
- DNI: Direct Normal Irradiance (W/m²).
- DHI: Diffuse Horizontal Irradiance (W/m²).
- Tamb: Ambient temperature (°C).
- TModA and TModB: Temperature readings from two different modules.
- WS: Wind speed (m/s).
- WSgust: Gust wind speed (m/s).
- WD: Wind direction (degrees).
- RH: Relative humidity (%).
- BP: Barometric pressure (hPa).
- Cleaning: A column indicating whether the sensors were cleaned at the time of measurement.
- Comments: Additional comments on the data points (if any).

# Analyses Performed

# 1. **Time Series Analysis**
   - **Objective**: To visualize and analyze the temporal patterns of GHI, DNI, DHI, and Tamb.
   - **Methodology**: Line graphs were plotted for each of these variables over time to observe monthly patterns, daily trends, and potential anomalies like peaks in solar irradiance or temperature fluctuations.

# 2. **Correlation Analysis**
   - **Objective**: To understand the relationships between various solar radiation components and temperature measures.
   - **Methodology**: Heatmaps and pair plots were used to visualize correlations between GHI, DNI, DHI, Tamb, TModA, and TModB. Scatter matrices were employed to investigate the relationship between wind conditions (WS, WSgust, WD) and solar irradiance.

# 3. **Wind Analysis**
   - **Objective**: To analyze wind speed and direction distribution.
   - **Methodology**: Polar plots were used to identify trends and significant wind events, showing the distribution of wind speed and direction, along with the variability of wind direction.

# 4. **Temperature Analysis**
   - **Objective**: To examine the influence of relative humidity (RH) on temperature readings and solar radiation.
   - **Methodology**: Scatter plots were used to analyze the relationship between RH and temperature, as well as their impact on solar radiation components.

# 5. **Histograms**
   - **Objective**: To visualize the frequency distribution of key variables.
   - **Methodology**: Histograms were created for GHI, DNI, DHI, WS, and temperatures to understand the distribution and spread of these variables.

# 6. **Z-Score Analysis**
   - **Objective**: To identify outliers in the data.
   - **Methodology**: Z-scores were calculated for key variables to flag data points that are significantly different from the mean.

# 7. **Bubble Charts**
   - **Objective**: To explore complex relationships between multiple variables.
   - **Methodology**: Bubble charts were plotted with GHI vs. Tamb vs. WS, with bubble size representing an additional variable like RH or BP.

# 8. **Data Cleaning**
   - **Objective**: To prepare the dataset for accurate analysis by handling anomalies and missing values.
   - **Methodology**: The dataset was cleaned by addressing null values, especially in the 'Comments' column, and handling any detected anomalies.

# Dashboard Development

A dashboard was developed using Streamlit to visualize the insights from the data analysis. This interactive tool allows users to explore the data and analysis results easily.

