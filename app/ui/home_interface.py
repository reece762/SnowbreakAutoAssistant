# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_home(object):
    def setupUi(self, home):
        home.setObjectName("home")
        home.resize(813, 900)
        self.gridLayout_2 = QtWidgets.QGridLayout(home)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SimpleCardWidget_option = SimpleCardWidget(home)
        self.SimpleCardWidget_option.setMinimumSize(QtCore.QSize(237, 320))
        self.SimpleCardWidget_option.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.SimpleCardWidget_option.setObjectName("SimpleCardWidget_option")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.SimpleCardWidget_option)
        self.gridLayout_7.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.CheckBox_person_5 = CheckBox(self.SimpleCardWidget_option)
        self.CheckBox_person_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CheckBox_person_5.setObjectName("CheckBox_person_5")
        self.gridLayout_7.addWidget(self.CheckBox_person_5, 6, 0, 1, 4)
        self.ToolButton_use_power = ToolButton(self.SimpleCardWidget_option)
        self.ToolButton_use_power.setObjectName("ToolButton_use_power")
        self.gridLayout_7.addWidget(self.ToolButton_use_power, 5, 4, 1, 1)
        self.CheckBox_stamina_2 = CheckBox(self.SimpleCardWidget_option)
        self.CheckBox_stamina_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CheckBox_stamina_2.setObjectName("CheckBox_stamina_2")
        self.gridLayout_7.addWidget(self.CheckBox_stamina_2, 3, 0, 1, 4)
        self.ToolButton_stamina = ToolButton(self.SimpleCardWidget_option)
        self.ToolButton_stamina.setEnabled(False)
        self.ToolButton_stamina.setObjectName("ToolButton_stamina")
        self.gridLayout_7.addWidget(self.ToolButton_stamina, 3, 4, 1, 1)
        self.PushButton_select_all = PushButton(self.SimpleCardWidget_option)
        self.PushButton_select_all.setObjectName("PushButton_select_all")
        self.gridLayout_7.addWidget(self.PushButton_select_all, 10, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_7.addItem(spacerItem, 1, 2, 1, 1)
        self.PushButton_no_select = PushButton(self.SimpleCardWidget_option)
        self.PushButton_no_select.setObjectName("PushButton_no_select")
        self.gridLayout_7.addWidget(self.PushButton_no_select, 10, 3, 1, 1)
        self.CheckBox_entry_1 = CheckBox(self.SimpleCardWidget_option)
        self.CheckBox_entry_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CheckBox_entry_1.setObjectName("CheckBox_entry_1")
        self.gridLayout_7.addWidget(self.CheckBox_entry_1, 2, 0, 1, 4)
        self.ToolButton_chasm = ToolButton(self.SimpleCardWidget_option)
        self.ToolButton_chasm.setEnabled(False)
        self.ToolButton_chasm.setObjectName("ToolButton_chasm")
        self.gridLayout_7.addWidget(self.ToolButton_chasm, 7, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_7.addItem(spacerItem1, 9, 2, 1, 1)
        self.CheckBox_chasm_6 = CheckBox(self.SimpleCardWidget_option)
        self.CheckBox_chasm_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CheckBox_chasm_6.setObjectName("CheckBox_chasm_6")
        self.gridLayout_7.addWidget(self.CheckBox_chasm_6, 7, 0, 1, 4)
        self.CheckBox_reward_7 = CheckBox(self.SimpleCardWidget_option)
        self.CheckBox_reward_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CheckBox_reward_7.setObjectName("CheckBox_reward_7")
        self.gridLayout_7.addWidget(self.CheckBox_reward_7, 8, 0, 1, 4)
        self.ToolButton_reward = ToolButton(self.SimpleCardWidget_option)
        self.ToolButton_reward.setObjectName("ToolButton_reward")
        self.gridLayout_7.addWidget(self.ToolButton_reward, 8, 4, 1, 1)
        self.CheckBox_use_power_4 = CheckBox(self.SimpleCardWidget_option)
        self.CheckBox_use_power_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CheckBox_use_power_4.setObjectName("CheckBox_use_power_4")
        self.gridLayout_7.addWidget(self.CheckBox_use_power_4, 5, 0, 1, 4)
        self.CheckBox_shop_3 = CheckBox(self.SimpleCardWidget_option)
        self.CheckBox_shop_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CheckBox_shop_3.setObjectName("CheckBox_shop_3")
        self.gridLayout_7.addWidget(self.CheckBox_shop_3, 4, 0, 1, 4)
        self.ToolButton_shop = ToolButton(self.SimpleCardWidget_option)
        self.ToolButton_shop.setObjectName("ToolButton_shop")
        self.gridLayout_7.addWidget(self.ToolButton_shop, 4, 4, 1, 1)
        self.ToolButton_person = ToolButton(self.SimpleCardWidget_option)
        self.ToolButton_person.setEnabled(True)
        self.ToolButton_person.setObjectName("ToolButton_person")
        self.gridLayout_7.addWidget(self.ToolButton_person, 6, 4, 1, 1)
        self.ToolButton_entry = ToolButton(self.SimpleCardWidget_option)
        self.ToolButton_entry.setEnabled(False)
        self.ToolButton_entry.setObjectName("ToolButton_entry")
        self.gridLayout_7.addWidget(self.ToolButton_entry, 2, 4, 1, 1)
        self.gridLayout_7.setColumnStretch(0, 1)
        self.gridLayout_7.setColumnStretch(1, 2)
        self.gridLayout_7.setColumnStretch(2, 1)
        self.gridLayout_7.setColumnStretch(3, 2)
        self.gridLayout_7.setColumnStretch(4, 1)
        self.gridLayout_2.addWidget(self.SimpleCardWidget_option, 0, 0, 1, 1)
        self.SimpleCardWidget_3 = SimpleCardWidget(home)
        self.SimpleCardWidget_3.setMinimumSize(QtCore.QSize(237, 165))
        self.SimpleCardWidget_3.setObjectName("SimpleCardWidget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.SimpleCardWidget_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 0, 0, 1, 1)
        self.BodyLabel = BodyLabel(self.SimpleCardWidget_3)
        self.BodyLabel.setObjectName("BodyLabel")
        self.gridLayout_5.addWidget(self.BodyLabel, 1, 0, 1, 1)
        self.ComboBox_after_use = ComboBox(self.SimpleCardWidget_3)
        self.ComboBox_after_use.setDefault(False)
        self.ComboBox_after_use.setProperty("items_", "")
        self.ComboBox_after_use.setObjectName("ComboBox_after_use")
        self.gridLayout_5.addWidget(self.ComboBox_after_use, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem3, 3, 0, 1, 1)
        self.PushButton_start = PushButton(self.SimpleCardWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PushButton_start.sizePolicy().hasHeightForWidth())
        self.PushButton_start.setSizePolicy(sizePolicy)
        self.PushButton_start.setMinimumSize(QtCore.QSize(0, 60))
        self.PushButton_start.setObjectName("PushButton_start")
        self.gridLayout_5.addWidget(self.PushButton_start, 4, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem4, 5, 0, 1, 1)
        self.gridLayout_2.addWidget(self.SimpleCardWidget_3, 1, 0, 1, 1)
        self.SimpleCardWidget_2 = SimpleCardWidget(home)
        self.SimpleCardWidget_2.setMinimumSize(QtCore.QSize(237, 320))
        self.SimpleCardWidget_2.setObjectName("SimpleCardWidget_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.SimpleCardWidget_2)
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setVerticalSpacing(4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.TitleLabel_setting = TitleLabel(self.SimpleCardWidget_2)
        self.TitleLabel_setting.setObjectName("TitleLabel_setting")
        self.gridLayout_8.addWidget(self.TitleLabel_setting, 0, 0, 1, 1)
        self.PopUpAniStackedWidget = PopUpAniStackedWidget(self.SimpleCardWidget_2)
        self.PopUpAniStackedWidget.setObjectName("PopUpAniStackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ScrollArea = ScrollArea(self.page)
        self.ScrollArea.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:None;")
        self.ScrollArea.setWidgetResizable(True)
        self.ScrollArea.setObjectName("ScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 309, 554))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.CheckBox_buy_12 = CheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox_buy_12.sizePolicy().hasHeightForWidth())
        self.CheckBox_buy_12.setSizePolicy(sizePolicy)
        self.CheckBox_buy_12.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_buy_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CheckBox_buy_12.setObjectName("CheckBox_buy_12")
        self.gridLayout.addWidget(self.CheckBox_buy_12, 16, 0, 1, 1)
        self.CheckBox_buy_9 = CheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox_buy_9.sizePolicy().hasHeightForWidth())
        self.CheckBox_buy_9.setSizePolicy(sizePolicy)
        self.CheckBox_buy_9.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_buy_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CheckBox_buy_9.setObjectName("CheckBox_buy_9")
        self.gridLayout.addWidget(self.CheckBox_buy_9, 12, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setAutoFillBackground(False)
        self.line_3.setStyleSheet("QFrame\n"
"{\n"
"    border:none;\n"
"    background-color: rgba(0, 159, 170, 15);\n"
"    min-height : 3px;\n"
"    max-height : 3px;\n"
"    border-radius: 3px;\n"
"}")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setLineWidth(10)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 11, 0, 1, 1)
        self.StrongBodyLabel = StrongBodyLabel(self.scrollAreaWidgetContents)
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")
        self.gridLayout.addWidget(self.StrongBodyLabel, 0, 0, 1, 1)
        self.CheckBox_buy_10 = CheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox_buy_10.sizePolicy().hasHeightForWidth())
        self.CheckBox_buy_10.setSizePolicy(sizePolicy)
        self.CheckBox_buy_10.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_buy_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CheckBox_buy_10.setObjectName("CheckBox_buy_10")
        self.gridLayout.addWidget(self.CheckBox_buy_10, 13, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setAutoFillBackground(False)
        self.line_4.setStyleSheet("QFrame\n"
"{\n"
"    border:none;\n"
"    background-color: rgba(0, 159, 170, 15);\n"
"    min-height : 3px;\n"
"    max-height : 3px;\n"
"    border-radius: 3px;\n"
"}")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setLineWidth(10)
        self.line_4.setMidLineWidth(0)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 15, 0, 1, 1)
        self.CheckBox_buy_15 = CheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox_buy_15.sizePolicy().hasHeightForWidth())
        self.CheckBox_buy_15.setSizePolicy(sizePolicy)
        self.CheckBox_buy_15.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_buy_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CheckBox_buy_15.setObjectName("CheckBox_buy_15")
        self.gridLayout.addWidget(self.CheckBox_buy_15, 20, 0, 1, 1)
        self.CheckBox_buy_11 = CheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox_buy_11.sizePolicy().hasHeightForWidth())
        self.CheckBox_buy_11.setSizePolicy(sizePolicy)
        self.CheckBox_buy_11.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_buy_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CheckBox_buy_11.setObjectName("CheckBox_buy_11")
        self.gridLayout.addWidget(self.CheckBox_buy_11, 14, 0, 1, 1)
        self.CheckBox_buy_5 = CheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox_buy_5.sizePolicy().hasHeightForWidth())
        self.CheckBox_buy_5.setSizePolicy(sizePolicy)
        self.CheckBox_buy_5.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_buy_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CheckBox_buy_5.setObjectName("CheckBox_buy_5")
        self.gridLayout.addWidget(self.CheckBox_buy_5, 6, 0, 1, 1)
        self.CheckBox_buy_3 = CheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox_buy_3.sizePolicy().hasHeightForWidth())
        self.CheckBox_buy_3.setSizePolicy(sizePolicy)
        self.CheckBox_buy_3.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_buy_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CheckBox_buy_3.setObjectName("CheckBox_buy_3")
        self.gridLayout.addWidget(self.CheckBox_buy_3, 4, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setAutoFillBackground(False)
        self.line_2.setStyleSheet("QFrame\n"
"{\n"
"    border:none;\n"
"    background-color: rgba(0, 159, 170, 15);\n"
"    min-height : 3px;\n"
"    max-height : 3px;\n"
"    border-radius: 3px;\n"
"}")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setLineWidth(10)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 7, 0, 1, 1)
        self.CheckBox_buy_13 = CheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox_buy_13.sizePolicy().hasHeightForWidth())
        self.CheckBox_buy_13.setSizePolicy(sizePolicy)
        self.CheckBox_buy_13.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_buy_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CheckBox_buy_13.setObjectName("CheckBox_buy_13")
        self.gridLayout.addWidget(self.CheckBox_buy_13, 17, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy)
        self.line_5.setAutoFillBackground(False)
        self.line_5.setStyleSheet("QFrame\n"
"{\n"
"    border:none;\n"
"    background-color: rgba(0, 159, 170, 15);\n"
"    min-height : 3px;\n"
"    max-height : 3px;\n"
"    border-radius: 3px;\n"
"}")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setLineWidth(10)
        self.line_5.setMidLineWidth(0)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 19, 0, 1, 1)
        self.CheckBox_buy_4 = CheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox_buy_4.sizePolicy().hasHeightForWidth())
        self.CheckBox_buy_4.setSizePolicy(sizePolicy)
        self.CheckBox_buy_4.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_buy_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CheckBox_buy_4.setObjectName("CheckBox_buy_4")
        self.gridLayout.addWidget(self.CheckBox_buy_4, 5, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet("QFrame\n"
"{\n"
"    border:none;\n"
"    background-color: rgba(0, 159, 170, 15);\n"
"    min-height : 3px;\n"
"    max-height : 3px;\n"
"    border-radius: 3px;\n"
"}")
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(10)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.CheckBox_buy_6 = CheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox_buy_6.sizePolicy().hasHeightForWidth())
        self.CheckBox_buy_6.setSizePolicy(sizePolicy)
        self.CheckBox_buy_6.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_buy_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CheckBox_buy_6.setObjectName("CheckBox_buy_6")
        self.gridLayout.addWidget(self.CheckBox_buy_6, 8, 0, 1, 1)
        self.CheckBox_buy_7 = CheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox_buy_7.sizePolicy().hasHeightForWidth())
        self.CheckBox_buy_7.setSizePolicy(sizePolicy)
        self.CheckBox_buy_7.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_buy_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CheckBox_buy_7.setObjectName("CheckBox_buy_7")
        self.gridLayout.addWidget(self.CheckBox_buy_7, 9, 0, 1, 1)
        self.CheckBox_buy_8 = CheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox_buy_8.sizePolicy().hasHeightForWidth())
        self.CheckBox_buy_8.setSizePolicy(sizePolicy)
        self.CheckBox_buy_8.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_buy_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CheckBox_buy_8.setObjectName("CheckBox_buy_8")
        self.gridLayout.addWidget(self.CheckBox_buy_8, 10, 0, 1, 1)
        self.CheckBox_buy_14 = CheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox_buy_14.sizePolicy().hasHeightForWidth())
        self.CheckBox_buy_14.setSizePolicy(sizePolicy)
        self.CheckBox_buy_14.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_buy_14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CheckBox_buy_14.setObjectName("CheckBox_buy_14")
        self.gridLayout.addWidget(self.CheckBox_buy_14, 18, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)
        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.ScrollArea, 0, 0, 1, 1)
        self.PopUpAniStackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.ComboBox_power_usage = ComboBox(self.page_2)
        self.ComboBox_power_usage.setProperty("items_", "")
        self.ComboBox_power_usage.setObjectName("ComboBox_power_usage")
        self.gridLayout_6.addWidget(self.ComboBox_power_usage, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem5, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CheckBox_is_use_power = CheckBox(self.page_2)
        self.CheckBox_is_use_power.setObjectName("CheckBox_is_use_power")
        self.horizontalLayout.addWidget(self.CheckBox_is_use_power)
        self.ComboBox_power_day = ComboBox(self.page_2)
        self.ComboBox_power_day.setObjectName("ComboBox_power_day")
        self.horizontalLayout.addWidget(self.ComboBox_power_day)
        self.BodyLabel_6 = BodyLabel(self.page_2)
        self.BodyLabel_6.setObjectName("BodyLabel_6")
        self.horizontalLayout.addWidget(self.BodyLabel_6)
        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.StrongBodyLabel_2 = StrongBodyLabel(self.page_2)
        self.StrongBodyLabel_2.setObjectName("StrongBodyLabel_2")
        self.gridLayout_6.addWidget(self.StrongBodyLabel_2, 1, 0, 1, 1)
        self.PopUpAniStackedWidget.addWidget(self.page_2)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.BodyLabel_7 = BodyLabel(self.page_4)
        self.BodyLabel_7.setScaledContents(False)
        self.BodyLabel_7.setWordWrap(True)
        self.BodyLabel_7.setObjectName("BodyLabel_7")
        self.gridLayout_11.addWidget(self.BodyLabel_7, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BodyLabel_3 = BodyLabel(self.page_4)
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.horizontalLayout_2.addWidget(self.BodyLabel_3)
        self.ComboBox_c1 = ComboBox(self.page_4)
        self.ComboBox_c1.setProperty("items_", "")
        self.ComboBox_c1.setObjectName("ComboBox_c1")
        self.horizontalLayout_2.addWidget(self.ComboBox_c1)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.gridLayout_11.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.StrongBodyLabel_3 = StrongBodyLabel(self.page_4)
        self.StrongBodyLabel_3.setObjectName("StrongBodyLabel_3")
        self.gridLayout_11.addWidget(self.StrongBodyLabel_3, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.BodyLabel_8 = BodyLabel(self.page_4)
        self.BodyLabel_8.setObjectName("BodyLabel_8")
        self.horizontalLayout_5.addWidget(self.BodyLabel_8)
        self.ComboBox_c4 = ComboBox(self.page_4)
        self.ComboBox_c4.setProperty("items_", "")
        self.ComboBox_c4.setObjectName("ComboBox_c4")
        self.horizontalLayout_5.addWidget(self.ComboBox_c4)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)
        self.gridLayout_11.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.BodyLabel_5 = BodyLabel(self.page_4)
        self.BodyLabel_5.setObjectName("BodyLabel_5")
        self.horizontalLayout_4.addWidget(self.BodyLabel_5)
        self.ComboBox_c3 = ComboBox(self.page_4)
        self.ComboBox_c3.setProperty("items_", "")
        self.ComboBox_c3.setObjectName("ComboBox_c3")
        self.horizontalLayout_4.addWidget(self.ComboBox_c3)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.gridLayout_11.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BodyLabel_4 = BodyLabel(self.page_4)
        self.BodyLabel_4.setObjectName("BodyLabel_4")
        self.horizontalLayout_3.addWidget(self.BodyLabel_4)
        self.ComboBox_c2 = ComboBox(self.page_4)
        self.ComboBox_c2.setProperty("items_", "")
        self.ComboBox_c2.setObjectName("ComboBox_c2")
        self.horizontalLayout_3.addWidget(self.ComboBox_c2)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.gridLayout_11.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem6, 6, 0, 1, 1)
        self.PopUpAniStackedWidget.addWidget(self.page_4)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.CheckBox_mail = CheckBox(self.page_3)
        self.CheckBox_mail.setObjectName("CheckBox_mail")
        self.gridLayout_10.addWidget(self.CheckBox_mail, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem7, 1, 0, 1, 1)
        self.PopUpAniStackedWidget.addWidget(self.page_3)
        self.gridLayout_8.addWidget(self.PopUpAniStackedWidget, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.SimpleCardWidget_2, 0, 1, 1, 1)
        self.SimpleCardWidget_4 = SimpleCardWidget(home)
        self.SimpleCardWidget_4.setMinimumSize(QtCore.QSize(237, 165))
        self.SimpleCardWidget_4.setObjectName("SimpleCardWidget_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.SimpleCardWidget_4)
        self.gridLayout_9.setVerticalSpacing(3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.TitleLabel_3 = TitleLabel(self.SimpleCardWidget_4)
        self.TitleLabel_3.setObjectName("TitleLabel_3")
        self.gridLayout_9.addWidget(self.TitleLabel_3, 0, 0, 1, 1)
        self.BodyLabel_tip = BodyLabel(self.SimpleCardWidget_4)
        self.BodyLabel_tip.setObjectName("BodyLabel_tip")
        self.gridLayout_9.addWidget(self.BodyLabel_tip, 1, 0, 1, 1)
        self.gridLayout_9.setRowStretch(0, 1)
        self.gridLayout_9.setRowStretch(1, 3)
        self.gridLayout_2.addWidget(self.SimpleCardWidget_4, 1, 1, 1, 1)
        self.SimpleCardWidget = SimpleCardWidget(home)
        self.SimpleCardWidget.setMinimumSize(QtCore.QSize(246, 485))
        self.SimpleCardWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.SimpleCardWidget.setObjectName("SimpleCardWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.SimpleCardWidget)
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.TitleLabel = TitleLabel(self.SimpleCardWidget)
        self.TitleLabel.setObjectName("TitleLabel")
        self.gridLayout_4.addWidget(self.TitleLabel, 0, 0, 1, 1)
        self.textBrowser_log = QtWidgets.QTextBrowser(self.SimpleCardWidget)
        self.textBrowser_log.setStyleSheet("border-radius: 5px;\n"
"border: 2px;")
        self.textBrowser_log.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_log.setObjectName("textBrowser_log")
        self.gridLayout_4.addWidget(self.textBrowser_log, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.SimpleCardWidget, 0, 2, 2, 1)
        self.gridLayout_2.setRowStretch(0, 2)

        self.retranslateUi(home)
        self.PopUpAniStackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(home)

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "Frame"))
        self.CheckBox_person_5.setText(_translate("home", "角色碎片"))
        self.CheckBox_stamina_2.setText(_translate("home", "领取体力"))
        self.PushButton_select_all.setText(_translate("home", "全选 "))
        self.PushButton_no_select.setText(_translate("home", "清空"))
        self.CheckBox_entry_1.setText(_translate("home", "自动登录"))
        self.CheckBox_chasm_6.setText(_translate("home", "精神拟境"))
        self.CheckBox_reward_7.setText(_translate("home", "领取奖励"))
        self.CheckBox_use_power_4.setText(_translate("home", "刷体力"))
        self.CheckBox_shop_3.setText(_translate("home", "商店购买"))
        self.BodyLabel.setText(_translate("home", "结束后进行"))
        self.PushButton_start.setText(_translate("home", "开始"))
        self.PushButton_start.setShortcut(_translate("home", "Ctrl+S"))
        self.TitleLabel_setting.setText(_translate("home", "设置"))
        self.CheckBox_buy_12.setText(_translate("home", "合成颗粒"))
        self.CheckBox_buy_9.setText(_translate("home", "初级职级认证"))
        self.StrongBodyLabel.setText(_translate("home", "选择要购买的商品"))
        self.CheckBox_buy_10.setText(_translate("home", "中级职级认证"))
        self.CheckBox_buy_15.setText(_translate("home", "光纤轴突"))
        self.CheckBox_buy_11.setText(_translate("home", "高级职级认证"))
        self.CheckBox_buy_5.setText(_translate("home", "精致强化套件"))
        self.CheckBox_buy_3.setText(_translate("home", "通用强化套件"))
        self.CheckBox_buy_13.setText(_translate("home", "芳烃塑料"))
        self.CheckBox_buy_4.setText(_translate("home", "优选强化套件"))
        self.CheckBox_buy_6.setText(_translate("home", "新手战斗记录"))
        self.CheckBox_buy_7.setText(_translate("home", "普通战斗记录"))
        self.CheckBox_buy_8.setText(_translate("home", "优秀战斗记录"))
        self.CheckBox_buy_14.setText(_translate("home", "单极纤维"))
        self.CheckBox_is_use_power.setText(_translate("home", "自动使用期限"))
        self.ComboBox_power_day.setProperty("items_", _translate("home", "1\n"
"2\n"
"3\n"
"4\n"
"5\n"
"6"))
        self.BodyLabel_6.setText(_translate("home", "天内的体力药"))
        self.StrongBodyLabel_2.setText(_translate("home", "选择体力使用方式"))
        self.BodyLabel_7.setText(_translate("home", "优先度从上到下，若选择角色超过2名时会自动用记忆补嵌包"))
        self.BodyLabel_3.setText(_translate("home", "角色1："))
        self.StrongBodyLabel_3.setText(_translate("home", "选择需要刷碎片的角色"))
        self.BodyLabel_8.setText(_translate("home", "角色4："))
        self.BodyLabel_5.setText(_translate("home", "角色3："))
        self.BodyLabel_4.setText(_translate("home", "角色2："))
        self.CheckBox_mail.setText(_translate("home", "领取邮件"))
        self.TitleLabel_3.setText(_translate("home", "提醒"))
        self.BodyLabel_tip.setText(_translate("home", "Body label"))
        self.TitleLabel.setText(_translate("home", "日志"))
from qfluentwidgets import BodyLabel, CheckBox, ComboBox, PopUpAniStackedWidget, PushButton, ScrollArea, SimpleCardWidget, StrongBodyLabel, TitleLabel, ToolButton
