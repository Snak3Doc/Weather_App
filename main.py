# main.py
### Imports ###
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QHBoxLayout, QLabel,
                             QPushButton, QLineEdit, QGroupBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import PyQt6.QtWidgets

from rich import print
from rich.traceback import install
install(show_locals=True)

from tools import get_weather, get_local_time, get_celsius, get_icon

### Varaibles ###

### Main Win Class ###
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.event_handlers()

    def setup_ui(self):
        ### Window Setup ###
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 300, 260)

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
        self.btn_search.clicked.connect(self.update_ui)

    def update_ui(self):
        if self.txt_search.text() != "":
            try:
                # Get Weather & Location Data
                city_name, country_code = self.txt_search.text().split(", ")
                weather_data = get_weather(city_name, country_code)
                local_time, local_date = get_local_time(weather_data["timezone"])
                icon = get_icon(weather_data["weather"][0]["icon"])

                temp = get_celsius(weather_data["main"]["temp"])
                description = weather_data["weather"][0]["description"].title()

                temp_feels = get_celsius(weather_data["main"]["feels_like"])
                temp_max = get_celsius(weather_data["main"]["temp_max"])
                temp_min = get_celsius(weather_data["main"]["temp_min"])
                humidity = weather_data["main"]["humidity"]
                wind = round(weather_data["wind"]["speed"] * 3.6, 2)

                # Update Seach Input
                self.txt_search.clear()
                self.txt_search.setPlaceholderText(f"{city_name}, {country_code}")

                # Update Info 1 Labels
                self.lbl_city.setText(f"City: {city_name}")
                self.lbl_country.setText(f"Country: {country_code}")

                # Update Info 2 Labels
                self.lbl_time.setText(f"Time: {local_time}")
                self.lbl_date.setText(f"Time: {local_date}")

                # Update Weather Info Labels
                self.lbl_icon.setPixmap(icon)
                self.lbl_temp.setText(temp)
                self.lbl_description.setText(description)

                # Update Weather Detail Labels
                self.lbl_feels.setText(f"Feels: {temp_feels}")
                self.lbl_max.setText(f"Max: {temp_max}")
                self.lbl_min.setText(f"Max: {temp_min}")
                self.lbl_humidity.setText(f"Humidity: {humidity}%")
                self.lbl_wind.setText(f"Wind: {wind}km/ph")

            except Exception as error:
                print("An exception occurred:", error)
                self.txt_search.clear()
                self.txt_search.setPlaceholderText("Entry format > Melbourne, AU")
        else:
            self.txt_search.setPlaceholderText("Entry format > Melbourne, AU")
        



### App Execution ###
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Windows")
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
