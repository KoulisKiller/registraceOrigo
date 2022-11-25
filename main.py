from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')



list = []
@app.route('/druha_stranka', methods=['GET', 'POST'])
def druha_stranka():

    if request.method == "POST" :
        return validace_form()
    else:
        return render_template('druha_stranka.html'), 200
def validace_form():
    nick = request.form['nick']
    je_plavec = request.form['je_plavec']
    if je_plavec == "1":
        list.append(nick)
        return  render_template('druha_stranka.html'), 200
    else:
        return "bad value", 400

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('prvni_stranka.html',ucastnici=list), 200




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
