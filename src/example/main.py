import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QLineEdit, QMainWindow, QPushButton

from example.components.parsers import ASTParser
from example.components.lexica import MyLexer
from example.components.ui import Ui_MainWindow


class MainWindow(QMainWindow):
    button_true: QPushButton
    button_false: QPushButton
    button_and: QPushButton
    button_or: QPushButton
    button_not: QPushButton
    button_lparen: QPushButton
    button_rparen: QPushButton
    button_equal: QPushButton
    input_text: QLineEdit
    result_text: QLineEdit
    prefix_text: QLineEdit

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button_true.clicked.connect(lambda: self.push("T"))
        self.ui.button_false.clicked.connect(lambda: self.push("F"))
        self.ui.button_and.clicked.connect(lambda: self.push(" AND "))
        self.ui.button_or.clicked.connect(lambda: self.push(" OR "))
        self.ui.button_not.clicked.connect(lambda: self.push("NOT "))
        self.ui.button_lparen.clicked.connect(lambda: self.push("("))
        self.ui.button_rparen.clicked.connect(lambda: self.push(")"))
        self.ui.button_equal.clicked.connect(self.push_equal)

    def push(self, text: str):
        current_text: str = self.ui.input_text.text()
        self.ui.input_text.setText(f"{current_text}{text}")

    def push_equal(self):
        lexer = MyLexer()
        parser = ASTParser()
        input_text = self.ui.input_text.text()
        tree = parser.parse(lexer.tokenize(input_text))
        if tree is None:
            self.ui.result_text.setText("ERROR")
            self.ui.prefix_text.setText("Invalid expression")
            return

        result = tree.evaluate()
        self.ui.result_text.setText(result.display_value())
        self.ui.prefix_text.setText(result.prefix)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
