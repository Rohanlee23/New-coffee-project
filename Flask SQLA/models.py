from extension import db

class User(db.Model,UserMixin):
 id = db.Column(db.Integer, primary_key=True)
 name = db.Column(db.String(50))
 email = db.Column(db.String(120), unique=True, nullable=False)
 password = db.Column(db.String(255), nullable=False)
 posts = db.relationship("Post", back_populates="user")

 def __str__(self):
    return self.name

class Post(db.Model, UserMixin):f
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100))
  body = db.Column(db.Text)
  user_id = db.Column(db.ForeignKey("user.id"), nullable=False)
  user = db.relationship("User", back_populates="posts")

class Customer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)

def __str__(self):
    return self.username

class Food(db.Model,UserMixin):
    __tablename__ = "food"
    food_id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(20), unique=True, nullable=False)
    food_price = db.Column(db.Numeric(10,2), nullable=False)
    # food_price = db.Column(db.Numeric(10,2), nullable=False)
    # food_image = db.Column(db.LargeBinary)
    food_type = db.Column(db.String(30), nullable=False)
  
def __repr__(self):
    return f'<Food {self.food_name}>'

