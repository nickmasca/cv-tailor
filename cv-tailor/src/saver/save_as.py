class Saver:
    def save_as_pdf(self, cv_text, output_path):
        from fpdf import FPDF
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        for line in cv_text.splitlines():
            pdf.cell(200, 10, txt=line, ln=True)
        
        pdf.output(output_path)

    def save_as_google_doc(self, cv_text, doc_id):
        from googleapiclient.discovery import build
        from google.oauth2 import service_account
        
        SCOPES = ['https://www.googleapis.com/auth/documents']
        SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'
        
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
        service = build('docs', 'v1', credentials=credentials)
        
        requests = [
            {
                'insertText': {
                    'location': {
                        'index': 1,
                    },
                    'text': cv_text
                }
            }
        ]
        
        service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()