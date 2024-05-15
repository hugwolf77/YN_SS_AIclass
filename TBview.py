# 2024.03.10 a-1.0 basic
import sys
import os
import sqlite3 as sq
from PySide6 import QtCore
from PySide6.QtCore import QFile, QIODevice 
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QFileDialog
from PySide6 import QtUiTools, QtGui

from PySide6.QtUiTools import QUiLoader

from GUI.DataView import DataViewer, GraphScreen





if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = DataViewer()
    sys.exit(app.exec())
