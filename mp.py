from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
import random



mixer.init()
class musicplayer:
    def __init__(self,Tk):
        self.root=Tk
        self.root=Tk
        self.root.title('Music_player')
        self.root.geometry('400x400')
        self.root.configure(background='black')

        #openfile
        def Openfile():
            global filename
            filename=filedialog.askopenfilename()

    
        #MENU
        self.menubar=Menu(self.root)
        self.root.configure(menu=self.menubar)

        #submenu
        self.submenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='File',menu=self.submenu)
        self.submenu.add_command(label='Open',command=Openfile)
        self.submenu.add_command(label='Exit',command=self.root.destroy)

        self.submenu2=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='About us',menu=self.submenu2)
        self.submenu2.add_command(label='We made a college project using oops')

        

         #mute
        def mute():
            self.scale.set(0)
            self.mute=ImageTk.PhotoImage(file='mute.png')
            mute=Button(self.root,image=self.mute,bd=0,bg='red',command=unmute,cursor='hand2').place(x=947,y=555,height=50,width=50)

        #volume img
        self.volumes=ImageTk.PhotoImage(file='volume.png')
        volumes=Button(self.root,image=self.volumes,bd=0,bg='red',command=mute,cursor='hand2').place(x=947,y=555,height=50,width=50)    

        #unmute
        def unmute():
            self.scale.set(100)
            self.volumes=ImageTk.PhotoImage(file='volume.png')
            volumes=Button(self.root,image=self.volumes,bd=0,bg='red',command=mute,cursor='hand2').place(x=947,y=555,height=50,width=50)

        #function for volume bar
        def volume(vol):
            volume=int(vol)/100
            mixer.music.set_volume(volume)

        #volume bar
        self.scale=Scale(self.root,from_=0,to=100,orient=VERTICAL,length=450,bg='black',command=volume,cursor='hand2')
        self.scale.set(25)
        self.scale.place(x=950,y=98)

        
         #ADDING LABEL
        
        
        #ADDING IMAGE
        self.photo=ImageTk.PhotoImage(file='everglade.jpg')
        photo=Label(self.root,image=self.photo).place(x=50,y=100,width=880,height=450)

        self.photop=ImageTk.PhotoImage(file='apple.png')
        photop=Label(self.root,image=self.photop,bg='black').place(x=50,y=100,width=880,height=450)


        self.photo_s1=ImageTk.PhotoImage(file='music.jpg')
        photo_s1=Label(self.root,image=self.photo_s1,bg='violet',cursor='hand2').place(x=00,y=1,width=100,height=110)

        self.file_label = Label(text='MUSIZ', bg='black', fg='red', font=('Arial', 30),cursor='hand2')
        self.file_label.place(x=100, y=28)

    
        #ADDING LEFT SIDE IMAGE

        self.file_label = Label(text='My playlist', bg='black', fg='white', font=('Arial', 30),cursor='hand2')
        self.file_label.place(x=1100, y=30)

        def playsmusic():
            mixer.music.load('Mere Dholna_192(Ghantalele.com).mp3')
            mixer.music.play()
            self.label3['text']='MUSIC playing'

        def playssmusic():
            mixer.music.load('song1.mp3')
            mixer.music.play()
            self.label3['text']='MUSIC playing'

        def playssmusicc():
            mixer.music.load('bajarang.mp3')
            mixer.music.play()
            self.label3['text']='MUSIC playing'

        def playssmusisc():
            mixer.music.load('Kun Faaya Kun_192(Ghantalele.com).mp3')
            mixer.music.play()
            self.label3['text']='MUSIC playing'

        def playssmusiiisc():
            mixer.music.load('128-Halki Halki Si - Asees Kaur 128 Kbps - Copy.mp3')
            mixer.music.play()
            self.label3['text']='MUSIC playing'
                
        

        def playrandomss():
                
                music_filess=['bajarang.mp3','song1.mp3','Mere Dholna_192(Ghantalele.com).mp3','128-Abrars Entry Jamal Kudu - Animal 128 Kbps.mp3','128-Galti - Vishal Mishra 128 Kbps.mp3','128-Halki Halki Si - Asees Kaur 128 Kbps.mp3','128-Mohabbat Karne Wale - Tulsi Kumar 128 Kbps.mp3','128-Saiyaan Dheere Dheere - Tony Kakkar 128 Kbps.mp3','128-Zaalim - Badshah 128 Kbps.mp3','128-Zindagi Tere Naam - Yodha 128 Kbps.mp3','Kun Faaya Kun_192(Ghantalele.com).mp3']
                random_musicc=random.choice(music_filess)
                mixer.music.load(random_musicc)
                mixer.music.play()
        def piics():
            self.photop=ImageTk.PhotoImage(file='apple.png')
            photop=Label(self.root,image=self.photop,bg='black',cursor='hand2').place(x=50,y=120,width=880,height=450)  

        def combine11():
            piics() 
            playrandomss()        
            


        def pics():
            self.photop=ImageTk.PhotoImage(file='hai.jpg')
            photop=Label(self.root,image=self.photop,bg='black',cursor='hand2').place(x=50,y=120,width=880,height=450)  

        def combine1():
            pics() 
            playssmusic() 

    

        def picss():
            self.photop=ImageTk.PhotoImage(file='mere.jpg')
            photop=Label(self.root,image=self.photop,bg='black',cursor='hand2').place(x=50,y=120,width=880,height=450)  

        def combine2():
            picss() 
            playsmusic()

        def picsss():
            self.photop=ImageTk.PhotoImage(file='hari.jpg')
            photop=Label(self.root,image=self.photop,bg='black',cursor='hand2').place(x=50,y=120,width=880,height=450) 

        def combine3():
            picsss()
            playssmusicc() 

        def piccsss():
            self.photop=ImageTk.PhotoImage(file='15.jpg')
            photop=Label(self.root,image=self.photop,bg='black',cursor='hand2').place(x=50,y=120,width=880,height=450) 

        def combine4():
            piccsss()
            playssmusisc() 


        def picccsss():
            self.photop=ImageTk.PhotoImage(file='hal.jpg')
            photop=Label(self.root,image=self.photop,bg='black',cursor='hand2').place(x=50,y=120,width=880,height=450)

        def combine5():
            picccsss()
            playssmusiiisc


        

        self.L_photo=ImageTk.PhotoImage(file='dholna.jpeg')
        L_photo=Button(self.root,image=self.L_photo,bd=0,bg='red',command=combine2,cursor='hand2').place(x=1050,y=100,width=70,height=70)


        self.file_label = Button(text='Mere Dholna', bg='red', fg='black', font=('Arial', 15),command=combine2,cursor='hand2')
        self.file_label.place(x=1120, y=100,height=70,width=200)

        self.L1_photo=ImageTk.PhotoImage(file='tu1.jpeg')
        L1_photo=Button(self.root,image=self.L1_photo,bd=0,bg='red',command=combine1,cursor='hand2').place(x=1050,y=200,width=70,height=70)

        self.file_label = Button(text='Tu hai Kahan', bg='red', fg='black', font=('Arial', 15),command=combine1,cursor='hand2')
        self.file_label.place(x=1120, y=200,height=70,width=200)

        self.L2_photo=ImageTk.PhotoImage(file='hanu.jpeg')
        L2_photo=Button(self.root,image=self.L2_photo,bd=0,bg='red',command=combine3,cursor='hand2').place(x=1050,y=300,width=70,height=70)

        self.file_label = Button(text='Hari aur main', bg='red', fg='black', font=('Arial', 15),command=combine3,cursor='hand2')
        self.file_label.place(x=1120, y=300,height=70,width=200)

        self.L3_photo=ImageTk.PhotoImage(file='5.jpeg')
        L3_photo=Button(self.root,image=self.L3_photo,bd=0,bg='red',command=combine4,cursor='hand2').place(x=1050,y=400,width=70,height=70)

        self.file_label = Button(text='Kun Faaya Kun', bg='red', fg='black', font=('Arial', 15),command=combine4,cursor='hand2')
        self.file_label.place(x=1120, y=400,height=70,width=200)


        self.L7_photo=ImageTk.PhotoImage(file='poster.jpeg')
        L7_photo=Button(self.root,image=self.L7_photo,bd=0,bg='red',command=combine5,cursor='hand2').place(x=1050,y=500,width=70,height=70)

        self.file_label = Button(text='Halki Halki si', bg='red', fg='black', font=('Arial', 15),command=combine5,cursor='hand2')
        self.file_label.place(x=1120, y=500,height=70,width=200)






        

         #FUNCTIONS FOR BUTTONS
        def playmusic():
          try:
                paused
          except NameError:
                try:    
                   mixer.music.load(filename)
                   mixer.music.play()
                   self.label1['text']='MUSIC PLAYING!'

                
                 
                except:
                    pass
          else:
                mixer.music.unpause()
                self.label5['text']='MUSIC UNPAUSED!'
    



                
        def pausemusic():
            global paused
            paused=TRUE
            mixer.music.pause()
            self.label2['text']='MUSIC PAUSED!'

        def stopmusic():
            mixer.music.stop()
            self.label3['text']='MUSIC STOP!' 

        



        
    
        #CREATING BUTTONS 
        self.photo_B1=ImageTk.PhotoImage(file='play.png')
        photo_B1=Button(self.root,image=self.photo_B1,bd=0,bg='violet',command=playmusic,cursor='hand2').place(x=370,y=650,height=100,width=100)

        
        self.photo_B2=ImageTk.PhotoImage(file='pause.png')
        photo_B2=Button(self.root,image=self.photo_B2,bd=0,bg='black',command=pausemusic,cursor='hand2').place(x=210,y=650,height=100,width=100)

        self.photo_B6=ImageTk.PhotoImage(file='stop1.jpeg')
        photo_B6=Button(self.root,image=self.photo_B6,bd=0,bg='black',command=stopmusic,cursor='hand2').place(x=530,y=650,height=100,width=100)


        self.photo_B3=ImageTk.PhotoImage(file='previous.png')
        photo_B3=Button(self.root,image=self.photo_B3,bd=0,bg='black',cursor='hand2',command=playrandomss).place(x=50,y=650,height=100,width=100)

        self.photo_B4=ImageTk.PhotoImage(file='next.png')
        photo_B4=Button(self.root,image=self.photo_B4,bd=0,bg='black',cursor='hand2',command=playrandomss).place(x=690,y=650,height=100,width=100)             

        self.photo_B5=ImageTk.PhotoImage(file='shuffle.jpg')
        photo_B5=Button(self.root,image=self.photo_B5,bd=0,bg='black',cursor='hand2',command=combine11).place(x=850,y=650,height=100,width=100)

        

        
root=Tk()
obj=musicplayer(root)
root.mainloop() 