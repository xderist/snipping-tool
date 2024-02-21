import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QFrame,
    QPushButton,
    QFileDialog,
    QDesktopWidget
)
import traceback

from PyQt5.QtCore import Qt

from Capturer import Capture

import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import os
#import time   

def show_exception_and_exit(exc_type, exc_value, tb):
    
    traceback.print_exception(exc_type, exc_value, tb)
    #raw_input("Press key to exit.")
    sys.exit(-1)

sys.excepthook = show_exception_and_exit


class ScreenRegionSelector(QMainWindow):
    
    def __init__(self,):
        super().__init__(None)
        self.m_width = 1300
        self.m_height = 500

        self.setWindowTitle("Lyft Receipt Snipping Tool")
        #self.setMinimumSize(self.m_width, self.m_height)
        self.resize(self.m_width, self.m_height)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        frame = QFrame()
        frame.setContentsMargins(0, 0, 0, 0)
        lay = QVBoxLayout(frame)
        lay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lay.setContentsMargins(5, 5, 5, 5)

        self.label = QLabel()
        self.btn_capture = QPushButton("Capture")
        self.btn_capture.clicked.connect(self.capture)
        
        self.btn_save = QPushButton("Save")
        sc = self.btn_save.clicked.connect(self.save)
        self.btn_save.setVisible(False)

        #+1 day button
        # self.btn_saveday1 = QPushButton("Save Day +1")
        # sc = self.btn_saveday1.clicked.connect(self.saveday1)
        # self.btn_saveday1.setVisible(False)

        lay.addWidget(self.label)
        lay.addWidget(self.btn_capture)
        lay.addWidget(self.btn_save)
        #lay.addWidget(self.btn_saveday1)

        self.setCentralWidget(frame)

    def capture(self):
        self.capturer = Capture(self)
        self.capturer.show()
        self.btn_save.setVisible(True)
        #self.btn_saveday1.setVisible(True)
    
    def save(self):
        #file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "text", "Image files (*.png)")
        #if file_name:
        self.capturer.imgmap.save("text.png")      
           
        img = Image.open('text.png')
        text = tess.image_to_string(img)

        #old = r"text.png"
        #new = r"Output/"

        x = text.split()
        size = len(x)
        if any(substring in 'XL' for substring in x):
            #first name initial
            for name1 in x[4:5]:
                name11 = (name1[0])

            #lastname
            for name2 in x[int(size-11):int(size-10)]:
                name22 = (name2)

            #date
            for date in x[int(size-4):int(size-3)]:
                date0 = date[0]
                date1 = date[1]
                date3 = date[3]
                date4 = date[4]
                date12 = (date0 + date1 + '-' + date3 + date4)
            #dollar
            for dollar in x[int(size-10):int(size-9)]: 
                myString = dollar
            index = myString.find('.')
            #$514 (4) x $5514 (5)
            if index == -1:
                
                fc = 2  
                icount = len(myString)
                if icount == 5:    
                    DString = list(myString)
                    myString = DString[1] + DString[2] + '.' + DString[3] + DString[4]
                    
                    try:
                        newName = 'LYFT ' + name11.upper() + name22.upper() + ' ' + date12 + ' ' + myString
                        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", newName, "Image files (*.png)")
                        open(file_name,'w')
                        #text = self.textEdit.setText() 
                        #file.write(text)
                        #file.close()
                        # if file_name:
                        #     self.capturer.imgmap.save(newName + ".png")
                        #os.rename(old, new + newName + '.png')
                    except FileExistsError:
                        newName = 'LYFT ' + name11.upper() + name22.upper() + ' ' + date12 + ' ' + myString + "(" + str(fc) + ")"
                        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", newName, "Image files (*.png)")
                        open(file_name,'w')
                        # if file_name:
                        #     self.capturer.imgmap.save(newName + ".png")
                        #os.rename(old, new + newName + '.png')
                        for fc in newName:
                            fc += 1
                        
                if icount == 4:    
                    DString = list(myString)
                    myString = DString[1] + '.' + DString[2] + DString[3]
                    
                    try:
                        newName = 'LYFT ' + name11.upper() + name22.upper() + ' ' + date12 + ' ' + myString
                        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", newName, "Image files (*.png)")
                        open(file_name,'w')
                        # if file_name:
                        #     self.capturer.imgmap.save(newName + ".png")
                        #os.rename(old, new + newName + '.png')
                    except FileExistsError:
                        newName = 'LYFT ' + name11.upper() + name22.upper() + ' ' + date12 + ' ' + myString + "(" + str(fc) + ")"
                        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", newName, "Image files (*.png)")
                        open(file_name,'w')
                        # if file_name:
                        #     self.capturer.imgmap.save(newName + ".png")
                        #os.rename(old, new + newName + '.png')
                        for fc in newName:
                            fc += 1

                if icount == 6:    
                    DString = list(myString)
                    myString = DString[1] + DString[2] + DString[3] + '.' + DString[4] + DString[5]
                    
                    try:
                        newName = 'LYFT ' + name11.upper() + name22.upper() + ' ' + date12 + ' ' + myString
                        open(file_name,'w')
                        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", newName, "Image files (*.png)")
                        # if file_name:
                        #     self.capturer.imgmap.save(newName + ".png")
                        #os.rename(old, new + newName + '.png')
                    except FileExistsError:
                        newName = 'LYFT ' + name11.upper() + name22.upper() + ' ' + date12 + ' ' + myString + "(" + str(fc) + ")"
                        open(file_name,'w')
                        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", newName, "Image files (*.png)")
                        # if file_name:
                        #     self.capturer.imgmap.save(newName + ".png")
                        #os.rename(old, new + newName + '.png')
                        for fc in newName:
                            fc += 1        
            else:
                 
                try:
                    newName = 'LYFT ' + name11.upper() + name22.upper() + ' ' + date12 + ' ' + myString[1:]
                    file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", newName, "Image files (*.png)")
                    open(file_name,'w')
                    # if file_name:
                    #     self.capturer.imgmap.save(newName + ".png")
                    #os.rename(old, new + newName + '.png')
                except FileExistsError:
                    newName = 'LYFT ' + name11.upper() + name22.upper() + ' ' + date12 + ' ' + myString[1:] + "(" + str(fc) + ")"
                    file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", newName, "Image files (*.png)")
                    open(file_name,'w')
                    # if file_name:
                    #     self.capturer.imgmap.save(newName + ".png")
                    #os.rename(old, new + newName + '.png')
                    for fc in newName:
                        fc += 1

        else:
            #first name initial
            for name1 in x[4:5]:
                name11 = name1[0]

            #lastname
            for name2 in x[int(size-10):int(size-9)]:
                name22 = (name2)

            #date
            for date in x[int(size-4):int(size-3)]:
                ldate = list(date)
                date12 = (ldate[0] + ldate[1] + '-' + ldate[3] + ldate[4])
            #dollar
            for dollar in x[int(size-9):int(size-8)]: 
                myString = dollar
            index = myString.find('.')
            #$514 (4) x $5514 (5)
            if index == -1:
                
                fc = 2  
                icount = len(myString)
                if icount == 5:    
                    DString = list(myString)
                    myString = DString[1] + DString[2] + '.' + DString[3] + DString[4]
                    
                    try:
                        newName = 'LYFT ' + name11.upper() + name22.upper() + ' ' + date12 + ' ' + myString
                        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", newName, "Image files (*.png)")
                        # if file_name:
                        #     self.capturer.imgmap.save(newName + ".png")
                        #os.rename(old, new + newName + '.png')
                    except FileExistsError:
                        newName = 'LYFT ' + name11.upper() + name22.upper() + ' ' + date12 + ' ' + myString + "(" + str(fc) + ")"
                        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", newName, "Image files (*.png)")
                        open(file_name,'w')
                        # if file_name:
                        #     self.capturer.imgmap.save(newName + ".png")
                        #os.rename(old, new + newName + '.png')
                        for fc in newName:
                            fc += 1
                        
                if icount == 4:    
                    DString = list(myString)
                    myString = DString[1] + '.' + DString[2] + DString[3]
                    
                    try:
                        newName = 'LYFT ' + name11.upper() + name22.upper() + ' ' + date12 + ' ' + myString
                        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", newName, "Image files (*.png)")
                        open(file_name,'w')
                        # if file_name:
                        #     self.capturer.imgmap.save(newName + ".png")
                        #os.rename(old, new + newName + '.png')
                    except FileExistsError:
                        newName = 'LYFT ' + name11.upper() + name22.upper() + ' ' + date12 + ' ' + myString + "(" + str(fc) + ")"
                        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", newName, "Image files (*.png)")
                        open(file_name,'w')
                        # if file_name:
                        #     self.capturer.imgmap.save(newName + ".png")
                        #os.rename(old, new + newName + '.png')
                        for fc in newName:
                            fc += 1

                if icount == 6:    
                    DString = list(myString)
                    myString = DString[1] + DString[2] + DString[3] + '.' + DString[4] + DString[5]
                    
                    try:
                        newName = 'LYFT ' + name11.upper() + name22.upper() + ' ' + date12 + ' ' + myString
                        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", newName, "Image files (*.png)")
                        open(file_name,'w')
                        # if file_name:
                        #     self.capturer.imgmap.save(newName + ".png")
                        #os.rename(old, new + newName + '.png')
                    except FileExistsError:
                        newName = 'LYFT ' + name11.upper() + name22.upper() + ' ' + date12 + ' ' + myString + "(" + str(fc) + ")"
                        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", newName, "Image files (*.png)")
                        open(file_name,'w')
                        # if file_name:
                        #     self.capturer.imgmap.save(newName + ".png")
                        #os.rename(old, new + newName + '.png')
                        for fc in newName:
                            fc += 1        
            else:
                 
                try:
                    newName = 'LYFT ' + name11.upper() + name22.upper() + ' ' + date12 + ' ' + myString[1:]
                    file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", newName, "Image files (*.png)")
                    open(file_name,'w')
                    # if file_name:
                    #     self.capturer.imgmap.save(newName + ".png")
                    #os.rename(old, new + newName + '.png')
                except FileExistsError:
                    newName = 'LYFT ' + name11.upper() + name22.upper() + ' ' + date12 + ' ' + myString[1:] + "(" + str(fc) + ")"
                    file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", newName, "Image files (*.png)")
                    open(file_name,'w')
                    # if file_name:
                    #     self.capturer.imgmap.save(newName + ".png")
                    #os.rename(old, new + newName + '.png')
                    for fc in newName:
                        fc += 1
        #QFileDialog.getSaveFileName(self, "Save Image", "text", "Image files (*.png)")     
        #time.sleep(1)
        os.remove('text.png')
              

        
        #check if the file with the new name already exists 
            #if os.path.isfile(newName): 
                #print("duplicate") 
            #else: 
        #     #rename the file to the new name 
        #     #if file doesn't exist 
                #os.rename(old, new + newName + '.png')
        

if __name__ == "__main__":
    app = QApplication(sys.argv)    
    app.setStyleSheet("""
    QFrame {
        background-color: #3f3f3f;
    }
                      
    QPushButton {
        border-radius: 5px;
        background-color: rgb(60, 90, 255);
        padding: 10px;
        color: white;
        font-weight: bold;
        font-family: Arial;
        font-size: 12px;
    }
                      
    QPushButton::hover {
        background-color: rgb(255, 0, 0)
    }
    """)
    selector = ScreenRegionSelector()
    selector.show()
    app.exit(app.exec_())

