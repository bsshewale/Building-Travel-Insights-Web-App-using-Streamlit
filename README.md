# Building-Travel-Insights-Web-App-using-Streamlit


---

# Travel Recommendation Insights Web App

## Overview

This project is a **Streamlit-based web application** developed to display **data-driven insights and visualizations** derived from a **travel recommendation model**. The app provides an interactive interface to explore patterns, trends, and recommendations generated using machine learning and analytics techniques.

---

## Features

* Interactive dashboards built using **Streamlit**
* Visual exploration of travel-related data
* Insights generated from a **machine learning–based travel recommendation model**
* User-friendly layout for non-technical users
* Scalable structure for future model and feature enhancements

---

## Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **NumPy**
* **Matplotlib / Seaborn**
* **Machine Learning models (Scikit-learn)**

---

## Project Structure

```
project-root/
│
├── app/
│   └── streamlit_app.py
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── model.py
│
├── data/
│   └── raw/
│       └── dataset.csv   
│
├── logs/                
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md

```

---

## How to Run the Application

1. Clone the repository:

```bash
git clone <repository-url>
cd <project-folder>
```

2. Create and activate virtual environment:

```bash
python -m venv myenv
myenv\\Scripts\\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

5. Open browser and visit:

```
http://localhost:8501
```
<img width="467" height="546" alt="image" src="https://github.com/user-attachments/assets/387a5318-ffd7-427e-9b9b-b8d43d180e4f" />

---

## Use Case

The application helps users and businesses:

* Understand travel behavior patterns
* Gain actionable insights from historical data
* Support recommendation-driven decision-making

---

## Future Enhancements

* Real-time recommendation predictions
* User input–based personalization
* Cloud deployment
* Model performance monitoring

---

## Author

**Bharat Shewale**
MS in Data Science & AI
Python | SQL | Machine Learning | Data Analytics

---


