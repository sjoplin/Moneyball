from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel

from scraper import singleurlscrape


def main():
    launch()


def launch():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()

    teamName = QLineEdit()
    teamName.setText('Georgia Tech')
    layout.addWidget(QLabel('Team Name from Website'))
    layout.addWidget(teamName)
    layout.addWidget(QLabel('Team HomePage'))

    newField = QLineEdit()
    newField.setText('Team URL')
    button = (newField)
    layout.addWidget(newField)
    newField2 = QLineEdit()
    newField2.setText('Previous Season URL')
    button2 = (newField2)
    layout.addWidget(newField2)
    submit = QPushButton('Submit')
    submit.clicked.connect(lambda: execute(teamName, button, button2))
    layout.addWidget(submit)
    window.setLayout(layout)
    window.show()

    app.exec_()


def execute(teamButton, button, previousSeason):
    desiredTeam = teamButton.text()
    url = button.text()
    url2 = previousSeason.text()
    singleurlscrape(desiredTeam, url, url2)


if __name__ == "__main__":
    main()
