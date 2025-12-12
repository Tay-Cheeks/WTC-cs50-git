from datetime import date

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
        #we only need username for this object to be created
        self.username = username



class MoodEntry:
    def __init__(self, user, mood: str, note: str = None):
        # TODO: store one check-in form, one user on one day
        self.user = user
        self.mood = mood
        self.note = note
        self.date = date.today()


class Home:
    def __init__(self, name): 
        # TODO: structure to hold users, mood entries, notes
        self.name = name #name of home
        self.users = [] #users will add
        self.mood_entries = [] #users will also add to this list
        self.anonymous_notes = []

    def add_user(self, user):
        if len(self.users) == 6:
            return f"This home is already full!"

        if any(existing_user.username == user.username for existing_user in self.users):
        #if the existing user is the same as the one being added
            return "User is already in the home!"

        #otherwise:
        self.users.append(user)
        return f"User successfully added!"

    def submit_mood(self, user:User, mood, note=None):
        today = date.today()

        #check if mood is already submitted today
        for entry in self.mood_entries:
            if entry.user.username == user.username and entry.date == today:
                raise ValueError("This user has already submitted their mood for the day!")
        
        #otherwise create and store user mood entry:
        new_entry = MoodEntry(user, mood, note)

        #append the entry
        self.mood_entries.append(new_entry)

    def get_aggregated_mood(self):
        today = date.today()

        todays_entries = [entry for entry in self.mood_entries if entry.date == today]

        if not todays_entries:
            return f"No mood entries captured today!"

        #count each mood entry
        goods = sum(1 for entry in todays_entries if entry.mood.lower() == "Good")
        neutrals = sum(1 for entry in todays_entries if entry.mood.lower() == "Neutral")
        lows = sum(1 for entry in todays_entries if entry.mood.lower() == "Low")


        if lows >= 2:
            return "Tense"
        if goods >= len(todays_entries) - 1:
            return "All Good"
        return "Mixed"


    
    # - get_vibe_summary()
    # - get_anonymous_notes()
