import sys

from PySide6 import QtCore, QtGui, QtWidgets

from menu_bar import MenuBar
from screens.download_screen import DownloadScreen
from screens.home_screen import HomeScreen


# window resize event
def window_resize(event):
    menu_bar.menu_frame.setGeometry(0, 0, menu_bar.menu_frame.width(), window.height())


app = QtWidgets.QApplication(sys.argv)

# set app stylesheet
with open("main.qss", "r") as file:
    main_style = file.read()

with open("menu_bar.qss", "r") as file:
    menu_style = file.read()

with open("screens/download_screen.qss", "r") as file:
    download_screen_style = file.read()

app.setStyleSheet(main_style + menu_style + download_screen_style)

window = QtWidgets.QWidget()
window.setWindowTitle("YT Downloader")

# screen size
screen = app.primaryScreen()
screen_size = screen.size()

# set window geometry
x = screen_size.width() / 2 - 800 / 2
y = screen_size.height() / 2 - 600 / 2
window.setGeometry(int(x), int(y), 800, 600)

# set window title
window.setWindowTitle("YT Downloader")

# set window icon
icon = QtGui.QIcon(r"icons\icon.ico")
window.setWindowIcon(icon)

# main frame layout
main_layout = QtWidgets.QHBoxLayout(window)
main_layout.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))

# main frame
main_frame = QtWidgets.QFrame(window)
main_frame.setObjectName("mainFrame")
main_layout.addWidget(main_frame)

# stacked widget
stacked_widget_layout = QtWidgets.QHBoxLayout(main_frame)
stacked_widget_layout.setContentsMargins(0, 0, 0, 0)
stacked_widget = QtWidgets.QStackedWidget(main_frame)
stacked_widget_layout.addWidget(stacked_widget)

# Home screen
home_screen = HomeScreen(stacked_widget)

# Download Screen
download_screen = DownloadScreen(stacked_widget, app)

# menu bar
menu_bar = MenuBar(main_frame, window, app, stacked_widget)

# window resize
window.resizeEvent = window_resize

window.show()
sys.exit(app.exec_())
