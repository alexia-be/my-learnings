# 02-social-media-fastapi

A social media style API built with Python and FastAPI, backed by PostgreSQL and tested with Postman. *(Work in progress, Part 1)*

## What it does and why I built it

This project is a REST API for posts: you can create, read, update and delete them, and the data is stored in a PostgreSQL database. FastAPI generates interactive API docs automatically at `/docs`.

I'm building it to learn how an API is created from the ground up, and later to learn how to automate API testing with pytest. It's a follow-up to my first tutorial project, `01-contact-book-api`: that one was built with Python alone, and this one adds a real database once the endpoints are in place.

**Course I'm following:** [Python API Development - Comprehensive Course for Beginners](https://www.youtube.com/watch?v=0sOvCWFmrtA) by Sanjeev Thiyagarajan (freeCodeCamp, YouTube)
**Started:** November 1, 2026
**Status:** In progress, Part 1 done (endpoints, PostgreSQL, SQLAlchemy ORM, response schemas).

## Tools and technologies

- **Python** and **FastAPI** for the API
- **Uvicorn** as the web server (installed with `fastapi[all]`)
- **Pydantic** for data validation and response schemas
- **PostgreSQL** and **pgAdmin** for the database
- **psycopg2** as the PostgreSQL driver (used first, with raw SQL)
- **SQLAlchemy** as the ORM
- **Postman** for testing endpoints (I saved my requests in a Postman collection)
- **VS Code** as my editor

## Endpoints

| Method | Path | What it does |
|--------|------|--------------|
| GET | `/` | Returns a hello world message |
| GET | `/posts` | List all posts |
| POST | `/posts` | Create a post (returns 201) |
| GET | `/posts/{id}` | Get one post (404 if it doesn't exist) |
| PUT | `/posts/{id}` | Update a post (404 if it doesn't exist) |
| DELETE | `/posts/{id}` | Delete a post (returns 204, or 404 if it doesn't exist) |

## Project structure

```
02-social-media-fastapi/
└── app/
    ├── __init__.py   # tells Python this folder is a package
    ├── main.py       # the API endpoints
    ├── database.py   # database connection (engine, session, base class)
    ├── models.py     # ORM models: the tables as Python classes
    └── schema.py     # Pydantic classes: validation and response models
```

## How it works

1. **Setup:** Created the project folder and a Python virtual environment, then installed FastAPI. I used `pip freeze` to see which dependencies were installed.
2. **First endpoint:** Added `main.py` with a root `GET /` endpoint, started the server with Uvicorn (`uvicorn main:app --reload`) and tested it in the browser. I learned how the path operation decorator (`@app.get("/")`) works.
3. **CRUD endpoints:** Built `GET /posts`, `POST`, get-one-post, `PUT` (update) and `DELETE`, tested with Postman and saved my requests in a Postman collection. At this stage the data lived in a Python variable inside `main.py`. FastAPI also generates interactive docs automatically at `/docs`.
4. **Validation:** Replaced the raw `dict` request body with a Pydantic `BaseModel`, with required, optional and default fields. Used `.model_dump()` to turn the model into a plain Python dictionary, and `HTTPException` to return the right status code when a post ID doesn't exist.
5. **Project structure:** Moved `main.py` into an `app/` package with an `__init__.py`.
6. **Database:** Installed PostgreSQL, created a server, database and table, and practiced basic SQL (querying and inserting data).
7. **Raw SQL version:** Connected the endpoints to the database with `psycopg2` and `RealDictCursor`, using parameterized queries (`%s`) to protect against SQL injection. Tested every endpoint with Postman and pgAdmin.
8. **ORM version:** Set up SQLAlchemy (`database.py` for the engine, session and base class, `models.py` for the tables as Python classes). First tested a simple GET endpoint with the ORM, then replaced all the raw SQL with `db.query` calls.
9. **Response schemas:** Moved my Pydantic classes into a dedicated `schema.py` file, and added a schema as the `response_model` on each endpoint, so only the declared fields are returned to the client. I tested this with Postman and checked the data in pgAdmin.

## How to run it


**1. Create and activate a virtual environment (Windows PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**2. Install dependencies**

```bash
pip install "fastapi[all]"
pip install psycopg2
pip install sqlalchemy
```

**3. Set up PostgreSQL**

Install PostgreSQL from [postgresql.org](https://www.postgresql.org/) and create an empty database named `02_social_media_fastapi` (I used pgAdmin). The `posts` table is created automatically when the app starts, from the models in `models.py`.

The app connects to PostgreSQL on `localhost` with the `postgres` user. Update the connection settings in `app/main.py` and `app/database.py` to match your own setup.

**4. Start the server**

```bash
uvicorn app.main:app --reload
```

**5. Try it out**

Open `http://127.0.0.1:8000/docs` for the auto-generated API docs, or test the endpoints with Postman.

## What I learned

- **Building REST APIs:** Creating endpoints for the full CRUD cycle, and returning proper HTTP status codes with `HTTPException`.
- **Data validation:** Using Pydantic to validate request bodies and shape responses, including required, optional and default fields.
- **Databases:** Basic SQL, connecting an app to PostgreSQL, and why parameterized queries prevent SQL injection.
- **ORMs:** How SQLAlchemy lets me work with the database through Python objects instead of raw SQL.
- **Separation of concerns:** Pydantic schemas (in `schema.py`) describe data as it travels over the API, while ORM models (in `models.py`) describe how data is stored in the database.
- **API testing:** Testing every endpoint in Postman, organizing requests into a collection, and verifying the data in pgAdmin.
- **Project structure:** Organizing code into a Python package.
- **Working with documentation:** Cross-checking a tutorial against the current official docs.

## Challenges and how I solved them

- **The tutorial is about 5 years old.** Some steps didn't match the current FastAPI documentation. I followed the latest docs alongside the video and compared the two at each step instead of only copying the tutorial.
- **Deprecated Pydantic code.** The tutorial uses `.dict()` (Pydantic v1), which is deprecated. I replaced it with `.model_dump()` after reading the [Pydantic v2 migration guide](https://pydantic.dev/docs/validation/latest/get-started/migration/#changes-to-pydanticbasemodel).
- **Getting stuck in general.** I try to find the problem myself first, using the docs and my own debugging. If I still can't solve it, I ask Claude.

## Next steps

I'm following the course as far as I can, and I'll update this README as I go. Still to come:

- Users and authentication (JWT)
- Votes and database relationships (joins)
- Database migrations with Alembic
- Automated API testing with **pytest** 
- and more