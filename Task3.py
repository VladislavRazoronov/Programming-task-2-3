from flask import Flask,render_template
site = Flask(__name__)
@site.route('/')
def base():
    return render_template('base.html')
if __name__ == '__main__':
    site.run(debug=True)