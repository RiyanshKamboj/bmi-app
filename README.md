# VCC_Project_Group_9
VCC_Project_Group_9

Setup Instructions
Clone the Repository

git clone https://github.com/RiyanshKamboj/VCC_Project_Group_9.git
cd VCC_Project_Group_9

2. Install Dependencies
Set up a virtual environment and install the required packages:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Build and Run Docker Container Locally
Build the Docker image and run it locally:
docker build -t home-price-prediction .
docker run -p 8080:8080 home-price-prediction

Code Documentation
Please find below the documentation of the code
Prerequisites:
A requirements.txt file listing the Python dependencies.
The application code, including the Flask app (usually in a file like app.py), should be in the same directory as the Dockerfile.
File Name: app.py
This code defines a small Flask web application that serves two purposes:
It provides a REST API to calculate a person's BMI (Body Mass Index).
It serves an HTML webpage where users can input their height and weight.
1. Flask Imports and App Initialization

from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

Imports:
Flask: The main class from the Flask framework used to create the web application.
render_template: Function used to render HTML templates (e.g., index.html).
request: Used to access data sent in the HTTP request (in this case, JSON data in POST requests).
jsonify: Used to return JSON responses to the client.
App Initialization:
app = Flask(__name__): This line initializes the Flask web application instance.
2. REST API for BMI Calculation


# REST API for BMI Calculation
@app.route('/api/calculate_bmi', methods=['POST'])
def calculate_bmi():
    try:
        data = request.json # Parse JSON from the incoming request
        height = float(data.get('height', 0)) # Extract height, default to 0 if missing
        weight = float(data.get('weight', 0))  # Extract weight, default to 0 if missing


        # Check if height and weight are positive
        if height <= 0 or weight <= 0:
            return jsonify({"error": "Height and weight must be positive numbers."}), 400


        # Calculate BMI
        bmi = weight / ((height / 100) ** 2)  # Convert height from cm to meters and calculate BMI
        category = categorize_bmi(bmi)  # Classify the BMI into a category
       
        # Return the result as a JSON response
        return jsonify({"bmi": round(bmi, 2), "category": category})
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Please enter valid numbers for height and weight."}), 400


def categorize_bmi(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obesity'


# Webpage for BMI Calculation
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)







    
    REST API endpoint for calculating Body Mass Index (BMI).
    
    The API expects a POST request with JSON data containing `height` (in cm) and `weight` (in kg).
    It calculates the BMI using the formula:
    
        BMI = weight / (height / 100)^2
    
    Returns:
        JSON response containing:
            - "bmi": Calculated BMI value rounded to 2 decimal places.
            - "category": Category of the BMI (e.g., "Underweight", "Normal weight").
            - In case of an error, returns a JSON error message and an HTTP 400 status code.
    
    Example Input:
    {
        "height": 170,
        "weight": 65
    }
    
    Example Response:
    {
        "bmi": 22.49,
        "category": "Normal weight"
    }
    
    Error Handling:
        - If height or weight is not a valid positive number, an error message is returned.
        - If non-numeric values are provided, it returns an error message.
    
 
File Name: Dockerfile
Description:
This Dockerfile is used to containerize a Python-based web application, particularly a Flask application, and run it using Gunicorn as the WSGI HTTP server. The Dockerfile creates a lightweight, production-ready container that listens on port 8000.
Instructions:
The Dockerfile uses Python 3.10 and installs dependencies from the requirements.txt file. It also exposes port 8000 for HTTP traffic and starts the Flask application using Gunicorn with 3 worker processes.

Key Sections of the Dockerfile:
1. Base Image



FROM python:3.10-slim




Purpose:
This line specifies that the Docker container will be based on the python:3.10-slim image, which is a smaller, lightweight version of Python 3.10.
The slim variant is used to keep the container size minimal by including only essential components.

2. Working Directory




WORKDIR /app




Purpose:
This command sets /app as the working directory inside the container. All subsequent instructions will be executed relative to this directory.

3. Copy requirements.txt



COPY requirements.txt .




Purpose:
This command copies the requirements.txt file from the host machine (your development environment) to the /app directory in the Docker container.
This file contains the list of Python dependencies required by the Flask application.

4. Install Dependencies




RUN pip install --no-cache-dir -r requirements.txt



Purpose:
This command installs the Python packages listed in the requirements.txt file using pip.
The --no-cache-dir flag is used to prevent pip from caching package installations, helping reduce the image size.

5. Copy the Application Code




COPY . .




Purpose:
This command copies the entire content of the current directory (which contains your application code) into the /app directory of the Docker container.

6. Expose Port



EXPOSE 8000




Purpose:
This tells Docker to expose port 8000 on the container so that it can be accessed externally. This port is where the Flask application will be served using Gunicorn.

7. Command to Run the Application



CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:8000", "app:app"]




Purpose:
This sets the default command to run when the container starts.
Gunicorn is used as the WSGI HTTP server to serve the Flask application (app:app), where:
-w 3: Specifies that 3 worker processes will handle requests.
-b 0.0.0.0:8000: Binds the server to 0.0.0.0 on port 8000, making it accessible from outside the container.


GCP Configuration settings:

VM Instances:
Lists and manages your virtual machine instances.


Instance Template:
It allows to create templates to streamline the creation of VM instances.


Instance Template configurations:
It shows all the configurations related to the created Instance template.






Instance Groups:
Manage groups of instances for auto-scaling and load balancing.


 
Summary:
This Dockerfile builds a containerized Python Flask web application using a lightweight base image (python:3.10-slim). The container installs the necessary dependencies, copies the application code, exposes port 8000, and serves the application using Gunicorn with 3 worker processes. The resulting container is small, efficient, and suitable for production deployments.
Please find below the screenshots of the web application.




