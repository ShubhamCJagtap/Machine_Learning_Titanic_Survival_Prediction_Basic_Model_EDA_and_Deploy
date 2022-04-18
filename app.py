from flask import Flask,render_template,request
import pickle
import numpy as np
from dotenv import load_dotenv

load_dotenv()

age_1=0
Salutation_1=0
gender_1 =0
Embarked_1=0
pclass_1=0
fare_1=0
alone = 0
def create_app():
    model = pickle.load(open('titanic_model.pkl','rb'))
    app = Flask(__name__)
    #model = pickle.load(open('titanic_model.pkl','rb'))
    @app.route('/')
    def main():
        return render_template('home.html')

    @app.route('/' ,methods=['GET','POST'])
    def home():
        
        if request.method =="POST":
            Salutation = request.form.get('Salutation')
            if Salutation=='Mr':
                Salutation_1=0
            elif Salutation=='Mrs':
                Salutation_1=1
            elif Salutation=='Miss':
                Salutation_1=2
            elif Salutation=='Master':
                Salutation_1=3
            elif Salutation=='Other':
                Salutation_1=4
            else:
                Salutation_1='Fault'
                return render_template('home.html',Salutation = Salutation_1,
                            firstname = 0,
                            gender = 0,
                            age = 0,
                            family_size=0,
                            Embarked=0,
                            pclass=0,
                            fare=0,result='Fault')
                
            firstname = request.form.get('firstname')
            if firstname=="":
                firstname='Unknown'
            
            gender = request.form.get('Gender')
            if gender=='male':
                gender_1=0
            elif gender=='female':
                gender_1=1
            else:
                gender_1='Fault'
                return render_template('home.html',Salutation = Salutation,
                            firstname = firstname,
                            gender = gender_1,
                            age = 0,
                            family_size=0,
                            Embarked=0,
                            pclass=0,
                            fare=0,result='Fault')
            
            age = request.form.get('Age')
            if age.isnumeric():
                age = int(age)
                if age<0:
                    age_1='Fault'
                elif age <=16:
                    age_1=0
                elif age>16 and age<=32:
                    age_1=1
                elif age>32 and age<=48:
                    age_1=2
                elif age>48 and age<=64:
                    age_1=3
                else:
                    age_1=4
            else:
                age_1='Fault'
                return render_template('home.html',Salutation = Salutation,
                            firstname = firstname,
                            gender = gender,
                            age = age_1,
                            family_size=0,
                            Embarked=0,
                            pclass=0,
                            fare=0,result='Fault')
                
            
                
            family_size = int(request.form.get('family_size'))
            if family_size>0:
                alone = 0
            else:
                alone = 1
                
            Embarked = request.form.get('Embarked')
            if Embarked =="Southampton":
                Embarked_1=0
            elif Embarked=="Cherbourg":
                Embarked_1=1
            elif Embarked=="Queenstown":
                Embarked_1=2
            else:
                Embarked_1="Fault"
                return render_template('home.html',Salutation = Salutation,
                            firstname = firstname,
                            gender = gender,
                            age = age,
                            family_size=family_size,
                            Embarked=Embarked_1,
                            pclass=0,
                            fare=0,result='Fault')
            
            pclass = request.form.get('pclass')
            if pclass =="Class 1":
                pclass_1=1
            elif pclass=="Class 2":
                pclass_1=2
            elif pclass=="Class 3":
                pclass_1=3
            else:
                pclass_1="Fault"
                return render_template('home.html',Salutation = Salutation,
                            firstname = firstname,
                            gender = gender,
                            age = age,
                            family_size=family_size,
                            Embarked=Embarked,
                            pclass=pclass_1,
                            fare=0,result='Fault')
                
            fare = request.form.get('fare')
            if fare =="0 $ : 8 $":
                fare_1=0
            elif fare=="8 $ : 15 $":
                fare_1=1
            elif fare=="15 $ : 31 $":
                fare_1=2
            elif fare=="More than 31$":
                fare_1=3
            else:
                fare_1='Fault'
                return render_template('home.html',Salutation = Salutation,
                            firstname = firstname,
                            gender = gender,
                            age = age,
                            family_size=family_size,
                            Embarked=Embarked,
                            pclass=pclass,
                            fare=fare_1,result='Fault')
                
            data = np.array([[pclass_1,gender_1,Embarked_1,Salutation_1,age_1,fare_1,family_size,alone]])
            pred = model.predict(data)
            
            return render_template('home.html',Salutation = Salutation,
                                firstname = firstname,
                                gender = gender,
                                age = age,
                                family_size=family_size,
                                Embarked=Embarked,
                                pclass=pclass,
                                fare=fare,result=pred)
    
    return app

create_app()