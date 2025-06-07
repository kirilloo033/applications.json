from flask import Flask, request, render_template, jsonify
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Разрешить CORS для разработки

# Путь к файлу для хранения заявок (в формате JSON)
APPLICATIONS_FILE = "applications.json"


def load_applications():
    """Загружает заявки из файла."""
    if os.path.exists(APPLICATIONS_FILE):
        with open(APPLICATIONS_FILE, 'r', encoding='utf-8') as f:  # Укажите кодировку
            try:
                return json.load(f)
            except json.JSONDecodeError:  # Если файл пустой или поврежден
                return []
    else:
        return []


def save_applications(applications):
    """Сохраняет заявки в файл."""
    with open(APPLICATIONS_FILE, 'w', encoding='utf-8') as f:  # Укажите кодировку
        json.dump(applications, f, indent=4, ensure_ascii=False)  # Отключите ASCII escaping


@app.route('/submit_application', methods=['POST'])
def submit_application():
    """Обрабатывает отправку формы заявки."""
    try:
        name = request.form.get('name')
        contact_method = request.form.get('contactMethod')
        phone = request.form.get('phone')
        email = request.form.get('email')
        telegram = request.form.get('telegram')
        message = request.form.get('message')

        if not name or not contact_method:
            return jsonify({'error': 'Необходимо заполнить имя и способ связи'}), 400

        new_application = {
            'name': name,
            'contactMethod': contact_method,
            'phone': phone,
            'email': email,
            'telegram': telegram,
            'message': message
        }

        applications = load_applications()
        applications.append(new_application)
        save_applications(applications)

        return jsonify({'success': 'Заявка успешно отправлена'}), 200

    except Exception as e:
        print(e)
        return jsonify({'error': 'Ошибка сервера'}), 500


@app.route('/admin')
def admin():
    """Отображает страницу администратора с заявками."""
    applications = load_applications()
    return render_template('admin.html', applications=applications)

if __name__ == '__main__':
    app.run(debug=True)