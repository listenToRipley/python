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

  @staticmethod
  def merge_comments(first, second):
    return f"{first}, {second}"


print(Comment.upvote)# upvote here is considered a function at this point
# # if passed at upvote() then it would get error as it should be an instance

first_comment = Comment("First comment")
m_1 = Comment.merge_comments("Thanks!", "Wonderful")
m_2 = first_comment.merge_comments("okay", "great!")
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

  @staticmethod
  def format_post(title, comment):
    return (
      f"Title: {title}\n"
      f"Comment: {comment}"
    )


my_post = Post('Title', 'Content', 'Author')
print(my_post.title)
print(my_post.author)
my_post.likes()
my_post.likes()
print(my_post.likes_qty)
format_post = Post.format_post("This is the title", "This is the post content.")
print(format_post)

class Calculator:
  @staticmethod
  def add(a,b):
    return a+b
  
  @staticmethod
  def subtract(a,b):
    return a-b
  
  @staticmethod
  def mult(a,b):
    return a*b
  
  @staticmethod
  def divide(a,b):
    if b!=0:
      return a/b
    raise ValueError("Can't divide by zero.")

print(Calculator.add(20,10))