from datetime import date

"""
models.py

Core object-oriented structure for the RoomTone simulation.

Classes:
- User: represents a person in a home (username only)
- MoodEntry: a daily mood check-in (Good/Neutral/Low + optional note)
- Home: container for up to 6 users, mood entries, and anonymous notes

This layer contains NO user interface and NO emotional language.
Pure logic only.
"""

class User:
    def __init__(self, username):
        self.username = username


class MoodEntry:
    def __init__(self, user, mood: str, note: str = None):
        self.user = user
        self.mood = mood
        self.note = note
        self.date = date.today()


class Home:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.mood_entries = []

    
    def add_user(self, user):
        if len(self.users) >= 6:
            raise ValueError("This home is already full.")
        if any(existing_user.username == user.username for existing_user in self.users):
            raise ValueError("User is already in the home.")
        self.users.append(user)
   

    def submit_mood(self, user: User, mood: str, note: str = None):
        today = date.today()

        for entry in self.mood_entries:
            if entry.user.username == user.username and entry.date == today:
                raise ValueError("Mood already submitted today.")

        self.mood_entries.append(MoodEntry(user, mood, note))

    def get_aggregated_mood(self):
        today = date.today()
        todays_entries = [entry for entry in self.mood_entries if entry.date == today]

        if not todays_entries:
            return "No Data"

        goods = sum(1 for entry in todays_entries if entry.mood.lower() == "good")
        neutrals = sum(1 for entry in todays_entries if entry.mood.lower() == "neutral")
        lows = sum(1 for entry in todays_entries if entry.mood.lower() == "low")

        if lows >= 2:
            return "Tense"
        if goods >= len(todays_entries) - 1:
            return "All Good"
        if neutrals >= 3:
            return "Mixed"

        return "Mixed"  # safe fallback

    def get_anonymous_notes(self):
        today = date.today()
        return [
            entry.note
            for entry in self.mood_entries
            if entry.date == today and entry.note
        ]

    def get_vibe_summary(self):
        """
        Returns raw, neutral data.
        No wording, no suggestions.
        """
        return {
            "vibe": self.get_aggregated_mood(),
            "anonymous_notes": self.get_anonymous_notes()
        }
