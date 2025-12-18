# test_project.py
import pytest
from models import Home, User, MoodEntry
from project import user_login, submit_mood_flow, view_home_vibe
from engine import SuggestionEngine

# Test that user_login adds a new user
def test_user_login_add_new_user(monkeypatch):
    home = Home("TestHome")
    monkeypatch.setattr('builtins.input', lambda _: "Thando")
    user = user_login(home)
    assert user.username == "Thando"
    assert len(home.users) == 1
    assert home.users[0].username == "Thando"

#Test that user_login returns existing user
def test_user_login_existing_user(monkeypatch):
    home = Home("TestHome")
    existing_user = User("Bob")
    home.add_user(existing_user)
    monkeypatch.setattr('builtins.input', lambda _: "Bob")
    user = user_login(home)
    assert user.username == "Bob"
    assert len(home.users) == 1  #still only 1 user

#Test that submit_mood_flow adds a MoodEntry
def test_submit_mood_flow(monkeypatch):
    home = Home("TestHome")
    user = User("Charlie")
    home.add_user(user)
    inputs = iter(["Good", "Feeling great"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    submit_mood_flow(home, user)
    assert len(home.mood_entries) == 1
    entry = home.mood_entries[0]
    assert entry.user.username == "Charlie"
    assert entry.mood == "Good"
    assert entry.note == "Feeling great"

# 4. Test view_home_vibe prints correct output
def test_view_home_vibe(monkeypatch, capsys):
    home = Home("TestHome")
    user = User("Zola")
    home.add_user(user)
    home.submit_mood(user, "Good", "All good here!")

    # Monkeypatch SuggestionEngine.suggest_for_home
    monkeypatch.setattr(SuggestionEngine, "suggest_for_home", lambda self, vibe: "Test suggestion")

    view_home_vibe(home)
    captured = capsys.readouterr()
    assert "Today's vibe" in captured.out
    assert "Test suggestion" in captured.out
    assert "Anonymous notes today" in captured.out
    assert "- All good here!" in captured.out

def test_empty_home_vibe(capsys):
    home = Home("EmptyHome")
    view_home_vibe(home)
    captured = capsys.readouterr()
    assert "No check-ins yet today" in captured.out or "Today's vibe" in captured.out

def test_home_full():
    home = Home("FullHome")
    for i in range(6):
        home.add_user(User(f"user{i}"))
    # Expect a ValueError when adding the 7th user
    with pytest.raises(ValueError) as exceptioninfo:
        home.add_user(User("user6"))
    assert "already full" in str(exceptioninfo.value)

def test_duplicate_user():
    home = Home("DupHome")
    user = User("Alice")
    home.add_user(user)
    # Expect a ValueError when adding a duplicate user
    with pytest.raises(ValueError) as exceptioninfo:
        home.add_user(User("Alice"))
    assert "already in the home" in str(exceptioninfo.value)

def test_submit_mood_twice():
    home = Home("MoodHome")
    user = User("Bob")
    home.add_user(user)
    home.submit_mood(user, "Good")
    with pytest.raises(ValueError):
        home.submit_mood(user, "Neutral")

def test_mood_without_note():
    home = Home("NoNoteHome")
    user = User("Carol")
    home.add_user(user)
    home.submit_mood(user, "Good")
    notes = home.get_anonymous_notes()
    assert notes == []

def test_mixed_low_moods():
    home = Home("MixedHome")
    users = [User(f"user{i}") for i in range(4)]
    for existing_u in users:
        home.add_user(existing_u)
    home.submit_mood(users[0], "Low")
    home.submit_mood(users[1], "Low")
    home.submit_mood(users[2], "Neutral")
    home.submit_mood(users[3], "Good")
    assert home.get_aggregated_mood() == "Tense"

def test_suggestion_engine_unknown_vibe():
    engine = SuggestionEngine()
    assert engine.suggest_for_home("UnknownVibe") == ""
    assert engine.suggest_for_user("UnknownMood") == ""