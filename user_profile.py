import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
import os


class MainWindow(toga.App):
    def __init__(self):
        super().__init__('User Profile GUI', 'org.example.userprofile')

    def startup(self):
        """Создаем и отображаем главное окно."""
        self.initializeUI()

    def initializeUI(self):
        """Настройки графического интерфейса приложения."""
        self.setUpMainWindow()

    def createImageSection(self):
        """Создает секцию с изображениями."""
        # Главный контейнер для изображений
        image_box = toga.Box(style=Pack(direction=COLUMN, align_items=CENTER))

        # Контейнер для профильного изображения поверх фона
        profile_container = toga.Box(style=Pack(width=250, height=200, direction=COLUMN, align_items=CENTER))

        try:
            # Фоновое изображение
            background_image = "images/skyblue.png"
            if os.path.exists(background_image):
                bg_image = toga.ImageView(
                    image=background_image,
                    style=Pack(width=250, height=200)
                )
                profile_container.add(bg_image)

            # Профильное изображение (с прозрачностью)
            profile_image = "images/profile_image.png"
            if os.path.exists(profile_image):
                profile_img = toga.ImageView(
                    image=profile_image,
                    style=Pack(width=100, height=100, margin_top=-150)
                )
                profile_container.add(profile_img)

        except Exception as error:
            print(f"Images not found. \nError: {error}")
            error_label = toga.Label(
                'Изображения не найдены',
                style=Pack(text_align=CENTER)
            )
            profile_container.add(error_label)

        image_box.add(profile_container)
        return image_box

    def setUpMainWindow(self):
        """Создаём метки, которые будут отображаться в окне."""
        # Главный контейнер с прокруткой
        main_scroll = toga.ScrollContainer(horizontal=False)

        # Основной контент
        main_box = toga.Box(style=Pack(direction=COLUMN, margin=10))

        # Добавляем изображения
        image_section = self.createImageSection()
        main_box.add(image_section)

        # Информация о пользователе
        user_label = toga.Label(
            'Иван Драго',
            style=Pack(font_size=20, font_weight='bold', margin_top=5, text_align=CENTER)
        )
        main_box.add(user_label)

        # Биография
        bio_label = toga.Label(
            'Биография',
            style=Pack(font_size=17, margin_top=5, margin_left=5)
        )
        main_box.add(bio_label)

        about_label = toga.Label(
            'Я инженер-программист с 10-летним\nопытом создания потрясающего кода',
            style=Pack(margin_top=2, margin_left=5, margin_right=5)
        )
        main_box.add(about_label)

        # Умения
        skills_label = toga.Label(
            'Умения',
            style=Pack(font_size=17, margin_top=5, margin_left=5)
        )
        main_box.add(skills_label)

        language_label = toga.Label(
            'Python | PHP | SQL | JavaScript',
            style=Pack(margin_top=2, margin_left=5)
        )
        main_box.add(language_label)

        # Опыт работы
        experience_label = toga.Label(
            'Опыт',
            style=Pack(font_size=17,  margin_top=5, margin_left=5)
        )
        main_box.add(experience_label)

        # Первое место работы
        developer_label = toga.Label(
            'Python Разработчик',
            style=Pack(margin_top=5, margin_left=5)
        )
        main_box.add(developer_label)

        dates_label = toga.Label(
            'Март 2011 - настоящее время',
            style=Pack(margin_top=2, margin_left=5, font_size=10)
        )
        main_box.add(dates_label)

        # Второе место работы
        driver_label = toga.Label(
            'Водитель доставки пиццы',
            style=Pack(margin_top=10, margin_left=5)
        )
        main_box.add(driver_label)

        driver_dates_label = toga.Label(
            'Aug 2015 - Dec 2017',
            style=Pack(margin_top=2, margin_left=5, font_size=10)
        )
        main_box.add(driver_dates_label)

        # Устанавливаем контент в ScrollContainer
        main_scroll.content = main_box

        # Создаем главное окно
        self.main_window = toga.MainWindow(title='2.1 - User Profile GUI', size=(250, 400))
        self.main_window.content = main_scroll
        self.main_window.show()


if __name__ == '__main__':
    app = MainWindow()
    app.main_loop()