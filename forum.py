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
        self.posts = []

    def register_user(self, username, email):
        user = User(username, email)
        self.users.append(user)
        return user

    def create_post(self, title, content, author):
        post = Post(title, content, author)
        self.posts.append(post)
        return post

    def find_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user

    # def find_post_by_username():

forum = Forum()

ripley = forum.register_user("listenToRipley", "ripley@wayland.com")
arthur = forum.register_user("dent.a","adent@gmail.com")

print(forum.users)

forum.create_post("Towels", "Are the best, don't panic.", arthur)

# print(forum.posts)
# print(forum.posts[0].title)
# print(forum.posts[0].content)
# print(forum.posts[0].author.username)
# print(forum.posts[0].author.email)

print(forum.find_user_by_username('ripley'))
print(forum.find_user_by_username('dent.a').__dict__)