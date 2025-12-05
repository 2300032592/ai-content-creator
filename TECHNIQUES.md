# LLM Customization Techniques - Weeks 1-2

## Overview
This document outlines the techniques used to customize Llama 3.3 70B responses for different content types.

---

## Technique 1: System Prompts (Primary Method)

### What is a System Prompt?
A system prompt is an instruction given to the LLM that defines its behavior, role, and guidelines for responding.

### Implementation in Our Project

**LinkedIn Post System Prompt:**
```
"Generate a professional LinkedIn post that is engaging and industry-relevant."
```
- **Purpose**: Guide model to create formal, industry-focused content
- **Result**: Posts with professional tone, industry keywords, engagement hooks

**Ad Copy System Prompt:**
```
"Generate compelling ad copy that is concise and persuasive."
```
- **Purpose**: Focus on sales-oriented, action-driven content
- **Result**: Short, persuasive CTAs with benefit statements

**Professional Email System Prompt:**
```
"Generate a professional email that is clear and courteous."
```
- **Purpose**: Maintain formal structure and respectful tone
- **Result**: Well-structured emails with proper greetings/closings

**Conversational Text System Prompt:**
```
"Generate friendly conversational text that is natural and engaging."
```
- **Purpose**: Create casual, relatable content
- **Result**: Natural dialogue with friendly tone

---

## Technique 2: Role-Based Prompting

### Concept
Define the AI's role to shape its responses. Example:
- "You are a professional LinkedIn strategist"
- "You are a creative advertising copywriter"
- "You are a business communication expert"

### Why It Works
The LLM aligns responses with the defined role's expertise and style.

---

## Technique 3: Context Injection

### Method
Provide specific context in system prompts:

```python
system_prompt = {
    "role": "professional LinkedIn strategist",
    "task": "create engaging posts",
    "guidelines": [
        "Include industry keywords",
        "Add engagement hook",
        "Keep professional tone",
        "150-300 words"
    ]
}
```

### Result
Model generates contextually appropriate content with specific guidelines.

---

## Technique 4: Output Constraints

### Token Limits
```python
max_tokens=200  # Controls response length
```
- **Effect**: Keeps responses concise and focused

### Temperature Control
```python
temperature=1.0  # Randomness level (0=deterministic, 1=creative)
```
- **Effect**: Balances creativity and consistency

---

## Technique 5: Few-Shot Prompting (Optional Enhancement)

### Concept
Provide examples in the prompt to guide output format.

**Example Enhancement:**
```
"Generate a professional LinkedIn post. Example format:
[Hook] → [Insight] → [Engagement question]

User prompt: Tell me about AI in healthcare
```

### Why It Works
Examples guide the model's output structure and style.

---

## Technique 6: Iterative Refinement

### Process
1. Generate initial content
2. Request refinement: "Make it more concise"
3. Further customize: "Add more technical details"

### Code Example
```python
def refine_content(content, refinement_instruction):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Refine this content: {content}"},
            {"role": "user", "content": refinement_instruction}
        ],
        model="llama-3.3-70b-versatile",
        max_tokens=200
    )
    return response.choices[0].message.content
```

---

## Summary Table

| Technique | Implementation | Impact |
|---|---|---|
| System Prompts | Specialized instructions per content type | ✅ High customization |
| Role-Based Prompting | Define AI role/expertise | ✅ Consistent style |
| Context Injection | Provide guidelines & constraints | ✅ Focused output |
| Token Limits | max_tokens parameter | ✅ Length control |
| Few-Shot Prompting | Provide examples | ✅ Format consistency |
| Iterative Refinement | Multiple passes/refinements | ✅ Quality improvement |

---

## Current Implementation Status

✅ **Implemented**: System Prompts, Role-Based Prompting, Context Injection, Token Limits
⏳ **Future Enhancement**: Few-Shot Prompting, Iterative Refinement
