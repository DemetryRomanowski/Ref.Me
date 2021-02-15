from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/download', methods=['GET'])
def download():
    return render_template('download.html')


@app.route('/download/linux_deb', methods=['GET'])
def linux_deb():
    return send_file('./downloads/refme_1.0-1.deb')


@app.route('/download/linux_rpm', methods=['GET'])
def linux_rpm():
    return send_file('./downloads/refme.rpm')


@app.route('/download/mac', methods=['GET'])
def mac():
    return send_file('./downloads/refme.app')


@app.route('/download/windows', methods=['GET'])
def windows():
    return send_file('./downloads/refme.exe')


if __name__ == '__main__':
    app.run()
