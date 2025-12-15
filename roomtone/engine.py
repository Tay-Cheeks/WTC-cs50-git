"""
SuggestionEngine:
Takes in the aggregated home vibe and returns a gentle suggestion.

This version uses simple rule-based logic.
A future version may plug in an ML recommendation model.
"""

class SuggestionEngine:

    home_suggestions = {
        "Tense": "Maybe give each other some breathing space today.",
        "Mixed": "Could be a good time to leave a kind note.",
        "All Good": "Today feels like a good day to reconnect.",
        "No Data": "No check-ins yet today."
    }

    user_suggestions = {
        "low": "Be gentle with yourself today. It’s okay to take things slow.",
        "neutral": "A small check-in or walk might help today.",
        "good": "Nice energy today — maybe share it with someone."
    }

    @classmethod
    def suggest_for_user(cls, mood: str) -> str:
        """
        Return a gentle suggestion based on an individual's mood.
        """
        if not mood:
            return ""
        return cls.user_suggestions.get(mood.lower(), "")

    @classmethod
    def suggest_for_home(cls, vibe: str) -> str:
        """
        Return a suggestion based on the home's aggregated vibe.
        """
        if not vibe:
            return ""
        return cls.home_suggestions.get(vibe, "")

    @classmethod
    def get_suggestion(cls, vibe: str) -> str:
        """
        Backwards-compatible method.
        """
        return cls.suggest_for_home(vibe)
