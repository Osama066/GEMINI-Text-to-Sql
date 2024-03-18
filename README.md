# GEMINI-Text-to-Sql
# Text to SQL Converter using Google Gemini

This project is a Streamlit web application that utilizes the Google Gemini API for converting English questions into SQL queries. It allows users to input natural language questions related to a specific SQL database schema and retrieve the corresponding SQL queries.

## Features

- Convert English questions to SQL queries.
- Execute SQL queries on an SQLite database.
- Display the results of SQL queries in the Streamlit interface.

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.6+
- pip (Python package manager)
- SQLite database with the necessary schema (refer to `schema.sql` for the example schema)



1. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Set up your Google API key by creating a `.env` file in the root directory of the project and adding your key:

    ```
    GOOGLE_API_KEY=your_google_api_key_here
    ```

2. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

3. Access the application in your web browser at `http://localhost:8501`.

4. Input an English question related to the provided prompt and click "Ask the question" to retrieve the corresponding SQL query and execute it on the SQLite database.


- Thanks to the Streamlit community for the wonderful framework.
- Thanks to Google for providing the Generative AI API.

![image](https://github.com/Osama066/GEMINI-Text-to-Sql/assets/109853647/6b358996-c776-4a16-aafd-499bc57b3958)


