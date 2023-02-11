from PyQt6.QtWidgets import QPushButton

class NumberButton(QPushButton):
    def __init__(self, name, val, label):
        super().__init__(name)

        self.val = val
        self.label = label

        self.setFixedSize(90, 90)
        self.setStyleSheet("""
                            QPushButton {
                                background-color: rgba(0, 0, 0, 0.3);
                                font-family: 'Lucida Console', Monaco, monospace;
                                font-size: 30px;
                                font-weight: bold;
                                border-style: solid;
                                border-width: 2px;
                                border-color: #FFFFFF;
                                border-radius: 45%;
                                text-align: center;
                                color: white;
                            
                            }          
                        
                            """)


