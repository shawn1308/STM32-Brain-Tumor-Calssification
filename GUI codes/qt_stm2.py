import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "main.qml")
    engine.load(QUrl.fromLocalFile(filename))

    sys.exit(app.exec_())