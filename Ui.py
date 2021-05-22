import PyQt5.QtCore as qc
import PyQt5.QtWidgets as qw

from game import Game

class UI(qw.QWidget):
    objectCount = 1
    gravitation_modifier = 1
    timeInterval = 100
    windowWidth = 500
    windowHeight = 500

    widthSlider = None
    heightSlider = None
    game = None
    gridLayout = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.initUiElements()
        self.default()

    def default(self):
        self.objectCount = 3
        self.gravitation_modifier = 1
        self.timeInterval = 100
        self.windowWidth = 500
        self.windowHeight = 500

        self.widthSlider.setValue(self.windowWidth)
        self.heightSlider.setValue(self.windowHeight)
        self.objectCountSlider.setValue(self.objectCount)

    def initUiElements(self):
        widthSlider = qw.QSlider(qc.Qt.Horizontal)
        widthSlider.setMinimum(100)
        widthSlider.setMaximum(1000)
        widthSlider.valueChanged.connect(self.setWindowWidth)
        widthSlider.setToolTip("Set horizontal size")
        self.widthSlider = widthSlider

        heightSlider = qw.QSlider(qc.Qt.Horizontal)
        heightSlider.setMinimum(100)
        heightSlider.setMaximum(1000)
        heightSlider.valueChanged.connect(self.setWindowHeight)
        heightSlider.setToolTip("Set vertical size")
        self.heightSlider = heightSlider

        objectCountSlider = qw.QSlider(qc.Qt.Horizontal)
        objectCountSlider.setMinimum(1)
        objectCountSlider.setMaximum(5)
        objectCountSlider.valueChanged.connect(self.setObjectCount)
        objectCountSlider.setToolTip("Set number of objects")
        self.objectCountSlider = objectCountSlider

        self.startGameButton = qw.QPushButton("Start")
        self.startGameButton.setToolTip("Start the game")
        self.startGameButton.clicked.connect(self.startGame)

        self.resetButton = qw.QPushButton("Reset settings")
        self.resetButton.clicked.connect(self.default)

        self.gridLayout = qw.QGridLayout(self)

        row = 0
        def addToLayout(name, element):
            nonlocal row
            self.gridLayout.addWidget(qw.QLabel(name), row, 0)
            self.gridLayout.addWidget(element, row, 1)
            self.gridLayout.addWidget(qw.QLabel(), row, 2)
            row += 1

        addToLayout("Width", widthSlider)
        addToLayout("Height", heightSlider)
        addToLayout("Anzahl Objekte", objectCountSlider)

        self.gridLayout.addWidget(self.startGameButton, row, 0, 1, 3)
        self.gridLayout.addWidget(self.resetButton, row + 1, 0, 1, 3)

    def updateValueText(self, slider, postfix=""):
        index = self.gridLayout.indexOf(slider)
        label = self.gridLayout.itemAt(index + 1).widget()
        label.setText(str(slider.value()) + postfix)

    def setWindowWidth(self, value):
        self.windowWidth = value
        self.updateValueText(self.widthSlider, "px")

    def setWindowHeight(self, value):
        self.windowHeight = value
        self.updateValueText(self.heightSlider, "px")

    def setObjectCount(self, value):
        self.objectCount = value
        self.updateValueText(self.objectCountSlider, " Objekt/e")

    def startGame(self):
        self.game = Game(self, self.objectCountSlider)
        self.game.show()
        self.game.closeEvent = self.gameClosed
        self.hide()

    def gameClosed(self, _):
        self.game.timer.stop()
        self.show()

