from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Бэкенд маникюрного салона запущен!"

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    if request.is_json:
        data = request.get_json()
        print(f"Имя: {data.get('name')}")
        print(f"Email: {data.get('email')}")
        print(f"Сообщение: {data.get('message')}")
        return jsonify({"message": "Сообщение успешно получено!"}), 200
    else:
        return jsonify({"message": "Ошибка: Ожидается JSON-данные"}), 400

@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    if request.is_json:
        data = request.get_json()
        print(f"Имя: {data.get('name')}")
        print(f"Телефон: {data.get('phone')}")
        print(f"Услуга: {data.get('service')}")
        print(f"Дата: {data.get('date')}")
        print(f"Время: {data.get('time')}")
        return jsonify({"message": "Заявка на запись успешно получена!"}), 200
    else:
        return jsonify({"message": "Ошибка: Ожидается JSON-данные"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
