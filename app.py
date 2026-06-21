import json
from pathlib import Path

from flask import Flask, jsonify


app = Flask(__name__)


def load_profile():
    profile_path = Path(__file__).parent / "data" / "profile.json"
    with profile_path.open(encoding="utf-8") as profile_file:
        return json.load(profile_file)


@app.get("/")
def index():
    profile = load_profile()
    return jsonify(
        {
            "message": f"Hello World from {profile['student']}!",
            "course": profile["course"],
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

