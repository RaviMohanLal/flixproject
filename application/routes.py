from application import app, db
# from flask import render_template, request, json, Response original
from flask import render_template,request,json,Response,redirect,flash,url_for #justin
#from application.models import videopop original
from application.models import User #justin
from urllib.request import urlopen
from application.forms import LoginForm,RegisterForm #justin


#original below
# videodata = [{"courseID":"1","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}, {"courseID":"6","title":"66","description":"666","credits":6666,"term":"66666"}]

@app.route("/") # root directory

@app.route("/index") #
@app.route("/home") # 
def index():
    return render_template("index.html", index=True)

# @app.route("/login") # original
# def login(): #original
    # return render_template("login.html", login=True) original

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email       = form.email.data
        password    = form.password.data

        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name}, you are successfully logged in!", "success")
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.","danger")
    return render_template("login.html", title="Login", form=form, login=True )

@app.route("/videocatalog") #
# @app.route("/videocatalog/<vid>") #
def videocatalog():
    url = "http://34.67.246.221/myflix/videos"
    response = urlopen(url)
    jdata = json.loads(response.read())
    #print(jdata)
    #videodata = videopop.objects.all()
    return render_template("videocatalog.html", data2=jdata,videocatalog=True)

# @app.route("/register") # original
# def register(): #original
#     return render_template("register.html", register=True) #original

#################### JUST IN ###################################################
@app.route("/register", methods=['POST','GET']) 
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_id     = User.objects.count()
        user_id     += 1

        email       = form.email.data
        password    = form.password.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data
        print("444444444444444444444444444")
        print("lastname")
        print("las444444444444s44444444444444444tna4444444me")
        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash("You are successfully registered!","success")
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=form, register=True)

################### JUST IN####################################################################

@app.route("/vid1", methods=["GET","POST"]) # 
def vid1():
    Title = request.args.get('Title')
    thumbnail = request.args.get('thumbnail')
    return render_template("vid1.html", vid1=True, data={"Title":Title,"thumbnail":thumbnail})

@app.route("/api")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = videodata
    else:
        jdata = videodata[int(idx)]

    return Response(json.dumps(jdata), mimetype="application/json")

################### JUST IN #################################################
@app.route("/user")
def user():
     #User(user_id=1, first_name="Christian", last_name="Hur", email="christian@uta.com", password="abc1234").save()
     #User(user_id=2, first_name="Mary", last_name="Jane", email="mary.jane@uta.com", password="password123").save()
     users = User.objects.all()
     return render_template("user.html", users=users)

