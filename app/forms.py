from flask.ext.wtf import Form 
from wtforms.fields import  TextField , BooleanField , PasswordField
from wtforms.validators import Required

#class LoginForm(Form):
#    openid = TextField( 'openid' , validators=[Required()] )
#    remember_me = BooleanField( 'remember_me' , default = False )

    
class LoginForm(Form):
     username = TextField( 'username' , validators=[Required()] )
     password = PasswordField( 'password' , validators=[Required()] )
     remember_me = BooleanField( 'remember_me' , default = False )