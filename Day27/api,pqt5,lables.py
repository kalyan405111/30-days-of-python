# import requests

# base_url = "https://pokeapi.co/api/v2/"

# def get_pokemon_info(name):
    # url = f"{base_url}pokemon/{name}"
    # response = requests.get(url)
# 
    # if response.status_code == 200:
        # pokemon_data = response.json()
        # return pokemon_data
    # else:
        # print(f"Failed to retrieve data {response.status_code}")
# 
# pokemon_name = "charizard"
# pokemon_info = get_pokemon_info(pokemon_name)

# if pokemon_info:
    # print(f"Name: {pokemon_info['name'].capitalize()}")
    # print(f"Id: {pokemon_info['id']}")
    # print(f"Height: {pokemon_info['height']}")
    # print(f"Weight: {pokemon_info['weight']}")

###########################################################
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtGui import QIcon

# class MainWindow(QMainWindow):
    # def __init__(self):
        # super().__init__()
        # self.setWindowTitle("My cool first GUI")
        # self.setGeometry(700, 300, 500, 500)
        # self.setWindowIcon(QIcon("kaki.png"))

# def main():
    # app = QApplication(sys.argv)
    # window = MainWindow()
    # window.show()
    # sys.exit(app.exec_())
# 
# if __name__ == "__main__":
    # main()

##################################################################
# PyQt5 QLabels
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #292929;"
                                           "background-color: #6fdcf7;"
                                           "font-weight: bold;"
                                           "font-style: italic;"
                                           "text-decoration: underline;")

        label.setAlignment(Qt.AlignTop)  # VERTICALLY TOP
        # label.setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM
        label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER

        # label.setAlignment(Qt.AlignRight)  # HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignHCenter)  # HORIZONTALLY CENTER
        label.setAlignment(Qt.AlignLeft)  # HORIZONTALLY LEFT

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # CENTER & CENTER
        # label.setAlignment(Qt.AlignCenter)  # CENTER & CENTER

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()