class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

class Post:
    def __init__(self, title:str, content:str, author: User):
        self.title = title
        self.content = content
        self.author = author
        
class Forum:
    def __init__(self):
        self.users = []
        self.posts = []

    def register_user(self, username: str, email:str):
        user = User(username, email)
        self.users.append(user)
        return user

    def create_post(self, title:ste, content:str, author:str):
        post = Post(title, content, author)
        self.posts.append(post)
        return post

    def find_user_by_username(self, username:str):
        for user in self.users:
            if user.username == username:
                return user

    def find_user_by_email(self, email:str):
        for user in self.users:
            if user.email == email:
                return user
            
    def find_post_by_username(self, user:str):
        found_posts = []

        for post in self.posts:
            if post.author == user:
                found_posts.append(post)

        return found_posts

forum = Forum()

ripley = forum.register_user("listenToRipley", "ripley@wayland.com")
arthur = forum.register_user("dent.a","adent@gmail.com")

print(forum.users)

forum.create_post("Towels", "Towels are the the best, don't loose yours.", arthur)

# print(forum.posts)
# print(forum.posts[0].title)
# print(forum.posts[0print([found_post)].content)
# print(forum.posts[0].author.username)
# print(forum.posts[0].author.email)

print(forum.find_user_by_username('ripley'))
print(forum.find_user_by_username('dent.a').__dict__)

forum.create_post("Panic", "Don't panic.", arthur)

# found_post = forum.find_post_by_username(arthur)
# found_post_titles = [post.title for post in found_post]
# print(found_post_titles)

user_email = "adent@gmail.com"
found_user = forum.find_user_by_email(user_email)

if found_user:
    print(forum.find_post_by_username(found_user))
else:
    print(f"User with email {user_email}, doesn't exist!")