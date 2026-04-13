from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

def generate_feedback(missing, score):

    if not missing:
        return "Your resume is well aligned with the job description. Consider adding measurable achievements and project impact."

    prompt = f"""
    You are a professional ATS resume reviewer.

    Candidate Score: {score}

    Missing Skills: {', '.join(missing)}

    Provide clear, professional suggestions to improve the resume.
    Focus on:
    - Adding missing technical skills
    - Improving project descriptions
    - Using measurable achievements

    Output in 3-4 concise bullet points.
    """

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(
        **inputs,
        max_length=150,
        temperature=0.7
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)