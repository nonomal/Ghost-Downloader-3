# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdateDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QHBoxLayout,
                               QSizePolicy, QVBoxLayout, QAbstractItemView, QHeaderView)

from qfluentwidgets import (PillPushButton, PrimaryPushButton, PushButton, StrongBodyLabel,
                            SubtitleLabel, TextEdit, TableWidget, FluentIcon)

class Ui_UpdateDialog(object):
    def setupUi(self, UpdateDialog):
        if not UpdateDialog.objectName():
            UpdateDialog.setObjectName(u"UpdateDialog")
        UpdateDialog.resize(681, 721)
        self.verticalLayout = QVBoxLayout(UpdateDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(11)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.titleLabel = SubtitleLabel(UpdateDialog)
        self.titleLabel.setObjectName(u"titleLabel")

        self.horizontalLayout.addWidget(self.titleLabel)

        self.versionLabel = StrongBodyLabel(UpdateDialog)
        self.versionLabel.setObjectName(u"versionLabel")

        self.horizontalLayout.addWidget(self.versionLabel)

        self.updatedDateLabel = StrongBodyLabel(UpdateDialog)
        self.updatedDateLabel.setObjectName(u"updatedDateLabel")

        self.horizontalLayout.addWidget(self.updatedDateLabel)

        self.horizontalLayout.addSpacing(16777215)

        self.sponsorButton = PillPushButton(UpdateDialog)
        self.sponsorButton.setObjectName(u"sponsorButton")
        self.sponsorButton.setProperty("hasIcon", True)
        self.sponsorButton.setIcon(FluentIcon.HEART)

        self.horizontalLayout.addWidget(self.sponsorButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.logTextEdit = TextEdit(UpdateDialog)
        self.logTextEdit.setObjectName(u"logTextEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logTextEdit.sizePolicy().hasHeightForWidth())
        self.logTextEdit.setSizePolicy(sizePolicy)
        self.logTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.logTextEdit)

        self.tableView = TableWidget(UpdateDialog)
        
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFixedHeight(150)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        # sizePolicy1.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy1)
        
        self.tableView.setBorderVisible(True)
        self.tableView.setBorderRadius(8)
        self.tableView.setWordWrap(False)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)  # ReadOnly
        self.tableView.setColumnCount(3)
        self.tableView.verticalHeader().setVisible(False)  # 隐藏垂直表头
        self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)  # 第一列拉伸

        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.noButton = PushButton(UpdateDialog)
        self.noButton.setObjectName(u"noButton")

        self.horizontalLayout_2.addWidget(self.noButton)

        self.yesButton = PrimaryPushButton(UpdateDialog)
        self.yesButton.setObjectName(u"yesButton")

        self.horizontalLayout_2.addWidget(self.yesButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(UpdateDialog)

        QMetaObject.connectSlotsByName(UpdateDialog)
    # setupUi

    def retranslateUi(self, UpdateDialog):
        UpdateDialog.setWindowTitle(QCoreApplication.translate("UpdateDialog", u"Dialog", None))
        self.titleLabel.setText(QCoreApplication.translate("UpdateDialog", u"\u68c0\u6d4b\u5230\u65b0\u7248\u672c", None))
        self.versionLabel.setText("")
        self.updatedDateLabel.setText("")
        self.sponsorButton.setText(QCoreApplication.translate("UpdateDialog", u"Sponsor", None))
        self.logTextEdit.setMarkdown("")

        self.noButton.setText(QCoreApplication.translate("UpdateDialog", u"\u7a0d\u540e\u518d\u8bf4", None))
        self.yesButton.setText(QCoreApplication.translate("UpdateDialog", u"\u4e0b\u8f7d\u6b64\u7248\u672c", None))
    # retranslateUi

