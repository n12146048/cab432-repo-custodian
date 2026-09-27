# Notes API

A small Flask API for creating, reading, and deleting notes.

## Requirements

- Python 3.10+
- Flask

## Running locally

Install Flask:

```bash
pip install flask

Start the application:

python app.py

The API will be available at:

http://localhost:8080

Endpoints
List notes
GET /notes

Get a note
GET /notes/<id>

Create a note
POST /notes
Content-Type: application/json

Example:

{
  "title": "Shopping",
  "body": "Buy milk"
}

Delete a note
DELETE /notes/<id>

Example
curl http://localhost:8080/notes

Health Check
GET /health
