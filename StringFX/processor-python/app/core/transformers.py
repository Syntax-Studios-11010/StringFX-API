import re

def to_mock_text(text: str) -> str:
    """Converts text to sPoNgEbOb MoCkInG tExT."""
    return "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(text))

def to_leet_speak(text: str) -> str:
    """Converts text to 1337sp34k."""
    leet_dict = {'a': '4', 'e': '3', 'g': '6', 'l': '1', 'o': '0', 's': '5', 't': '7'}
    return "".join(leet_dict.get(c.lower(), c) for c in text)

def to_slugify(text: str) -> str:
    """Converts text to a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'[-\s]+', '-', text)

def sanitize_text(text: str, custom_blacklist: list = None, replacement: str = "*") -> str:
    """Simple profanity/blacklist filter."""
    blacklist = custom_blacklist or ["badword", "fudge", "heck"] # Default list
    processed_text = text
    for word in blacklist:
        # Case insensitive replacement
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        processed_text = pattern.sub(replacement * len(word), processed_text)
    return processed_text