"""
models.py

Core object-oriented structure for the RoomTone simulation.

Classes:
- User: represents a person in a home (username only)
- MoodEntry: a daily mood check-in (Good/Neutral/Low + optional note)
- Home: container for up to 6 users, mood entries, and anonymous notes

This layer contains NO user interface — pure logic.
"""

class User:
    def __init__(self, username):
        # TODO: store basic user info
        pass


class MoodEntry:
    def __init__(self, username, mood, note=None):
        # TODO: store one day's mood check-in + optional note
        pass


class Home:
    def __init__(self, name):
        # TODO: structure to hold users, mood entries, notes
        pass

    # TODO: add methods:
    # - add_user()
    # - submit_mood()
    # - get_aggregated_mood()
    # - get_vibe_summary()
    # - get_anonymous_notes()
