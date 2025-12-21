# AI Content Generator - Copilot Instructions

## Project Overview
AI-powered content generator using Llama 3.3 70B via Groq API. Streamlit web app that creates 4 content types (LinkedIn posts, ad copy, professional emails, conversational text) with auto-detection of tone, length, and audience from user prompts.

## Architecture

**3-Layer Design:**
- `app.py`: Streamlit UI with content type selector and parameter controls
- `model.py`: Content generation orchestration with content-specific system prompts
- `llm_client.py`: Groq API wrapper with retry logic
- `prompt_analyzer.py`: Heuristic-based auto-detection for tone/audience/keywords

**Data Flow:** User prompt → prompt_analyzer (if auto-detection enabled) → model builds system prompt → llm_client calls Groq API → formatted response

## Critical Setup

**Environment:**
```bash
# Always activate venv first
.\venv\Scripts\Activate.ps1
# Run app
streamlit run app.py
```

**Required:** `GROQ_API_KEY` in `.env` file (format: `GROQ_API_KEY=gsk_...`)

**Dependencies:** Groq SDK (0.37.0), Streamlit, python-dotenv. See [requirements.txt](requirements.txt) for full list.

## Code Conventions

**System Prompts (model.py):**
- Each content type has base prompt in `SYSTEM_PROMPTS` dict
- Build dynamic prompts via `_build_system_prompt()` that appends tone/length/audience/keywords
- Length mapping: Short (80-120 words), Medium (150-250 words), Long (300-450 words)

**LLM Parameters:**
- Default: `max_tokens=320`, `temperature=0.8`, `model="llama-3.3-70b-versatile"`
- Retry logic: 3 attempts with exponential backoff (2^attempt, capped at 8s)

**Auto-Detection Logic (prompt_analyzer.py):**
- Keyword-based heuristics, NOT ML
- Extracts tone via keyword matching (e.g., "formal" → Professional, "sales" → Persuasive)
- Filters stop words to extract relevant keywords (max 10 returned)
- Returns dict: `{"tone": str|None, "length": str, "audience": str, "keywords": List[str]}`

**UI Pattern:**
- 3-column layout for tone/length/audience selectors
- Auto-detection checkbox toggles between manual controls and heuristic analysis
- Effective values merge user selections with detected values (user selection takes precedence if not "Auto")

## Key Files

- [app.py](app.py) - Main Streamlit UI, demonstrates parameter merging logic for auto-detection
- [model.py](model.py) - System prompt construction patterns, shows how to build dynamic prompts per content type
- [llm_client.py](llm_client.py) - Groq API integration with retry pattern and error handling
- [prompt_analyzer.py](prompt_analyzer.py) - Heuristic detection implementation, stop word filtering

## Common Tasks

**Adding new content type:**
1. Add entry to `SYSTEM_PROMPTS` dict in [model.py](model.py)
2. Add option to selectbox in [app.py](app.py#L15)
3. Test with various tone/length combinations

**Modifying LLM behavior:**
- Adjust system prompts in [model.py](model.py#L4-L9) for tone changes
- Modify `temperature` parameter in [model.py](model.py#L35) for creativity (0=deterministic, 1=creative)
- Change `max_tokens` for length control (currently 320)

**Improving detection:**
- Extend keyword lists in [prompt_analyzer.py](prompt_analyzer.py#L6-L29)
- Add domain-specific patterns to existing conditionals
- Update `_STOP` set for better keyword extraction

## Testing Notes
- No automated tests currently. Manual testing via Streamlit interface required.
- Debug info displays file path and CWD at top of app (see [app.py](app.py#L10-L11))
- Test with diverse prompts to validate auto-detection accuracy
