from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        # Access the value of the input field with the ID 'cityInput'
        city = request.form['city']
        api_key = 'b6412077223314ba343848fe2eff635a'
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(api_url)
        if response.status_code == 200:
            weather = response.json()
        else:
            weather = None
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run()