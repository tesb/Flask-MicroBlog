

from app import app

from flask import render_template

from flask import flash,redirect
from forms import LoginForm

from hashlib import md5


@app.route('/')
@app.route('/index')
def index():
    #return 'Hello flask'
    posts = [
        { 
            'author': 'John', 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': 'Susan', 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    user={'user':'ab'}
    return render_template('index.html',title='aaaa' , username='sb',posts=posts)


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data==app.config['USERNAME'] and form.password.data==app.config['PASSWORD']:
            flash( 'SUCCESS!!!the user name is :' + form.username.data + 'the user\'s password is : ' + form.password.data)
            return redirect('/index')
        else:
            flash('error username or password')
            return redirect('/index')
    return render_template('login.html',form=form)


@app.route('/posts')
def posts():

    posts = [
                {
                'avatra':'http://7u2m64.com1.z0.glb.clouddn.com/avatar/dfc8b71b0a9384829ffbc91dcd988c19' ,
                'author':'tom',
                'email':'stevensin@126.com',
                'posts':'dasgjkhliudzdzk,jhdsalfiughildasfdasgjdzk,jhdsalfiughildasgjkhlihliudzk,jhdsalfiughildasf'
                },
                {
                'avatra':'http://7u2m64.com1.z0.glb.clouddn.com/avatar/08983f8adde41ef38412bf1f6a311d7e' ,
                'author':'tom',
                'email':'ibinary@126.com',
                'posts':'gjkhliudzk,jhdsalfiughildasf'
                }
             ]
    #posts['avatar'] = 'http://7u2m64.com1.z0.glb.clouddn.com/avatar/' + md5(posts['email']).hexdigest()

    
    return render_template('posts.html', posts = posts)


@app.route('/usercenter')
def usercenter():
    user = {
            'username':'Mical',
            'email':'tesb@tesb.tk',
            'total':14
            }
    md5email = md5( user['email'] ).hexdigest()
    gravatra = 'http://7u2m64.com1.z0.glb.clouddn.com/avatar/' + md5email 
    user['gravatra'] = gravatra
    return render_template('user.html' , user=user  )
    
    
@app.route('/test')
def test():
    md = md5('sss').hexdigest()
    return render_template('test.html',typee=md)


@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404
















