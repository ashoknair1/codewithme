"""MiniCRM — the running project for Project Series 03 (AI SDLC).

A tiny CRM in Python + Flask: contacts and a deals pipeline, stored in a
JSON file on disk. Built stage by stage across the series from the intent,
spec and plan in ../ep01-beginner-intent-spec-plan/.

Run:  pip install -r requirements.txt && python app.py
Test: python -m pytest -q
"""
import json
import os
import uuid

from flask import Flask, jsonify, request

DATA_FILE = os.environ.get("MINICRM_DATA", "minicrm.json")
STAGES = ["lead", "qualified", "proposal", "won", "lost"]

app = Flask(__name__)


def _load() -> dict:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {"contacts": [], "deals": []}


def _save(data: dict) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


@app.get("/")
def home():
    data = _load()
    totals = {s: 0 for s in STAGES}
    for deal in data["deals"]:
        totals[deal["stage"]] += deal["value"]
    return jsonify(
        {"contacts": len(data["contacts"]), "deals": len(data["deals"]),
         "pipeline_totals": totals}
    )


@app.post("/contacts")
def add_contact():
    body = request.get_json(force=True)
    name = (body.get("name") or "").strip()
    if not name:
        return jsonify({"error": "name is required"}), 400
    data = _load()
    contact = {"id": uuid.uuid4().hex[:8], "name": name,
               "email": (body.get("email") or "").strip()}
    data["contacts"].append(contact)
    _save(data)
    return jsonify(contact), 201


@app.post("/deals")
def add_deal():
    body = request.get_json(force=True)
    title = (body.get("title") or "").strip()
    value = body.get("value")
    if not title or not isinstance(value, (int, float)) or value < 0:
        return jsonify({"error": "title and a non-negative value are required"}), 400
    data = _load()
    deal = {"id": uuid.uuid4().hex[:8], "title": title, "value": value,
            "stage": "lead", "contact_id": body.get("contact_id")}
    data["deals"].append(deal)
    _save(data)
    return jsonify(deal), 201


@app.post("/deals/<deal_id>/stage")
def move_deal(deal_id):
    stage = (request.get_json(force=True).get("stage") or "").strip()
    if stage not in STAGES:
        return jsonify({"error": f"stage must be one of {STAGES}"}), 400
    data = _load()
    for deal in data["deals"]:
        if deal["id"] == deal_id:
            deal["stage"] = stage
            _save(data)
            return jsonify(deal)
    return jsonify({"error": "deal not found"}), 404


if __name__ == "__main__":
    app.run(port=5057, debug=False)
