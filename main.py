# main.py
### Imports ###
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QHBoxLayout, QLabel,
                             QPushButton, QLineEdit, QGroupBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from rich import print
from rich.traceback import install
install(show_locals=True)
from rich.console import Console
console = Console()

from tools import get_weather, get_forecast, get_local_time, get_celsius, get_icon, validate_string_format

### Varaibles ###
h1_font = QFont("Exo 2", 30)
h2_font = QFont("Exo 2", 12)
h3_font = QFont("Exo 2", 8)


### Main Win Class ###
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.event_handlers()

    def setup_ui(self):
        ### Window Setup ###
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 400, 260)

        ### UI Setup ###
        ## Search UI
        # Widgets
        self.txt_search = QLineEdit(self, placeholderText="eg Hanoi, VN")
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
        lyt_main_info_1.addWidget(self.lbl_city, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_main_info_1.addWidget(self.lbl_country, alignment=Qt.AlignmentFlag.AlignCenter)

        ## Info 2 UI
        # Widgets
        self.lbl_time = QLabel("Time:", self)
        self.lbl_date = QLabel("Date:", self)

        # Layouts
        lyt_main_info_2 = QHBoxLayout()

        # Setup
        lyt_main_info_2.addWidget(self.lbl_time, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_main_info_2.addWidget(self.lbl_date, alignment=Qt.AlignmentFlag.AlignCenter)

        ## Weather UI
        # Widgets
        self.grpb_weather = QGroupBox("Weather", self)

        self.lbl_weather_icon = QLabel("'Icon'", self)
        self.lbl_weather_temp = QLabel("'Temp'", self, font=h1_font)
        self.lbl_weather_description = QLabel("'Description'", self)

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
        lyt_weather_info.addWidget(self.lbl_weather_icon, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_weather_info.addWidget(self.lbl_weather_temp, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_weather_info.addWidget(self.lbl_weather_description, alignment=Qt.AlignmentFlag.AlignCenter)

        lyt_weather_detail.addWidget(self.lbl_feels, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_weather_detail.addWidget(self.lbl_max, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_weather_detail.addWidget(self.lbl_min, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_weather_detail.addWidget(self.lbl_humidity, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_weather_detail.addWidget(self.lbl_wind, alignment=Qt.AlignmentFlag.AlignCenter)

        lyt_weather_main.addLayout(lyt_weather_info)
        lyt_weather_main.addLayout(lyt_weather_detail)

        self.grpb_weather.setLayout(lyt_weather_main)

        lyt_main_weather.addWidget(self.grpb_weather)


        ## Forcast UI
        # Widgets
        self.grpb_forcast = QGroupBox("Forcast", self)

        self.lbl_forecast_icon_1 = QLabel("'icon'", self)
        self.lbl_forecast_temp_1 = QLabel("'temp'", self)
        self.lbl_forecast_description_1 = QLabel("'description'", self, font=h3_font)

        self.lbl_forecast_icon_2 = QLabel("'icon'", self)
        self.lbl_forecast_temp_2 = QLabel("'temp'", self)
        self.lbl_forecast_description_2 = QLabel("'description'", self, font=h3_font)

        self.lbl_forecast_icon_3 = QLabel("'icon'", self)
        self.lbl_forecast_temp_3 = QLabel("'temp'", self)
        self.lbl_forecast_description_3 = QLabel("'description'", self, font=h3_font)

        self.lbl_forecast_icon_4 = QLabel("'icon'", self)
        self.lbl_forecast_temp_4 = QLabel("'temp'", self)
        self.lbl_forecast_description_4 = QLabel("'description'", self, font=h3_font)

        self.lbl_forecast_icon_5 = QLabel("'icon'", self)
        self.lbl_forecast_temp_5 = QLabel("'temp'", self)
        self.lbl_forecast_description_5 = QLabel("'description'", self, font=h3_font)

        # Layouts
        lyt_main_forecast = QHBoxLayout()
        lyt_forecast_main = QHBoxLayout()

        lyt_forecast_info_1 = QVBoxLayout()
        lyt_forecast_info_2 = QVBoxLayout()
        lyt_forecast_info_3 = QVBoxLayout()
        lyt_forecast_info_4 = QVBoxLayout()
        lyt_forecast_info_5 = QVBoxLayout()

        # Setup
        lyt_forecast_info_1.addWidget(self.lbl_forecast_icon_1, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_forecast_info_1.addWidget(self.lbl_forecast_temp_1, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_forecast_info_1.addWidget(self.lbl_forecast_description_1, alignment=Qt.AlignmentFlag.AlignCenter)

        lyt_forecast_info_2.addWidget(self.lbl_forecast_icon_2, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_forecast_info_2.addWidget(self.lbl_forecast_temp_2, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_forecast_info_2.addWidget(self.lbl_forecast_description_2, alignment=Qt.AlignmentFlag.AlignCenter)

        lyt_forecast_info_3.addWidget(self.lbl_forecast_icon_3, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_forecast_info_3.addWidget(self.lbl_forecast_temp_3, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_forecast_info_3.addWidget(self.lbl_forecast_description_3, alignment=Qt.AlignmentFlag.AlignCenter)

        lyt_forecast_info_4.addWidget(self.lbl_forecast_icon_4, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_forecast_info_4.addWidget(self.lbl_forecast_temp_4, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_forecast_info_4.addWidget(self.lbl_forecast_description_4, alignment=Qt.AlignmentFlag.AlignCenter)

        lyt_forecast_info_5.addWidget(self.lbl_forecast_icon_5, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_forecast_info_5.addWidget(self.lbl_forecast_temp_5, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_forecast_info_5.addWidget(self.lbl_forecast_description_5, alignment=Qt.AlignmentFlag.AlignCenter)

        lyt_forecast_main.addLayout(lyt_forecast_info_1)
        lyt_forecast_main.addLayout(lyt_forecast_info_2)
        lyt_forecast_main.addLayout(lyt_forecast_info_3)
        lyt_forecast_main.addLayout(lyt_forecast_info_4)
        lyt_forecast_main.addLayout(lyt_forecast_info_5)

        self.grpb_forcast.setLayout(lyt_forecast_main)

        lyt_main_forecast.addWidget(self.grpb_forcast)

        self.forecast_lbls = [
                            [self.lbl_forecast_icon_1, self.lbl_forecast_temp_1, self.lbl_forecast_description_1],
                            [self.lbl_forecast_icon_2, self.lbl_forecast_temp_2, self.lbl_forecast_description_2],
                            [self.lbl_forecast_icon_3, self.lbl_forecast_temp_3, self.lbl_forecast_description_3],
                            [self.lbl_forecast_icon_4, self.lbl_forecast_temp_4, self.lbl_forecast_description_4],
                            [self.lbl_forecast_icon_5, self.lbl_forecast_temp_5, self.lbl_forecast_description_5]
                            ]
        

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
        lyt_main.addLayout(lyt_main_forecast)

        central_widget.setLayout(lyt_main)
        self.setCentralWidget(central_widget)


    def event_handlers(self):
        self.btn_search.clicked.connect(self.update_ui)


    def update_ui(self):
        if validate_string_format(self.txt_search.text()):
            try:
                # Get Weather & Location Data
                city_name, country_code = self.txt_search.text().split(", ")
                weather_data = get_weather(city_name, country_code)
                forecast_data = get_forecast(city_name, country_code)
                if isinstance(weather_data, dict):
                    # Extract Data from weather_data
                    local_time, local_date = get_local_time(weather_data["timezone"])
                    weather_icon = get_icon(weather_data["weather"][0]["icon"]).scaled(75, 50)

                    weather_temp = get_celsius(weather_data["main"]["temp"])
                    weather_description = weather_data["weather"][0]["description"].title()

                    weather_temp_feels = get_celsius(weather_data["main"]["feels_like"])
                    weather_temp_max = get_celsius(weather_data["main"]["temp_max"])
                    weather_temp_min = get_celsius(weather_data["main"]["temp_min"])
                    weather_humidity = weather_data["main"]["humidity"]
                    weather_wind = int(round(weather_data["wind"]["speed"] * 3.6, 0))

                    # Update Seach Input
                    self.txt_search.clear()
                    self.txt_search.setPlaceholderText(f"{city_name}, {country_code}")

                    # Update Info 1 Labels
                    self.lbl_city.setText(f"City {city_name}")
                    self.lbl_country.setText(f"Country {country_code}")

                    # Update Info 2 Labels
                    self.lbl_time.setText(f"Time {local_time}")
                    self.lbl_date.setText(f"Date {local_date}")

                    # Update Weather Info Labels
                    self.lbl_weather_icon.setPixmap(weather_icon)
                    #!self.lbl_weather_temp.setFont(h1_font)
                    self.lbl_weather_temp.setText(weather_temp)
                    self.lbl_weather_description.setText(weather_description)

                    # Update Weather Detail Labels
                    self.lbl_feels.setText(f"Feels {weather_temp_feels}")
                    self.lbl_max.setText(f"Max {weather_temp_max}")
                    self.lbl_min.setText(f"Max {weather_temp_min}")
                    self.lbl_humidity.setText(f"Humidity {weather_humidity}%")
                    self.lbl_wind.setText(f"Wind {weather_wind}km/ph")

                if isinstance(forecast_data, dict):
                    for data, lbls in zip(forecast_data["list"][0::8], self.forecast_lbls):
                        forecast_icon = get_icon(data["weather"][0]["icon"])
                        forecast_temp = get_celsius(data["main"]["temp"])
                        forecast_description = data["weather"][0]["description"].title()

                        lbls[0].setPixmap(forecast_icon)
                        lbls[1].setText(forecast_temp)
                        #!lbls[2].setFont(h3_font)
                        lbls[2].setText(forecast_description)

                else:
                    self.txt_search.clear()
                    self.txt_search.setPlaceholderText(f"{weather_data}. Check format > Hanoi, VN")

            except:
                console.print_exception()
                self.txt_search.clear()
                self.txt_search.setPlaceholderText("Check format > Hanoi, VN")
        else:
            self.txt_search.clear()
            self.txt_search.setPlaceholderText("Check format > Hanoi, VN")
        

### App Execution ###
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(h2_font)
    app.setStyle("Windows")
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
