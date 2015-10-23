# Enter the Huis van Tekst
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
             abort, render_template, flash, jsonify
from functools import wraps
from hashlib import sha1, sha256

# configuration
DATABASE = '/home/professor/NEAR/gegevensbank/maan.db'
DEBUG = True
SECRET_KEY = 'my precious'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

pwdhsh = lambda x: sha1(sha256(x).hexdigest()).hexdigest()

def connect_db():
        return sqlite3.connect(DATABASE)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("You must log in for the Quadrivium.")
            return redirect(url_for("parlor"))
    return wrap

@app.route('/', methods=["GET","POST"])
def dueropening():
    error = None
    gendertitles = {'mr': 'Mr.', 'ms': 'Ms.', 'mrs': 'Mrs.'} # helper for the select
    if request.method == "POST":
        target = request.form["title"] # the value that should be selected
        usr = request.form["username"]
        eml = request.form["email"]
        pwd = request.form["password"]
        cpwd = request.form["passwordcheck"]
        if pwd != cpwd:
            error = "<span style='color:red;'>Passwords must match!</span>"
        else:
            pwd = pwdhsh(pwd)
            g.db = connect_db()
            g.db.execute("insert into signees(title, username, email, password, start) values ('{}', '{}', '{}', '{}', date('now'));".format(target, usr, eml, pwd))
            g.db.commit()
            g.db.close()
            flash("{} {}, If You're Reading This, You've Successfully Signed Up! When you get ready to enter the Quadrivium, log in with your username and password.".format(target.title(), usr.title()))
            return redirect(url_for("attic"))
    return render_template("mijnHuisVanDeRam.html", error=error, gendertitles=gendertitles)

@app.route('/melkstal', methods=['GET','POST'])
def parlor():
    error = None
    if request.method == "POST":
        g.db = connect_db()
        cur = g.db.execute("select * from signees where username='{}';".format(request.form["username"]))
        for i in cur:
            if request.form["username"] != i[2] or pwdhsh(request.form["password"]) != i[4]:
                error = "Invalid. Please try again."
            else:
                session["logged_in"] = True
                flash("You were logged in, {}!".format(request.form["username"]))
                g.db.close();
                return redirect(url_for("storage_room"))
    return render_template("mijnHuisVanDeVissen.html", error=error)

@app.route('/portiek')
def porch():
    session.pop("logged_in", None)
    flash("You've been logged out.")
    return redirect(url_for("dueropening"))

@app.route('/zolderkamertje/')
def attic():
    return render_template('grammar.html')

@app.route('/badkamer/')
def bathroom():
    return render_template('logic.html')

@app.route('/slaapkamer/')
def bedroom():
    return render_template('rhetoric.html')

@app.route('/berging/')
@login_required
def storage_room():
    g.db = connect_db()
    cur = g.db.execute("select * from persons")
    persons = [dict(name=row[0], gender=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('arithemetic.html', persons=persons)

@app.route('/eetkamer/')
@login_required
def dining_room():
    return render_template('geometry.html')

@app.route('/hol/')
@login_required
def den():
    musicians = {"Chronixx":"Terrible and Dread","D'angelo":"Voodoo",
                 "Ludwig van Beethoven":"Symphony No. 5","Michael Jackson":"Invincible",
                 "Bob Marley":"<strong>Emancipate</strong> yourselves from mental slavery, none but ourselves can free our minds!"}
    return render_template('music.html', musicians=musicians)

@app.route('/keuken/')
@login_required
def kitchen():
    celestial_bodies = {"Earth":"1 day","Moon":"27.5 days","Sun":"365 days",
                        "Mercury":"88 days","Venus":"224.7","Mars":"687",
                        "Jupiter":"4330.6","Saturn":"10755.7","Uranus":"30687",
                        "Neptune":"60190","Pluto":"90483.5"}
    return render_template('astronomy.html', celestial_bodies=celestial_bodies)



@app.route('/voogd/<verstandhouding>')
def rapport(verstandhouding):
    pass

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200



@app.route('/vestibule/')
def foyer():
    "English Kitchen Servant"
    return render_template('mijnHuisVanDeStier.html')

@app.route('/nis/')
def alcove():
    "alkoof, The Mental Vault"
    return render_template('mijnHuisVanDeTweelingen.html')

@app.route('/Vitruvius/')
def atrium():
    return render_template('mijnHuisVanDeLeeuw.html')

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/kelder/')
def basement():
    return render_template('mijnHuisVanDeMaagd.html')

@app.route('/serre/')
def conservatory():
    "A form for a basic client."
    return render_template('mijnHuisVanDeBoogschutter.html')

@app.route('/parkeergarage/')
def garage():
    return render_template('mijnHuisVanDeWeegschaal.html')

@app.route('/kwekerij/')
def nursery():
    return render_template('mijnHuisVanDeSkorpion.html')

@app.route('/vooraadkast/')
def larder():
    "bijkeuken"
    return render_template('pagestructure.html')

@app.route('/washok/')
def laundry_room():
    "wasruimte"
    pass

@app.route('/bibliotheek/')
def library():
    return render_template('mijnHuisVanDeWaterman.html')

@app.route('/woonkamer/')

def living_room():
    "huiskamer"
    pass

@app.route('/vliering/')
def loft():
    pass

@app.route('/hoekje/')
def nook():
    pass

@app.route('/kantoor/')
def office():
    pass

@app.route('/provisiekaast/')
def pantry():
    pass

@app.route('/recreatieruimte/')
def recreation_room():
    pass

@app.route('/heiligdommen/')
def shrines():
    pass

@app.route('/trappenhuis/')
def stairwell():
    pass

@app.route('/veranda/')
def sunroom():
    pass

@app.route('/zwembad/')
def swimming_pool():
    pass

@app.route('/werkplaats/')
def workshop():
    pass

@app.route('/open_haard/')
def fireplace():
    pass

@app.route('/haard/')
def hearth():
    return render_template('mijnhuis.html')

if __name__ == '__main__':
    app.run(debug=True)
