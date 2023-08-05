from documentServiceDesign.models.document import Document, Permission


class DocumentFactory:
    @staticmethod
    def create_text_document(name, content, owner):
        return TextDocument(name, content, owner)


class TextDocument(Document):
    def _has_permission(self, user, permission):
        for access in self.access_list:
            if access.user == user and access.permission == permission:
                return True
        return False

    def read(self, user):
        if self._has_permission(user, Permission.READ.value) or self._has_permission(user, Permission.EDIT.value):
            return self.content
        else:
            return "Unauthorized to read this document."

    def edit(self, user, new_content):
        if self._has_permission(user, Permission.EDIT.value):
            self.content = new_content
        else:
            return "Unauthorized to edit this document."
