## Лабораторна робота №5
### Тема

Візуалізація якості стану дорожнього покриття за допомогою фреймворку Kivy.

### Мета

Розробити програму для візуалізації руху машини на дорозі та якості дороги за допомогою даних датчиків.

### Підготовка робочого середовище, встановлення проекту

Створення віртуального середовища

`python -m venv ./venv`

Активація середовища для linux

`source ./venv/bin/activate`

Активація середовища для windows

`venv\Scripts\activate`

Встановлення необхідних бібліотек

`pip install -r requirements.txt`

### Завдання

Для відображення мапи використовується віджет [Mapview](https://mapview.readthedocs.io/en/1.0.4/) для Kivy.

Для візуалізації руху машини можна використовувати MapMarker та рухати його відповідно GPS даних.
Для позначення нерівностей на дорозі також використовувати маркери. Зображення для маркерів можна знайти в папці images.

Для створення та редагування маршруту машини на мапі використовуйте клас LineMapLayer та функцію 
`add_point()` з файлу lineMapLayer.py. Додавання лінії на мапу:

```python
map_layer = LineMapLayer()
mapview.add_layer(map_layer, mode="scatter")
```

Щоб створити затримку при відображенні руху машини можна використовувати
функцію `kivy.clock.Clock.schedule_once()` або `kivy.clock.Clock.schedule_interval()`.

Дані для відображення на мапі (координати та стан дороги) зчитуються з бази даних через вебсокет.
Для їх отримання використовуйте функцію `get_new_points()` з datasource.py.

**Шаблон основного файлу проєкту**

```python
from kivy.app import App
from kivy_garden.mapview import MapMarker, MapView
from kivy.clock import Clock
from lineMapLayer import LineMapLayer


class MapViewApp(App):
    def __init__(self, **kwargs):
        super().__init__()
        # додати необхідні змінні

    def on_start(self):
        """
        Встановлює необхідні маркери, викликає функцію для оновлення мапи
        """

    def update(self, *args):
        """
        Викликається регулярно для оновлення мапи
        """

    def update_car_marker(self, point):
        """
        Оновлює відображення маркера машини на мапі
        :param point: GPS координати
        """

    def set_pothole_marker(self, point):
        """
        Встановлює маркер для ями
        :param point: GPS координати
        """

    def set_bump_marker(self, point):
        """
        Встановлює маркер для лежачого поліцейського
        :param point: GPS координати
        """

    def build(self):
        """
        Ініціалізує мапу MapView(zoom, lat, lon)
        :return: мапу
        """
        self.mapview = MapView()
        return self.mapview


if __name__ == '__main__':
    MapViewApp().run()
```
