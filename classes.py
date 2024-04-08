class User:
  def __init__(self, username, email):
    self.username = username
    self.email = email

  def info(self):
    print(f"Use {self.username} has email {self.email}")

first_user = User('user1', 'example@example.com')
print(first_user.info())

class Comment: 
  def __init__(self, text):
    self.text = text
    self.votes_qty = 0

  def upvote(self):
    self.votes_qty +=1


print(Comment.upvote)# upvote here is considered a function at this point
# # if passed at upvote() then it would get error as it should be an instance

first_comment = Comment("First comment")
print(first_comment.text)
print(first_comment.votes_qty)
print(first_comment.__dict__)
print(first_comment.upvote) # bound method now that the instance has been created
first_comment.upvote()
#also valid syntax = Comment.upvote(first_comment) but it is not recommended
print(first_comment.votes_qty)


class Post:
  def __init__(self, title, content, author):
    self.title = title
    self.content = content
    self.author = author
    self.likes_qty = 0 #default value

  def likes(self):
    self.likes_qty += 1


my_post = Post('Title', 'Content', 'Author')
print(my_post.title)
print(my_post.author)
my_post.likes()
my_post.likes()
print(my_post.likes_qty)