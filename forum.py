class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        
class Forum:
    def __init__(self):
        self.users = []
        self.post = []