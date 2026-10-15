### CRUD Operations
* Best practice is use operation in plural form for url i.e. posts for posting , users for user creation
* Use id in case of fetching single values
<img width="928" height="542" alt="image" src="https://github.com/user-attachments/assets/53a52b0c-0134-4728-b479-26c9184ffd95" />

##### To run uvicorn server with auto re-load when ever we save a code
`uvicorn main:app --reload` - our main file location followed by function name

`uvicorn app.main:app --reload` - If we move our file to app floder so , `app->main.py->app()` function as we need app as imporatable module

### FastAPI Documentation 
* FastAPI includes ReDoc to provide a clean, professional, and easy-to-read reference manual for your API.While the default Swagger UI is interactive and great for testing endpoints, ReDoc is built for documentation clarity and long-term maintenance. It automatically converts your FastAPI code's OpenAPI schema into a highly organized, user-friendly webpage.
`http://127.0.0.1:8000/docs` - You will see the automatic interactive API documentation (provided by Swagger UI)
`http://127.0.0.1:8000/redoc` - You will see the alternative automatic documentation (provided by ReDoc)
<img width="828" height="281" alt="image" src="https://github.com/user-attachments/assets/7559a248-d99e-41b3-830e-4a8eacb37bff" />

## SQL Insert,Delete,Update codes in pgadmin
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/2ca125fb-1fb4-4b63-9688-4b3eef289019" />

# FastAPI + SQLAlchemy + PostgreSQL — Simple Example and Notes

## 1. Basic understanding

- FastAPI: Creates API endpoints.
- PostgreSQL: The actual database server that stores data.
- pgAdmin: A graphical tool used to manage PostgreSQL and execute SQL queries.
- Psycopg2: A database driver that connects Python to PostgreSQL.
- SQLAlchemy: An ORM that lets us interact with database tables using Python code instead of writing SQL manually for every operation.

### How they work together

text
```
FastAPI (Python code)
        |
        v
SQLAlchemy (ORM)
        |
        v
Psycopg2 (Database driver)
        |
        v
PostgreSQL (Database server)
        ^
        |
     pgAdmin
 (Manage and view data)
```

## 2. Traditional method — Using SQL directly

Suppose we have a `students` table in PostgreSQL, created using pgAdmin.

python
```
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="school",
    user="postgres",
    password="your_password"
)

cursor = conn.cursor()

cursor.execute(
    "INSERT INTO students (name, age) VALUES (%s, %s)",
    ("Rahul", 21)
)

conn.commit()

cursor.close()
conn.close()
```

Notes:

- We write the SQL statement manually.
- Psycopg2 sends the SQL to PostgreSQL.
- PostgreSQL executes the query and stores the data.

## 3. ORM method — Using SQLAlchemy

Install the required packages:

bash
```
pip install fastapi sqlalchemy psycopg2-binary
```

Now we can perform the same operation using Python objects.

python
```
from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

DATABASE_URL = (
    "postgresql+psycopg2://postgres:your_password@localhost/school"
)

engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer)

with Session(engine) as session:
    student = Student(name="Rahul", age=21)

    session.add(student)
    session.commit()
```

Notes:

1. `Student` is a Python class representing the database table.
2. `Student(name="Rahul", age=21)` creates a Python object.
3. `session.add(student)` stages the object for insertion.
4. `session.commit()` commits the transaction.
5. SQLAlchemy generates the necessary SQL.
6. Psycopg2 sends the SQL to PostgreSQL.
7. PostgreSQL stores the data.

The `students` table must already exist for this example to work. Alternatively, SQLAlchemy can create it using `Base.metadata.create_all(engine)`.

## 4. What SQL does SQLAlchemy generate?

Your Python code:

python
```
student = Student(name="Rahul", age=21)
session.add(student)
session.commit()
```

Conceptually, SQLAlchemy generates an SQL statement similar to:

sql
```
INSERT INTO students (name, age)
VALUES ('Rahul', 21);
```

You don't need to write this SQL manually in your application code.

## 5. Important notes to remember

| Technology | Purpose |
| --- | --- |
| FastAPI | Builds APIs |
| SQLAlchemy | Converts ORM operations into SQL |
| Psycopg2 | Connects Python to PostgreSQL |
| PostgreSQL | Stores and processes data |
| pgAdmin | Manages the database graphically |

Final takeaway:
Traditional approach: Python + Psycopg2 + manually written SQL.
ORM approach: Python + SQLAlchemy + Psycopg2, where SQLAlchemy generates SQL 
Important: ORM does not eliminate SQL. It reduces the need to write SQL manually. PostgreSQL still executes SQL behind the scenes.