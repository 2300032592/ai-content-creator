from typing import Optional, List
from llm_client import chat_completion

SYSTEM_PROMPTS = {
    "LinkedIn Post": "Generate a professional LinkedIn post.",
    "Ad Copy": "Generate compelling ad copy that is concise and persuasive.",
    "Professional Email": "Generate a professional email that is clear and courteous.",
    "Conversational Text": "Generate friendly conversational text that is natural and engaging.",
}

def _build_system_prompt(content_type: str, tone: Optional[str], length: str, audience: str, keywords: List[str]) -> str:
    base = SYSTEM_PROMPTS.get(content_type, "Generate high-quality content.")
    parts = [base]
    if tone:
        parts.append(f"Tone: {tone}.")
    if audience:
        parts.append(f"Audience: {audience}.")
    if length == "Short":
        parts.append("Length: ~80-120 words.")
    elif length == "Medium":
        parts.append("Length: ~150-250 words.")
    elif length == "Long":
        parts.append("Length: ~300-450 words.")
    if keywords:
        parts.append(f"Focus on these keywords where relevant: {', '.join(keywords[:6])}.")
    parts.append("Be clear, coherent, and avoid filler.")
    return " ".join(parts)

def generate_content(prompt: str, content_type: str, tone: Optional[str], length: str, audience: str, keywords: List[str] | None = None) -> str:
    system_prompt = _build_system_prompt(content_type, tone, length, audience, keywords or [])
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]
    return chat_completion(messages, max_tokens=320, temperature=0.8)