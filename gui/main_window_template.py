# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_template2.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet(u"\n"
"/* \u041e\u0431\u0449\u0438\u0439 \u0444\u043e\u043d \u043e\u043a\u043d\u0430 \u2014 \u043f\u0435\u0441\u043e\u043a */\n"
"QMainWindow {\n"
"    background-color: #d2b48c;\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0438 \u0432 \u0441\u0442\u0438\u043b\u0435 \u0434\u0435\u0440\u0435\u0432\u0430/\u043a\u043e\u0436\u0438 */\n"
"QPushButton {\n"
"    background-color: #8b5a2b;\n"
"    border: 2px solid #c2a15b;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"    color: #fff0e0;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #a5713c;\n"
"    border-color: #e0b87a;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #6b3e1a;\n"
"}\n"
"\n"
"/* \u041e\u0431\u043b\u0430\u0441\u0442\u044c \u043a\u0430\u0440\u0442\u044b \u2014 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u043f\u0435\u0441\u043e\u043a, \u0440\u0430\u043c\u043a\u0430 \u043f\u043e\u0434 \u0434\u0435\u0440\u0435\u0432\u043e */\n"
"QGraphicsView {\n"
"    background-color"
                        ": #f5e6d3;\n"
"    border: 3px solid #b97f3a;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"/* \u0413\u0440\u0443\u043f\u043f\u044b \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u0438 \u043b\u043e\u0433\u0430 */\n"
"QGroupBox {\n"
"    color: #4e2a1a;\n"
"    border: 2px solid #b97f3a;\n"
"    border-radius: 8px;\n"
"    margin-top: 0.5ex;\n"
"    font-weight: bold;\n"
"    background-color: rgba(210, 180, 140, 0.5);\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 5px;\n"
"    color: #4e2a1a;\n"
"    background-color: #f5e6d3;\n"
"}\n"
"\n"
"/* \u041c\u0435\u0442\u043a\u0438 \u0432\u043d\u0443\u0442\u0440\u0438 \u0433\u0440\u0443\u043f\u043f */\n"
"QLabel {\n"
"    color: #3b2a1f;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u0435 \u043b\u043e\u0433\u0430 */\n"
"QTextEdit {\n"
"    background-color: #4a2e1e;\n"
"    color: #f5e6d3;\n"
"    border: 1px solid #b97f3a;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-"
                        "size: 11px;\n"
"}\n"
"\n"
"/* \u0421\u043b\u0430\u0439\u0434\u0435\u0440 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u0438 */\n"
"QSlider::groove:horizontal {\n"
"    height: 6px;\n"
"    background: #c2a15b;\n"
"    border-radius: 3px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #8b5a2b;\n"
"    width: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #a5713c;\n"
"}\n"
"   ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topLayout = QHBoxLayout()
        self.topLayout.setObjectName(u"topLayout")
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")

        self.topLayout.addWidget(self.startButton)

        self.pauseButton = QPushButton(self.centralwidget)
        self.pauseButton.setObjectName(u"pauseButton")

        self.topLayout.addWidget(self.pauseButton)

        self.stepButton = QPushButton(self.centralwidget)
        self.stepButton.setObjectName(u"stepButton")

        self.topLayout.addWidget(self.stepButton)

        self.resetButton = QPushButton(self.centralwidget)
        self.resetButton.setObjectName(u"resetButton")

        self.topLayout.addWidget(self.resetButton)


        self.verticalLayout.addLayout(self.topLayout)

        self.bottomLayout = QHBoxLayout()
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.infoGroup = QGroupBox(self.centralwidget)
        self.infoGroup.setObjectName(u"infoGroup")
        self.gridLayout = QGridLayout(self.infoGroup)
        self.gridLayout.setObjectName(u"gridLayout")
        self.grassValueLabel = QLabel(self.infoGroup)
        self.grassValueLabel.setObjectName(u"grassValueLabel")

        self.gridLayout.addWidget(self.grassValueLabel, 4, 1, 1, 1)

        self.herbivoresValueLabel = QLabel(self.infoGroup)
        self.herbivoresValueLabel.setObjectName(u"herbivoresValueLabel")

        self.gridLayout.addWidget(self.herbivoresValueLabel, 2, 1, 1, 1)

        self.statusLabel = QLabel(self.infoGroup)
        self.statusLabel.setObjectName(u"statusLabel")

        self.gridLayout.addWidget(self.statusLabel, 5, 0, 1, 1)

        self.predatorsLabel = QLabel(self.infoGroup)
        self.predatorsLabel.setObjectName(u"predatorsLabel")

        self.gridLayout.addWidget(self.predatorsLabel, 3, 0, 1, 1)

        self.predatorsValueLabel = QLabel(self.infoGroup)
        self.predatorsValueLabel.setObjectName(u"predatorsValueLabel")

        self.gridLayout.addWidget(self.predatorsValueLabel, 3, 1, 1, 1)

        self.grassLabel = QLabel(self.infoGroup)
        self.grassLabel.setObjectName(u"grassLabel")

        self.gridLayout.addWidget(self.grassLabel, 4, 0, 1, 1)

        self.stepValueLabel = QLabel(self.infoGroup)
        self.stepValueLabel.setObjectName(u"stepValueLabel")

        self.gridLayout.addWidget(self.stepValueLabel, 0, 1, 1, 1)

        self.statusValueLabel = QLabel(self.infoGroup)
        self.statusValueLabel.setObjectName(u"statusValueLabel")

        self.gridLayout.addWidget(self.statusValueLabel, 5, 1, 1, 1)

        self.stepLabel = QLabel(self.infoGroup)
        self.stepLabel.setObjectName(u"stepLabel")

        self.gridLayout.addWidget(self.stepLabel, 0, 0, 1, 1)

        self.herbivoresLabel = QLabel(self.infoGroup)
        self.herbivoresLabel.setObjectName(u"herbivoresLabel")

        self.gridLayout.addWidget(self.herbivoresLabel, 2, 0, 1, 1)

        self.sizeValueLabel = QLabel(self.infoGroup)
        self.sizeValueLabel.setObjectName(u"sizeValueLabel")

        self.gridLayout.addWidget(self.sizeValueLabel, 1, 1, 1, 1)

        self.sizeLabel = QLabel(self.infoGroup)
        self.sizeLabel.setObjectName(u"sizeLabel")

        self.gridLayout.addWidget(self.sizeLabel, 1, 0, 1, 1)


        self.bottomLayout.addWidget(self.infoGroup)

        self.logGroup = QGroupBox(self.centralwidget)
        self.logGroup.setObjectName(u"logGroup")
        self.verticalLayout_2 = QVBoxLayout(self.logGroup)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mapView = QGraphicsView(self.logGroup)
        self.mapView.setObjectName(u"mapView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.mapView.sizePolicy().hasHeightForWidth())
        self.mapView.setSizePolicy(sizePolicy)
        self.mapView.setMinimumSize(QSize(500, 500))

        self.verticalLayout_2.addWidget(self.mapView)


        self.bottomLayout.addWidget(self.logGroup)


        self.verticalLayout.addLayout(self.bottomLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0444\u0440\u0438\u043a\u0430\u043d\u0441\u043a\u0430\u044f \u0441\u0430\u0432\u0430\u043d\u043d\u0430 \u2014 \u0441\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u044f", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"\U0001f981 \U00000421\U00000442\U00000430\U00000440\U00000442", None))
        self.pauseButton.setText(QCoreApplication.translate("MainWindow", u"\u23f8 \u041f\u0430\u0443\u0437\u0430", None))
        self.stepButton.setText(QCoreApplication.translate("MainWindow", u"\u27a1 \u0428\u0430\u0433", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"\U0001f504 \U00000421\U00000431\U00000440\U0000043e\U00000441", None))
        self.infoGroup.setTitle(QCoreApplication.translate("MainWindow", u"\U0001f4ca \U00000418\U0000043d\U00000444\U0000043e\U00000440\U0000043c\U00000430\U00000446\U00000438\U0000044f \U0000043e \U00000441\U00000430\U00000432\U00000430\U0000043d\U0000043d\U00000435      ", None))
        self.grassValueLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.herbivoresValueLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"\U0001f4cc \U00000421\U00000442\U00000430\U00000442\U00000443\U00000441:", None))
        self.predatorsLabel.setText(QCoreApplication.translate("MainWindow", u"\U0001f981 \U00000425\U00000438\U00000449\U0000043d\U00000438\U0000043a\U00000438:", None))
        self.predatorsValueLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.grassLabel.setText(QCoreApplication.translate("MainWindow", u"\U0001f33f \U00000422\U00000440\U00000430\U00000432\U00000430:", None))
        self.stepValueLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.statusValueLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0443\u0437\u0430", None))
        self.stepLabel.setText(QCoreApplication.translate("MainWindow", u"\u23f1 \u0428\u0430\u0433:", None))
        self.herbivoresLabel.setText(QCoreApplication.translate("MainWindow", u"\U0001f992 \U00000422\U00000440\U00000430\U00000432\U0000043e\U0000044f\U00000434\U0000043d\U0000044b\U00000435:", None))
        self.sizeValueLabel.setText(QCoreApplication.translate("MainWindow", u"0 x 0", None))
        self.sizeLabel.setText(QCoreApplication.translate("MainWindow", u"\U0001f5fa \U00000420\U00000430\U00000437\U0000043c\U00000435\U00000440\U0000044b:", None))
        self.logGroup.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u0442\u0430 \u0441\u0430\u0432\u0430\u043d\u043d\u044b", None))
    # retranslateUi

