import sys
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    # width, _ = QInputDialog.getInt(
    #     None, "Размер карты", "Введите ширину (N):", 20, 1, 200
    # )
    # height, _ = QInputDialog.getInt(
    #     None, "Размер карты", "Введите высоту (M):", 20, 1, 200
    # )
    # if width and height:
    width = 20
    height = 20
    window = MainWindow(width, height)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
