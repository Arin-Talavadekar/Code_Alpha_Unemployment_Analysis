import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 1️⃣ India's Unemployment Trend Over Time
def plot_unemployment_trend(df):
    fig, ax = plt.subplots(figsize=(12,6))
    sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)', ax=ax)
    ax.set_title("India's Unemployment Trend Over Time")
    plt.xticks(rotation=45)
    fig.tight_layout()
    return fig

# 2️⃣ Unemployment Rate by Region Over Time
def plot_region_trend(df):
    fig, ax = plt.subplots(figsize=(14,8))
    sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)', hue='Region', ax=ax)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.set_title('Unemployment Rate by Region Over Time')
    plt.xticks(rotation=45)
    fig.tight_layout()
    return fig

# 3️⃣ Average Unemployment Rate by Region
def plot_avg_region_bar(df):
    region_avg = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(12,6))
    region_avg.plot(kind='bar', ax=ax)
    ax.set_ylabel('Average Unemployment Rate (%)')
    ax.set_title('Average Unemployment Rate by Region')
    fig.tight_layout()
    return fig

# 4️⃣ Unemployment Rate Distribution by Area (Boxplot)
def plot_area_boxplot(df):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='Area', y='Estimated Unemployment Rate (%)', ax=ax)
    ax.set_title('Unemployment Rate Distribution by Area')
    fig.tight_layout()
    return fig

# 5️⃣ Correlation Matrix
def plot_corr_matrix(df):
    fig, ax = plt.subplots(figsize=(8,6))
    corr = df[['Estimated Unemployment Rate (%)','Estimated Employed','Estimated Labour Participation Rate (%)']].corr()
    sns.heatmap(corr, annot=True, cmap='viridis', ax=ax)
    ax.set_title('Correlation Matrix')
    plt.xticks(rotation=90)
    fig.tight_layout()
    return fig

# 6️⃣ Unemployment Rate by Month (Boxplot)
def plot_month_boxplot(df):
    fig, ax = plt.subplots()
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df['Month'] = df['Date'].dt.month
    sns.boxplot(data=df, x='Month', y='Estimated Unemployment Rate (%)', ax=ax)
    ax.set_title('Unemployment Rate by Month')
    fig.tight_layout()
    return fig
