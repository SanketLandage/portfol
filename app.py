from flask import Flask ,render_template,request,redirect,url_for
import csv

app = Flask(__name__)

@app.route('/')
def myHome():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)



def write_to_file(data):
	with open('database.txt',mode = 'a') as database:
		email= data['email']
		name= data['name']
		message= data['message']
		file = database.write(f'\n {name} , {email} , {message} ')


@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
	if request.method == 'POST':
		try:

			data = request.form.to_dict()

			write_to_file(data)
			return redirect('/contact.html')
		except:
			return ' Oops something went wrong not able to connect to the database !'
	else:
		return 'Something went wrong visit after some time , Thank you !'