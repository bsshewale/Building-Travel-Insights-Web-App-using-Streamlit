
import streamlit as st
import pandas as pd
from Model import get_hotel_recommendations, df

import logging

# Initialize the logger
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Function to log user feedback
def log_feedback(feedback_data):
    try:
        # Log the user feedback to a file
        with open('feedback.log', 'a') as feedback_file:
            feedback_file.write(f"{feedback_data}\n")
        logger.info("User feedback logged successfully.")
    except Exception as e:
        logger.error(f"Error logging user feedback: {str(e)}")

st.title('Hotel Recommendation App')

# Create dropdowns for Package Type, Start City, and Destination
package_types = df['Package Type'].unique()
start_cities = df['Start City'].unique()
destinations = df['Destination'].unique()

package_type = st.selectbox('Select Package Type:', package_types)
start_city = st.selectbox('Select Start City:', start_cities)
destination = st.selectbox('Select Destination:', destinations)

# Slider for Price
price = st.slider('Select Maximum Price:', min_value=0, max_value=df['Price Per Two Persons'].max(), value=10000)

# Get recommendations on button click
if st.button('Get Recommendations'):
    recommended_hotels = get_hotel_recommendations(package_type, start_city, price, destination)
    if isinstance(recommended_hotels, str):
        st.warning(recommended_hotels)
    else:
        st.table(recommended_hotels)

# Collect user feedback
st.write("Provide feedback:")
feedback_input = st.text_area("Enter your feedback here:")
if st.button("Submit Feedback"):
    if feedback_input:
        log_feedback(feedback_input)
        st.success("Thank you for your feedback!")

# Optionally, you can display some information about the selected filters
st.write('Selected Filters:')
st.write(f'Package Type: {package_type}')
st.write(f'Start City: {start_city}')
st.write(f'Destination: {destination}')
st.write(f'Maximum Price: {price}')