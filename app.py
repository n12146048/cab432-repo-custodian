from flask import Flask, jsonify, request

app = Flask(__name__)

notes = [
    {"id": 1, "title": "Welcome", "body": "This is the first note."},
    {"id": 2, "title": "Demo", "body": "This API is intentionally small."},
]


@app.get("/notes")
def list_notes():
    return jsonify(notes)


@app.get("/notes/<int:note_id>")
def get_note(note_id):
    note = next((n for n in notes if n["id"] == note_id), None)

    if note is None:
        return jsonify({"error": "Note not found"}), 404

    return jsonify(note)


@app.post("/notes")
def create_note():
    data = request.get_json()

    if not data or "title" not in data or "body" not in data:
        return jsonify({"error": "title and body are required"}), 400

    note = {
        "id": max(n["id"] for n in notes) + 1,
        "title": data["title"],
        "body": data["body"],
    }

    notes.append(note)
    return jsonify(note), 201


@app.delete("/notes/<int:note_id>")
def delete_note(note_id):
    note = next((n for n in notes if n["id"] == note_id), None)

    if note is None:
        return jsonify({"error": "Note not found"}), 404

    notes.remove(note)
    return jsonify({"message": "Note deleted"})


# Deliberately undocumented endpoint for the demo.
@app.get("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
