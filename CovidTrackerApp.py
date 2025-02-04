import sys 
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class CovidTrackerApp(QWidget):   #This might be done and completed will know as the coding goes on.
    def __init__(self):
        super().__init__()
        self.country_label = QLabel("Enter Country Name: ", self)
        self.country_input = QLineEdit(self)
        self.get_data_button = QPushButton("🦠 Get Data 🦠", self)
        self.get_data_button.clicked.connect(self.fetch_data)
        self.results_label = QLabel(self)
        self.initUI()

    def initUI(self):
    #This is where I start designing the main window title and dimensions.
        self.setWindowTitle("Covid-19 Tracker App")
        self.setGeometry(100, 100, 400, 300)

        vbox = QVBoxLayout()

        vbox.addWidget(self.country_label)
        vbox.addWidget(self.country_input)
        vbox.addWidget(self.get_data_button)
        vbox.addWidget(self.results_label)

        self.setLayout(vbox)

        self.country_label.setAlignment(Qt.AlignCenter)
        self.country_input.setAlignment(Qt.AlignCenter)
        self.results_label.setAlignment(Qt.AlignCenter)

        self.country_label.setObjectName("country_label")
        self.country_input.setObjectName("country_input")
        self.get_data_button.setObjectName("get_data_button")
        self.results_label.setObjectName("results_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#country_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#country_input{
                font-size: 40px;
            }
            QPushButton#get_data_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#results_label{
                font-size: 50px;          
            }
        """)

    def fetch_data(self):
        country = self.country_input.text()
        url = "https://disease.sh/v3/covid-19/countries"

        if not country:
            self.results_label.setText("Please enter a valid country name.")
            return
        
        try:
            response = requests.get(f"{url}/{country}")
            response.raise_for_status()
            data = response.json()

            self.results_label.setText(
                f"COVID-19 Stats for {data['country']}:\n"
                f"Total Cases: {data['cases']:,}\n"
                f"Deaths: {data['deaths']:,}\n"
                f"Recovered: {data['recovered']:,}\n"
                f"Active Cases: {data['active']:,}"
            )
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvlaid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not Found:\nCountry not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Server Unavaliable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occured:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")
    
    def display_error(self, message):
        self.results_label.setStyleSheet("font-size: 30px;")
        self.results_label.setText(message)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CovidTrackerApp()
    window.show()
    sys.exit(app.exec_())