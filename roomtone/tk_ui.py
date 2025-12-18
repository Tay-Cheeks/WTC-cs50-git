import tkinter as tk
from tkinter import messagebox
from models import Home, User
from storage import Storage
from engine import SuggestionEngine
from datetime import date

#COLOUR FONTS
BG_COLOR = "#f6f4f8"
CARD_COLOR = "#ffffff"

PURPLE = "#9b8ec1"
PURPLE_DARK = "#7f73a6"

OLIVE = "#a3b18a"
OLIVE_DARK = "#7d8f69"

TEXT_PRIMARY = "#2f2f2f"
TEXT_MUTED = "#6b6b6b"

TITLE_FONT = ("Helvetica", 22, "bold")
SUB_FONT = ("Helvetica", 12)
BODY_FONT = ("Helvetica", 11)
BUTTON_FONT = ("Helvetica", 11, "bold")

#HELPERS
def rounded_frame(parent, bg, padx=20, pady=20):
    frame = tk.Frame(parent, bg=bg)
    frame.pack(padx=padx, pady=pady, fill="x")
    return frame

def styled_button(parent, text, command, bg, hover_bg=None):
    btn = tk.Button(
        parent,
        text=text,
        command=command,
        font=BUTTON_FONT,
        bg=bg,
        fg="white",
        activebackground=bg,
        relief="flat",
        bd=0,
        padx=20,
        pady=10,
        cursor="hand2"
    )
    if hover_bg:
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_bg))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg))
    return btn

def vibe_color(vibe):
    return {
        "All Good": OLIVE_DARK,
        "Mixed": PURPLE_DARK,
        "Tense": "#b56576",
        "No Data": TEXT_MUTED
    }.get(vibe, TEXT_PRIMARY)

#MAIN UI
class RoomToneUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RoomTone")
        self.root.geometry("540x640")
        self.root.configure(bg=BG_COLOR)

        self.home = None
        self.user = None
        self.engine = SuggestionEngine()

        self.home_frame()

    #HOME SELECTION
    def home_frame(self):
        self.clear_root()
        frame = rounded_frame(self.root, BG_COLOR, padx=30, pady=30)

        tk.Label(frame, text="🌿 RoomTone", font=TITLE_FONT, bg=BG_COLOR, fg=PURPLE_DARK).pack(pady=(0,20))
        tk.Label(frame, text="Select existing home:", font=BODY_FONT, bg=BG_COLOR, fg=TEXT_PRIMARY).pack(anchor="w")

        homes = Storage.list_homes()
        self.home_var = tk.StringVar(value=homes[0] if homes else "")
        home_dropdown = tk.OptionMenu(frame, self.home_var, *homes)
        home_dropdown.config(font=BODY_FONT)
        home_dropdown.pack(fill="x", pady=5)

        tk.Label(frame, text="Or create new home:", font=BODY_FONT, bg=BG_COLOR, fg=TEXT_PRIMARY).pack(anchor="w", pady=(10,0))
        self.new_home_entry = tk.Entry(frame, font=BODY_FONT)
        self.new_home_entry.pack(fill="x", pady=5)

        styled_button(frame, "Join / Create Home", self.join_create_home, PURPLE, PURPLE_DARK).pack(fill="x", pady=20)

    def join_create_home(self):
        name = self.new_home_entry.get().strip()
        if name:
            self.home = Home(name)
            Storage.save_home(self.home)
        else:
            if not self.home_var.get():
                messagebox.showerror("Error", "No home selected or entered.")
                return
            try:
                self.home = Storage.load_home(self.home_var.get())
            except ValueError:
                messagebox.showinfo("Info", "Home not found. Creating new one.")
                self.home = Home(self.home_var.get())
                Storage.save_home(self.home)

        self.user_frame()

    #USER LOG IN
    def user_frame(self):
        self.clear_root()
        frame = rounded_frame(self.root, BG_COLOR, padx=30, pady=30)

        tk.Label(frame, text=f"Home: {self.home.name}", font=TITLE_FONT, bg=BG_COLOR, fg=OLIVE_DARK).pack(pady=(0,20))
        tk.Label(frame, text="Enter your username:", font=BODY_FONT, bg=BG_COLOR, fg=TEXT_PRIMARY).pack(anchor="w")
        self.username_entry = tk.Entry(frame, font=BODY_FONT)
        self.username_entry.pack(fill="x", pady=5)

        styled_button(frame, "Login / Add User", self.login_user, PURPLE, PURPLE_DARK).pack(fill="x", pady=20)

    def login_user(self):
        username = self.username_entry.get().strip()
        if not username:
            messagebox.showerror("Error", "Username cannot be empty.")
            return
        user = next((existing_u for  existing_u in self.home.users if existing_u.username == username), None)
        if user:
            self.user = user
        else:
            if len(self.home.users) >= 6:
                messagebox.showerror("Error", "Home is full! Cannot add new user.")
                return
            self.user = User(username)
            self.home.add_user(self.user)
            Storage.save_home(self.home)
        self.main_frame()

    #MAIN MOOD AND VIBE
    def main_frame(self):
        self.clear_root()
        header = tk.Frame(self.root, bg=BG_COLOR)
        header.pack(pady=20)
        tk.Label(header, text="RoomTone", font=TITLE_FONT, bg=BG_COLOR, fg=PURPLE_DARK).pack()
        tk.Label(header, text=f"Home: {self.home.name} • User: {self.user.username}", font=SUB_FONT, bg=BG_COLOR, fg=TEXT_MUTED).pack()

        nav_frame = tk.Frame(self.root, bg=BG_COLOR)
        nav_frame.pack(pady=(0,10), fill="x", padx=20)

        styled_button(nav_frame, "Switch Home", self.home_frame, OLIVE, OLIVE_DARK).pack(side="left", padx=5)
        styled_button(nav_frame, "Switch User", self.user_frame, PURPLE, PURPLE_DARK).pack(side="left", padx=5)


        #Mood Card
        card = rounded_frame(self.root, CARD_COLOR, padx=20, pady=20)
        tk.Label(card, text="How are you feeling today?", font=("Helvetica", 13, "bold"), bg=CARD_COLOR, fg=PURPLE_DARK).pack(anchor="w")

        self.mood_var = tk.StringVar(value="Neutral")
        for mood in ["Good", "Neutral", "Low"]:
            tk.Radiobutton(card, text=mood, variable=self.mood_var, value=mood, bg=CARD_COLOR, font=BODY_FONT).pack(anchor="w")

        self.note_entry = tk.Entry(card, font=BODY_FONT)
        self.note_entry.pack(fill="x", pady=8)
        self.note_entry.insert(0, "Optional anonymous note")

        styled_button(card, "Submit Mood", self.submit_mood, PURPLE, PURPLE_DARK).pack(fill="x", pady=8)
        self.user_suggestion = tk.Label(card, text="", wraplength=440, justify="left", font=BODY_FONT, bg=CARD_COLOR, fg=TEXT_PRIMARY)
        self.user_suggestion.pack(anchor="w", pady=6)

        #Vibe Card
        vibe_card = rounded_frame(self.root, CARD_COLOR, padx=20, pady=20)
        tk.Label(vibe_card, text="Home Vibe", font=("Helvetica", 13, "bold"), bg=CARD_COLOR, fg=OLIVE_DARK).pack(anchor="w")
        self.vibe_value = tk.Label(vibe_card, text="—", font=("Helvetica", 14, "bold"), bg=CARD_COLOR, fg=TEXT_PRIMARY)
        self.vibe_value.pack(anchor="w", pady=4)
        self.home_suggestion = tk.Label(vibe_card, text="", wraplength=440, justify="left", font=BODY_FONT, bg=CARD_COLOR, fg=TEXT_PRIMARY)
        self.home_suggestion.pack(anchor="w", pady=6)

        tk.Label(vibe_card, text="Anonymous Notes", font=("Helvetica", 12, "bold"), bg=CARD_COLOR, fg=TEXT_MUTED).pack(anchor="w", pady=(10,4))
        self.notes_text = tk.Text(vibe_card, height=6, wrap="word", font=BODY_FONT, bg=CARD_COLOR, relief="flat")
        self.notes_text.pack(fill="both", expand=True)
        self.notes_text.config(state="disabled")

        styled_button(vibe_card, "Refresh Home Vibe", self.view_vibe, OLIVE, OLIVE_DARK).pack(fill="x", pady=8)
        self.view_vibe()

    #ACTIONS
    def submit_mood(self):
        mood = self.mood_var.get()
        note = self.note_entry.get().strip()
        if note == "Optional anonymous note":
            note = None
        try:
            self.home.submit_mood(self.user, mood, note)
            Storage.save_home(self.home)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        suggestion = self.engine.suggest_for_user(mood)
        self.user_suggestion.config(text=f"Suggestion for you: {suggestion}")
        self.note_entry.delete(0, tk.END)
        self.view_vibe()

    def view_vibe(self):
        summary = self.home.get_vibe_summary()
        vibe = summary.get("vibe", "No Data")
        self.vibe_value.config(text=vibe, fg=vibe_color(vibe))
        home_tip = self.engine.suggest_for_home(vibe)
        self.home_suggestion.config(text=home_tip)
        self.notes_text.config(state="normal")
        self.notes_text.delete("1.0", tk.END)

        for note in summary.get("anonymous_notes", []):
            self.notes_text.insert(tk.END, f"• {note}\n\n")
        self.notes_text.config(state="disabled")

    #UTILITY
    def clear_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()


#LAUNCH
def launch_app():
    root = tk.Tk()
    app = RoomToneUI(root)
    root.mainloop()
