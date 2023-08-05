from enum import Enum
from documentServiceDesign.models.access import Access
from abc import ABC, abstractmethod


class Permission(Enum):
    READ = 1
    EDIT = 2


class GrantType(Enum):
    READ = 1
    EDIT = 2


class Document(ABC):
    def __init__(self, name, content, owner):
        self.name = name
        self.content = content
        self.owner = owner
        self.access_list = []

    def add_access(self, user, permission):
        access = Access(user, self, permission)
        self.access_list.append(access)
        return access

    def remove_access(self, access):
        self.access_list.remove(access)

    @abstractmethod
    def read(self, user):
        pass

    def edit(self, user, new_content):
        pass


