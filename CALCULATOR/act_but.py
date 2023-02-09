from PyQt6.QtWidgets import QPushButton


class ActionButton(QPushButton):
    def __init__(self, name, val, label):
        super().__init__(name)

        self.val = val
        self.label = label

        self.setFixedSize(90, 90)
        self.setStyleSheet("""
                            QPushButton {
                                background-color: rgba(255, 0, 0, 0.4);
                                font-family: 'Lucida Console', Monaco, monospace;
                                font-size: 30px;
                                font-weight: bold;
                                padding: 16px;
                                border-radius: 45%;
                                text-align: center;
                            }

                            """)