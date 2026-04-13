import re

def clean_text(text):
    text = text.lower()
    return re.sub(r'[^a-zA-Z0-9 ]', ' ', text)