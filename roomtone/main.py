"""
main.py

Entry point for RoomTone — a CLI-based emotional check-in tool
for shared homes.

Handles:
- Startup menu
- Home creation/join flow
- User mood check-ins
- Viewing the home vibe dashboard
- Saving/loading data

This file orchestrates interactions between:
- models.py (Home, User, MoodEntry)
- engine.py (SuggestionEngine)
- storage.py (local JSON persistence)
"""

from models import Home, User, MoodEntry
from engine import SuggestionEngine
from storage import Storage

def main():
    # TODO: implement CLI menus, home selection,
    # user interactions, mood submissions, viewing dashboard, saving data.
    pass


if __name__ == "__main__":
    main()
