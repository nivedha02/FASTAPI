### CRUD Operations
* Best practice is use operation in plural form for url i.e. posts for posting , users for user creation
* Use id in case of fetching single values
<img width="928" height="542" alt="image" src="https://github.com/user-attachments/assets/53a52b0c-0134-4728-b479-26c9184ffd95" />

##### To run uvicorn server with auto re-load when ever we save a code
`uvicorn main:app --reload` - our main file location followed by function name
'uvicorn app.main:app -- reload` - If we move our file to app floder so , app->main.py->app() function

### FastAPI Documentation 
* FastAPI includes ReDoc to provide a clean, professional, and easy-to-read reference manual for your API.While the default Swagger UI is interactive and great for testing endpoints, ReDoc is built for documentation clarity and long-term maintenance. It automatically converts your FastAPI code's OpenAPI schema into a highly organized, user-friendly webpage.
`http://127.0.0.1:8000/docs` - You will see the automatic interactive API documentation (provided by Swagger UI)
`http://127.0.0.1:8000/redoc` - You will see the alternative automatic documentation (provided by ReDoc)
<img width="828" height="281" alt="image" src="https://github.com/user-attachments/assets/7559a248-d99e-41b3-830e-4a8eacb37bff" />

