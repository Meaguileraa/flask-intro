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

MEANNESS = ['ugly', 'mean', 'annoying', 'rude', 'immature', 'childish',
     'grumpy', 'bossy']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>Hi! Welcome to the home page.
      <body>
        <a href ="/hello">Start Here</a> 
      </body>

    </html>"""

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

        <form action="/greet" method='GET'>
          What's your name? <input type="text" name="person">
          What compliment would you like?<br>
          <input type="radio" name="compliment" value="amazing">Amazing<br>
          <input type="radio" name="compliment" value="cool">Cool<br>
          <input type="radio" name="compliment" value="smart">Smart<br>
          <input type="radio" name="compliment" value="determined">Determined<br>
          <input type="radio" name="compliment" value="beautiful">Beautiful<br>
          <input type="radio" name="compliment" value="nice">Nice<br>
          <input type="radio" name="compliment" value="wonderful">Wonderful<br>
          <input type="radio" name="compliment" value="awesome">Awesome<br>

          What diss would you like?<br>
          <input type="radio" name="diss" value="ugly">Ugly<br>
          <input type="radio" name="diss" value="mean">Mean<br>
          <input type="radio" name="diss" value="annoying">Annoying<br>
          <input type="radio" name="diss" value="rude">Rude<br>
          <input type="radio" name="diss" value="immature">Immature<br>
          <input type="submit" value="Submit"><br>
        </form>

      </body>
  </html>
  """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")
    diss = request.args.get("diss")
    #y=x intentional error to view the debugger page

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player,compliment or diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
