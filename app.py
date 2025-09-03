

import pandas as pd
import numpy as np
import sqlparse
import spacy
import re
from dateutil.parser import parse
from datetime import datetime, timedelta
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': '20.205.160.191',
    'user': 'oneapp_usr',
    'password': '79dtefxvLhJM13H5zYI1',
    'database': 'only_app'
}

#Load dataset from CSV file
dataset_df = pd.read_csv(r"C:\Users\anish\python_prg\labeldataset_1.csv")

# Load spaCy model for named entity recognition
nlp = spacy.load("en_core_web_sm")

# Function to extract names from user input using spaCy and filter out custom names present in the input
def extract_names(text, custom_names=[]):
    doc = nlp(text)
    custom_names_present = [name for name in custom_names if name.lower() in text.lower()]
    spaCy_names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    return list(set(custom_names_present + spaCy_names))

# Function to extract user ID from user input
def extract_user_id(text):
    user_id_match = re.search(r'\b\d{8}\b', text)
    if user_id_match:
        return user_id_match.group()
    else:
        return None

# Function to extract date from user input using dateutil
def extract_date(text):
    try:
        parsed_date = parse(text, fuzzy=True)
        return parsed_date.strftime('%Y-%m-%d')
    except ValueError:
        return None

# Function to predict keyword based on input sentence
def predict_keyword(sentence, custom_names=[]):
    names = extract_names(sentence, custom_names)
    user_id = extract_user_id(sentence)
    date = extract_date(sentence)
    return user_id, names, date

# Connect to MySQL database and execute SQL query
def execute_mysql_query(sql_query):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql_query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except Exception as e:
        return f"Error executing MySQL query: {e}"

# Route to handle GET and POST requests
@app.route('/get_input', methods=['GET', 'POST'])
def get_input():
    # Get user input from the JSON data sent in the POST request
    json_data = request.get_json()
    user_input = json_data.get('input')

    if user_input is None:
        return "Error: No input provided", 400

    # Example of custom names (replace with your own list)
    custom_names = ["yogesh", "naren", "dhamotharan", "prasad","pragathi","haritha","akshaya","aathif shah","selva kumar", "Sam", "Subash", "Karthikeyan", "hariskumar", "Muthu", "jenin", "Narayanan",
      "Vignesh S", "Sabari", "Vignesh", "Karthick Raj", "Ahamed Nasith", "Mohan A",
      "Syed", "Jeevanand", "Ebinesar", "Fathima M K", "Dineshkumar", "Chinthamani K",
      "Gandhi", "Karthivashan", "Arul", "Phil", "Suresh", "mani", "Vignesh S"]

    user_id, names, date = predict_keyword(user_input, custom_names)

    if names:
        # Fetch additional details from MySQL based on extracted information
        sql_query = f"SELECT * FROM your_table WHERE user_id = '{user_id}' AND user_name IN {tuple(names)} AND due_date = '{date}'"
        result = execute_mysql_query(sql_query)

        return jsonify({'user_id': user_id, 'names': names, 'date': date, 'data_from_mysql': result}), 200
    else:
        return "No names extracted", 200

if __name__ == '__main__':
    app.run(debug=True)
