import flask
from flask_login import LoginManager, login_required
from form import LoginForm

app = flask.Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db = [["t","s"]]

def query(id, p):
    if(list(id, p) in db):
        return True
    return False

def queryAndGet(id):
    for i in db:
        if(i[0] == id):
            return User(id,i[1])
    return None

class User:
    def __init__(self,id,pas):
        self.username,self.password = id, pas
        self.is_authenticated = query(username, password)
        if(self.is_authenticated):
            self.christmasFriend = (db.index(list(self.username,self.password)) + 1) % len(db)
        else:
            self.christmasFriend = None
def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.username

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

@login_manager.user_loader
def load_user(user_id):
    return queryAndGet(user_id)

@app.route('/')
@app.route('/index')
@login_required
def index():
    return "whooa there's nothing here. Strange things happen to those who click <a href='/logout'>here</a>."

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        user = User(form.username.data,form.password.data).is_authenticated()
        if user is not None:
            flask.flash("Invalid username/password")
            return redirect(url_for('login'))
        flask.flash('That works, what you see is your friend')
        return user.christmasFriend
    return flask.render_template('login.html', form=form)

if __name__ == '__main__':
   app.run()
