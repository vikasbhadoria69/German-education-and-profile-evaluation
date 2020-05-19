from flask import Flask, render_template,request
app = Flask(__name__,template_folder='template')

@app.route('/')
def home():
    return render_template('Engg_mmgt_Univ.html')


if __name__ == "__main__": 
    app.run(debug=True)