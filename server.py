"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
     <!doctype html><html>
     <a href="/hello">Hi! This is the new home page.</a>
     
     
     </html>
    """

@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
        
          Pick a compliment:
          <select name="compliment">
            <option value="awesome"> Awesome</option>
            <option value="terrific"> Terrific</option>
          </select>
          <input type="submit" value="Submit">
        </form>
        <form action="/diss">
        What's your nickname? <input type="text" name="person">
        
        Pick a diss:
        <select name="insult">
          <option value="bigot"> Bigot</option>
          <option value="fascist"> Fascist</option>
          <option value="racist"> Racist</option>
          <option value="trumpsterfire"> Trumpster Fire</option>
        </select>
        <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route('/diss')
def insult_person():
   """insult person by their nickname"""
   name = request.args.get("person")

   insult = request.args.get("insult")
   return """
   
   <!doctype html>
   <html>
    <head>
      <title>A Diss</title>
    </head>
    <body>
      Hi, {}! I think you're a {}
    </body>
    </html>
    """.format(name, insult)

@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")
    
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
