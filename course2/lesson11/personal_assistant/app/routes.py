from flask import request, render_template
from app import app

contacts = []

@app.route('/contacts', methods=['GET'])
def getcontact():
    return render_template('formaddcontacts.html', title='Form')


@app.route('/contacts', methods=['POST'])
def postcontact():
    global contacts
    data = {
        'name': request.form.get('name'),
        'surname': request.form.get('surname'),
        'adress': request.form.get('adress'),
        'note': request.form.get('note'),
        'tag': request.form.get('tag'),
        'email': request.form.get('email'),
        'phone': request.form.get('phone'),
        'birthday': request.form.get('birthday')
    }
    contacts +=[data]
    return render_template('contacts.html', contacts=contacts)
