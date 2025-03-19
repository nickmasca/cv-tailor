import pytest
from unittest.mock import patch
import pyperclip
from src.scraper.scraper import read_job_spec_from_pdf, read_job_spec_from_clipboard
import tempfile
import os

@patch("pdfminer.high_level.extract_text", return_value="Sample job spec text")
def test_read_job_spec_from_pdf(mock_extract_text):
    pdf_path = os.path.join(os.path.dirname(__file__), 'mocks', 'mock_job_spec.pdf')
    print(f"PDF path: {pdf_path}")
    result = read_job_spec_from_pdf(pdf_path)
    print(f"Extracted text: {result}")
    
    assert "Sample job spec text" in result

@patch("pyperclip.paste", return_value="Sample clipboard text")
def test_read_job_spec_from_clipboard(mock_paste):
    result = read_job_spec_from_clipboard()
    
    assert result == "Sample clipboard text"
    mock_paste.assert_called_once()