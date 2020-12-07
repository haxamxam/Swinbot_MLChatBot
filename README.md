# Swinbot Tensorflow Chatbot

<p align="center">
  <img src="https://github.com/haxamxam/Swinbot_MLChatBot/blob/master/static/images/chatbot_main.png" width="350" title="hover text">
</p>

*Thanks for visiting*

Tensorflow based Chatbot using <strong>Flask, Python and JavaScript </strong>. 

Made as a University Research Project. It is currently deployed on the default WSGI server.



**Link to the chatbot deployed through Heroku:**
https://serene-fjord-29620.herokuapp.com/

## Here is how to run it:

*Note: Please make sure you have Python 3.6 or 3.7 installed and a virtual environment set up. I used PyCharm as my preferred IDE.*

Install the requirements file

```
pip install -r requirements.txt
```
## Python Execution

Run the application as a Python file

```
python app.py
```

Upon successful execution of the code the chatbot will be deployed to a local host at:

http://127.0.0.1:5000/

## Flask Application

Run the application as a Flask application. If you use the Flask executable to start your server, you can use the script below to change the default from 127.0.0.1 and open it up to non local connections. Simply run the flask app with your acquired IPv4 address

```
flask run -h 192.168.X.X
```
## Chatbot Application

The final chatbot looks like the following

<p align="center">
  <img src="https://github.com/haxamxam/Swinbot_MLChatBot/blob/master/static/images/ezgif.com-crop.gif" width="800" title="hover text">
</p>


## Inspiration and Resources

Inspired the by the tutorial:

https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077

