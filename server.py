from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_txt(data):
    with open("database.txt", mode='a') as database_txt:
        email = data['email']
        subject = data['subject']
        message = data['message']
        txt_writer = database_txt.write(f'\nEmail: {email}, Subject: {subject}, Message: {message}')


def write_to_csv(data):
    with open("database.csv", mode='a') as database_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database_csv, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_txt(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again!'



    
    



# @app.route('/<username>/<int:id>')
# def hello_world_user(username, id):
#     return render_template('index.html', name = username, id = id)


# @app.route('/about')
# def blog():
#     return render_template('about.html')
    

# @app.route('/blog/2020/dogs')
# def blog_dogs():
#     return 'pretty nice dogs'
