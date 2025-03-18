from scraper.scraper import Scraper
from cv_loader.google_docs_loader import GoogleDocsLoader
from tailor.llm_tailor import LLMTailor
from diff_viewer.markdown_diff import generate_diff
from saver.save_as import Saver

def main():
    # Step 1: Scrape job specification
    url = input("Enter the job specification URL: ")
    pdf_path = input("Enter the path to the job specification PDF (or leave blank): ")
    
    scraper = Scraper()
    if url:
        job_spec = scraper.scrape_from_url(url)
    elif pdf_path:
        job_spec = scraper.scrape_from_pdf(pdf_path)
    else:
        print("No job specification provided.")
        return

    # Step 2: Load CV from Google Docs
    doc_id = input("Enter the Google Docs document ID for your CV: ")
    loader = GoogleDocsLoader()
    cv_text = loader.load_cv(doc_id)

    # Step 3: Tailor the CV using the LLM
    tailor = LLMTailor()
    tailored_cv = tailor.tailor_cv(cv_text, job_spec)

    # Step 4: View changes as diffs
    diff = generate_diff(cv_text, tailored_cv)
    print("Differences between original and tailored CV:")
    print(diff)

    # Step 5: Save the new CV version
    save_option = input("Save tailored CV as (1) PDF or (2) Google Doc? Enter 1 or 2: ")
    saver = Saver()
    if save_option == '1':
        output_path = input("Enter the output path for the PDF: ")
        saver.save_as_pdf(tailored_cv, output_path)
        print(f"Tailored CV saved as PDF at {output_path}.")
    elif save_option == '2':
        new_doc_id = input("Enter the Google Docs document ID to update: ")
        saver.save_as_google_doc(tailored_cv, new_doc_id)
        print(f"Tailored CV updated in Google Docs with ID {new_doc_id}.")
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()