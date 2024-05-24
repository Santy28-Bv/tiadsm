from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about_us")
def aboutus():
    return render_template('about_us.html')


@app.route("/layout")
def layout():
    return render_template('layout.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

def pagina_no_encontrada(error):
    return render_template('404.html'),404


@app.route("/Elhermano")
def hermano():
    return render_template('elhermano.html')


if __name__=='__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)
    


#Activar entorno virtual .venv\Scripts\activate
#Correr aplicación python app\app.py run

