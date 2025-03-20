from pdfminer.high_level import extract_text
import docx  # This should be correct if python-docx is installed

class LocalFileLoader:
    def load_cv(self, file_path):
        if file_path.endswith('.pdf'):
            return self._load_pdf(file_path)
        elif file_path.endswith('.docx'):
            return self._load_docx(file_path)
        else:
            raise ValueError("Unsupported file format. Please provide a .pdf or .docx file.")

    def _load_pdf(self, file_path):
        """
        Reads job specification from a local PDF file.
        
        :param pdf_path: Path to the PDF file.
        :return: Text content of the PDF file.
        """
        try:
            text = extract_text(file_path)
            return text
        except Exception as e:
            print(f"Error reading PDF file: {e}")
            return ""

    def _load_docx(self, file_path):
        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text