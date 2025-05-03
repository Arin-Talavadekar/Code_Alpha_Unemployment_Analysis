import streamlit as st
import pandas as pd
import Viz_utils  # this is the file you just made

# Load your cleaned dataset
df = pd.read_csv('cleaned_unemployment_data.csv')

# Sidebar navigation (optional)
st.sidebar.title("Unemployment Analysis")
option = st.sidebar.selectbox("Select Visualization", (
    "India's Unemployment Trend",
    "Region-wise Trend",
    "Average by Region",
    "Area Distribution Boxplot",
    "Correlation Matrix",
    "Month-wise Boxplot"
))

# Display selected visualization
if option == "India's Unemployment Trend":
    st.pyplot(Viz_utils.plot_unemployment_trend(df))

elif option == "Region-wise Trend":
    st.pyplot(Viz_utils.plot_region_trend(df))

elif option == "Average by Region":
    st.pyplot(Viz_utils.plot_avg_region_bar(df))

elif option == "Area Distribution Boxplot":
    st.pyplot(Viz_utils.plot_area_boxplot(df))

elif option == "Correlation Matrix":
    st.pyplot(Viz_utils.plot_corr_matrix(df))

elif option == "Month-wise Boxplot":
    st.pyplot(Viz_utils.plot_month_boxplot(df))
