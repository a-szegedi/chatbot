import json
import re
from fuzzywuzzy import fuzz

class ChatBot:
    def __init__(self, faq_path):
        self.faq = self.load_faq(faq_path)

    def load_faq(self, path):
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def find_response(self, user_input):
        user_input = user_input.lower()

        for entry in self.faq:
            for keyword in entry["keywords"]:
                pattern = r'\b' + re.escape(keyword) + r'\b'
                if re.search(pattern, user_input):
                    return entry["response"]

        best_match = None
        highest_score = 0

        for entry in self.faq:
            for keyword in entry["keywords"]:
                score = fuzz.token_set_ratio(user_input, keyword)
                if score > highest_score:
                    highest_score = score
                    best_match = entry

        if highest_score >= 60:
            return best_match["response"]
        else:
            return "Entschuldigung, dazu habe ich leider keine passende Antwort. Bitte kontaktieren Sie den Support."