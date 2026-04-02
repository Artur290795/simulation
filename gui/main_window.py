"""
Главное окно приложения, связывающее интерфейс и симуляцию.
"""

from PySide6.QtWidgets import QMainWindow, QInputDialog, QMessageBox

from gui.main_window_template import Ui_MainWindow
from gui.constants import PREDATORS_DEFAULT_AMOUNT, HERBIVORES_DEFAULT_AMOUNT
from core.simulation import Simulation


class MainWindow(QMainWindow):
    """
    ui – объект сгенерированного интерфейса.

    simulation – экземпляр Simulation.

    initialise_simulation –
    запрашивает количество существ через диалоги, создаёт симуляцию, подключает сигналы и рендерер.

    setup_connectors – подключает кнопки к методам.

    print_info – обновляет метки статистики (вызывается по сигналу).

    on_start_btn_clicked, on_pause_btn_clicked, on_step_btn_clicked, on_reset_btn_clicked –
    обработчики кнопок.
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.simulation = None
        self.setup_connectors()
        self.initialise_simulation()
        self.ui.statusValueLabel.setText("Готов к работе")

    def initialise_simulation(self):
        predators_amount, ok1 = QInputDialog.getInt(
            self,
            "Количество хищников",
            "Сколько хищников разместить?",
            PREDATORS_DEFAULT_AMOUNT,
        )
        if ok1:
            herbivores_amount, ok2 = QInputDialog.getInt(
                self,
                "Количество травоядных",
                "Сколько травоядных разместить?",
                HERBIVORES_DEFAULT_AMOUNT,
            )
            if ok2:
                if 0 <= predators_amount and 0 <= herbivores_amount:
                    self.simulation = Simulation(predators_amount, herbivores_amount)
                    self.simulation.data_changed.connect(self.print_info)
                    self.simulation.set_map_view(self.ui.mapView)
                    return
        QMessageBox.information(
            self,
            "Ошибка",
            "Вы ввели не валидные значения для существ,\n"
            "Приложение выбирает значение по умолчанию:\n"
            f"Травоядных: {HERBIVORES_DEFAULT_AMOUNT}\n"
            f"Хищников: {PREDATORS_DEFAULT_AMOUNT}",
        )
        self.simulation = Simulation(
            PREDATORS_DEFAULT_AMOUNT, HERBIVORES_DEFAULT_AMOUNT
        )
        self.simulation.data_changed.connect(self.print_info)
        self.simulation.set_map_view(self.ui.mapView)
        return

    def setup_connectors(self):
        self.ui.startButton.clicked.connect(self.on_start_btn_clicked)
        self.ui.pauseButton.clicked.connect(self.on_pause_btn_clicked)
        self.ui.stepButton.clicked.connect(self.on_step_btn_clicked)
        self.ui.resetButton.clicked.connect(self.on_reset_btn_clicked)

    def on_start_btn_clicked(self):
        self.ui.statusValueLabel.setText("Выполняется симуляция...")
        self.simulation.start_simulation()

    def on_pause_btn_clicked(self):
        self.ui.statusValueLabel.setText("Пауза")
        self.simulation.pause_simulation()

    def on_step_btn_clicked(self):
        self.simulation.next_turn()

    def on_reset_btn_clicked(self):
        self.ui.statusValueLabel.setText("Готов к работе")
        self.simulation.reset_simulation()

    def print_info(self):
        self.ui.stepValueLabel.setText(str(self.simulation.game_counter))
        self.ui.sizeValueLabel.setText(
            f"{self.simulation.width} x {self.simulation.height}"
        )
        self.ui.herbivoresValueLabel.setText(str(self.simulation.herbivores_amount))
        self.ui.predatorsValueLabel.setText(str(self.simulation.predators_amount))
        self.ui.grassValueLabel.setText(str(self.simulation.grasses_amount))
        if not self.simulation.is_running:
            self.ui.statusValueLabel.setText("Симуляция окончена")
