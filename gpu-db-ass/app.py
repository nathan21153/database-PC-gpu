from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():  # put application's code here
    return render_template('main-page.html')

@app.route('/info-page')
def info_page():  # put application's code here
    return render_template('info-page.html')

@app.route('/gpu-page')
def gpu_page():  # put application's code here
    return render_template('gpu-page.html')

if __name__ == '__main__':
    app.run()
