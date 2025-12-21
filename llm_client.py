import os
import time
from typing import List, Dict, Any
from dotenv import load_dotenv
from groq import Groq

__all__ = ["chat_completion"]

# Load env
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise RuntimeError("GROQ_API_KEY is not set. Add it to .env (GROQ_API_KEY=gsk_...)")

_client = Groq(api_key=API_KEY)

def chat_completion(
    messages: List[Dict[str, str]],
    model: str = "llama-3.3-70b-versatile",
    max_tokens: int = 320,
    temperature: float = 0.8,
    retries: int = 3,
) -> str:
    last_err: Any = None
    for attempt in range(1, retries + 1):
        try:
            resp = _client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return (resp.choices[0].message.content or "").strip()
        except Exception as e:
            last_err = e
            time.sleep(min(2**attempt, 8))
    raise last_err