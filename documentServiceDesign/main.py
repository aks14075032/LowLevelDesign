from models.user import User
from services.documentService import DocumentService
from models.document import Permission


user1 = User("user1")
user2 = User("user2")
user3 = User("user3")

document = DocumentService.create_document("text", "Sample Document", "Hello World!", user1)

user2_read_access = document.add_access(user2, Permission.READ.value)
document.add_access(user3, Permission.EDIT.value)

print(document.read(user2))  # Output: "Hello World!"
document.edit(user3, "Updated content.")  # Successful edit
print(document.read(user3))  # Output: "Updated content!"

print(document.edit(user2, "Unauthorized edit."))  # Unauthorized edit

document.remove_access(user2_read_access)
print(document.read(user2))