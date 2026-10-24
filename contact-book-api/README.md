# Contact Book REST API

A simple REST API built with Python and Flask that lets you list, view, create, update, and delete contacts.

## What it does and why I built it

This is a Contact Book API. It has endpoints to get all contacts, get one contact by id, create a contact, update a contact, and delete a contact. If you ask for a contact id that doesn't exist, it returns an error message.

I built it to learn REST APIs and Python. I followed the course *Skill Up with Python: Hands-on Web Development Projects* by Pearson and Shaun Wassell on LinkedIn Learning. I completed it in one day, on October 23, 2026.

## Tools and technologies

- Python
- Flask 
- VS Code
- Postman

## How it works

1. **Set up:** I created an environment in a project folder and added a `server.py` file.
2. **List endpoint:** I created an endpoint that returns all contacts and tested it from the browser URL.
3. **Get one contact:** I created an endpoint that returns a specific contact by id. It returns an error message if no contact exists for that id.
4. **Create:** I created a POST endpoint to add a contact and tested it with Postman.
5. **Update:** I created a PUT endpoint to update a contact and tested it.
6. **Delete:** I created a DELETE endpoint to remove a contact and tested it.

## How to run it

1. Clone the repo and go into the project folder:
   ```bash
   git clone https://github.com/alexia-be/my-learnings.git
   cd my-learnings/contact-book-api
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   ```
3. Install Flask:
   ```bash
   pip install flask
   ```
4. Start the server:
   ```bash
   python server.py
   ```
5. The API runs at `http://127.0.0.1:5000`.

## How to use it

| Action | Method | Endpoint |
|---|---|---|
| List all contacts | GET | `http://127.0.0.1:5000/contacts` |
| Get one contact | GET | `http://127.0.0.1:5000/contacts/<id>` |
| Create a contact | POST | `http://127.0.0.1:5000/contacts` |
| Update a contact | PUT | `http://127.0.0.1:5000/contacts/<id>` |
| Delete a contact | DELETE | `http://127.0.0.1:5000/contacts/<id>` |

Replace `<id>` with the contact's id. I tested the list endpoint in the browser and the POST, PUT, and DELETE endpoints with Postman. For POST and PUT, I send the contact details in the request body (raw) with two fields: `name` and `phone`.

## What I learned

- What Flask is and how to use it to create API endpoints with Python.
- How to return an error message when a requested contact doesn't exist.
- How to test requests with Postman.
- The contacts are stored in the Python file itself, so a contact created through the API isn't saved there. After a server restart, anything I added is gone and the GET endpoint can't return it. This is why real apps use a database, which keeps data when the server restarts.
- How `for` loops work in Python, which I understand better after using them in the endpoints.

## Next steps

I want to go deeper into Python to understand how apps work in general. I plan to keep learning by building more projects and continuing my training.