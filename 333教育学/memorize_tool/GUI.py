from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from MyConst import *
from JsonFunc import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.add = Add()
        self.select = Select()
        self.memorize = Memorize()
        self.button_add = QPushButton(self)
        self.button_select = QPushButton(self)
        self.button_memorize = QPushButton(self)
        self.initUI()

    def initUI(self):
        self.move(600, 400)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.button_memorize.setText("背诵")
        self.button_memorize.setFont(CuzFont)
        self.button_memorize.setGeometry(QRect((WINDOW_WIDTH - BUTTON_WIDTH) // 2, MARGIN
                                               , BUTTON_WIDTH, BUTTON_HEIGHT))
        self.button_select.setText("查找数据")
        self.button_select.setFont(CuzFont)
        self.button_select.setGeometry(QRect((WINDOW_WIDTH - BUTTON_WIDTH) // 2, MARGIN * 2 + BUTTON_HEIGHT
                                             , BUTTON_WIDTH, BUTTON_HEIGHT))
        self.button_add.setText("添加数据")
        self.button_add.setFont(CuzFont)
        self.button_add.setGeometry(QRect((WINDOW_WIDTH - BUTTON_WIDTH) // 2, MARGIN * 3 + 2 * BUTTON_HEIGHT
                                          , BUTTON_WIDTH, BUTTON_HEIGHT))

        self.button_memorize.clicked.connect(self.memorize.show)

        self.button_select.clicked.connect(self.select.show)

        self.button_add.clicked.connect(self.add.show)

        self.show()


class Memorize(QWidget):
    def __init__(self):
        super().__init__()
        self.data_dict_list = get_memorize_data()
        self.label_data = QLabel(self)
        self.button_right = QPushButton(self)
        self.button_left = QPushButton(self)
        self.label_pos_info = QLabel(self)
        self.label_countdown_info = QLabel(self)
        self.label_unit_info = QLabel(self)
        self.label_book_info = QLabel(self)
        self.label_time_info = QLabel(self)
        self.button_start = QPushButton(self)
        self.pos = 0
        self.initUI()

    def initUI(self):
        self.resize(MEMORIZE_WIDTH, MEMORIZE_HEIGHT)

        self.button_start.setText("开始")
        self.button_start.setFont(CuzFont)
        self.button_start.setGeometry(
            QRect((MEMORIZE_WIDTH - BUTTON_WIDTH) // 2, MEMORIZE_HEIGHT - MARGIN - BUTTON_HEIGHT,
                  BUTTON_WIDTH, BUTTON_HEIGHT))
        self.button_start.clicked.connect(self.memorizeButtonClicked)

        self.label_time_info.setFont(CuzFont)
        self.label_time_info.setText("当前学习天数为:" + str(get_cur_time()))
        self.label_time_info.setGeometry(QRect(MARGIN, MEMORIZE_HEIGHT - MARGIN - COMMON_HEIGHT,
                                               MEMORIZE_LABEL_TIME_INFO_WIDTH, COMMON_HEIGHT))

        self.label_book_info.setFont(CuzFont)
        self.label_book_info.setText("当前科目为:")
        self.label_book_info.setGeometry(QRect(MARGIN, MARGIN, MEMORIZE_LABEL_BOOK_INFO_WIDTH, COMMON_HEIGHT))

        self.label_unit_info.setFont(CuzFont)
        self.label_unit_info.setText("当前单元为:")
        self.label_unit_info.setGeometry(QRect(MARGIN + MEMORIZE_LABEL_BOOK_INFO_WIDTH, MARGIN,
                                               MEMORIZE_LABEL_UNIT_INFO_WIDTH, COMMON_HEIGHT))

        self.label_countdown_info.setFont(CuzFont)
        self.label_countdown_info.setText("当前为 天前的内容")
        self.label_countdown_info.setGeometry(QRect(MARGIN, 2 * MARGIN + COMMON_HEIGHT,
                                                    MEMORIZE_LABEL_COUNTDOWN_INFO_WIDTH, COMMON_HEIGHT))

        self.label_pos_info.setFont(CuzFont)
        self.label_pos_info.setText("当前进度为:0/0")
        self.label_pos_info.setGeometry(
            QRect(2 * MARGIN + MEMORIZE_LABEL_COUNTDOWN_INFO_WIDTH, 2 * MARGIN + COMMON_HEIGHT,
                  MEMORIZE_LABEL_POS_INFO_WIDTH, COMMON_HEIGHT))

        self.button_left.setText('<')
        self.button_left.setFont(largeFont)
        self.button_left.setGeometry(QRect(MARGIN, (MEMORIZE_HEIGHT - BUTTON_CHANGE_HEIGHT) // 2,
                                           BUTTON_CHANGE_WIDTH, BUTTON_CHANGE_HEIGHT))
        self.button_left.clicked.connect(self.leftClicked)

        self.button_right.setText('>')
        self.button_right.setFont(largeFont)
        self.button_right.setGeometry(
            QRect(MEMORIZE_WIDTH - MARGIN - BUTTON_CHANGE_WIDTH, (MEMORIZE_HEIGHT - BUTTON_CHANGE_HEIGHT) // 2,
                  BUTTON_CHANGE_WIDTH, BUTTON_CHANGE_HEIGHT))
        self.button_right.clicked.connect(self.rightClicked)

        self.label_data.setWordWrap(True)
        self.label_data.setFont(largeFont)
        self.label_data.setAlignment(Qt.AlignCenter)
        self.label_data.setGeometry(QRect(2 * MARGIN + BUTTON_CHANGE_WIDTH, 3 * MARGIN + 2 * COMMON_HEIGHT,
                                          MEMORIZE_WIDTH - 4 * MARGIN - 2 * BUTTON_CHANGE_WIDTH,
                                          MEMORIZE_HEIGHT - 5 * MARGIN - BUTTON_HEIGHT - 2 * COMMON_HEIGHT))

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            # 16777220 = Enter key
            if self.button_right.isEnabled():
                self.button_right.click()


    def memorizeButtonClicked(self):
        self.set_data_pos(0)

    def set_data_pos(self, pos):
        data_dict = self.data_dict_list[pos]
        self.pos = pos
        self.label_book_info.setText("当前科目为:" + data_dict["book_name"])
        self.label_unit_info.setText("当前单元为: Unit" + str(data_dict["unit"]) + ' ' + data_dict["desc"])
        self.label_countdown_info.setText("当前为" + str(data_dict["repeat_interval"]) + "天前的内容")
        self.label_pos_info.setText("当前进度为:" + str(pos + 1) + "/" + str(len(self.data_dict_list)))
        self.label_data.setText(data_dict["data"])
        if pos == 0:
            self.button_left.setEnabled(False)
        else:
            self.button_left.setEnabled(True)
        if pos == len(self.data_dict_list) - 1:
            self.button_right.setEnabled(False)
        else:
            self.button_right.setEnabled(True)

    def leftClicked(self):
        self.set_data_pos(self.pos - 1)

    def rightClicked(self):
        self.set_data_pos(self.pos + 1)


class Select(QWidget):
    def __init__(self):
        super().__init__()
        self.label_data = QLabel(self)
        self.button_right = QPushButton(self)
        self.button_left = QPushButton(self)
        self.comboBox_select_unit = QComboBox(self)
        self.label_unit_info = QLabel(self)
        self.comboBox_select_book = QComboBox(self)
        self.label_select_book = QLabel(self)
        self.book_data = []
        self.combo_index_list = []
        self.unit_data_dict_list = []
        self.pos = 0
        self.initUI()
        self.comboBoxIndexChanged()

    def initUI(self):
        self.resize(SELECT_WIDTH, SELECT_HEIGHT)

        self.label_select_book.setText("选择要查找内容的学科：")
        self.label_select_book.setFont(CuzFont)
        self.label_select_book.setGeometry(QRect(MARGIN, MARGIN,
                                                 SELECT_LABEL_SELECT_BOOK_WIDTH, COMMON_HEIGHT))

        self.comboBox_select_book.addItems(get_book_name())
        self.comboBox_select_book.setFont(CuzFont)
        self.comboBox_select_book.setGeometry(QRect(MARGIN + SELECT_LABEL_SELECT_BOOK_WIDTH, MARGIN,
                                                    SELECT_COMBOBOX_SELECT_BOOK_WIDTH, COMMON_HEIGHT))
        self.comboBox_select_book.currentIndexChanged.connect(self.comboBoxIndexChanged)

        self.label_unit_info.setText("选择要查找内容的单元：")
        self.label_unit_info.setFont(CuzFont)
        self.label_unit_info.setGeometry(
            QRect(2 * MARGIN + SELECT_LABEL_SELECT_BOOK_WIDTH + SELECT_COMBOBOX_SELECT_BOOK_WIDTH,
                  MARGIN, SELECT_LABEL_UNIT_INFO_WIDTH, COMMON_HEIGHT))

        self.comboBox_select_unit.setFont(CuzFont)
        self.comboBox_select_unit.setGeometry(QRect(
            2 * MARGIN + SELECT_LABEL_SELECT_BOOK_WIDTH + SELECT_COMBOBOX_SELECT_BOOK_WIDTH + SELECT_LABEL_UNIT_INFO_WIDTH,
            MARGIN, SELECT_COMBOBOX_SELECT_UNIT_WIDTH, COMMON_HEIGHT))
        self.comboBox_select_unit.currentIndexChanged.connect(self.unitIndexChanged)

        self.button_left.setText('<')
        self.button_left.setFont(largeFont)
        self.button_left.setGeometry(QRect(MARGIN, (SELECT_HEIGHT - BUTTON_CHANGE_HEIGHT) // 2,
                                           BUTTON_CHANGE_WIDTH, BUTTON_CHANGE_HEIGHT))
        self.button_left.clicked.connect(self.leftClicked)

        self.button_right.setText('>')
        self.button_right.setFont(largeFont)
        self.button_right.setGeometry(
            QRect(SELECT_WIDTH - MARGIN - BUTTON_CHANGE_WIDTH, (SELECT_HEIGHT - BUTTON_CHANGE_HEIGHT) // 2,
                  BUTTON_CHANGE_WIDTH, BUTTON_CHANGE_HEIGHT))
        self.button_right.clicked.connect(self.rightClicked)

        self.label_data.setWordWrap(True)
        self.label_data.setFont(largeFont)
        self.label_data.setText("测试信息")
        self.label_data.setAlignment(Qt.AlignCenter)
        self.label_data.setGeometry(QRect(2 * MARGIN + BUTTON_CHANGE_WIDTH, 2 * MARGIN + COMMON_HEIGHT,
                                          SELECT_WIDTH - 4 * MARGIN - 2 * BUTTON_CHANGE_WIDTH,
                                          SELECT_HEIGHT - 2 * (2 * MARGIN + COMMON_HEIGHT)))

    def comboBoxIndexChanged(self):
        self.book_data = get_book_data(self.comboBox_select_book.currentText())
        self.initData()
        self.comboBox_select_unit.clear()
        for data_dict in self.book_data:
            self.comboBox_select_unit.addItem(data_dict["unit_info"])
        self.set_data_pos(0)

    def initData(self):
        self.combo_index_list = []
        self.unit_data_dict_list = []
        cnt = 0
        for data_dict in self.book_data:
            self.combo_index_list.append(cnt)
            for data_item in data_dict["data"]:
                cnt += 1
                self.unit_data_dict_list.append({"unit_index": len(self.combo_index_list) - 1, "data": data_item})

    def set_data_pos(self, pos):
        self.pos = pos
        self.comboBox_select_unit.setCurrentIndex(self.unit_data_dict_list[pos]["unit_index"])
        self.label_data.setText(self.unit_data_dict_list[pos]["data"])
        if pos == 0:
            self.button_left.setEnabled(False)
        else:
            self.button_left.setEnabled(True)
        if pos == len(self.unit_data_dict_list) - 1:
            self.button_right.setEnabled(False)
        else:
            self.button_right.setEnabled(True)

    def leftClicked(self):
        self.set_data_pos(self.pos - 1)

    def rightClicked(self):
        self.set_data_pos(self.pos + 1)

    def unitIndexChanged(self):
        self.set_data_pos(self.combo_index_list[self.comboBox_select_unit.currentIndex()])

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            # 16777220 = Enter key
            if self.button_right.isEnabled():
                self.button_right.click()


class Add(QWidget):
    def __init__(self):
        super().__init__()
        self.lineEdit_time_info = QLineEdit(self)
        self.label_time_info = QLabel(self)
        self.textEdit_main_data = QTextEdit(self)
        self.lineEdit_unit_desc = QLineEdit(self)
        self.lineEdit_unit_info = QLineEdit(self)
        self.label_unit_info = QLabel(self)
        self.comboBox_select_book = QComboBox(self)
        self.label_select_book = QLabel(self)
        self.button_add_data = QPushButton(self)
        self.cur_book_name = ""
        self.initUI()

    def initUI(self):
        self.resize(ADD_WIDTH, ADD_HEIGHT)

        self.button_add_data.setText("添加")
        self.button_add_data.setFont(CuzFont)
        self.button_add_data.setGeometry(QRect((ADD_WIDTH - BUTTON_WIDTH) // 2, ADD_HEIGHT - BUTTON_HEIGHT - MARGIN,
                                               BUTTON_WIDTH, BUTTON_HEIGHT))
        self.button_add_data.clicked.connect(self.addButtonClicked)

        self.label_select_book.setText("选择添加内容的学科：")
        self.label_select_book.setFont(CuzFont)
        self.label_select_book.setGeometry(QRect(MARGIN, MARGIN,
                                                 ADD_LABEL_SELECT_BOOK_WIDTH, COMMON_HEIGHT))

        self.comboBox_select_book.addItems(get_book_name())
        self.comboBox_select_book.setFont(CuzFont)
        self.comboBox_select_book.setGeometry(QRect(MARGIN + ADD_LABEL_SELECT_BOOK_WIDTH, MARGIN,
                                                    ADD_COMBOBOX_SELECT_BOOK_WIDTH, COMMON_HEIGHT))
        self.comboBox_select_book.currentIndexChanged.connect(self.comboBoxIndexChanged)

        self.cur_book_name = self.comboBox_select_book.currentText()
        self.label_unit_info.setText("当前添加的内容为 Unit")
        self.label_unit_info.setFont(CuzFont)
        self.label_unit_info.setGeometry(
            QRect(2 * MARGIN + ADD_LABEL_SELECT_BOOK_WIDTH + ADD_COMBOBOX_SELECT_BOOK_WIDTH, MARGIN,
                  ADD_LABEL_UNIT_INFO_WIDTH, COMMON_HEIGHT))

        self.lineEdit_unit_info.setText(str(get_book_blank_unit(self.cur_book_name)))
        self.lineEdit_unit_info.setFont(CuzFont)
        self.lineEdit_unit_info.setGeometry(
            QRect(2 * MARGIN + ADD_LABEL_SELECT_BOOK_WIDTH + ADD_COMBOBOX_SELECT_BOOK_WIDTH + ADD_LABEL_UNIT_INFO_WIDTH
                  , MARGIN, ADD_LINEEDIT_UNIT_INFO_WIDTH, COMMON_HEIGHT))

        self.lineEdit_unit_desc.setText("description")
        self.lineEdit_unit_desc.setStyleSheet("color: rgb(160,160,160);")
        self.lineEdit_unit_desc.setFont(CuzFont)
        self.lineEdit_unit_desc.setGeometry(QRect(
            2.4 * MARGIN + ADD_LABEL_SELECT_BOOK_WIDTH + ADD_COMBOBOX_SELECT_BOOK_WIDTH + ADD_LABEL_UNIT_INFO_WIDTH + ADD_LINEEDIT_UNIT_INFO_WIDTH,
            MARGIN, ADD_LINEEDIT_UNIT_DESC_WIDTH, COMMON_HEIGHT))
        self.lineEdit_unit_desc.textChanged.connect(self.lineEditTextChanged)

        self.textEdit_main_data.setFont(CuzFont)
        self.textEdit_main_data.setGeometry(QRect(MARGIN, 2 * MARGIN + COMMON_HEIGHT, ADD_WIDTH - 2 * MARGIN,
                                                  ADD_HEIGHT - 4 * MARGIN - COMMON_HEIGHT - BUTTON_HEIGHT))

        self.label_time_info.setFont(CuzFont)
        self.label_time_info.setText("当前学习天数为:")
        self.label_time_info.setGeometry(QRect(MARGIN, ADD_HEIGHT - COMMON_HEIGHT - MARGIN,
                                               ADD_LABEL_TIME_INFO_WIDTH, COMMON_HEIGHT))

        self.lineEdit_time_info.setFont(CuzFont)
        self.lineEdit_time_info.setText(str(get_cur_time()))
        self.lineEdit_time_info.setGeometry(
            QRect(MARGIN + ADD_LABEL_TIME_INFO_WIDTH, ADD_HEIGHT - COMMON_HEIGHT - MARGIN,
                  ADD_LINEEDIT_TIME_INFO_WIDTH, COMMON_HEIGHT))

    def comboBoxIndexChanged(self):
        self.cur_book_name = self.comboBox_select_book.currentText()
        self.lineEdit_unit_info.setText(str(get_book_blank_unit(self.cur_book_name)))

    def lineEditTextChanged(self):
        self.lineEdit_unit_desc.setStyleSheet("color: rgb(0,0,0);")

    def addButtonClicked(self):
        unit = int(self.lineEdit_unit_info.text())
        time = int(self.lineEdit_time_info.text())
        desc = self.lineEdit_unit_desc.text()
        if desc == "description" or desc == "":
            QMessageBox.about(self, "Alert", "单元描述不能为空，请重新输入")
            return
        main_data = self.textEdit_main_data.toPlainText()
        if main_data == "":
            QMessageBox.about(self, "Alert", "内容不能为空，请重新输入")
            return
        main_data_lines = main_data.strip().split('\n')
        # print(main_data_lines)
        add_data_to_json(self.cur_book_name, time, unit, desc, main_data_lines)
        QMessageBox.about(self, "Alert", "添加成功！")
        return
