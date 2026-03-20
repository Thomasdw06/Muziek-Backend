from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/generate-music", methods=["POST"])
def generate_music():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "error": "No JSON body received"
        }), 400

    required_fields = ["goal", "mood", "genre", "bpm", "duration_seconds"]
    missing = [field for field in required_fields if field not in data]

    if missing:
        return jsonify({
            "success": False,
            "error": f"Missing fields: {', '.join(missing)}"
        }), 400

    goal = data["goal"]
    mood = data["mood"]
    genre = data["genre"]
    bpm = data["bpm"]
    duration_seconds = data["duration_seconds"]

    return jsonify({
        "success": True,
        "provider": "mubert",
        "title": f"{mood.title()} {goal.title()} Track",
        "audio_url": "https://example.com/test-track.mp3",
        "description": f"A {genre} track at {bpm} BPM for {goal}.",
        "listening_instructions": f"Listen for about {duration_seconds} seconds with headphones and focus on the rhythm."
    })
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
