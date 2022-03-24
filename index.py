from flask import Flask, render_template, request, flash, session, url_for, redirect
import os
from jinja2 import StrictUndefined
from flask_sqlalchemy import SQLAlchemy
from numpy import character
from sqlalchemy import create_engine


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.jinja_env.undefined = StrictUndefined
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)
print("Connected to DB.")

## ESTABLISH VARIABLES
index = 0
question = -1
vaderCount = 0
kenobiCount = 0
reyCount = 0
yodaCount = 0
jarCount = 0
bobaCount = 0
ahsokaCount = 0
hanCount = 0
maulCount = 0
kyloCount = 0
mandoCount = 0
padmeCount = 0
counter_dict = {}
character = ''


## CLASS TO GET CHARACTER INFORMATION FROM DB
class Character(db.Model):
    __tablename__ = "characters"

    char_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100))
    planet = db.Column(db.String(100))
    hair = db.Column(db.String(100))
    image = db.Column(db.String(100))
    weapon = db.Column(db.String(100))
    birthday = db.Column(db.String(100))
    movie = db.Column(db.String(100))
    height = db.Column(db.String(100))
    vehicle = db.Column(db.String(100))
    result = db.Column(db.Text)

    def __repr__(self):
        return f"{self.name}"


## CLASS TO GET QUESTION INFORMATION FROM DB
class Question(db.Model):
    __tablename__ = "questions"

    question_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    question = db.Column(db.String(100))
    answer1 = db.Column(db.String(100))
    answer2 = db.Column(db.String(100))
    answer3 = db.Column(db.String(100))
    answer4 = db.Column(db.String(100))
    image1 = db.Column(db.String(100))
    image2 = db.Column(db.String(100))
    image3 = db.Column(db.String(100))
    image4 = db.Column(db.String(100))

    def __repr__(self):
        return f"{self.question}"


## GET ALL CHARACTERS FROM DATABASE
def get_characters():
    char_list = Character.query.all()
    return(char_list)


## GET QUESTIONS FROM DATABASE
def get_questions():
    quest_list = Question.query.all()
    return(quest_list)


# INCREASE COUNT FUNCTIONS
def yoda_plus():
    global yodaCount
    yodaCount += 1
def kenobi_plus():
    global kenobiCount
    kenobiCount += 1
def vader_plus():
    global vaderCount
    vaderCount += 1
def rey_plus():
    global reyCount
    reyCount += 1
def ahsoka_plus():
    global ahsokaCount
    ahsokaCount += 1
def han_plus():
    global hanCount
    hanCount += 1
def maul_plus():
    global maulCount
    maulCount += 1
def kylo_plus():
    global kyloCount
    kyloCount += 1
def mando_plus():
    global mandoCount
    mandoCount += 1
def boba_plus():
    global bobaCount
    bobaCount += 1
def padme_plus():
    global padmeCount
    padmeCount += 1
def jar_plus():
    global jarCount
    jarCount += 1
    

## DISPLAY MAIN PAGE, RESET QUESTIONS AND COUNTERS
@app.route('/')
def main():
    global yodaCount
    global kenobiCount
    global vaderCount
    global reyCount
    global ahsokaCount
    global hanCount
    global maulCount
    global kyloCount
    global mandoCount
    global bobaCount
    global padmeCount
    global jarCount
    vaderCount = 0
    kenobiCount = 0
    reyCount = 0
    yodaCount = 0
    jarCount = 0
    bobaCount = 0
    ahsokaCount = 0
    hanCount = 0
    maulCount = 0
    kyloCount = 0
    mandoCount = 0
    padmeCount = 0

    global question
    question = 0
    return render_template('main.html')


## DISPLAY CHARACTER ROSTER
@app.route('/roster')
def roster():
    obj_list = get_characters()
    return render_template('roster.html',characters=obj_list)



## DISPLAY ALL QUESTIONS
@app.route('/questions')
def list_questions():
    obj_list = get_questions()
    return render_template('questions.html', questions=obj_list)


## START QUIZ AND ADVANCE TO NEXT QUESTION WHEN NEXT IS CLICKED
@app.route('/quiz', methods=["GET"])
def question_base():
    obj_list = get_questions()
    return render_template('question_base.html', questions=obj_list, number=question)


## INCREASE COUNTERS BASED ON ANSWER SELECTED BY USER
@app.route('/quiz', methods=["POST"])
def answer():
    try:
        answer = request.form['answer']
    except:
        print("You must select an option!")
        return redirect(url_for('question_base'))

    global question
    question += 1
    ## QUESTION 1
    if question == 1 and answer == 'Rock':
        boba_plus()
        vader_plus()
        kylo_plus()
    elif question == 1 and answer == 'Pop':
        jar_plus()
        rey_plus()
        maul_plus()
        ahsoka_plus()
    elif question == 1 and answer == 'Country':
        yoda_plus()
        han_plus()
        mando_plus()
    elif question == 1 and answer == 'Indie':
        kenobi_plus()
        padme_plus()
    ## QUESTION 2
    elif question == 2 and answer == 'Coruscant':
        vader_plus()
        ahsoka_plus()
        maul_plus()
    elif question == 2 and answer == 'Naboo':
        kenobi_plus()
        jar_plus()
        kylo_plus()
        padme_plus()    
    elif question == 2 and answer == 'Kashyyyk':
        rey_plus()
        boba_plus()
        mando_plus()
    elif question == 2 and answer == 'Takodana':
        boba_plus()
        rey_plus()
        han_plus()
    ## QUESTON 3
    elif question == 3 and answer == 'Doctor':
        yoda_plus()
        padme_plus()
    elif question == 3 and answer == 'Mechanic':
        boba_plus()
        mando_plus()
        ahsoka_plus()
        maul_plus()
    elif question == 3 and answer == 'Air Traffic Controller':
        vader_plus()
        rey_plus()
        han_plus()
    elif question == 3 and answer == 'Salesman':
        kenobi_plus()
        jar_plus()
        kylo_plus()
    ## QUESTION 4
    elif question == 4 and answer == 'Bravery':
        kenobi_plus()
        rey_plus()
        han_plus()
    elif question == 4 and answer == 'Friendship':
        yoda_plus()
        rey_plus()
        jar_plus()
        padme_plus()
    elif question == 4 and answer == 'Power':
        vader_plus()
        boba_plus()
        maul_plus()
        kylo_plus()
    elif question == 4 and answer == 'Loytalty':
        jar_plus()
        ahsoka_plus()
        mando_plus()
    ## QUESTION 5
    elif question == 5 and answer == 'Steak':
        vader_plus()
        kenobi_plus()
        mando_plus()
    elif question == 5 and answer == 'Pasta':
        boba_plus()
        yoda_plus()
        ahsoka_plus()
    elif question == 5 and answer == 'Enchiladas':
        rey_plus()
        maul_plus()
        padme_plus()
    elif question == 5 and answer == 'Orange Chicken':
        jar_plus()
        kylo_plus()
        han_plus()
    ## QUESTION 6
    elif question == 6 and answer == 'Blue':
        kenobi_plus()
        yoda_plus()
        padme_plus()
    elif question == 6 and answer == 'Red':
        vader_plus()
        kylo_plus()
    elif question == 6 and answer == 'Purple':
        boba_plus()
        mando_plus()
        maul_plus()
    elif question == 6 and answer == 'Yellow':
        jar_plus()
        rey_plus()
        ahsoka_plus()
        han_plus()
    ## QUESTION 7
    elif question == 7 and answer == 'Anger':
        vader_plus()
        kylo_plus()
        maul_plus()
    elif question == 7 and answer == 'Fear':
        rey_plus()
        boba_plus()
        ahsoka_plus()
        mando_plus()
    elif question == 7 and answer == 'Jealousy':
        jar_plus()
        kenobi_plus()
        han_plus()
    elif question == 7 and answer == 'Yes-Man':
        yoda_plus()
        padme_plus()
    ## QUESTION 8
    elif question == 8 and answer == 'R2-D2':
        kenobi_plus()
        yoda_plus()
        ahsoka_plus()
    elif question == 8 and answer == 'BB-8':
        rey_plus()
        jar_plus()
        kylo_plus()
        padme_plus()
    elif question == 8 and answer == 'C-3PO':
        vader_plus()
        boba_plus()
        han_plus()
    elif question == 8 and answer == 'BD-1':
        rey_plus()
        maul_plus()
        mando_plus()
    ## QUESTION 9
    elif question == 9 and answer == 'Spring':
        yoda_plus()
        padme_plus()
        mando_plus()
    elif question == 9 and answer == 'Summer':
        jar_plus()
        maul_plus()
        kylo_plus()
    elif question == 9 and answer == 'Fall':
        rey_plus()
        kenobi_plus()
        ahsoka_plus()
        han_plus()
    elif question == 9 and answer == 'Winter':
        vader_plus()
        boba_plus()
    ## QUESTION 10
    elif question == 10 and answer == 'Life of the Party':
        jar_plus()
        maul_plus()
        han_plus()
        return redirect(url_for('results'))
    elif question == 10 and answer == 'Talk to Friends':
        rey_plus()
        kenobi_plus()
        ahsoka_plus()
        padme_plus()
        return redirect(url_for('results'))
    elif question == 10 and answer == 'Brief Appearance':
        boba_plus()
        mando_plus()
        return redirect(url_for('results'))
    elif question == 10 and answer == 'No Parties':
        yoda_plus()
        vader_plus()
        kylo_plus()
        return redirect(url_for('results'))

    return redirect(url_for('question_base'))


## DISPLAY RESULTS
@app.route('/results')
def results():
    global counter_dict
    ## ADD COUNTS TO A DICTIONARY
    counter_dict['Yoda'] = yodaCount
    counter_dict['Obi Wan Kenobi'] = kenobiCount
    counter_dict['Darth Vader'] = vaderCount
    counter_dict['Rey Skywalker'] = reyCount
    counter_dict['Ahsoka Tano'] = ahsokaCount
    counter_dict['Han Solo'] = hanCount
    counter_dict['Maul'] = maulCount
    counter_dict['Kylo Ren'] = kyloCount
    counter_dict['The Mandalorian'] = mandoCount
    counter_dict['Boba Fett'] = bobaCount
    counter_dict['Padme Amidala'] = padmeCount
    counter_dict['Jar Jar Bink'] = jarCount

    ## FIND HIGHEST COUNT IN DICTIONARY
    c = max(counter_dict, key= lambda x: counter_dict[x])
    
    ## GET CHARACTER OBJECTS
    obj_list = get_characters()

    ## GET CHARACTER THAT MATCHES THE ONE WITH THE HIGHEST COUNT
    for obj in obj_list:
        if obj.name == c:
            character = obj
    return render_template('results.html', character=character)



@app.route('/yours')
def yours():
    return render_template('yours.html')


if __name__ == '__main__':
    app.run()




    
