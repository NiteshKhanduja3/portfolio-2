from flask import Flask, render_template,url_for,request, redirect 
import csv
app = Flask(__name__)

@app.route('/')
def myhome():
    return  render_template('index.html')

@app.route('/submit_form')
def form():
    return  render_template('submit_form.html')
@app.route('/thankyou')
def thanks():
    return render_template('thankyou.html')


def write_to_csv(data):
    with open('database.csv',mode='a') as database2:
        name =data["name"]
        email= data["email"]
        phonenumber =data ["phonenumber"]
        message =data["message"]
        
        csv_writer = csv.writer(database2,delimiter =',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,phonenumber,message])

# def write_to_file(data):
#     with open('database.txt',mode='a') as database:
#         name =data["name"]
#         email= data["email"]
#         phonenumber =data ["phonenumber"]
#         message =data["message"]
        
#         file = database.write(f'\n{name},{email},{phonenumber},{message}')





@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
          data = request.form.to_dict()
          write_to_csv(data)
          return redirect('/thankyou')
          
        except:
            return "did not saved to database"
    else:
            return "something went wrong"




# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/blog/nitesh')
# def niteshbio():
#     return "This is the Bio"



