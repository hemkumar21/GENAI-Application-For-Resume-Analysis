import os
from resume_summarizer.pdf_extractor import extract_text_from_pdf
from resume_summarizer.openai_summarizer import summarize_resume

def main(pdf_path):
    resume_text = extract_text_from_pdf(pdf_path)
    summary = summarize_resume(resume_text)
    print(summary)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Summarize a resume PDF.")
    parser.add_argument("pdf_path", type=str, help="Path to the resume PDF file")
    args = parser.parse_args()

    # Ensure the API key is set
    if not os.getenv("OPENAI_API_KEY"):
        raise EnvironmentError("Please set the OPENAI_API_KEY environment variable.")

    main(args.pdf_path)
