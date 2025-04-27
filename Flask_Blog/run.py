# Running the application is only purpose of file
from Flask_Blog import app # imports from the __init__.py file, so app must exist there

if __name__ == '__main__': ## if running directly with python
    app.run(debug=True)