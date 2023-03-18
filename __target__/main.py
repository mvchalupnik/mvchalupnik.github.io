"""
https://www.transcrypt.org/
Transcrypt steps:
1. Download Python 3.9 from www.python.org
2. Install Transcrypt from the command prompt by typing python -m pip install transcrypt
3. Create a new folder hello containing hello.html and hello.py
4. Go to that new folder and type python -m transcrypt -b -m -n hello.py
5. In that same new folder start an HTTP server by typing python -m http.server
6. In your browser, navigate to localhost:8000/hello.html to see the result


To force reload (prevent browser caching, useful for testing CSS)
cmd shift R

Helpful tips:
#To debug: (to print object contents)
console.log(JSON.stringify(object, null, 4));

#In your browser, navigate to localhost:8000/main.html to see the result

To compile:
python -m transcrypt -b -m -n main.py
python -m http.server
"""
from gameplay import FirstScreen

app1 = FirstScreen()
