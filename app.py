from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# REST API for BMI Calculation
@app.route('/api/calculate_bmi', methods=['POST'])
def calculate_bmi():
    try:
        data = request.json
        height = float(data.get('height', 0))
        weight = float(data.get('weight', 0))
        
        if height <= 0 or weight <= 0:
            return jsonify({"error": "Height and weight must be positive numbers."}), 400

        # Calculate BMI
        bmi = weight / ((height / 100) ** 2)
        category = categorize_bmi(bmi)
        
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
