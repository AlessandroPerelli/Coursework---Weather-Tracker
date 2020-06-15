# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from mplwidget import MplWidget
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import itertools
import requests
import graph_plotting


def weather(low_weather_list, high_weather_list, day_list):

    # removes degrees symbol from each item
    low_weather_list = [sub[:-1] for sub in low_weather_list]
    high_weather_list = [sub[:-1] for sub in high_weather_list]

    # converts all items in list to integers
    low_weather_list = [int(x) for x in low_weather_list]
    high_weather_list = [int(x) for x in high_weather_list]

    low_weather_y = [
        low_weather_list[0],
        low_weather_list[1],
        low_weather_list[2],
        low_weather_list[3],
        low_weather_list[4],
        low_weather_list[5],
        low_weather_list[6],
    ]

    high_weather_y = [
        high_weather_list[0],
        high_weather_list[1],
        high_weather_list[2],
        high_weather_list[3],
        high_weather_list[4],
        high_weather_list[5],
        high_weather_list[6],
    ]

    day_list_x = [
        "Today",
        day_list[1],
        day_list[2],
        day_list[3],
        day_list[4],
        day_list[5],
        day_list[6],
    ]

    print(high_weather_y)
    print(low_weather_y)
    print(day_list_x)

    """     plt.plot(day_list_x, high_weather_y, label="Highest Temperature")
    plt.plot(day_list_x, low_weather_y, label="Lowest Temperature")
    plt.xlabel("Day")
    plt.ylabel("Temperature")
    plt.title("Temperatures for next seven days")
    plt.legend() """

    return low_weather_y, high_weather_y, day_list_x


def bbc():
    temperature_list_unsorted = []
    temperature_list = []
    temperature_feel_list = []
    time_list_front = []
    change_of_rain_list_unseperated = []
    change_of_rain_list = []
    high_and_low_temp_list = []
    high_temp_list = []
    low_temp_list = []
    time_list_not_complete = []
    time_list = []
    final_time_list = []

    postcode = input("Enter your postcode")

    URL = "https://www.bbc.co.uk/weather/{}".format(postcode.lower())
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    weather_results_cm23 = soup.find(class_="wr-time-slot-container__slots")

    day_weather_results = soup.find(
        class_="wr-day-carousel__viewport wr-js-day-carousel-scroll"
    )

    for i in weather_results_cm23:
        temperatures = i.find_all("span", class_="wr-value--temperature--c")

    for i in weather_results_cm23:
        front_time = i.find_all(
            "span", class_="wr-time-slot-primary__hours wr-u-font-weight-500"
        )

    for i in weather_results_cm23:
        chance_of_rain_unseperated = i.find_all("div", class_="wr-u-font-weight-500")

    for i in day_weather_results:
        high_and_low_temp = i.find_all("span", class_="wr-value--temperature--c")

    for i in day_weather_results:
        days = i.find_all("div", class_=("wr-day__title wr-js-day-content-title"))

    for i in temperatures:
        temperature_list_unsorted.extend([i.text])

    for i in temperature_list_unsorted[::2]:
        temperature_list.append(i)

    for i in temperature_list_unsorted[1::2]:
        temperature_feel_list.append(i)

    for i in front_time:
        time_list_front.append([i.text])

    for i in chance_of_rain_unseperated:
        change_of_rain_list_unseperated.append([i.text])

    for i in change_of_rain_list_unseperated:
        for x in i:
            change_of_rain_list.append(str(x).replace("chance of precipitation", ""))

    for i in high_and_low_temp:
        high_and_low_temp_list.append(i.text)

    for i in high_and_low_temp_list[::2]:
        low_temp_list.append(i)

    for i in high_and_low_temp_list[1::2]:
        high_temp_list.append(i)

    for i in days:
        time_list_not_complete.append([i.text])

    for i in time_list_not_complete:
        for x in i:
            time_list.append(str(x).replace("\xa0", ""))

    for i in time_list:
        final_time_list.append(str(i[:-7]))

    """ graph_plotting.feeling_temp_to_actual_temp(
        temperature_list, temperature_feel_list, time_list_front
    )
    """

    weather(low_temp_list, high_temp_list, final_time_list)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1151, 803)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(772, 40, 371, 731))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.languagelabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.languagelabel.setFont(font)
        self.languagelabel.setObjectName("languagelabel")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.languagelabel
        )
        self.languagebox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.languagebox.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.languagebox.setFont(font)
        self.languagebox.setObjectName("languagebox")
        self.languagebox.addItem("")
        self.languagebox.addItem("")
        self.languagebox.addItem("")
        self.languagebox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.languagebox)
        self.websitelabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.websitelabel.setFont(font)
        self.websitelabel.setObjectName("websitelabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.websitelabel)
        self.websitebox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.websitebox.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.websitebox.setFont(font)
        self.websitebox.setObjectName("websitebox")
        self.websitebox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.websitebox)
        self.typeofdatalabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.typeofdatalabel.setFont(font)
        self.typeofdatalabel.setObjectName("typeofdatalabel")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.typeofdatalabel
        )
        self.typeofdatabox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.typeofdatabox.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.typeofdatabox.setFont(font)
        self.typeofdatabox.setObjectName("typeofdatabox")
        self.typeofdatabox.addItem("")
        self.typeofdatabox.addItem("")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.typeofdatabox
        )
        self.emailaddresslabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.emailaddresslabel.setFont(font)
        self.emailaddresslabel.setObjectName("emailaddresslabel")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.emailaddresslabel
        )
        self.emailedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.emailedit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.emailedit.setFont(font)
        self.emailedit.setObjectName("emailedit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.emailedit)
        self.finddatabutton = QtWidgets.QPushButton(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.finddatabutton.sizePolicy().hasHeightForWidth()
        )
        self.finddatabutton.setSizePolicy(sizePolicy)
        self.finddatabutton.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.finddatabutton.setFont(font)
        self.finddatabutton.setObjectName("finddatabutton")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.SpanningRole, self.finddatabutton
        )
        self.comparewebsitesbutton = QtWidgets.QPushButton(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.comparewebsitesbutton.sizePolicy().hasHeightForWidth()
        )
        self.comparewebsitesbutton.setSizePolicy(sizePolicy)
        self.comparewebsitesbutton.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comparewebsitesbutton.setFont(font)
        self.comparewebsitesbutton.setAutoDefault(False)
        self.comparewebsitesbutton.setObjectName("comparewebsitesbutton")
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.SpanningRole, self.comparewebsitesbutton
        )
        self.emailresultsbutton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.emailresultsbutton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.emailresultsbutton.setFont(font)
        self.emailresultsbutton.setObjectName("emailresultsbutton")
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.SpanningRole, self.emailresultsbutton
        )
        self.clearallbutton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.clearallbutton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.clearallbutton.setFont(font)
        self.clearallbutton.setObjectName("clearallbutton")
        self.formLayout.setWidget(
            9, QtWidgets.QFormLayout.SpanningRole, self.clearallbutton
        )
        self.emailedit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.emailedit_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.emailedit_2.setFont(font)
        self.emailedit_2.setObjectName("emailedit_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.emailedit_2)
        self.emailaddresslabel_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.emailaddresslabel_2.setFont(font)
        self.emailaddresslabel_2.setObjectName("emailaddresslabel_2")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.emailaddresslabel_2
        )
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 40, 751, 651))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Mpwidget = MplWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Mpwidget.sizePolicy().hasHeightForWidth())
        self.Mpwidget.setSizePolicy(sizePolicy)
        self.Mpwidget.setObjectName("Mpwidget")
        self.gridLayout.addWidget(self.Mpwidget, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 690, 751, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.today = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.today.setFont(font)
        self.today.setObjectName("today")
        self.horizontalLayout.addWidget(self.today)
        self.tomorrow = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tomorrow.setFont(font)
        self.tomorrow.setObjectName("tomorrow")
        self.horizontalLayout.addWidget(self.tomorrow)
        self.twod = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.twod.setFont(font)
        self.twod.setObjectName("twod")
        self.horizontalLayout.addWidget(self.twod)
        self.threed = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.threed.setFont(font)
        self.threed.setObjectName("threed")
        self.horizontalLayout.addWidget(self.threed)
        self.fourd = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fourd.setFont(font)
        self.fourd.setObjectName("fourd")
        self.horizontalLayout.addWidget(self.fourd)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(560, -10, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(True)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.finddatabutton.clicked.connect(lambda: self.get_data())
        self.languagebox.currentIndexChanged.connect(lambda: self.change_language())

    def get_data(self):
        if self.websitebox.currentText() == "BBC":
            lowy, highy, x = bbc()
            self.Mpwidget.canvas.ax.plot(x, y)
            self.Mpwidget.canvas.draw()

    def plot_data(self):
        x = range(0, 10)
        y = range(0, 20, 2)
        self.Mpwidget.canvas.ax.plot(x, y)
        self.Mpwidget.canvas.draw()

    def change_language(self):
        selected_language = self.languagebox.currentText()
        if selected_language == "日本語 (漢字)":
            self.today.setText("今日")
            self.tomorrow.setText("明日")
            self.twod.setText("㏡")
            self.threed.setText("㏢")
            self.fourd.setText("㏣")
            self.languagelabel.setText("言葉")
            self.websitelabel.setText("ウエブサイト")
            self.finddatabutton.setText("データを見つけます")
            self.comparewebsitesbutton.setText("ウエブサイトを比べます")
            self.clearallbutton.setText("全てをデリートします")
            self.emailaddresslabel.setText("メールアドレス")
            self.typeofdatalabel.setText("データの種類")
            self.emailresultsbutton.setText("メールの結果")
            self.emailaddresslabel_2.setText("雄弁番号")
            self.title.setText("天気予報")
        elif selected_language == "日本語 (かな)":
            self.today.setText("きょう")
            self.tomorrow.setText("あした")
            self.twod.setText("ににち")
            self.threed.setText("さんにち")
            self.fourd.setText("よんにち")
            self.languagelabel.setText("ことば")
            self.websitelabel.setText("ウエブサイト")
            self.finddatabutton.setText("データをみつけます")
            self.comparewebsitesbutton.setText("ウエブサイトをくらべます")
            self.clearallbutton.setText("すべてをデリートします")
            self.emailaddresslabel.setText("メールアドレス")
            self.typeofdatalabel.setText("データのしゅるい")
            self.emailresultsbutton.setText("メールのけっか")
            self.emailaddresslabel_2.setText("ゆうべんばんごう")
            self.title.setText("てんきよほう")
        elif selected_language == "Italiano":
            self.today.setText("Oggi")
            self.tomorrow.setText("Dommani")
            self.twod.setText("Due Giorni")
            self.threed.setText("Tre Giorni")
            self.fourd.setText("Quatro Giorni")
            self.languagelabel.setText("Lingua")
            self.websitelabel.setText("Sito Web")
            self.finddatabutton.setText("Trova informationi")
            self.comparewebsitesbutton.setText("ウエブサイトをくらべます")
            self.clearallbutton.setText("すべてをデリートします")
            self.emailaddresslabel.setText("E-Mail")
            self.typeofdatalabel.setText("Tipo di informatione")
            self.emailresultsbutton.setText("Manda risultati via email")
        elif selected_language == "English":
            self.today.setText("Today")
            self.tomorrow.setText("Tomorrow")
            self.twod.setText("Two Days")
            self.threed.setText("Three Days")
            self.fourd.setText("Four Days")
            self.languagelabel.setText("Language")
            self.websitelabel.setText("Website")
            self.finddatabutton.setText("Find Data")
            self.comparewebsitesbutton.setText("Compare websites")
            self.clearallbutton.setText("Clear All")
            self.emailaddresslabel.setText("Email Address")
            self.typeofdatalabel.setText("Type of Data")
            self.emailresultsbutton.setText("Email Results")
            self.emailaddresslabel_2.setText("Postcode")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.languagelabel.setText(_translate("MainWindow", "Language"))
        self.languagebox.setItemText(0, _translate("MainWindow", "English"))
        self.languagebox.setItemText(1, _translate("MainWindow", "Italiano"))
        self.languagebox.setItemText(2, _translate("MainWindow", "日本語 (漢字)"))
        self.languagebox.setItemText(3, _translate("MainWindow", "日本語 (かな)"))
        self.websitelabel.setText(_translate("MainWindow", "Website"))
        self.websitebox.setItemText(0, _translate("MainWindow", "BBC"))
        self.typeofdatalabel.setText(_translate("MainWindow", "Type of Data"))
        self.typeofdatabox.setItemText(0, _translate("MainWindow", "Weather"))
        self.typeofdatabox.setItemText(1, _translate("MainWindow", "Precipitation"))
        self.emailaddresslabel.setText(_translate("MainWindow", "Email Address"))
        self.finddatabutton.setText(_translate("MainWindow", "Find Data"))
        self.comparewebsitesbutton.setText(_translate("MainWindow", "Compare websites"))
        self.emailresultsbutton.setText(_translate("MainWindow", "Email Results"))
        self.clearallbutton.setText(_translate("MainWindow", "Clear All"))
        self.emailaddresslabel_2.setText(_translate("MainWindow", "Postcode"))
        self.today.setText(_translate("MainWindow", "Today"))
        self.tomorrow.setText(_translate("MainWindow", "Tomorrow"))
        self.twod.setText(_translate("MainWindow", "2 Days"))
        self.threed.setText(_translate("MainWindow", "3 Days"))
        self.fourd.setText(_translate("MainWindow", "4 Days"))
        self.title.setText(_translate("MainWindow", "Weather Tracker"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
