from documentServiceDesign.services.documentFactory import DocumentFactory


class DocumentService:
    @staticmethod
    def create_document(document_type, name, content, owner):
        if document_type == 'text':
            return DocumentFactory.create_text_document(name, content, owner)
        else:
            raise ValueError('Invalid document type')
