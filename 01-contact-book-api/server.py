from flask import Flask, request

app = Flask(__name__)

next_id = 5

contacts = [
    { 'id': '1', 'name': 'Shaun', 'phone': '123-456-7891'},
    { 'id': '2', 'name': 'Bob', 'phone': '111-222-3333'},
    { 'id': '3','name': 'Sue', 'phone': '444-555-6666'},
    { 'id': '4', 'name': 'Betty', 'phone': '777-888-9999'},
]


# GET all contacts
@app.get('/contacts')
def list_contacts():
    return contacts

# GET specific contact
@app.get('/contacts/<id>')
def read_single_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            return contact
    return 'That contact does not exist.'

# POST contact
@app.post('/contacts')
def create_contact():
    global next_id

    new_contact = {
        'id': f'{next_id}',
        'name': request.json['name'],
        'phone': request.json ['phone'],
    }

    contacts.append(new_contact)

    next_id += 1

    return new_contact

# PUT contact
@app.put('/contacts/<id>')
def update_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            contact['name'] = request.json['name'] if 'name' in request.json else contact['name']
            contact['phone'] = request.json['phone'] if 'phone' in request.json else contact['phone']
            return contact

    return 'There is no contact with that id!'

# DELETE contact
@app.delete('/contacts/<id>')
def delete_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            contacts.remove(contact)
            return contact

    return 'There is no contact with that id!'
    




if __name__ == '__main__':
    app.run(debug=True)