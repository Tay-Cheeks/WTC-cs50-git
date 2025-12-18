# RoomTone

#### Video Demo: `<INSERT_YOUR_VIDEO_URL_HERE>`

#### Description:

RoomTone is a Python-based command-line tool designed to help people living in shared homes check in on their moods and track the overall emotional vibe of their household. It allows multiple users to submit their daily mood, leave anonymous notes, and receive gentle suggestions based on the aggregated home mood. The project demonstrates concepts in Python including object-oriented programming, file I/O, exception handling, and unit testing with `pytest`.

---

## Features

* **Home Management:** Create or join a home and manage multiple users (up to six per home).
* **Mood Tracking:** Each user can submit a daily mood (`Good`, `Neutral`, or `Low`) along with optional anonymous notes.
* **Home Vibe Summary:** Aggregates all user moods to display the overall “vibe” of the home.
* **Suggestions:** Provides thoughtful suggestions for the home or individual users based on moods.
* **Persistent Storage:** All home data, users, and mood entries are saved locally in JSON format to maintain continuity across sessions.
* **Edge Case Handling:** Prevents duplicate users in a home and limits the number of users per home.
* **Test Coverage:** Core functions are tested using `pytest` for reliability and correctness.

---

## File Structure

```
roomtone/
│
├── project.py               # Main program entry point (contains main function and CLI flows)
├── models.py                # Defines Home, User, MoodEntry classes
├── engine.py                # SuggestionEngine class for mood-based suggestions
├── storage.py               # Persistent storage using JSON
├── test_project.py          # Pytest test suite for main functions and edge cases
├── requirements.txt 
├── tk_ui.py                 # Python dependencies (standard library only)
└── README.md                # Project documentation
```

---

## How It Works

1. **Start the Program:** The user launches `project.py`.
2. **Home Flow:** The program lists existing homes. Users can join an existing home or create a new one.
3. **User Login:** Users can log in with a username or create a new user in the home.
4. **Submit Mood:** Users submit their daily mood and optional anonymous notes.
5. **View Home Vibe:** Users can view a summary of the home’s overall vibe along with any suggestions and notes.
6. **Switch Users:** Multiple users can check in sequentially.
7. **Exit:** All data is saved automatically to `roomtone_data.json`.

---

## Testing

RoomTone includes unit tests using `pytest` to ensure correctness and edge case handling. Examples include:

* `test_view_home_vibe()` – verifies mood aggregation and suggestions.
* `test_home_full()` – ensures no more than six users can be added to a home.
* `test_duplicate_user()` – prevents adding the same username twice.

To run tests:

```bash
pytest test_project.py
```

---

## Design Decisions

* **CLI Interface:** Chosen for simplicity and to meet project requirements.
* **JSON Storage:** Ensures data persistence without external databases.
* **Suggestion Engine:** Currently rule-based; can be extended with ML models in future iterations.
* **Edge Case Handling:** Designed to prevent user duplication and handle empty mood submissions gracefully.

---

#### Author

* **Name:** `Thando Majola`
* **GitHub Username:** `https://gitlab.com/Tay-Cheeks/cs50-roomtone`
* **edX Username:** `Thando971012`
* **City/Country:** `Johannesburg, South Africa`
* **Date:** `15 December 2025`


