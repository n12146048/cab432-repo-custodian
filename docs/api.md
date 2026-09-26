```markdown
# Notes API Reference

## GET /notes

Returns all notes.

### Response

```json
[
  {
    "id": 1,
    "title": "Welcome",
    "body": "This is the first note."
  }
]

GET /notes/<id>
Returns a single note.

Example
curl http://localhost:5000/notes/1

Success response
{
  "id": 1,
  "title": "Welcome",
  "body": "This is the first note."
}

Not found
Returns HTTP 404 when the note doesn't exist.

POST /notes
Creates a new note.

Request
{
  "title": "My note",
  "body": "Some text"
}

Success
Returns HTTP 201 with the newly created note.

DELETE /notes/<id>
Deletes a note.

Success
Returns HTTP 200.

Not found
Returns HTTP 404.

