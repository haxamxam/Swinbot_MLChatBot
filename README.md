# Swinbot
*Thanks for visiting*

Tensorflow based Chatbot using <strong>Flask, Python and JavaScript </strong>. 

Made as a University Research Project. It is currently deployed on the default WSGI server.

## Here is how to run it:

*Note: Please make sure you have Python 3.6 or 3.7 installed and a virtual environment set up. I used PyCharm as my preferred IDE.*

Install the requirements file

```
pip install requirements.txt
```

Run the application as a Python file

```
python app.py
```

Run the application as a Flask application. If you use the Flask executable to start your server, you can use the script below to change the default from 127.0.0.1 and open it up to non local connections.

```
flask run --host=0.0.0.0

```
Upon successful execution of the code the chatbot will be deployed to a local host at:

http://127.0.0.1:5000/

Inspired the by the tutorial

https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077

