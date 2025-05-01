from flask import Flask, render_template, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr')
def generate_qr():
    discount_code = "DISCOUNT2025"
    img = qrcode.make(f"https://example.com/discount?code={discount_code}")
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
