import os
WORDS_FILE = "../arabic_bloom_api/arabic_words.json"
import json
def get_app_status():
    return {'status': 'ok', 'message': 'API is running', 'version': '1.0.0'}
def load_words():
    if os.path.exists(WORDS_FILE):
        with open(WORDS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []