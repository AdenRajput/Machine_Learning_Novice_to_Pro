# Import necessary libraries
import streamlit as st
import seaborn as sns
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


# # add image banner
# from PIL import Image
# image = Image.open('banner.png')
# st.image(image, use_column_width=True)

# Title of the app
st.title("Exploratory Data Analysis App")

st.write("This is a simple example exploring the Iris dataset.")

# Load the iris dataset from seaborn
df = sns.load_dataset('iris')

# Add a checkbox in the sidebar. When checked, the EDA report is generated.
#if st.sidebar.checkbox("Generate EDA Report"):
    # Generate the ProfileReport
profile = ProfileReport(df, explorative=True)

    # Display the report in Streamlit
st_profile_report(profile)
