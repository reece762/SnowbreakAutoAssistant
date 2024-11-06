# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'additional_features_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_additional_features(object):
    def setupUi(self, additional_features):
        additional_features.setObjectName("additional_features")
        additional_features.resize(721, 675)
        self.gridLayout = QtWidgets.QGridLayout(additional_features)
        self.gridLayout.setContentsMargins(0, 0, 0, 3)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(additional_features)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_fishing = QtWidgets.QWidget()
        self.page_fishing.setObjectName("page_fishing")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_fishing)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SimpleCardWidget = SimpleCardWidget(self.page_fishing)
        self.SimpleCardWidget.setObjectName("SimpleCardWidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.SimpleCardWidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.TitleLabel = TitleLabel(self.SimpleCardWidget)
        self.TitleLabel.setObjectName("TitleLabel")
        self.gridLayout_7.addWidget(self.TitleLabel, 0, 0, 1, 1)
        self.textBrowser_log_fishing = QtWidgets.QTextBrowser(self.SimpleCardWidget)
        self.textBrowser_log_fishing.setStyleSheet("")
        self.textBrowser_log_fishing.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_log_fishing.setObjectName("textBrowser_log_fishing")
        self.gridLayout_7.addWidget(self.textBrowser_log_fishing, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.SimpleCardWidget, 0, 1, 3, 1)
        self.SimpleCardWidget_fish = SimpleCardWidget(self.page_fishing)
        self.SimpleCardWidget_fish.setObjectName("SimpleCardWidget_fish")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.SimpleCardWidget_fish)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.LineEdit_fish_lower = LineEdit(self.SimpleCardWidget_fish)
        self.LineEdit_fish_lower.setObjectName("LineEdit_fish_lower")
        self.gridLayout_5.addWidget(self.LineEdit_fish_lower, 8, 1, 1, 1)
        self.PixmapLabel = PixmapLabel(self.SimpleCardWidget_fish)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PixmapLabel.sizePolicy().hasHeightForWidth())
        self.PixmapLabel.setSizePolicy(sizePolicy)
        self.PixmapLabel.setStyleSheet("")
        self.PixmapLabel.setScaledContents(True)
        self.PixmapLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PixmapLabel.setObjectName("PixmapLabel")
        self.gridLayout_5.addWidget(self.PixmapLabel, 6, 2, 4, 1)
        self.LineEdit_fish_base = LineEdit(self.SimpleCardWidget_fish)
        self.LineEdit_fish_base.setEnabled(False)
        self.LineEdit_fish_base.setObjectName("LineEdit_fish_base")
        self.gridLayout_5.addWidget(self.LineEdit_fish_base, 6, 1, 1, 1)
        self.PushButton_reset = PushButton(self.SimpleCardWidget_fish)
        self.PushButton_reset.setObjectName("PushButton_reset")
        self.gridLayout_5.addWidget(self.PushButton_reset, 9, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 10, 1, 1, 1)
        self.CheckBox_is_save_fish = CheckBox(self.SimpleCardWidget_fish)
        self.CheckBox_is_save_fish.setObjectName("CheckBox_is_save_fish")
        self.gridLayout_5.addWidget(self.CheckBox_is_save_fish, 1, 0, 1, 3)
        self.ComboBox_fishing_mode = ComboBox(self.SimpleCardWidget_fish)
        self.ComboBox_fishing_mode.setObjectName("ComboBox_fishing_mode")
        self.gridLayout_5.addWidget(self.ComboBox_fishing_mode, 0, 1, 1, 2)
        self.BodyLabel_tip_fish = BodyLabel(self.SimpleCardWidget_fish)
        self.BodyLabel_tip_fish.setText("")
        self.BodyLabel_tip_fish.setTextFormat(QtCore.Qt.MarkdownText)
        self.BodyLabel_tip_fish.setWordWrap(True)
        self.BodyLabel_tip_fish.setObjectName("BodyLabel_tip_fish")
        self.gridLayout_5.addWidget(self.BodyLabel_tip_fish, 11, 0, 1, 3)
        self.PrimaryPushButton_get_color = PrimaryPushButton(self.SimpleCardWidget_fish)
        self.PrimaryPushButton_get_color.setObjectName("PrimaryPushButton_get_color")
        self.gridLayout_5.addWidget(self.PrimaryPushButton_get_color, 9, 1, 1, 1)
        self.LineEdit_fish_upper = LineEdit(self.SimpleCardWidget_fish)
        self.LineEdit_fish_upper.setObjectName("LineEdit_fish_upper")
        self.gridLayout_5.addWidget(self.LineEdit_fish_upper, 7, 1, 1, 1)
        self.BodyLabel = BodyLabel(self.SimpleCardWidget_fish)
        self.BodyLabel.setObjectName("BodyLabel")
        self.gridLayout_5.addWidget(self.BodyLabel, 3, 0, 1, 1)
        self.BodyLabel_5 = BodyLabel(self.SimpleCardWidget_fish)
        self.BodyLabel_5.setObjectName("BodyLabel_5")
        self.gridLayout_5.addWidget(self.BodyLabel_5, 6, 0, 1, 1)
        self.BodyLabel_7 = BodyLabel(self.SimpleCardWidget_fish)
        self.BodyLabel_7.setObjectName("BodyLabel_7")
        self.gridLayout_5.addWidget(self.BodyLabel_7, 8, 0, 1, 1)
        self.BodyLabel_6 = BodyLabel(self.SimpleCardWidget_fish)
        self.BodyLabel_6.setObjectName("BodyLabel_6")
        self.gridLayout_5.addWidget(self.BodyLabel_6, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 4, 1, 1, 1)
        self.SpinBox_fish_times = SpinBox(self.SimpleCardWidget_fish)
        self.SpinBox_fish_times.setMinimum(1)
        self.SpinBox_fish_times.setMaximum(99999)
        self.SpinBox_fish_times.setObjectName("SpinBox_fish_times")
        self.gridLayout_5.addWidget(self.SpinBox_fish_times, 3, 1, 1, 2)
        self.BodyLabel_2 = BodyLabel(self.SimpleCardWidget_fish)
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        self.gridLayout_5.addWidget(self.BodyLabel_2, 0, 0, 1, 1)
        self.CheckBox_is_limit_time = CheckBox(self.SimpleCardWidget_fish)
        self.CheckBox_is_limit_time.setObjectName("CheckBox_is_limit_time")
        self.gridLayout_5.addWidget(self.CheckBox_is_limit_time, 2, 0, 1, 3)
        self.StrongBodyLabel = StrongBodyLabel(self.SimpleCardWidget_fish)
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")
        self.gridLayout_5.addWidget(self.StrongBodyLabel, 5, 0, 1, 3)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout_5.setColumnStretch(2, 1)
        self.gridLayout_2.addWidget(self.SimpleCardWidget_fish, 0, 0, 1, 1)
        self.PushButton_start_fishing = PushButton(self.page_fishing)
        self.PushButton_start_fishing.setObjectName("PushButton_start_fishing")
        self.gridLayout_2.addWidget(self.PushButton_start_fishing, 1, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.stackedWidget.addWidget(self.page_fishing)
        self.page_action = QtWidgets.QWidget()
        self.page_action.setObjectName("page_action")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_action)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.PushButton_start_action = PushButton(self.page_action)
        self.PushButton_start_action.setObjectName("PushButton_start_action")
        self.gridLayout_3.addWidget(self.PushButton_start_action, 2, 0, 1, 1)
        self.SimpleCardWidget_action = SimpleCardWidget(self.page_action)
        self.SimpleCardWidget_action.setObjectName("SimpleCardWidget_action")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.SimpleCardWidget_action)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.BodyLabel_4 = BodyLabel(self.SimpleCardWidget_action)
        self.BodyLabel_4.setObjectName("BodyLabel_4")
        self.gridLayout_6.addWidget(self.BodyLabel_4, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem2, 2, 0, 1, 1)
        self.SpinBox_action_times = SpinBox(self.SimpleCardWidget_action)
        self.SpinBox_action_times.setProperty("value", 20)
        self.SpinBox_action_times.setObjectName("SpinBox_action_times")
        self.gridLayout_6.addWidget(self.SpinBox_action_times, 0, 1, 1, 1)
        self.BodyLabel_tip_action = BodyLabel(self.SimpleCardWidget_action)
        self.BodyLabel_tip_action.setText("")
        self.BodyLabel_tip_action.setTextFormat(QtCore.Qt.MarkdownText)
        self.BodyLabel_tip_action.setObjectName("BodyLabel_tip_action")
        self.gridLayout_6.addWidget(self.BodyLabel_tip_action, 1, 0, 1, 2)
        self.gridLayout_3.addWidget(self.SimpleCardWidget_action, 1, 0, 1, 1)
        self.SimpleCardWidget_2 = SimpleCardWidget(self.page_action)
        self.SimpleCardWidget_2.setObjectName("SimpleCardWidget_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.SimpleCardWidget_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.TitleLabel_2 = TitleLabel(self.SimpleCardWidget_2)
        self.TitleLabel_2.setObjectName("TitleLabel_2")
        self.gridLayout_8.addWidget(self.TitleLabel_2, 0, 0, 1, 1)
        self.textBrowser_log_action = QtWidgets.QTextBrowser(self.SimpleCardWidget_2)
        self.textBrowser_log_action.setStyleSheet("")
        self.textBrowser_log_action.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_log_action.setObjectName("textBrowser_log_action")
        self.gridLayout_8.addWidget(self.textBrowser_log_action, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.SimpleCardWidget_2, 1, 1, 2, 1)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.stackedWidget.addWidget(self.page_action)
        self.page_jigsaw = QtWidgets.QWidget()
        self.page_jigsaw.setObjectName("page_jigsaw")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_jigsaw)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.SimpleCardWidget_jigsaw = SimpleCardWidget(self.page_jigsaw)
        self.SimpleCardWidget_jigsaw.setObjectName("SimpleCardWidget_jigsaw")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.SimpleCardWidget_jigsaw)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.LineEdit_jigsaw_piece_11 = LineEdit(self.SimpleCardWidget_jigsaw)
        self.LineEdit_jigsaw_piece_11.setObjectName("LineEdit_jigsaw_piece_11")
        self.gridLayout_10.addWidget(self.LineEdit_jigsaw_piece_11, 13, 2, 1, 1)
        self.SpinBox_max_solutions = SpinBox(self.SimpleCardWidget_jigsaw)
        self.SpinBox_max_solutions.setMinimum(1)
        self.SpinBox_max_solutions.setMaximum(200)
        self.SpinBox_max_solutions.setProperty("value", 10)
        self.SpinBox_max_solutions.setObjectName("SpinBox_max_solutions")
        self.gridLayout_10.addWidget(self.SpinBox_max_solutions, 0, 1, 1, 2)
        self.BodyLabel_tip_jigsaw = BodyLabel(self.SimpleCardWidget_jigsaw)
        self.BodyLabel_tip_jigsaw.setTextFormat(QtCore.Qt.MarkdownText)
        self.BodyLabel_tip_jigsaw.setWordWrap(True)
        self.BodyLabel_tip_jigsaw.setObjectName("BodyLabel_tip_jigsaw")
        self.gridLayout_10.addWidget(self.BodyLabel_tip_jigsaw, 14, 0, 1, 3)
        self.PixmapLabel_best_solution = PixmapLabel(self.SimpleCardWidget_jigsaw)
        self.PixmapLabel_best_solution.setMinimumSize(QtCore.QSize(250, 200))
        self.PixmapLabel_best_solution.setObjectName("PixmapLabel_best_solution")
        self.gridLayout_10.addWidget(self.PixmapLabel_best_solution, 3, 0, 11, 1)
        self.BodyLabel_3 = BodyLabel(self.SimpleCardWidget_jigsaw)
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.gridLayout_10.addWidget(self.BodyLabel_3, 0, 0, 1, 1)
        self.BodyLabel_19 = BodyLabel(self.SimpleCardWidget_jigsaw)
        self.BodyLabel_19.setObjectName("BodyLabel_19")
        self.gridLayout_10.addWidget(self.BodyLabel_19, 12, 1, 1, 1)
        self.BodyLabel_18 = BodyLabel(self.SimpleCardWidget_jigsaw)
        self.BodyLabel_18.setObjectName("BodyLabel_18")
        self.gridLayout_10.addWidget(self.BodyLabel_18, 11, 1, 1, 1)
        self.LineEdit_jigsaw_piece_9 = LineEdit(self.SimpleCardWidget_jigsaw)
        self.LineEdit_jigsaw_piece_9.setObjectName("LineEdit_jigsaw_piece_9")
        self.gridLayout_10.addWidget(self.LineEdit_jigsaw_piece_9, 11, 2, 1, 1)
        self.BodyLabel_17 = BodyLabel(self.SimpleCardWidget_jigsaw)
        self.BodyLabel_17.setObjectName("BodyLabel_17")
        self.gridLayout_10.addWidget(self.BodyLabel_17, 10, 1, 1, 1)
        self.BodyLabel_10 = BodyLabel(self.SimpleCardWidget_jigsaw)
        self.BodyLabel_10.setObjectName("BodyLabel_10")
        self.gridLayout_10.addWidget(self.BodyLabel_10, 3, 1, 1, 1)
        self.LineEdit_jigsaw_piece_4 = LineEdit(self.SimpleCardWidget_jigsaw)
        self.LineEdit_jigsaw_piece_4.setObjectName("LineEdit_jigsaw_piece_4")
        self.gridLayout_10.addWidget(self.LineEdit_jigsaw_piece_4, 6, 2, 1, 1)
        self.LineEdit_jigsaw_piece_3 = LineEdit(self.SimpleCardWidget_jigsaw)
        self.LineEdit_jigsaw_piece_3.setObjectName("LineEdit_jigsaw_piece_3")
        self.gridLayout_10.addWidget(self.LineEdit_jigsaw_piece_3, 5, 2, 1, 1)
        self.BodyLabel_20 = BodyLabel(self.SimpleCardWidget_jigsaw)
        self.BodyLabel_20.setObjectName("BodyLabel_20")
        self.gridLayout_10.addWidget(self.BodyLabel_20, 13, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem3, 15, 0, 1, 1)
        self.LineEdit_jigsaw_piece_1 = LineEdit(self.SimpleCardWidget_jigsaw)
        self.LineEdit_jigsaw_piece_1.setObjectName("LineEdit_jigsaw_piece_1")
        self.gridLayout_10.addWidget(self.LineEdit_jigsaw_piece_1, 3, 2, 1, 1)
        self.BodyLabel_8 = BodyLabel(self.SimpleCardWidget_jigsaw)
        self.BodyLabel_8.setObjectName("BodyLabel_8")
        self.gridLayout_10.addWidget(self.BodyLabel_8, 2, 0, 1, 1)
        self.BodyLabel_11 = BodyLabel(self.SimpleCardWidget_jigsaw)
        self.BodyLabel_11.setObjectName("BodyLabel_11")
        self.gridLayout_10.addWidget(self.BodyLabel_11, 4, 1, 1, 1)
        self.LineEdit_jigsaw_piece_5 = LineEdit(self.SimpleCardWidget_jigsaw)
        self.LineEdit_jigsaw_piece_5.setObjectName("LineEdit_jigsaw_piece_5")
        self.gridLayout_10.addWidget(self.LineEdit_jigsaw_piece_5, 7, 2, 1, 1)
        self.LineEdit_jigsaw_piece_2 = LineEdit(self.SimpleCardWidget_jigsaw)
        self.LineEdit_jigsaw_piece_2.setObjectName("LineEdit_jigsaw_piece_2")
        self.gridLayout_10.addWidget(self.LineEdit_jigsaw_piece_2, 4, 2, 1, 1)
        self.BodyLabel_12 = BodyLabel(self.SimpleCardWidget_jigsaw)
        self.BodyLabel_12.setObjectName("BodyLabel_12")
        self.gridLayout_10.addWidget(self.BodyLabel_12, 5, 1, 1, 1)
        self.LineEdit_jigsaw_piece_6 = LineEdit(self.SimpleCardWidget_jigsaw)
        self.LineEdit_jigsaw_piece_6.setObjectName("LineEdit_jigsaw_piece_6")
        self.gridLayout_10.addWidget(self.LineEdit_jigsaw_piece_6, 8, 2, 1, 1)
        self.LineEdit_jigsaw_piece_7 = LineEdit(self.SimpleCardWidget_jigsaw)
        self.LineEdit_jigsaw_piece_7.setObjectName("LineEdit_jigsaw_piece_7")
        self.gridLayout_10.addWidget(self.LineEdit_jigsaw_piece_7, 9, 2, 1, 1)
        self.BodyLabel_13 = BodyLabel(self.SimpleCardWidget_jigsaw)
        self.BodyLabel_13.setObjectName("BodyLabel_13")
        self.gridLayout_10.addWidget(self.BodyLabel_13, 6, 1, 1, 1)
        self.BodyLabel_16 = BodyLabel(self.SimpleCardWidget_jigsaw)
        self.BodyLabel_16.setObjectName("BodyLabel_16")
        self.gridLayout_10.addWidget(self.BodyLabel_16, 9, 1, 1, 1)
        self.BodyLabel_14 = BodyLabel(self.SimpleCardWidget_jigsaw)
        self.BodyLabel_14.setObjectName("BodyLabel_14")
        self.gridLayout_10.addWidget(self.BodyLabel_14, 7, 1, 1, 1)
        self.BodyLabel_15 = BodyLabel(self.SimpleCardWidget_jigsaw)
        self.BodyLabel_15.setObjectName("BodyLabel_15")
        self.gridLayout_10.addWidget(self.BodyLabel_15, 8, 1, 1, 1)
        self.LineEdit_jigsaw_piece_8 = LineEdit(self.SimpleCardWidget_jigsaw)
        self.LineEdit_jigsaw_piece_8.setObjectName("LineEdit_jigsaw_piece_8")
        self.gridLayout_10.addWidget(self.LineEdit_jigsaw_piece_8, 10, 2, 1, 1)
        self.LineEdit_jigsaw_piece_10 = LineEdit(self.SimpleCardWidget_jigsaw)
        self.LineEdit_jigsaw_piece_10.setObjectName("LineEdit_jigsaw_piece_10")
        self.gridLayout_10.addWidget(self.LineEdit_jigsaw_piece_10, 12, 2, 1, 1)
        self.BodyLabel_9 = BodyLabel(self.SimpleCardWidget_jigsaw)
        self.BodyLabel_9.setObjectName("BodyLabel_9")
        self.gridLayout_10.addWidget(self.BodyLabel_9, 2, 1, 1, 2)
        self.CheckBox_auto_update_pieces_num = CheckBox(self.SimpleCardWidget_jigsaw)
        self.CheckBox_auto_update_pieces_num.setObjectName("CheckBox_auto_update_pieces_num")
        self.gridLayout_10.addWidget(self.CheckBox_auto_update_pieces_num, 1, 0, 1, 3)
        self.gridLayout_10.setColumnStretch(0, 4)
        self.gridLayout_10.setColumnStretch(1, 1)
        self.gridLayout_10.setColumnStretch(2, 1)
        self.gridLayout_4.addWidget(self.SimpleCardWidget_jigsaw, 0, 0, 1, 1)
        self.PushButton_start_jigsaw = PushButton(self.page_jigsaw)
        self.PushButton_start_jigsaw.setObjectName("PushButton_start_jigsaw")
        self.gridLayout_4.addWidget(self.PushButton_start_jigsaw, 1, 0, 1, 1)
        self.SimpleCardWidget_3 = SimpleCardWidget(self.page_jigsaw)
        self.SimpleCardWidget_3.setObjectName("SimpleCardWidget_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.SimpleCardWidget_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.TitleLabel_log_jigsaw = TitleLabel(self.SimpleCardWidget_3)
        self.TitleLabel_log_jigsaw.setObjectName("TitleLabel_log_jigsaw")
        self.gridLayout_9.addWidget(self.TitleLabel_log_jigsaw, 0, 0, 1, 1)
        self.textBrowser_log_jigsaw = QtWidgets.QTextBrowser(self.SimpleCardWidget_3)
        self.textBrowser_log_jigsaw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_log_jigsaw.setObjectName("textBrowser_log_jigsaw")
        self.gridLayout_9.addWidget(self.textBrowser_log_jigsaw, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.SimpleCardWidget_3, 0, 1, 2, 1)
        self.gridLayout_4.setColumnStretch(0, 2)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.stackedWidget.addWidget(self.page_jigsaw)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.SegmentedWidget = SegmentedWidget(additional_features)
        self.SegmentedWidget.setObjectName("SegmentedWidget")
        self.gridLayout.addWidget(self.SegmentedWidget, 0, 0, 1, 1)

        self.retranslateUi(additional_features)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(additional_features)

    def retranslateUi(self, additional_features):
        _translate = QtCore.QCoreApplication.translate
        additional_features.setWindowTitle(_translate("additional_features", "Frame"))
        self.TitleLabel.setText(_translate("additional_features", "日志"))
        self.PushButton_reset.setText(_translate("additional_features", "重置"))
        self.CheckBox_is_save_fish.setText(_translate("additional_features", "是否保存新纪录截图"))
        self.PrimaryPushButton_get_color.setText(_translate("additional_features", "校准颜色"))
        self.BodyLabel.setText(_translate("additional_features", "钓鱼次数："))
        self.BodyLabel_5.setText(_translate("additional_features", "基准HSV值"))
        self.BodyLabel_7.setText(_translate("additional_features", "颜色查找下限"))
        self.BodyLabel_6.setText(_translate("additional_features", "颜色查找上限"))
        self.BodyLabel_2.setText(_translate("additional_features", "钓鱼模式"))
        self.CheckBox_is_limit_time.setText(_translate("additional_features", "是否限制单次收杆时间间隔上限"))
        self.StrongBodyLabel.setText(
            _translate("additional_features", "校准完美收杆区域HSV（当收杆出错，日志说黄色块大于2时用）"))
        self.PushButton_start_fishing.setText(_translate("additional_features", "开始钓鱼"))
        self.PushButton_start_action.setText(_translate("additional_features", "开始行动"))
        self.BodyLabel_4.setText(_translate("additional_features", "刷取次数"))
        self.TitleLabel_2.setText(_translate("additional_features", "日志"))
        self.BodyLabel_tip_jigsaw.setText(_translate("additional_features", "Body label"))
        self.BodyLabel_3.setText(_translate("additional_features", "寻找最大方案数："))
        self.BodyLabel_19.setText(_translate("additional_features", "10号碎片"))
        self.BodyLabel_18.setText(_translate("additional_features", "9号碎片"))
        self.BodyLabel_17.setText(_translate("additional_features", "8号碎片"))
        self.BodyLabel_10.setText(_translate("additional_features", "1号碎片"))
        self.BodyLabel_20.setText(_translate("additional_features", "11号碎片"))
        self.BodyLabel_8.setText(_translate("additional_features", "当前寻找到的最优方案："))
        self.BodyLabel_11.setText(_translate("additional_features", "2号碎片"))
        self.BodyLabel_12.setText(_translate("additional_features", "3号碎片"))
        self.BodyLabel_13.setText(_translate("additional_features", "4号碎片"))
        self.BodyLabel_16.setText(_translate("additional_features", "7号碎片"))
        self.BodyLabel_14.setText(_translate("additional_features", "5号碎片"))
        self.BodyLabel_15.setText(_translate("additional_features", "6号碎片"))
        self.BodyLabel_9.setText(_translate("additional_features", "当前用户碎片数量："))
        self.CheckBox_auto_update_pieces_num.setText(_translate("additional_features", "是否自动获取当前碎片数量"))
        self.PushButton_start_jigsaw.setText(_translate("additional_features", "开始拼图"))
        self.TitleLabel_log_jigsaw.setText(_translate("additional_features", "日志"))


from qfluentwidgets import BodyLabel, CheckBox, ComboBox, LineEdit, PixmapLabel, PrimaryPushButton, PushButton, \
    SegmentedWidget, SimpleCardWidget, SpinBox, StrongBodyLabel, TitleLabel
