# main.py
### Imports ###
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QHBoxLayout, QLabel,
                             QPushButton, QLineEdit, QGroupBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import (QIcon)
import PyQt6.QtWidgets

from rich import print
from rich.traceback import install
install(show_locals=True)

import tools

### Varaibles ###

### Main Win Class ###
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.event_handlers()
        self.update_ui()

    def setup_ui(self):
        ### Window Setup ###
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 300, 500)

        ### UI Setup ###
        ## Search UI
        # Widgets
        self.txt_search = QLineEdit(self, placeholderText="eg Melbourne, AU")
        self.btn_search = QPushButton("Search", self)

        # Layouts
        lyt_main_search = QHBoxLayout()

        # Setup
        lyt_main_search.addWidget(self.txt_search)
        lyt_main_search.addWidget(self.btn_search)

        ## Info 1 UI
        # Widgets
        self.lbl_city = QLabel("City:", self)
        self.lbl_country = QLabel("Country:", self)

        # Layouts
        lyt_main_info_1 = QHBoxLayout()

        # Setup
        lyt_main_info_1.addWidget(self.lbl_city)
        lyt_main_info_1.addWidget(self.lbl_country)

        ## Info 2 UI
        # Widgets
        self.lbl_time = QLabel("Time:", self)
        self.lbl_date = QLabel("Date:", self)

        # Layouts
        lyt_main_info_2 = QHBoxLayout()

        # Setup
        lyt_main_info_2.addWidget(self.lbl_time)
        lyt_main_info_2.addWidget(self.lbl_date)

        ## Weather UI
        # Widgets
        self.grpb_weather = QGroupBox("Weather", self)

        self.lbl_icon = QLabel("'Icon'", self)
        self.lbl_temp = QLabel("'Temp'", self)
        self.lbl_description = QLabel("'Description'", self)

        self.lbl_feels = QLabel("Feels:", self)
        self.lbl_max = QLabel("Max:", self)
        self.lbl_min = QLabel("Min:", self)
        self.lbl_humidity = QLabel("Humidity:", self)
        self.lbl_wind = QLabel("Wind:", self)

        # Layouts
        lyt_main_weather = QHBoxLayout()
        lyt_weather_main = QHBoxLayout()
        lyt_weather_info = QVBoxLayout()
        lyt_weather_detail = QVBoxLayout()
        
        # Setup
        lyt_weather_info.addWidget(self.lbl_icon)
        lyt_weather_info.addWidget(self.lbl_temp)
        lyt_weather_info.addWidget(self.lbl_description)

        lyt_weather_detail.addWidget(self.lbl_feels)
        lyt_weather_detail.addWidget(self.lbl_max)
        lyt_weather_detail.addWidget(self.lbl_min)
        lyt_weather_detail.addWidget(self.lbl_humidity)
        lyt_weather_detail.addWidget(self.lbl_wind)

        lyt_weather_main.addLayout(lyt_weather_info)
        lyt_weather_main.addLayout(lyt_weather_detail)

        self.grpb_weather.setLayout(lyt_weather_main)

        lyt_main_weather.addWidget(self.grpb_weather)



        ## Forcast UI
        # Widgets
        # Layouts
        # Setup

        ## Main Win Layout
        # Widgets
        central_widget = QWidget()

        # Layouts
        lyt_main = QVBoxLayout()

        # Setup
        lyt_main.addLayout(lyt_main_search)
        lyt_main.addLayout(lyt_main_info_1)
        lyt_main.addLayout(lyt_main_info_2)
        lyt_main.addLayout(lyt_main_weather)
        #TODO: Add Forcast Layout

        central_widget.setLayout(lyt_main)
        self.setCentralWidget(central_widget)


    def event_handlers(self):
        pass

    def update_ui(self):
        pass



### App Execution ###
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Windows")
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
