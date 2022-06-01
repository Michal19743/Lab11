from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def main():
     dane = {'tytul':'Strona główna', 'tresc':'To jest strona główna.'}
     return render_template('index.html', tytul=dane['tytul'], tresc=dane['tresc'])

	
@app.route("/about")
def about():
     dane = {'tytul':'O mnie', 'tresc':'Nazywam się Majkel Rakowski.'}
     return render_template('omnie.html', tytul=dane['tytul'], tresc=dane['tresc'])

@app.route('/info')
def info():
    posty = [
        {
         'author': {'username': 'Pablo'},
         'body': 'Szpadlo'
        },
        {
         'author': {'username': 'Mati'},
         'body': 'Taki'
    }]
    dane = {'tytul':'Informacje', 'tresc':'Zarchiwizowane informacje.'}
    return render_template('info.html', tytul=dane['tytul'], tresc=dane['tresc'], posty=posty)
 
@app.route("/kontent")

def kontent():
     dane = {'tytul':'Kontent', 'tresc':'kontent: '}
     return render_template('kontent.html', tytul=dane['tytul'], tresc=dane['tresc'])
	
if __name__ == "__main__":
	app.run()
