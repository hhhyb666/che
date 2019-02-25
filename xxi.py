from models import User,session,Base


#models.CreatDb()
#dt=User(username="user11",password_hash="user11")

# models.delDb()
#session.add(dt)
#session.commit()
#name=models.User.query.filter_by(username='peter').first()
#print(name.username)
#users = User.query.all()
#user = session.query(User).all()[0].username
user=session.query(User).filter_by(locale='http://123.127.164.20:21935').first().username
print (user)