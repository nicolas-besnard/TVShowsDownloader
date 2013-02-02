#from PySide.QtCore import *
#from PySide.QtGui import *
from PyQt4 import QtCore, QtGui
import sys
from window import *

app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)


#list
item = QtGui.QListWidgetItem("test")
item.setData(5, 'toto')
ui.listWidget.insertItem(0, item)

#list box
catList = ui.comboBox
catList.addItem("All", 0)
catList.addItem("HD - TV Shows", 208)

#search
def fn_btn_search():
    """
    """
    #search field
    search_field = ui.textEdit

    #cat field
    cat_field = ui.comboBox
    search_value = search_field.toPlainText()
    cat_value = cat_field.currentText()
    cat_nb_value = cat_field.itemData(cat_field.currentIndex()).toString()
    print "Search : "+ search_value
    print "Cat : "+ cat_value +"["+ cat_nb_value +"]"
    print ui.listWidget.currentItem().text()
    print ui.listWidget.currentItem().data(5).toString()


btn_search = ui.pushButton
btn_search.clicked.connect(fn_btn_search)


MainWindow.show()
sys.exit(app.exec_())

