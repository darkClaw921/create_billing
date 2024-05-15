from flask import Flask, render_template, request
from pprint import pprint
app = Flask(__name__)

# Список выбора
projects = [['Сопровождение сделки купли-продажи', 1],
         ['Разработка стратегии фин. инвестиций', 5],
         ['Разработка альтернативной стратегии инвестирования', 7],
         ['Консультация по инвестированию', 9],
         ['Проект поддержки Комбината ', 11],
         ['Поддержка Янтарного комбината', 13],
         ['Аудит компании', 15],
         ['Поглощение Битриксом Microsoft', 19],
         ['Проект "Свежий ветер"', 31],
         ['Коттеджный поселок 65 км', 33],
         ['Формирование маркетинговой политики', 35],
         ['Сопровождение сделки купли-продажи', 37],
         ['Фиксированный проект с авансовыми платежами', 39],
         ['Проект юр. сопровождения сделки', 41],
         ['Проект сопровождения юридической сделки', 43],
         ['Создание биллинга из затраченного времени', 45]]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pprint(request.form)
        selected_item_index = int(request.form['item'])
        selected_item_value = projects[selected_item_index][1]
        return f"The second element of the selected item is: {selected_item_value}"
    return render_template('index.html', items=projects)


if __name__ == '__main__':
    app.run(debug=True)
