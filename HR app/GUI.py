
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
import sys
import time
import random
import hexdump
import linecache



def_data = {"employees": ["john", "mike", "marry", "chris" , "aaron" , "paul"],
     "salaries":         [ 4000,   1000, 50000, 10000,30000,50000],
     "qualifications":   ["GCSE,BSc", "GCSE", "GCSE, BSc,Msc,PhD", "GCSE,B.E", "MBA", "GCSE,BSc,Msc,PhD"],
     "departments":      ["IT", "HR", 'Academic', "IT", "HR", "reserach"],
     }
class PersonalInfo:
    def __init__(self, name: str, salary: int, qualifications, departaments):
        self.name = name
        self.salary = salary
        self.qualifications = qualifications
        self.departaments = departaments

    def __str__(self) -> str:
        return "\n{\n name: " + self.name + ",\t\n salary: " + str(self.salary) + ",\t\n qualifications: " + str(self.qualifications) + ",\t\n departments: " + str(self.departaments) + "\n}"
        

def getDB():
    database  = dict()
    for i, person in enumerate(def_data["employees"]):
        database[person] = PersonalInfo(
                                 name = def_data["employees"][i], 
                                 salary = def_data["salaries"][i],
                                 qualifications = def_data["qualifications"][i].split(','),
                                 departaments = def_data["departments"][i]
             )
    return database    


def emp(y):
    my_string =''
    for x in y:
        my_string += ' ,'+ x
    return my_string

def indexing(name):
    for i in range(len(def_data["employees"])):
        if name == def_data["employees"][i]:
            return i







class security():
    def encrypt(key, plaintext):
        
        plaintext = list(plaintext)#Convert the plaintext to a list of characters
        random.seed(key)
        
        keystream = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(len(plaintext))]# Generate a random stream of characters to use as the keystream
        
        
        ciphertext = [chr(ord(a) ^ ord(b)) for (a, b) in zip(plaintext, keystream)]# Perform the encryption by XORing the plaintext with the keystream
        
        return ''.join(ciphertext)

    def decrypt(key, ciphertext):
        random.seed(key)
        
        keystream = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(len(ciphertext))]# Generate the keystream using the same method as the encrypt() function
        
        
        plaintext = [chr(ord(a) ^ ord(b)) for (a, b) in zip(ciphertext, keystream)]# Decrypt the ciphertext by XORing it with the keystream
        
        return ''.join(plaintext)






class LoginWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Login')
        self.setWindowIcon(QIcon(''))
        self.window_width, self.window_height = 600, 200
        self.setFixedSize(self.window_width, self.window_height)

        layout = QGridLayout()
        self.setLayout(layout)

        labels = {}
        self.lineEdits = {}

        labels['Username'] = QLabel('Username')
        labels['Password'] = QLabel('Password')

        self.lineEdits['Username'] = QLineEdit()
        self.lineEdits['Password'] = QLineEdit()
        self.lineEdits['Password'].setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(labels['Username'],            0, 0, 1, 1)
        layout.addWidget(self.lineEdits['Username'],    0, 1, 1, 3)

        layout.addWidget(labels['Password'],            1, 0, 1, 1)
        layout.addWidget(self.lineEdits['Password'],    1, 1, 1, 3)

        button_login = QPushButton('&Log In', clicked=self.checkCredential)
        layout.addWidget(button_login,                  2, 3, 1, 1)

        self.status = QLabel('')
        self.status.setStyleSheet('font-size: 25px; color: red;')
        layout.addWidget(self.status,                   3, 0, 1, 3)




    def checkCredential(self):
        username = self.lineEdits['Username'].text()
        password = self.lineEdits['Password'].text()

        
        f = linecache.getline(r"database.txt", 1)
        l = linecache.getline(r"database.txt", 2)
        if username == security.decrypt(2137, f):
            if password == security.decrypt(2137, l):
                time.sleep(1)
                self.mainApp = Window()
                self.mainApp.show()
                self.close()
            else:
                self.status.setText('incorrect password or username')
        else:
            self.status.setText('incorrect password or username')                

class SearchButton(QPushButton):
    def __init__(self, parent=None):
        QPushButton.__init__(self)
        self.clicked.connect(self.update_text)
        self.parent_component = parent

    def update_text(self):
        text = self.parent_component.get_info()
        if text:
            self.parent_component.setPlaceholder(text)
  

# Subclass QMainWindow to customize application's main window
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QGridLayout()
        self.setLayout(self.layout)


        self.db = getDB()

        self.setWindowTitle("Employee database")


        self.searchbar = QLineEdit(self)
        self.completer = QCompleter(list(self.db.keys()))
        self.searchbar.setCompleter(self.completer)

        self.textHolder = QLabel()
        self.textHolder.setFixedSize(QSize(300,200))

        self.button = SearchButton(self)
        self.addbutton = QPushButton("add", clicked=self.addEmployee)
        self.deletebutton = QPushButton("delete", clicked=self.deleteEmployee)
        self.editbutton = QPushButton("edit",clicked=self.editEmployee)


        # Set the central widget of the Window.
        self.layout.addWidget(self.searchbar,       0, 0)
        self.layout.addWidget(self.textHolder,      1, 0)
        self.layout.addWidget(self.button,          0, 1)
        self.layout.addWidget(self.addbutton,       1, 1)
        self.layout.addWidget(self.deletebutton,    2, 1)
        self.layout.addWidget(self.editbutton,      3, 1)
    
    def get_info(self):
        query = self.searchbar.text()
        if query in self.db:
            return self.db[query]
        else:
            return None


    def setPlaceholder(self, content):
        self.textHolder.setText(content.__str__())

    def addEmployee(self):
        self.mainApp = addingWindow()
        self.mainApp.show()
        self.close()

    def deleteEmployee(self):
        self.mainApp = deleteWindow()
        self.mainApp.show()
        self.close()

    def editEmployee(self):
        self.mainApp = editingWindow()
        self.mainApp.show()
        self.close()
        
  


class addingWindow(QWidget):
    db1 = def_data
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('adding an employee')
        self.setWindowIcon(QIcon(''))
        self.window_width, self.window_height = 600, 200
        self.setFixedSize(self.window_width, self.window_height)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.textHolder = QLabel("name")
        self.textHolder.setFixedSize(QSize(200,40))
        self.searchbar = QLineEdit(self)

        self.textHolder1 = QLabel("salary")
        self.textHolder1.setFixedSize(QSize(200,40))
        self.searchbar1 = QLineEdit(self)

        self.textHolder2 = QLabel("qualifications")
        self.textHolder2.setFixedSize(QSize(200,40))
        self.searchbar2 = QLineEdit(self)

        self.textHolder3 = QLabel("department")
        self.textHolder3.setFixedSize(QSize(200,40))
        self.searchbar3 = QLineEdit(self)

        self.layout.addWidget(self.textHolder,      0, 0, 1, 1)
        self.layout.addWidget(self.searchbar,       0, 1, 1, 3)

        self.layout.addWidget(self.textHolder1,     1, 0, 1, 1)
        self.layout.addWidget(self.searchbar1,      1, 1, 1, 3)

        self.layout.addWidget(self.textHolder2,     2, 0, 1, 1)
        self.layout.addWidget(self.searchbar2,      2, 1, 1, 3)

        self.layout.addWidget(self.textHolder3,     3, 0, 1, 1)
        self.layout.addWidget(self.searchbar3,      3, 1, 1, 3)
        
        self.savebutton = QPushButton('save', clicked=self.saving)

        self.layout.addWidget(self.savebutton,      4, 3, 1, 1)

        self.returnbutton = QPushButton('return', clicked=self.returning)

        self.layout.addWidget(self.returnbutton,    4, 2, 1, 1)
        
    def saving(self):
        name = self.searchbar.text()
        salary = int(self.searchbar1.text())
        qualifications = self.searchbar2.text()
        department = self.searchbar3.text()

        def_data["employees"].append(name)
        def_data["salaries"].append(salary)
        def_data["qualifications"].append(qualifications)
        def_data["departments"].append(department)

        self.mainApp = Window()
        self.mainApp.show()
        self.close()

    def returning(self):
        self.mainApp = Window()
        self.mainApp.show()
        self.close()    


class deleteWindow(QWidget):
    db1 = def_data
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('deleting an employee')
        self.setWindowIcon(QIcon(''))
        self.window_width, self.window_height = 800, 400
        self.setFixedSize(self.window_width, self.window_height)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.db = getDB()

        self.deletingemployee = QLineEdit(self)
        self.completer = QCompleter(list(self.db.keys()))
        self.deletingemployee.setCompleter(self.completer)
        
        self.textHolder2 = QLabel("what employee you wanna delete?")

        self.layout.addWidget(self.deletingemployee,       0, 0)
        self.layout.addWidget(self.textHolder2,            0, 1)

        self.savebutton = QPushButton('save changes', clicked=self.deleting)

        self.layout.addWidget(self.savebutton,       2, 1)

        self.returnbutton = QPushButton('return', clicked=self.returning)

        self.layout.addWidget(self.returnbutton,       2, 0)
        
        
    def deleting(self):
        name = self.deletingemployee.text()
        
        i = indexing(name)
        def_data["employees"].pop(i)
        def_data["departments"].pop(i)
        def_data["qualifications"].pop(i)
        def_data["salaries"].pop(i)
        
        self.mainApp = Window()
        self.mainApp.show()
        self.close()

    def returning(self):
        self.mainApp = Window()
        self.mainApp.show()
        self.close()        



class editingWindow(QWidget):
    db1 = def_data
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('editing an employee')
        self.setWindowIcon(QIcon(''))
        self.window_width, self.window_height = 800, 200
        self.setFixedSize(self.window_width, self.window_height)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.db = getDB()

        self.textHolder = QLabel("what employee you wanna edit ")
        self.textHolder.setFixedSize(QSize(300,40))

        self.searchbar = QLineEdit(self)
        self.completer = QCompleter(list(self.db.keys()))
        self.searchbar.setCompleter(self.completer)
        
        self.editbutton = QPushButton("edit",clicked=self.edit)

        self.layout.addWidget(self.textHolder,       0, 0, 1, 1)
        self.layout.addWidget(self.searchbar,        0, 1, 1, 3)
        self.layout.addWidget(self.editbutton,       5, 1, 1, 3)
        
        
        
    def edit(self):
        name = self.searchbar.text()
        self.i = indexing(name)
        
        
        
        print(def_data["employees"][self.i])




        self.textHolder1 = QLabel("name")
        self.textHolder1.setFixedSize(QSize(300,40))
        self.searchbar1 = QLineEdit(def_data["employees"][self.i])

        self.textHolder2 = QLabel("salary")
        self.textHolder2.setFixedSize(QSize(300,40))
        self.searchbar2 = QLineEdit(str(def_data["salaries"][self.i]))

        self.textHolder3 = QLabel("qualifications")
        self.textHolder3.setFixedSize(QSize(300,40))
        self.searchbar3 = QLineEdit(def_data["qualifications"][self.i])

        self.textHolder4 = QLabel("department")
        self.textHolder4.setFixedSize(QSize(300,40))
        self.searchbar4 = QLineEdit(def_data["departments"][self.i])

        self.layout.removeWidget(self.textHolder)
        self.layout.removeWidget(self.searchbar)
        self.layout.removeWidget(self.editbutton)
        self.textHolder.deleteLater()
        self.searchbar.deleteLater()
        self.editbutton.deleteLater()
        
        self.layout.addWidget(self.textHolder1,      1, 0, 1, 1)
        self.layout.addWidget(self.searchbar1,       1, 1, 1, 3)

        self.layout.addWidget(self.textHolder2,     2, 0, 1, 1)
        self.layout.addWidget(self.searchbar2,      2, 1, 1, 3)

        self.layout.addWidget(self.textHolder3,     3, 0, 1, 1)
        self.layout.addWidget(self.searchbar3,      3, 1, 1, 3)

        self.layout.addWidget(self.textHolder4,     4, 0, 1, 1)
        self.layout.addWidget(self.searchbar4,      4, 1, 1, 3)

        self.savebutton = QPushButton('save', clicked=self.saving)

        self.layout.addWidget(self.savebutton,      5, 3, 1, 1)

        self.returnbutton = QPushButton('return', clicked=self.returning)

        self.layout.addWidget(self.returnbutton,    5, 2, 1, 1)

    def saving(self):
        name = self.searchbar1.text()
        salary = int(self.searchbar2.text())
        qualifications = self.searchbar3.text()
        department = self.searchbar4.text()

        print(def_data["employees"][self.i])
        def_data["employees"][self.i] = name
        def_data["salaries"][self.i] = salary
        def_data["qualifications"][self.i] = qualifications
        def_data["departments"][self.i] = department

        self.mainApp = Window()
        self.mainApp.show()
        self.close()

    def returning(self):
        self.mainApp = Window()
        self.mainApp.show()
        self.close()



        

        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet('''
                        QWidget {
                                font-size: 25px;
                                }
                        QLineEdit {
                                height: 50px;
                                }
                    ''')
 
    
    loginWindow = LoginWindow()
    loginWindow.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')




