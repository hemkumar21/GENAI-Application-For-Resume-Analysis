import unittest
from resume_summarizer.pdf_extractor import extract_text_from_pdf

class TestPDFExtractor(unittest.TestCase):
    def test_extract_text_from_pdf(self):
        pdf_path = "tests/sample_resume.pdf"
        text = extract_text_from_pdf(pdf_path)
        self.assertIn("John Doe", text)

if __name__ == "__main__":
    unittest.main()
