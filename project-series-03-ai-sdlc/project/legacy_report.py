"""legacy_report.py — the BEFORE state for Ep 5's refactor episode.

This module is deliberately written the way old code really looks: one long
function, magic values, no validation, a bare except. In Ep 5 the agent
refactors it under a security + behavior review while the tests in
../ep05-advanced-big-codebase/ keep it honest. Do not 'fix' it early —
the mess is the teaching material.
"""
import json


def report(path):
    try:
        d = json.load(open(path))
    except:
        return "no data"
    t = 0
    s = ""
    for x in d["deals"]:
        if x["stage"] == "won":
            t = t + x["value"]
    s = s + "WON TOTAL: " + str(t) + "\n"
    for x in d["contacts"]:
        s = s + x["name"] + " <" + x["email"] + ">\n"
    return s
