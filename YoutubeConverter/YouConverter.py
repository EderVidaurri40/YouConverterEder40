import tkinter as tk
import tkinter.font as TkFont
from tkinter import ttk
from pytube import YouTube
import os
import time



 

class main_window():
    root = tk.Tk()
    root.title('YouConverter')
    root.minsize(900, 600)
    root.iconbitmap("img/you.ico") #ONLY FOR WINDOWS 
    
    #im = Image.open('img/you.ico')  ##
    #photo = ImageTk.PhotoImage(im)  ## ONLY FOR LINUX
    #root.wm_iconphoto(True, photo)  ##
    
    window_height = 600 
    window_width = 1000
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    root.resizable(False,False)
    root.configure(bg='#46324F')
    
    bigfont = TkFont.Font(family="Helvetica",size=27)
    root.option_add('*TCombobox*Listbox.font',bigfont)
    barColor = ttk.Style()
    barColor.configure("color.Horizontal.TProgressbar", background='#8409BD')
    

    
class UIfunctions():
    def mp3convert():
        try:
            
            url = UI.urlEntry.get()
            my_convertion = YouTube(url)
            mp3 = my_convertion.streams.filter(only_audio=True).first()
            UIfunctions.start()
            out_file = mp3.download(output_path='Descargas')
            UIfunctions.finish()
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            UI.urlEntry.delete(0, 'end')
            
        except:
            errWinUrl()
            UI.urlEntry.delete(0, 'end')
            
        
    def mp4convert():
        try:
            url = UI.urlEntry.get()
            my_convertion = YouTube(url)
            mp4 = my_convertion.streams.get_highest_resolution()
            UIfunctions.start()
            out_file = mp4.download(output_path='Descargas')
            UIfunctions.finish()
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp4'
            os.rename(out_file, new_file)
            UI.urlEntry.delete(0, 'end')
            
            
        except:
            errWinUrl()
            UI.urlEntry.delete(0, 'end')
            
       
    def convert():
        UI.progressBar['value'] =0
        option = UI.boxvar.get()
        
        if option == "mp3":
            UIfunctions.mp3convert()
        elif option == "mp4":
            UIfunctions.mp4convert()
        else:
            errWinType()

    def start():
        task = 60
        x = 0
        while(x<task):
            time.sleep(0.0200)
            UI.progressBar['value']+=1
            x+=1
            main_window.root.update_idletasks()
            
    def finish():
        task = 40
        x = 0
        while(x<task):
            time.sleep(0.0200)
            UI.progressBar['value']+=1
            x+=1
            main_window.root.update_idletasks()
        
            
           

    
        
        
class UI ():
    
    
    urlText=tk.LabelFrame(text="URL:")
    urlText.config(width=300,height=70,font=('Arial', 24),borderwidth=0, background='#46324F', foreground='#EDE5F1')
    urlText.place(x=30,y=60)
    
    urlvarentry = tk.StringVar()
    urlEntry = tk.Entry(textvariable=urlvarentry)
    urlEntry.config(font=('Arial',20), background='#948999', foreground='#FFFFFF',insertbackground='#810FBB', highlightcolor='#630BDA', selectbackground='#0B76DA' )
    urlEntry.place(x=30, y=100,width=940,height =50)
    
    convertButt = tk.Button(text="Convertir", command=UIfunctions.convert)
    convertButt.config(font=('Arial',20), background='#46324F', foreground='#EDE5F1',activebackground='#810FBB', activeforeground='#EDE5F1',  cursor='hand2')
    convertButt.place(x=820,y=180, width=155, height = 70)
    
    textType = tk.LabelFrame(main_window.root,text="Tipo de conversion:")
    textType.config(width=300,height=70,font=('Arial', 24),borderwidth=0, background='#46324F', foreground='#EDE5F1')
    textType.place(x=410,y=180)
    
    boxvar = tk.StringVar()
    fileType = ttk.Combobox(state='readonly',textvariable=boxvar,values=("mp3","mp4"))
    fileType.config(font=('Arial', 27), background='#46324F',  cursor='hand2')
    fileType.place(x=710, y=180,width=100, height = 70 )
    
    
    
    
    progressBar = ttk.Progressbar(main_window.root, maximum=100, style='color.Horizontal.TProgressbar')
    progressBar.place(x=30, y=300, width=940)
    
    
    creatorLabel = tk.Label(main_window.root, text="Created by Eder Vargas")
    creatorLabel.config(font=('Arial',17), background='#46324F', foreground='#5F536D')
    creatorLabel.place(x=20, y=560)
    
    
    
    
def errWinType():
    def closeBu():
        winError.destroy()
    winError = tk.Toplevel(main_window.root)
    winError.title('Valores Incorrectos')
    winError.wait_visibility()
    winError.grab_set_global()

 
    
    winError.iconbitmap("img/error.ico") #ONLY FOR WINDOWS
    
    #im = Image.open('img/error.ico')  ##
    #photo = ImageTk.PhotoImage(im)  ## ONLY FOR LINUX
    #winError.wm_iconphoto(True, photo)  ##
    
    window_height = 150
    window_width = 400
    screen_width = winError.winfo_screenwidth()
    screen_height = winError.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    winError.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    winError.resizable(False,False)
    winError.configure(bg='#583881')
    infoError = tk.LabelFrame(winError,text="Por favor elija un tipo de conversion")
    infoError.config(font=('Arial',15), borderwidth=0, background='#583881', foreground='#EDE5F1')
    infoError.place(x=41,y=50, width=340, height=150)
    acceptButt= tk.Button(winError,text="Aceptar", command=closeBu, activebackground='#810FBB', activeforeground='#EDE5F1',  cursor='hand2')
    acceptButt.config(font=('Arial',14), background='#583881', foreground='#EDE5F1')
    acceptButt.place(x=160,y=100)
    
def errWinUrl():
    def closeBu():
        winErrorurl.destroy()
    winErrorurl = tk.Toplevel(main_window.root)
    winErrorurl.title('URL no encontrada')
    winErrorurl.wait_visibility()
    winErrorurl.grab_set_global()
    
    winErrorurl.iconbitmap("img/error.ico") #ONLY FOR WINDOWS
    
    #im = Image.open('img/error.ico')  ##
    #photo = ImageTk.PhotoImage(im)  ## ONLY FOR LINUX
    #winErrorurl.wm_iconphoto(True, photo)  ##
    
    window_height = 150
    window_width = 400
    screen_width = winErrorurl.winfo_screenwidth()
    screen_height = winErrorurl.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    winErrorurl.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    winErrorurl.resizable(False,False)
    winErrorurl.configure(bg='#583881')
    infoError = tk.LabelFrame(winErrorurl,text="La URL ingresada es incorrecta o \n no tiene conexion a internet")
    infoError.config(font=('Arial',15), borderwidth=0, background='#583881', foreground='#EDE5F1')
    infoError.place(x=57,y=30, width=340, height=150)
    acceptButt= tk.Button(winErrorurl,text="Aceptar", command=closeBu)
    acceptButt.config(font=('Arial',14), background='#583881', foreground='#EDE5F1',activebackground='#810FBB',  activeforeground='#EDE5F1', cursor='hand2')
    acceptButt.place(x=160,y=100)
    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    UI.pPercentage.configure(text= per + "%")
    UI.pPercentage.update()

    #Update progress bar
    UI.progressBar.set(float(percentage_of_completion) / 100)

        
        
    
    
    
    
if __name__ == "__main__":
  main_window.root.mainloop()
  
  
  

