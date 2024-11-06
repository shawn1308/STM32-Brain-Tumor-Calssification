import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel

app = QApplication(sys.argv)
window = QWidget()

layout1 = QHBoxLayout()
layout1.addWidget(QLabel('This is the first layout.'))
layout1.setContentsMargins(0, 0, 0, 0)
layout1.setSpacing(0)

layout2 = QHBoxLayout()
layout2.addWidget(QLabel('This is the second layout.'))
layout2.setContentsMargins(0, 0, 0, 0)
layout2.setSpacing(0)

layout = QHBoxLayout()
layout.addLayout(layout1, 1)
layout.addLayout(layout2, 3)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())