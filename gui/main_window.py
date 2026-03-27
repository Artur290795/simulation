from PySide6.QtWidgets import QLabel, QMainWindow

from gui.main_window_template import Ui_MainWindow
from core.simulation import Simulation


class MainWindow(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.simulation = Simulation(width, height)
        self.simulation.set_map_view(self.ui.mapView)
        self.setup_ui(width, height)

    def setup_ui(self, width, height):
        self.size_label = QLabel(f"{width} x {height}")
        layout = self.ui.infoGroup.layout()
        row = layout.rowCount()
        layout.addWidget(QLabel("Размеры:"), row, 0)
        layout.addWidget(self.size_label, row, 1)

        self.setup_connectors()

    def setup_connectors(self):
        self.ui.startButton.clicked.connect(self.on_start_btn_clicked)
        self.ui.pauseButton.clicked.connect(self.on_pause_btn_clicked)
        self.ui.stepButton.clicked.connect(self.on_step_btn_clicked)
        self.ui.resetButton.clicked.connect(self.on_reset_btn_clicked)

    def on_start_btn_clicked(self):
        self.simulation.start_actions()
        self.print_info()

    def on_pause_btn_clicked(self):
        self.simulation.pause_actions()

    def on_step_btn_clicked(self):
        self.simulation.turn_actions()
        self.print_info()
        

    def on_reset_btn_clicked(self):
        self.simulation.reset_actions()

    def print_info(self):
        self.ui.stepValueLabel.setText(str(self.simulation.game_counter))
        self.ui.sizeValueLabel.setText(
            f"{self.simulation.width} x {self.simulation.height}"
        )
        self.ui.herbivoresValueLabel.setText(str(self.simulation.herbivores_amount))
        self.ui.predatorsValueLabel.setText(str(self.simulation.predators_amount))
        self.ui.grassValueLabel.setText(str(self.simulation.grasses_amount))
