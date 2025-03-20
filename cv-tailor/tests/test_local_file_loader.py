import pytest
from unittest.mock import patch
from src.cv_loader.local_file_loader import LocalFileLoader
import os


@patch("pdfminer.high_level.extract_text", return_value="Sample job spec text")

def test_load_pdf(mock_pdf_reader):
    pdf_path = os.path.join(os.path.dirname(__file__), 'mocks', 'mock_job_spec.pdf')
    print(f"PDF path: {pdf_path}")

    loader = LocalFileLoader()
    result = loader.load_cv(pdf_path)
    print(f"PDF content: {result}")

    assert "Sample job spec text" in result

@patch("docx.Document")
def test_load_docx(mock_docx):
    mock_doc = mock_docx.return_value
    mock_doc.paragraphs = [type('Paragraph', (object,), {'text': 'Sample DOCX text'})()]
    
    loader = LocalFileLoader()
    result = loader.load_cv("dummy_path.docx")
    
    assert result == "Sample DOCX text"
    mock_docx.assert_called_once_with("dummy_path.docx")

def test_load_cv_invalid_format():
    loader = LocalFileLoader()
    with pytest.raises(ValueError, match="Unsupported file format. Please provide a .pdf or .docx file."):
        loader.load_cv("dummy_path.txt")