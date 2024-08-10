import openai

def summarize_resume(resume_text):
    prompt = f"Summarize the following resume into the format: name|college|internships|projects|certifications\n\nResume:\n{resume_text}\n\nSummary:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )

    summary = response.choices[0].text.strip()
    return summary
