FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . /app

# Expose the port the app runs on (5002 in this case)
EXPOSE 5002

# Run the Flask app with gunicorn, binding to 0.0.0.0:5002
CMD ["gunicorn", "run:app", "-b", "0.0.0.0:5002"]
