import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER


class MainWindow(toga.App):
    def __init__(self):
        super().__init__('Пример Toga', 'org.example.helloworld')           #toga обязательно должно быть id

    def startup(self):
        """Создаем и отображаем главное окно."""
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс приложения."""
        self.setUpMainWindow()

    def setUpMainWindow(self):
        """Создаем Toga для отображения в главном окне."""
        main_box = toga.Box(style=Pack(direction=COLUMN, margin=20))        #margin внешний отступ, pedding внутренний отступ

        # Текстовый лейбл
        hello_label = toga.Label(
            'Привет!',
            style=Pack(margin=(0, 10), text_align=CENTER)
        )
        main_box.add(hello_label)

        # Изображение
        try:
            image = "images/world.png"
            world_image = toga.ImageView(
                image=image,
                style=Pack(margin=(0, 20), width=200, height=150)
            )
            main_box.add(world_image)
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")

        # Создаем главное окно
        self.main_window = toga.MainWindow(title='Пример Toga', size=(250, 250))
        self.main_window.content = main_box
        self.main_window.show()


if __name__ == '__main__':
    app = MainWindow()
    app.main_loop()