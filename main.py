class Comment: 
  def __init__(self, text):
    self.text = text
    self.votes_qty = 0

  def upvote(self):
    self.votes_qty +=1


first_comment = Comment("First comment")
print(first_comment.text)
print(first_comment.votes_qty)
print(first_comment.__dict__)
first_comment.upvote()
print(first_comment.votes_qty)

class User:
  def __init__(self, username, email):
    self.username = username
    self.email = email

  def info(self):
    print(f"Use {self.username} has email {self.email}")

first_user = User('user1', 'example@example.com')
print(first_user.info())