from pdfminer.high_level import extract_text
import pyperclip

def read_job_spec_from_pdf(pdf_path):
    """
    Reads job specification from a local PDF file.
    
    :param pdf_path: Path to the PDF file.
    :return: Text content of the PDF file.
    """
    try:
        text = extract_text(pdf_path)
        return text
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return ""

def read_job_spec_from_clipboard():
    """
    Reads job specification from the clipboard.
    
    :return: Text content from the clipboard.
    """
    return pyperclip.paste()

# Example usage
if __name__ == "__main__":
#    pdf_path = "path/to/job_spec.pdf"
    # pdf_path = "/Users/Nicholas.Masca/Documents/Jobs/Candidate Brief - Allwyn - Director of Data and AI.pdf"
    # job_spec_pdf = read_job_spec_from_pdf(pdf_path)
    # print("Job Specification from PDF:\n", job_spec_pdf)

   job_spec_clipboard = read_job_spec_from_clipboard()
   print("Job Specification from Clipboard:\n", job_spec_clipboard)