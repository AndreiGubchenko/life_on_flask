from flask import Flask, render_template
import game_of_life

app = Flask(__name__)


@app.route('/')
def index():
    game_of_life.GameOfLife(25, 25)
    return render_template("index.html")


@app.route('/live')
def live():
    game_obj = game_of_life.GameOfLife()
    if game_obj.counter:
        game_obj.form_new_generation()
    else:
        game_obj.counter += 1

    return render_template('live.html', game_obj=game_obj)


if __name__ == '__main__':
    app.run("127.0.0.1", 5000, debug=True)
