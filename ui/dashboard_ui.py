from PyQt6 import QtCore, QtGui, QtWidgets

font_mid = QtGui.QFont()
font_mid.setFamily("./font/Inter_18pt-Medium.ttf")
font_mid.setPointSize(15)

font_regular = QtGui.QFont()
font_regular.setPointSize(12)
font_regular.setFamily("./font/OpenSans-Regular.ttf")

font_bold = QtGui.QFont()
font_bold.setFamily("./font/Inter_18pt-Bold.ttf")
font_bold.setPointSize(15)

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(969, 600)
        MainWindow.setStyleSheet("""*{background:none;border:none;margin:0;padding:0;}
                                 QDateEdit, QLineEdit{border-radius:10px;padding:2px;margin:1px 6px;}
                                 #IconMenu, #SideMenu{background-color:#221402;padding:0px;margin:0px;}
                                 #IconMenu QPushButton, #IconMenu QLabel, #SideMenu QPushButton, #SideMenu QLabel{
                                    background-color:#221402;
                                    color:#C6CDCA;
                                    text-align: left;
                                    padding:14px 12px;
                                    }
                                 #IconMenuItems QPushButton, #MenuItems QPushButton{border-radius:10px;}
                                 #IconMenuItems QPushButton:checked, #MenuItems QPushButton:checked,#IconMenuItems QPushButton:hover, #MenuItems QPushButton:hover {
                                    background-color: #010905;
                                    }
                                 #header{background-color:#2D221B}
                                 #header QLabel, #header QPushButton{color:#C6CDCA;font-size:16px;}
                                 #header #userBtn{margin-right:20px;}
                                 """)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget_Layout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.centralwidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget_Layout.setSpacing(0)
        self.centralwidget_Layout.setObjectName("centralwidget_Layout")

        # *************************** Icon Menu *********************************
        self.IconMenu = QtWidgets.QWidget(parent=self.centralwidget)
        self.IconMenu.setMaximumSize(QtCore.QSize(80, 16777215))
        self.IconMenu.setFont(font_regular)
        self.IconMenu.setObjectName("IconMenu")
        self.IconMenu.setHidden(True)

        self.IconMenu_Layout = QtWidgets.QVBoxLayout(self.IconMenu)
        self.IconMenu_Layout.setContentsMargins(0, 0, 0, 0)
        self.IconMenu_Layout.setSpacing(0)
        self.IconMenu_Layout.setObjectName("IconMenu_Layout")
        self.IconMenuToggle = QtWidgets.QFrame(parent=self.IconMenu)
        self.IconMenuToggle.setMinimumSize(QtCore.QSize(0, 50))
        self.IconMenuToggle.setMaximumSize(QtCore.QSize(16777215, 50))
        self.IconMenuToggle.setFont(font_regular)
        self.IconMenuToggle.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.IconMenuToggle.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.IconMenuToggle.setObjectName("IconMenuToggle")
        self.IconMenuToggle_Layout = QtWidgets.QVBoxLayout(self.IconMenuToggle)
        self.IconMenuToggle_Layout.setContentsMargins(9, -1, -1, -1)
        self.IconMenuToggle_Layout.setObjectName("IconMenuToggle_Layout")
        self.IconToggleBtn = QtWidgets.QPushButton(parent=self.IconMenuToggle)
        self.IconToggleBtn.setFont(font_regular)
        self.IconToggleBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.IconToggleBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/menu.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.IconToggleBtn.setIcon(icon)
        self.IconToggleBtn.setIconSize(QtCore.QSize(28, 28))
        self.IconToggleBtn.setCheckable(True)
        self.IconToggleBtn.setAutoRepeat(False)
        self.IconToggleBtn.setAutoExclusive(True)
        self.IconToggleBtn.setObjectName("IconToggleBtn")
        self.IconMenuToggle_Layout.addWidget(self.IconToggleBtn)
        self.IconMenu_Layout.addWidget(self.IconMenuToggle)
        self.IconMenuItems = QtWidgets.QFrame(parent=self.IconMenu)
        self.IconMenuItems.setFont(font_regular)
        self.IconMenuItems.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.IconMenuItems.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.IconMenuItems.setObjectName("IconMenuItems")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.IconMenuItems)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # *** Home Icon Button ****
        self.homeIconBtn = QtWidgets.QPushButton(parent=self.IconMenuItems)
        self.homeIconBtn.setFont(font_regular)
        self.homeIconBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.homeIconBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.homeIconBtn.setIcon(icon1)
        self.homeIconBtn.setIconSize(QtCore.QSize(28, 28))
        self.homeIconBtn.setCheckable(True)
        self.homeIconBtn.setChecked(True)
        self.homeIconBtn.setAutoExclusive(True)
        self.homeIconBtn.setAutoRepeatDelay(100)
        self.homeIconBtn.setAutoDefault(False)
        self.homeIconBtn.setFlat(False)
        self.homeIconBtn.setObjectName("homeIconBtn")
        self.verticalLayout_2.addWidget(self.homeIconBtn)


        # *** space ****
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        # *** license Icon Button ****
        self.licenseIconBtn = QtWidgets.QPushButton(parent=self.IconMenuItems)
        self.licenseIconBtn.setFont(font_regular)
        self.licenseIconBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.licenseIconBtn.setText("")
        licenseIcon = QtGui.QIcon()
        licenseIcon.addPixmap(QtGui.QPixmap("./icons/key.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.licenseIconBtn.setIcon(licenseIcon)
        self.licenseIconBtn.setIconSize(QtCore.QSize(28, 28))
        self.licenseIconBtn.setCheckable(True)
        self.licenseIconBtn.setAutoExclusive(True)
        self.licenseIconBtn.setAutoRepeatDelay(100)
        self.licenseIconBtn.setAutoDefault(False)
        self.licenseIconBtn.setFlat(False)
        self.licenseIconBtn.setObjectName("licenseIconBtn")
        self.verticalLayout_2.addWidget(self.licenseIconBtn)

        # *** Logout Icon Button ****
        self.logoutIconBtn = QtWidgets.QPushButton(parent=self.IconMenuItems)
        self.logoutIconBtn.setFont(font_regular)
        self.logoutIconBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logoutIconBtn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./icons/log-out.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.logoutIconBtn.setIcon(icon6)
        self.logoutIconBtn.setIconSize(QtCore.QSize(28, 28))
        self.logoutIconBtn.setCheckable(True)
        self.logoutIconBtn.setAutoExclusive(True)
        self.logoutIconBtn.setAutoRepeatDelay(100)
        self.logoutIconBtn.setAutoDefault(False)
        self.logoutIconBtn.setFlat(False)
        self.logoutIconBtn.setObjectName("logoutIconBtn")
        self.verticalLayout_2.addWidget(self.logoutIconBtn)
        self.IconMenu_Layout.addWidget(self.IconMenuItems)
        self.centralwidget_Layout.addWidget(self.IconMenu)

        # *************************** end Icon Menu **********************************************
        self.SideMenu = QtWidgets.QWidget(parent=self.centralwidget)
        self.SideMenu.setMinimumSize(QtCore.QSize(200, 0))
        self.SideMenu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SideMenu.setFont(font_regular)
        self.SideMenu.setObjectName("SideMenu")
        self.SideMenu_Layout = QtWidgets.QVBoxLayout(self.SideMenu)
        self.SideMenu_Layout.setContentsMargins(0, 0, 0, 0)
        self.SideMenu_Layout.setSpacing(0)
        self.SideMenu_Layout.setObjectName("SideMenu_Layout")
        self.MenuToggle = QtWidgets.QFrame(parent=self.SideMenu)
        self.MenuToggle.setMinimumSize(QtCore.QSize(0, 50))
        self.MenuToggle.setMaximumSize(QtCore.QSize(16777215, 50))
        self.MenuToggle.setFont(font_regular)
        self.MenuToggle.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.MenuToggle.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.MenuToggle.setObjectName("MenuToggle")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MenuToggle)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ToggleBtn = QtWidgets.QPushButton(parent=self.MenuToggle)
        self.ToggleBtn.setFont(font_regular)
        self.ToggleBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ToggleBtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./icons/chevrons-left.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ToggleBtn.setIcon(icon7)
        self.ToggleBtn.setIconSize(QtCore.QSize(28, 28))
        self.ToggleBtn.setCheckable(True)
        self.ToggleBtn.setAutoExclusive(True)
        self.ToggleBtn.setObjectName("ToggleBtn")
        self.verticalLayout.addWidget(self.ToggleBtn)
        self.SideMenu_Layout.addWidget(self.MenuToggle)
        self.MenuItems = QtWidgets.QFrame(parent=self.SideMenu)
        self.MenuItems.setFont(font_regular)
        self.MenuItems.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.MenuItems.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.MenuItems.setObjectName("MenuItems")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.MenuItems)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # *************************** Menu Item ************************************************
        # *** home button ***
        self.homeBtn = QtWidgets.QPushButton(parent=self.MenuItems)
        self.homeBtn.setFont(font_regular)
        self.homeBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QtCore.QSize(28, 28))
        self.homeBtn.setCheckable(True)
        self.homeBtn.setChecked(True)
        self.homeBtn.setAutoExclusive(True)
        self.homeBtn.setAutoRepeatDelay(100)
        self.homeBtn.setAutoDefault(False)
        self.homeBtn.setFlat(False)
        self.homeBtn.setObjectName("homeBtn")
        self.verticalLayout_3.addWidget(self.homeBtn)


        # *** space ***
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)

        # *** license button ***
        self.licenseBtn = QtWidgets.QPushButton(parent=self.MenuItems)
        self.licenseBtn.setFont(font_regular)
        self.licenseBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.licenseBtn.setIcon(licenseIcon)
        self.licenseBtn.setIconSize(QtCore.QSize(28, 28))
        self.licenseBtn.setCheckable(True)
        self.licenseBtn.setAutoExclusive(True)
        self.licenseBtn.setAutoRepeatDelay(100)
        self.licenseBtn.setAutoDefault(False)
        self.licenseBtn.setFlat(False)
        self.licenseBtn.setObjectName("licenseBtn")
        self.verticalLayout_3.addWidget(self.licenseBtn)

        # *** Logout button ***
        self.logoutBtn = QtWidgets.QPushButton(parent=self.MenuItems)
        self.logoutBtn.setFont(font_regular)
        self.logoutBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logoutBtn.setIcon(icon6)
        self.logoutBtn.setIconSize(QtCore.QSize(28, 28))
        self.logoutBtn.setCheckable(True)
        self.logoutBtn.setAutoExclusive(True)
        self.logoutBtn.setAutoRepeatDelay(100)
        self.logoutBtn.setAutoDefault(False)
        self.logoutBtn.setFlat(False)
        self.logoutBtn.setObjectName("logoutBtn")
        self.verticalLayout_3.addWidget(self.logoutBtn)

        # *************************** Menu Item end *********************************
        self.SideMenu_Layout.addWidget(self.MenuItems)
        self.centralwidget_Layout.addWidget(self.SideMenu)
        self.MainBody = QtWidgets.QWidget(parent=self.centralwidget)
        self.MainBody.setFont(font_regular)
        self.MainBody.setObjectName("MainBody")
        self.MainBody_Layout = QtWidgets.QVBoxLayout(self.MainBody)
        self.MainBody_Layout.setContentsMargins(0, 0, 0, 0)
        self.MainBody_Layout.setSpacing(0)
        self.MainBody_Layout.setObjectName("MainBody_Layout")
        self.Header = QtWidgets.QWidget(parent=self.MainBody)
        self.Header.setMinimumSize(QtCore.QSize(0, 50))
        self.Header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Header.setObjectName("Header")
        self.Header.setStyleSheet("""
            * {
                background-color:#FFFFFF;
                border-bottom:1px solid #B5B5B5;
            }
            #LeftHeader, #RightHeader, #tagline, #logo, #tag, QLabel{
                border-bottom: none;
            }
        """)
        self.Header_Layout = QtWidgets.QHBoxLayout(self.Header)
        self.Header_Layout.setObjectName("Header_Layout")
        self.LeftHeader = QtWidgets.QWidget(parent=self.Header)
        self.LeftHeader.setObjectName("LeftHeader")
        self.LeftHeader_Layout = QtWidgets.QHBoxLayout(self.LeftHeader)
        self.LeftHeader_Layout.setContentsMargins(-1, 0, -1, -1)
        self.LeftHeader_Layout.setObjectName("LeftHeader_Layout")
        self.tagline = QtWidgets.QLabel(parent=self.LeftHeader)
        self.tagline.setFont(font_mid)
        self.tagline.setObjectName("tagline")
        self.LeftHeader_Layout.addWidget(self.tagline)

        self.Header_Layout.addWidget(self.LeftHeader, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.Header_Layout.addItem(spacerItem2)
        self.RightHeader = QtWidgets.QWidget(parent=self.Header)
        self.RightHeader.setFont(font_mid)
        self.RightHeader.setStyleSheet("""
            QWidget {
                padding: 0;
                margin: 0;
            }
            QLabel {
                margin: 0;
                padding: 0;
            }
        """)
        self.RightHeader.setObjectName("RightHeader")
        self.RightHeader_Layout = QtWidgets.QHBoxLayout(self.RightHeader)
        self.RightHeader_Layout.setContentsMargins(0, 0, 20, 0)  # Right margin of 20px
        self.RightHeader_Layout.setSpacing(10)  # Space between logo and tag
        self.RightHeader_Layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)  # Vertical center alignment

        # Keep the logo and tag code the same, just ensure they're added to the layout
        self.logo = QtWidgets.QLabel(parent=self.RightHeader)
        self.logo.setMinimumSize(QtCore.QSize(30, 30))
        self.logo.setMaximumSize(QtCore.QSize(30, 30))
        self.logo.setPixmap(QtGui.QPixmap("./images/logo.png"))
        self.logo.setScaledContents(True)
        self.RightHeader_Layout.addWidget(self.logo)

        self.tag = QtWidgets.QLabel(parent=self.RightHeader)
        self.tag.setFont(font_mid)
        self.RightHeader_Layout.addWidget(self.tag)
        self.Header_Layout.addWidget(self.RightHeader)
        self.MainBody_Layout.addWidget(self.Header)
        self.Body = QtWidgets.QWidget(parent=self.MainBody)
        self.Body.setFont(font_regular)
        self.Body.setObjectName("Body")
        self.Body.setStyleSheet("""QStackedWidget{background-color:#F3F3F3;}""")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # *********** StackWidget *******************
        print("debug 1")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.Body)
        self.stackedWidget.setFont(font_regular)
        self.stackedWidget.setObjectName("stackedWidget")

        ## ************* Pages will add here *****************

        self.horizontalLayout.addWidget(self.stackedWidget)
        self.MainBody_Layout.addWidget(self.Body)
        self.centralwidget_Layout.addWidget(self.MainBody)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.ToggleBtn.clicked.connect(self.IconMenu.show)  # type: ignore
        self.ToggleBtn.clicked.connect(self.SideMenu.hide)  # type: ignore
        self.IconToggleBtn.clicked.connect(self.SideMenu.show)  # type: ignore
        self.IconToggleBtn.clicked.connect(self.IconMenu.hide)  # type: ignore

        self.homeBtn.toggled['bool'].connect(self.homeIconBtn.setChecked)  # type: ignore
        self.homeIconBtn.toggled['bool'].connect(self.homeBtn.setChecked)  # type: ignore

        self.licenseBtn.toggled['bool'].connect(self.licenseBtn.setChecked)  # type: ignore
        self.licenseIconBtn.toggled['bool'].connect(self.licenseBtn.setChecked)  # type: ignore

        self.logoutBtn.toggled['bool'].connect(self.logoutIconBtn.setChecked)  # type: ignore
        self.logoutIconBtn.toggled['bool'].connect(self.logoutBtn.setChecked)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.IconToggleBtn.setToolTip(_translate("MainWindow", "Expand Menu"))

        self.homeIconBtn.setToolTip(_translate("MainWindow", "Home"))


        self.licenseIconBtn.setToolTip(_translate("MainWindow", "License"))
        self.logoutIconBtn.setToolTip(_translate("MainWindow", "Logout"))
        self.ToggleBtn.setToolTip(_translate("MainWindow", "Narrow"))

        self.homeBtn.setToolTip(_translate("MainWindow", "Home"))
        self.homeBtn.setText(_translate("MainWindow", "Home"))


        self.licenseBtn.setToolTip(_translate("MainWindow", "License"))
        self.licenseBtn.setText(_translate("MainWindow", "License"))

        self.logoutBtn.setToolTip(_translate("MainWindow", "Exit"))
        self.logoutBtn.setText(_translate("MainWindow", "Exit"))
        self.tag.setText(_translate("MainWindow", "Sofmark"))

        self.tagline.setText(_translate("MainWindow", "AI Writing Software"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
