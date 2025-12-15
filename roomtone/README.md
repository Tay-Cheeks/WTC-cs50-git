Here’s a clean, professional README for your RoomTone project:

---

# RoomTone

RoomTone is a command-line interface (CLI) tool for emotional check-ins in shared homes. It allows users to submit daily moods, view aggregated home vibes, and receive gentle suggestions to support overall emotional well-being.

## Features

* Create or join a home with multiple users (up to 6 per home)
* Submit daily mood check-ins (`Good`, `Neutral`, or `Low`)
* Leave optional anonymous notes
* View home-level aggregated mood and suggestions
* View individual user mood suggestions
* Persistent local storage of homes, users, and mood entries

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd roomtone
```

3. Ensure Python 3.9+ is installed. No external packages are required.

## Usage

Run the CLI tool:

```bash
python project.py
```

### Main Flow

1. **Home Management**

   * Create a new home or join an existing home.
2. **User Login**

   * Enter a username to log in or create a new user.
3. **Main Menu**

   * Submit Mood: Enter your mood for the day and optionally leave a note.
   * View Home Vibe Summary: See the aggregated home mood, home-level suggestion, individual suggestions, and anonymous notes.
   * Switch/Add User: Log in as a different user or add a new user.
   * Exit: Save all data and exit the application.

### Mood Options

* Good
* Neutral
* Low

## Data Storage

RoomTone stores all data in a local JSON file (`roomtone_data.json`).
This includes homes, users, daily moods, and anonymous notes.

## File Structure

* `project.py`: CLI entry point, handles menus and user interactions.
* `models.py`: Core object-oriented structure for `Home`, `User`, and `MoodEntry`.
* `storage.py`: Handles saving and loading data to/from JSON.
* `engine.py`: Provides gentle suggestions for home and individual moods.

## Contributing

Contributions are welcome. Suggestions include:

* Adding persistent user authentication
* Enhancing mood suggestions with AI/ML
* Adding reports or mood history visualization

## License

This project is open source and available under the MIT License.

---
