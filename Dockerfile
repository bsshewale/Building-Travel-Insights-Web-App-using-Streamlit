# Lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency list first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY Model.py .

# Copy datasets
COPY datasets/ ./datasets

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit properly inside container
CMD ["streamlit", "run", "Model.py", "--server.port=8501", "--server.address=0.0.0.0"]
