import re

_STOP = {
    "the","a","an","and","or","to","of","in","on","for","with","is","are","be","as",
    "this","that","it","at","by","from","about","into","over","after","up","out",
}

def analyze(prompt: str):
    p = (prompt or "").lower()

    # tone
    tone = None
    if any(w in p for w in ["formal","professional","official","respectful"]):
        tone = "Professional"
    elif any(w in p for w in ["casual","friendly","informal","conversational"]):
        tone = "Casual"
    elif any(w in p for w in ["sales","ad","marketing","persuasive","cta"]):
        tone = "Persuasive"
    elif any(w in p for w in ["support","helpful","service"]):
        tone = "Friendly"

    # length
    length = "Medium"
    if any(w in p for w in ["short","brief","concise","tweet","100 words"]):
        length = "Short"
    elif any(w in p for w in ["long","detailed","elaborate","in-depth","400 words"]):
        length = "Long"

    # audience
    audience = "General"
    if "b2b" in p or "business" in p or "enterprise" in p:
        audience = "B2B"
    elif "b2c" in p or "consumer" in p or "customers" in p:
        audience = "B2C"
    elif any(w in p for w in ["technical","engineer","developer","it team"]):
        audience = "Technical"
    elif "non-technical" in p or "layman" in p:
        audience = "Non-technical"

    # keywords
    tokens = re.findall(r"[a-zA-Z][a-zA-Z\-]+", p)
    keywords = [t for t in tokens if t not in _STOP][:10]

    return {"tone": tone, "length": length, "audience": audience, "keywords": keywords}