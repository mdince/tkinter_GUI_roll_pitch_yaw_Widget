from tkinter import *
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


root = Tk()
root.title('Hermod Hyperloop Kullanıcı Arayüzü')
#root.iconbitmap('Hermod-Logo2.ico')
root.geometry("1100x500")
# root.attributes('-fullscreen', True)
root['background'] = '#000000'

rpy_frame = Frame(root, bg="black")
rpy_frame.place(x=25, y=25)


img = ImageTk.PhotoImage(Image.open("C:/Users/ASUS/Desktop/İnformatik/Hyperloop/Arayüz/gui yaw pitch roll/angle.png").resize((250,250)))

def rotate_rimg(degrees):
    new_image = rimg.rotate(-int(degrees), fillcolor="black")
    photoimage = ImageTk.PhotoImage(new_image)
    rollimage.image = photoimage #Prevent garbage collection
    rollimage.config(image = photoimage)

def rotate_pimg(degrees):
    new_image = pimg.rotate(-int(degrees), fillcolor="black")
    photoimage = ImageTk.PhotoImage(new_image)
    pitchimage.image = photoimage #Prevent garbage collection
    pitchimage.config(image = photoimage)

def rotate_yimg(degrees):
    new_image = yimg.rotate(-int(degrees), fillcolor="black")
    photoimage = ImageTk.PhotoImage(new_image)
    yawimage.image = photoimage #Prevent garbage collection
    yawimage.config(image = photoimage)



rimg = Image.open("C:/Users/ASUS/Desktop/İnformatik/Hyperloop/Arayüz/gui yaw pitch roll/roll.png").resize((60,60))
width, height = rimg.size
rimg.thumbnail((width, height))
photorimg = ImageTk.PhotoImage(rimg)

rollframe = Frame(rpy_frame, bg="black", highlightbackground="black",highlightthickness=2, padx=20, pady=20)
rollframe.grid(row=0, column=0)
rollcanvas = Canvas(rollframe, width=250, height=250, highlightthickness=0)
rollcanvas.grid(row=0, column=0)
rollcanvas.create_image(0,0, image = img, anchor="nw")
rolllabel = Label(rollframe, text="Roll", bg="black", fg="#FFFFFF", font=('lucida', 12), padx=20, pady=20)
rolllabel.grid(row=1, column=0)
rollimage = Label(rollframe, image=photorimg, bd = 0)
rollimage_window = rollcanvas.create_window(125.5,125.5 , window=rollimage)

rs = Scale(rollframe, from_=-90, to=90, tickinterval= 30, orient=HORIZONTAL, length=300, command =rotate_rimg)
rs.grid(row=2, column=0)
rs.set(0)



pimg = Image.open("C:/Users/ASUS/Desktop/İnformatik/Hyperloop/Arayüz/gui yaw pitch roll/pitch.png").resize((100,100))
width, height = pimg.size
pimg.thumbnail((width, height))
photopimg = ImageTk.PhotoImage(pimg)

pitchframe = Frame(rpy_frame, bg="black",highlightbackground="black",highlightthickness=2, padx=20, pady=20)
pitchframe.grid(row=0, column=1)
pitchcanvas = Canvas(pitchframe, width=250, height=250, highlightthickness=0)
pitchcanvas.grid(row=0, column=0)
pitchcanvas.create_image(0,0, image = img, anchor="nw")
pitchlabel = Label(pitchframe, text="Pitch", bg="black", fg="#FFFFFF", font=('lucida', 12), padx=20, pady=20)
pitchlabel.grid(row=1, column=0)
pitchimage = Label(pitchframe, image=photopimg, bd = 0)
pitchimage_window = pitchcanvas.create_window(125.5,125.5 , window=pitchimage)

ps = Scale(pitchframe, from_=-90, to=90, tickinterval= 30, orient=HORIZONTAL, length=300, command = rotate_pimg)
ps.grid(row=2, column=0)
ps.set(0)



yimg = Image.open("C:/Users/ASUS/Desktop/İnformatik/Hyperloop/Arayüz/gui yaw pitch roll/yaw.png").resize((100,100))
width, height = yimg.size
yimg.thumbnail((width, height))
photoyimg = ImageTk.PhotoImage(yimg)

yawframe = Frame(rpy_frame, bg="black", highlightbackground="black",highlightthickness=2, padx=20, pady=20)
yawframe.grid(row=0, column=2)
yawcanvas = Canvas(yawframe, width=250, height=250, highlightthickness=0)
yawcanvas.grid(row=0, column=0)
yawcanvas.create_image(0,0, image = img, anchor="nw")
yawlabel = Label(yawframe, text="Yaw", bg="black", fg="#FFFFFF", font=('lucida', 12), padx=20, pady=20)
yawlabel.grid(row=1, column=0)
yawimage = Label(yawframe, image=photoyimg, bd = 0)
yawimage_window = yawcanvas.create_window(125.5,125.5 , window=yawimage)

ys = Scale(yawframe, from_=-90, to=90, tickinterval= 30, orient=HORIZONTAL, length=300, command = rotate_yimg)
ys.grid(row=2, column=0)
ys.set(0)


root.mainloop()