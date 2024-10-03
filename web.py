import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

def load_data():
    day_df = pd.read_csv('day.csv')
    hour_df = pd.read_csv('hour.csv')
    return day_df, hour_df

day_df, hour_df = load_data()

# Convert 'dteday' to datetime format and create year, month, and day columns. I make it so only can choose per day, because if can be chosen per hour, gonna be very complicated
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df['year'] = day_df['dteday'].dt.year
day_df['month'] = day_df['dteday'].dt.month
day_df['day'] = day_df['dteday'].dt.day

# Sidebar
st.title("Bike Dataset Data Analysis :sparkles:")

st.sidebar.header("Select Analysis Type:")
analysis_type = st.sidebar.radio("Choose analysis type:", ('Seasonal Analysis', 'Weather Analysis', 'Weekdays vs Weekend', 'Monthly Transactions'))

st.sidebar.header("Select Date Range:")
min_date = day_df['dteday'].min()
max_date = day_df['dteday'].max()

start_date, end_date = st.sidebar.date_input(
    "Date range:",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

filtered_day_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & (day_df['dteday'] <= pd.to_datetime(end_date))]

if analysis_type == 'Seasonal Analysis':
    st.header("Total Transactions by Season")

    season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
    filtered_day_df['season_name'] = filtered_day_df['season'].map(season_mapping)

    # Group transactions by season
    seasonal_transactions = filtered_day_df.groupby('season_name')['cnt'].sum().reset_index()
    highest_season_index = seasonal_transactions['cnt'].idxmax()

    total_transactions = seasonal_transactions['cnt'].sum()
    st.metric("Total Transactions", value=f"{total_transactions:,}")

    # Set colors for the plot and the color for the biggest data
    colors = ['#90CAF9'] * len(seasonal_transactions)
    colors[highest_season_index] = '#0096C7'

    # Plotting the total transactions for each season
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='season_name', y='cnt', data=seasonal_transactions, palette=colors, ax=ax)
    ax.set_title('Total Transactions by Season')
    ax.set_xlabel('Season')
    ax.set_ylabel('Total Number of Transactions (cnt)')
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
    st.pyplot(fig)

elif analysis_type == 'Weather Analysis':
    st.header("Total Transactions by Weather Type")

    # Group transactions by weather type
    weather_transactions = filtered_day_df.groupby('weathersit')['cnt'].sum().reset_index()
    highest_weather_index = weather_transactions['cnt'].idxmax()

    total_transactions = weather_transactions['cnt'].sum()
    st.metric("Total Transactions", value=f"{total_transactions:,}")

    # Set colors for the bar plot and the color for the biggest data
    colors = ['#90CAF9'] * len(weather_transactions)
    colors[highest_weather_index] = '#0096C7'

    # Plotting the total transactions for each weather type
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=weather_transactions, palette=colors, ax=ax)
    ax.set_title('Total Transactions by Weather')
    ax.set_xlabel('Weather')
    ax.set_ylabel('Total Number of Transactions (cnt)')
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
    st.pyplot(fig)

elif analysis_type == 'Weekdays vs Weekend':
    st.header("Total Transactions by Weekdays vs Weekend")

    filtered_day_df['is_weekend'] = filtered_day_df['weekday'].apply(lambda x: 1 if x >= 5 else 0)

    # Group transactions by weekend vs weekday
    weekend_transactions = filtered_day_df.groupby('is_weekend')['cnt'].sum().reset_index()
    highest_weekend_index = weekend_transactions['cnt'].idxmax()

    total_transactions = weekend_transactions['cnt'].sum()
    st.metric("Total Transactions", value=f"{total_transactions:,}")

    # Set colors for the bar plot
    colors = ['#90CAF9'] * len(weekend_transactions)
    colors[highest_weekend_index] = '#0096C7'

    # Plotting the total transactions for weekdays vs weekend
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='is_weekend', y='cnt', data=weekend_transactions, palette=colors, ax=ax)
    ax.set_title('Total Transactions by Weekdays/Weekend')
    ax.set_xlabel('Day (0 = Weekday, 1 = Weekend)')
    ax.set_ylabel('Total Number of Transactions (cnt)')
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
    st.pyplot(fig)

elif analysis_type == 'Monthly Transactions':
    st.header("Total Transactions by Month for Each Year")

    # Grouping by 'year' and 'month' and calculating the sum of 'cnt'
    monthly_transactions = filtered_day_df.groupby(['year', 'month'])['cnt'].sum().reset_index()

    total_transactions = monthly_transactions['cnt'].sum()
    st.metric("Total Transactions", value=f"{total_transactions:,}")

    # Plotting the total transactions for each month of each year
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.lineplot(data=monthly_transactions, x='month', y='cnt', hue='year', marker='o', ax=ax)
    ax.set_title('Total Transactions by Month for Each Year')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Number of Transactions (cnt)')
    ax.set_xticks(range(1, 13))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
    st.pyplot(fig)
