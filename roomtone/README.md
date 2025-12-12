# Roomtone — CS50 Python Project (Planning Phase)

Roomtone is a command-line based prototype for a future mental-wellbeing application designed for student residences, small homes, and support groups. This phase focuses entirely on Python, object-oriented programming, and clean architecture. The goal is to build a fully functional CLI prototype that can later evolve into a real application.

---

## Project Purpose

* Provide a simple mental-health daily check-in system.
* Allow up to 6 users per "Home" to log moods, write notes, and track patterns.
* Generate suggestions based on mood and note content.
* Establish a foundation for future machine learning features.

---

## Core Architecture

This is a pure Python application. All logic is implemented through clear OOP design.

Directory layout:

```
roomtone/
│── main.py              # Entry point for the command-line interface
│── models.py            # User, Home, Note, MoodEntry classes
│── engine.py            # Core logic for check-in flow and interactions
│── storage.py           # JSON-based save/load functionality
│── util_text.py         # Text processing helpers
│── util_stats.py        # Mood statistics and trend helpers
│── suggestion_engine.py # Rule-based suggestion system
│── README.md
```

---

## File and Module Overview

### main.py

* Command-line interface
* Menus, prompts, and navigation
* User selects a home, logs in, records mood, and views summaries

### models.py

* `User`: name, mood history, notes
* `Home`: container for up to 6 users and shared data
* `MoodEntry`: mood rating, tags, timestamp
* `Note`: reflective text entry

### engine.py

* Houses the application flow and interactions
* Creates homes and registers users
* Guides the daily flow: log mood → write note → view suggestion

### storage.py

* Handles persistent storage using JSON
* Can be replaced with a database later

### util_text.py

* Text cleaning
* Keyword extraction
* Basic sentiment scoring (non-ML)

### util_stats.py

* Weekly averages
* Trend detection
* Tracking streaks and improvement metrics

### suggestion_engine.py

* Generates suggestions based on mood and text signals
* Rule-based for now but structured for future ML integration

---

## Future ML Integration (Not Part of CS50 Phase)

The system is designed so that machine learning can later be added for:

* Better suggestions
* Semantic similarity searches
* Pattern detection across notes

The CS50 version, however, contains no ML.

---

## How to Run

```
python3 main.py
```

The CLI guides you through creating a home, adding users, logging moods, writing notes, and viewing summaries.

---

## Project Status

Phase 1 (CS50 Python CLI): In progress

Next steps:

1. Generate basic scaffolding files
2. Write class definitions
3. Build CLI workflows
4. Test with sample data
