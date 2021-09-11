import os
import socket
from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5 import QtCore

import datetime

from cmpt import pywhatkit

try:
    from components.timecv import *
except:
    from timecv import *
    
try:
    from msgboxpy import alert,Styles
except:
    from components.msgboxpy import alert,Styles

history_file = "HST0016.dll"
    
def tmp_txt(text):
    open("tmp.txt","w").write(text)
    os.system("notepad tmp.txt&&del tmp.txt")
window = "Your Window"
class Main:
    def open_file(self,img_inp):
        filter = "Image Files (*.png)"
        fileName = QFileDialog.getOpenFileName(self.centralwidget,'Open File',os.getcwd(),filter="All Files (*.*)")

        img_inp.setText(fileName[0])
        
    def save_file_and_get_path(main_widget,df_text:str="WText_to_image.txt"):
        options = QFileDialog.Options()
        file = QFileDialog.getSaveFileName(main_widget,"Save Image",df_text,"Text File (*.txt)")
        return file[0]

    def FileDialog(directory='', forOpen=True, fmt='', isFolder=False):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseCustomDirectoryIcons
        dialog = QFileDialog(caption="Open Folder")
        dialog.setOptions(options)

        dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)

        # ARE WE TALKING ABOUT FILES OR FOLDERS
        if isFolder:
            dialog.setFileMode(QFileDialog.DirectoryOnly)
        else:
            dialog.setFileMode(QFileDialog.AnyFile)
        # OPENING OR SAVING:
        dialog.setAcceptMode(QFileDialog.AcceptOpen) if forOpen else dialog.setAcceptMode(QFileDialog.AcceptSave)

        # SET FORMAT, IF SPECIFIED
        if fmt != '' and isFolder is False:
            dialog.setDefaultSuffix(fmt)
            dialog.setNameFilters([f'{fmt} (*.{fmt})'])

        # SET THE STARTING DIRECTORY
        if directory != '':
            dialog.setDirectory(str(directory))
        else:
            dialog.setDirectory(str(os.path.dirname(__file__)))


        if dialog.exec_() == QDialog.Accepted:
            path = dialog.selectedFiles()[0]  # returns a list
            return path
        else:
            return ''
    def __init__(self):
        pass          
    class Gmail():
        def open_gmail_nh(mw):
            mw.destroy()
            os.system("python components/gmail_nh.py")
            
        def send_gmail(timeEdit,email_sender: str, password: str, subject: str, message: str, email_receiver: str):
            
            mtm = str(timeEdit.time())
            
            msection = mtm[19:]
            
            hour = str(datetime.now().hour)
            minute = str(datetime.now().minute)
            
            m = datetime.today().strftime("%H:%M %p")
            if m.endswith("AM"):    
                p = "AM"
            else:
                p = "PM"   
            
            ihour = msection.split(',')[0]
            iminute = msection.split(',')[1].replace(")","").strip()
            ip = "AM"
            
            if hour.startswith("0"):
                hour = hour[1:]
                
            if minute.startswith("0"):
                minute = minute[1:]
            
            hour = int(hour)
            minute = int(minute)
            
            ihour = int(ihour)
            iminute = int(iminute)
              
            if ihour == 0:
                ihour = 12    
            else:
                if ihour>=12:
                    ip = "PM"        
            while True:
                if hour == ihour and minute == iminute and p == ip:
                    pywhatkit.send_mail(email_sender,password,subject,message,email_receiver)    
                    break

    class MMenu():   
        def open_watsintro(self,window):
            
            window.destroy() 
            alert("Loading This may take a while....",Styles.Icons.ICON_INFORMATION,"Load alert")
            os.system("python components/watsintro.py")
        def open_wmenu(self,window):
            window.destroy() 
            os.system("python components/wmenu.py")            
        def open_gmenu(mw):
            mw.destroy()
            os.system("python components/gmenu.py")    
        def open_image_to_text():
            window.destroy() 
            os.system("python components/img_to_text.py")
        def open_text_to_image():
            #os.system("python components/text_to_img.py")
            
            alert("Currently in Development.....",Styles.Icons.ICON_INFORMATION,"IEx1432")            
                
    def open_mw(mw):

        if socket.gethostbyname(socket.gethostname()) == "127.0.0.1":
            al = alert(f"AWM - Auto Whatsapp Messager requires an active network Connection!",Styles.Icons.ICON_ERROR|Styles.Buttons.RETRY_CANCEL,"Internet Error")
            if al =="retry":
                while True:
                    if socket.gethostbyname(socket.gethostname()) == "127.0.0.1":
                        alrt = alert(f"No Network Connection Found!",Styles.Icons.ICON_ERROR|Styles.Buttons.RETRY_CANCEL,"Internet Error")            
                        if alrt!="retry":
                            break
                    else:
                        mw.destroy()
                        os.system("python components/mw.py")                
        else:    
            mw.destroy()                       
            os.system("python components/mw.py")

    def open_mgw():
        if socket.gethostbyname(socket.gethostname()) == "127.0.0.1":
            al = alert(f"AWM - Auto Whatsapp Messager requires an active network Connection!",Styles.Icons.ICON_ERROR|Styles.Buttons.RETRY_CANCEL,"Internet Error")
            if al =="retry":
                while True:
                    if socket.gethostbyname(socket.gethostname()) == "127.0.0.1":
                        alrt = alert(f"No Network Connection Found!",Styles.Icons.ICON_ERROR|Styles.Buttons.RETRY_CANCEL,"Internet Error")            
                        if alrt!="retry":
                            break
                    else:
                        window.destroy() 
                        os.system("python components/mgw.py")                
        else:   
            window.destroy()             
            os.system("python components/mgw.py") 



    class History():

            def show_history():
                if open("HST0016.dll","r").read().strip()!="--------------------":        
                    hst_dat = open("HST0016.dll","r").read()
                    tmp_txt(hst_dat)     
                else:
                    alert("You Currently Don't have any histories",Styles.Icons.ICON_ERROR,"Error:HST0016x15")    
                    
            def history_exporter():
                if open("HST0016.dll","r").read().strip()!="--------------------":        
                    saved_file = Main.save_file_and_get_path(None,"My Whatsapp History.txt")
                    if saved_file.strip()!="" and saved_file!=None and os.path.exists(saved_file):
                        hst = open(history_file).read()
                        with open(saved_file) as file:
                            file.write(hst)
                else:
                    alert("You Currently Don't have any histories",Styles.Icons.ICON_ERROR,"Error:HST0016x15")  
 
            def clear_history():
                if open("HST0016.dll","r").read().strip()!="--------------------":
                    open("HST0016.dll","w").write("")
                else:
                    alert("You Currently Don't have any histories",Styles.Icons.ICON_ERROR,"Error:HST0016x15")        
                
    def bug_reporter():
        if socket.gethostbyname(socket.gethostname()) == "127.0.0.1":
            al = alert(f"AWM Bug Reporter needs an active network Connection!",Styles.Icons.ICON_ERROR|Styles.Buttons.RETRY_CANCEL,"Internet Error")
            if al =="retry":
                while True:
                    if socket.gethostbyname(socket.gethostname()) == "127.0.0.1":
                        alrt = alert(f"No Network Connection Found!",Styles.Icons.ICON_ERROR|Styles.Buttons.RETRY_CANCEL,"Internet Error")            
                        if alrt!="retry":
                            break
                    else:
                        os.system("python bug_reporter.py")                
        else:               
            os.system("python bug_reporter.py")   