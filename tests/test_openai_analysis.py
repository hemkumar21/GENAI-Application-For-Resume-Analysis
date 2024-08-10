import unittest
from resume_summarizer.openai_summarizer import summarize_resume

class TestOpenAISummarizer(unittest.TestCase):
    def test_summarize_resume(self):
        resume_text = """
        Jake P
        Email: jake.p@example.com
        Phone: (123) 456-7890

        Education:
        - Bachelor of Science in Computer Science, University of Example, 2020-2024

        Experience:
        - Software Engineering Intern, Example Corp, Summer 2023
          - Developed features for the company's main product using Python and JavaScript
          - Collaborated with a team of 5 to design and implement a new module

        Projects:
        - Personal Portfolio Website
          - Built a personal portfolio website using HTML, CSS, and JavaScript
          - Showcased projects and skills

        Certifications:
        - Certified Python Developer, Python Institute
        - AWS Certified Solutions Architect

        Skills:
        - Programming Languages: Python, JavaScript, C++
        - Web Development: HTML, CSS, React
        - Cloud: AWS
        """
        summary = summarize_resume(resume_text)
        self.assertIn("Jake P", summary)

if __name__ == "__main__":
    unittest.main()
