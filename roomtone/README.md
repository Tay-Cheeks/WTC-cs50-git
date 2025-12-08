# 🌿 RoomTone (CS50 Python Project)

RoomTone is a command-line application that allows people living together
(roommates, partners, family) to quietly check in on the emotional mood
of their home — without confrontation.

This is a **Python + OOP CLI simulation** of the future full app.

---

## Features

- Create or join a home (max 6 users)
- Daily mood check-ins: Good, Neutral, Low
- Optional anonymous “soft note”
- Home vibe aggregation (All Good / Mixed / Tense)
- Gentle suggestions based on mood
- JSON-based local data storage

---

## File Structure

roomtone/
│── main.py # CLI controller
│── models.py # OOP classes
│── engine.py # suggestion logic
│── storage.py # JSON persistence
│── README.md

## How to Run

```bash
python main.py
```
