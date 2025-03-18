class GoogleDocsLoader:
    def __init__(self, service):
        self.service = service

    def load_cv(self, doc_id):
        try:
            document = self.service.documents().get(documentId=doc_id).execute()
            return document.get('body').get('content')
        except Exception as e:
            print(f"An error occurred while loading the CV: {e}")
            return None