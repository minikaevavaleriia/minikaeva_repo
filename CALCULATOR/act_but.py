from PyQt6.QtWidgets import QPushButton


class ActionButton(QPushButton):
    def __init__(self, name, val, label):
        super().__init__(name)

        self.val = val
        self.label = label
