from groq import Groq

client = Groq(api_key="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")

SYSTEM_PROMPTS = {
    "LinkedIn Post": "Generate a professional LinkedIn post that is engaging and industry-relevant.",
    "Ad Copy": "Generate compelling ad copy that is concise and persuasive.",
    "Professional Email": "Generate a professional email that is clear and courteous.",
    "Conversational Text": "Generate friendly conversational text that is natural and engaging."
}

def generate_content(prompt, content_type):
    system_prompt = SYSTEM_PROMPTS.get(content_type, "Generate high-quality content.")
    
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        model="llama-3.3-70b-versatile",
        max_tokens=200
    )
    return response.choices[0].message.content