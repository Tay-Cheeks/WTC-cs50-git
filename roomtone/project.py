"""
Entry point for RoomTone - a CLI-based emotional check-in tool
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

from models import Home, User
from storage import Storage
from engine import SuggestionEngine
from datetime import date
from tk_ui import launch_app #tkinter


def user_login(home):
    """Handle user login or creation."""
    while True:
        username = input("Enter your username: ").strip()
        user = next((existing_u for existing_u in home.users if existing_u.username == username), None)
        if user:
            print(f"Welcome back, {username}!")
            return user
        else:
            if len(home.users) >= 6:
                print("Home is full! Cannot add new user.")
            else:
                user = User(username)
                home.add_user(user)
                Storage.save_home(home)
                print(f"User '{username}' added to home '{home.name}'.")
                return user

def submit_mood_flow(home, user):
    """Handle mood submission for a user."""
    print("\n--- Mood Submission ---")
    mood = input("How are you feeling today? (Good/Neutral/Low) ").strip().capitalize()
    note = input("Optional: leave an anonymous note (or leave blank): ").strip() or None
    try:
        home.submit_mood(user, mood, note)
        Storage.save_home(home)
        print("Mood submitted successfully!")
    except ValueError as e:
        print(e)

def view_home_vibe(home):
    """Display home vibe summary with suggestion and anonymous notes."""
    summary = home.get_vibe_summary()
    vibe = summary['vibe']
    engine = SuggestionEngine()

    # Home-level suggestion
    home_suggestion = engine.suggest_for_home(vibe)

    print("\n--- Home Vibe Summary ---")
    print(f"Today's vibe: {vibe}")
    print(f"Suggestion: {home_suggestion}\n")

    # Per-user suggestions
    print("--- Individual Suggestions ---")
    for user in home.users:
        # get today's mood entry for the user
        today_entry = next((entry for entry in home.mood_entries
                            if entry.user.username == user.username and entry.date == date.today()), None)
        if today_entry:
            user_suggestion = engine.suggest_for_user(today_entry.mood)
            print(f"{user.username}'s mood: {today_entry.mood} -> Suggestion: {user_suggestion}")
        else:
            print(f"{user.username} has not submitted a mood today.")

    # Anonymous notes
    notes = summary["anonymous_notes"]
    if notes:
        print("\nAnonymous notes today:")
        for note in notes:
            print(f"- {note}")
    else:
        print("\nNo notes submitted today.")

def main():
    launch_app()

    print("🌿 Welcome to RoomTone!")

    # Step 1: List homes
    homes = Storage.list_homes()
    if homes:
        print("\nExisting homes:")
        for home in homes:
            print(f"- {home}")
    else:
        print("\nNo homes yet.")

    # Step 2: Join or create
    while True:
        choice = input("\nDo you want to [J]oin or [C]reate a home? ").strip().upper()
        if choice == "J":
            if not homes:
                print("No homes exist yet. You will need to create one.")
                choice = "C"
                continue
            home_name = input("Enter the name of the home you want to join: ").strip()
            try:
                home = Storage.load_home(home_name)
            except ValueError:
                print("Home not found. Creating a new one instead.")
                home = Home(home_name)
                Storage.save_home(home)
            break
        elif choice == "C":
            home_name = input("Enter new home name: ").strip()
            home = Home(home_name)
            Storage.save_home(home)
            break
        else:
            print("Invalid choice. Please type 'J' to join or 'C' to create a home.")


    # Step 3: User login
    user = user_login(home)

    # Step 4: Main CLI loop
    while True:
        print("\n--- RoomTone Menu ---")
        print("1. Submit Mood")
        print("2. View Home Vibe Summary")
        print("3. Switch/Add User")
        print("4. Exit")
        menu_choice = input("Enter your choice (1-4): ").strip()

        if menu_choice == "1":
            submit_mood_flow(home, user)
        elif menu_choice == "2":
            view_home_vibe(home)
        elif menu_choice == "3":
            user = user_login(home)
        elif menu_choice == "4":
            Storage.save_home(home)
            print("Exiting RoomTone. Have a calm day!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()




# def main():
#     print("🌿Welcome to RoomTone!")

#     # Step 1: List homes
#     homes = Storage.list_homes()
#     if homes:
#         print("Existing homes:")
#         for home in homes:
#             print(f"- {home}")
#     else:
#         print("No homes yet.")

#     choice = input("Do you want to [J]oin or [C]reate a home? ").strip().upper()
#     if choice == "J":
#         home_name = input("Enter home name to join: ").strip()

#         try:
#             home = Storage.load_home(home_name)
#         except ValueError:
#             print("Home not found. Creating a new one instead.")
#             home = Home(home_name)
#             Storage.save_home(home)
#     else:
#         home_name = input("Enter new home name: ").strip()
#         home = Home(home_name)
#         Storage.save_home(home)

#     # Loop for multiple user interactions
#     while True:
#         print("\n--- User Login ---")
#         username = input("Enter your username: ").strip()
#         user = next((existing_u for existing_u in home.users if existing_u.username == username), None)

#         if not user:
#             if len(home.users) >= 6:
#                 print("Home is full! Cannot add new user.")
#                 continue #reloop
#             user = User(username)
#             home.add_user(user)
#             Storage.save_home(home)
#             print(f"User '{username}' added to home '{home.name}'.")

#         # Mood submission
#         print("\n--- Mood Submission ---")
#         mood = input("How are you feeling today? (Good/Neutral/Low) ").strip().capitalize()
#         note = input("Optional: leave a soft note (or leave blank): ").strip() or None

#         try:
#             home.submit_mood(user, mood, note)
#             Storage.save_home(home)
#             print("Mood submitted successfully!")
#         except ValueError as e:
#             print(e)

#         # View home vibe summary
#         summary = home.get_vibe_summary()
#         print("\n--- Home Vibe Summary ---")
#         print(f"Today's vibe: {summary['vibe']}")
#         print(f"Suggestion: {summary['suggestion']}")
#         if summary["anonymous_notes"]:
#             print("Anonymous notes today:")
#             for n in summary["anonymous_notes"]:
#                 print(f"- {n}")
#         else:
#             print("No notes submitted today.")

#         # Continue or exit
#         cont = input("\nDo you want another user to check in? (Y/N) ").strip().upper()
#         if cont != "Y":
#             print("Exiting RoomTone. Have a calm day!")
#             break

# if __name__ == "__main__":
#     main()


