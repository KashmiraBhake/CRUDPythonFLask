from flask import Blueprint,render_template,request

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/new_patient',methods=['GET','POST'])
def new_patient():
    return render_template('new_patient.html',boolean=True)

@views.route('/create_new_patient',methods=['GET','POST'])
def create_new_patient():
    data = request.form
    print(data)
    firstName=request.form.get('firstName')
    lastName=request.form.get('lastName')
    age=request.form.get('age')
    gender=request.form.get('gender')
    city=request.form.get('city')
    pincode=request.form.get('pincode')
    return render_template('submit_patient.html',firstName=firstName,lastName=lastName,age=age,gender=gender,city=city,pincode=pincode)