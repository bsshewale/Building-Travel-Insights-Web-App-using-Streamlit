import streamlit as st
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.model import train_tfidf_model
from src.recommender import get_hotel_recommendations
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

st.title("Travel Recommendation System")

df = preprocess_data(load_data())
_, cosine_sim = train_tfidf_model(df['Hotel_Info'])

package_type = st.selectbox("Package Type", df['Package Type'].unique())
start_city = st.selectbox("Start City", df['Start City'].unique())
destination = st.selectbox("Destination", df['Destination'].unique())
price = st.slider("Max Price", 10000, 300000, 100000)

if st.button("Recommend"):
    result = get_hotel_recommendations(
        df, cosine_sim, package_type, start_city, price, destination
    )
    if result is None:
        st.warning("No matching hotels found.")
    else:
        st.dataframe(result.head(10))
