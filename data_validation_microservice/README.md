# Add Data Validation Microservice

This microservice provides an API for validating and storing data using Flask and MySQL.

## Requirements

- Python 3.x
- Flask
- MySQL (Using XAMPP)

## Setup

1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Update the MySQL credentials in `app/config.py`.
4. Run the Flask app:
    ```bash
    python run.py
    ```

## Endpoints

- **POST /add-data**: Validate and add data to the database.
  - Request body: `{"data": "<string>"}`
  - Response: `{"message": "Data added successfully!"}` on success, `{"errors": [...]}` on failure.
