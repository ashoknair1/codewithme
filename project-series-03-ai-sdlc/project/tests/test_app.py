"""Tests for MiniCRM (Series 03) — the harness the agent must keep green."""
import importlib
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setenv("MINICRM_DATA", str(tmp_path / "data.json"))
    import app as app_module

    importlib.reload(app_module)
    app_module.app.config.update(TESTING=True)
    return app_module.app.test_client()


def test_add_contact_requires_name(client):
    r = client.post("/contacts", json={"name": "  "})
    assert r.status_code == 400


def test_contact_then_deal_flow(client):
    r = client.post("/contacts", json={"name": "Ana", "email": "ana@example.com"})
    assert r.status_code == 201
    contact_id = r.get_json()["id"]

    r = client.post("/deals", json={"title": "Website rebuild", "value": 2500,
                                    "contact_id": contact_id})
    assert r.status_code == 201
    deal = r.get_json()
    assert deal["stage"] == "lead"

    r = client.post(f"/deals/{deal['id']}/stage", json={"stage": "won"})
    assert r.status_code == 200

    r = client.get("/")
    body = r.get_json()
    assert body["contacts"] == 1 and body["deals"] == 1
    assert body["pipeline_totals"]["won"] == 2500


def test_bad_stage_and_missing_deal(client):
    r = client.post("/deals/nope/stage", json={"stage": "won"})
    assert r.status_code == 404
    r = client.post("/deals", json={"title": "X", "value": -5})
    assert r.status_code == 400
