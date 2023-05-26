# from image_functions import image_functions
import cv2
import numpy as np
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Image Editor")
root.iconbitmap("icon.ico")

# All Functions
def top_pop(title, img, img_f):
    global myImage
    global top
    top = Toplevel()
    top.title(title)
    top.iconbitmap("icon.ico")
    myImage = Label(top, image=img)
    myImage.image = img
    myImage.pack()
    btn1 = Button(top, text="Save Image", command=lambda:save(img_f)).pack(fill="both")
    btn2 = Button(top, text="Close window", command=top.destroy).pack(fill="both")

def cv2_to_PIL(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_array = Image.fromarray(img)
    img_final = ImageTk.PhotoImage(img_array)
    return img_final

def save(img):
    def get_filename():
        cv2.imwrite((str(e.get())+".jpg"), img)
        pop.destroy()
    pop = Toplevel()
    pop.title("File name")
    pop.iconbitmap("icon.ico")
    e = Entry(pop, width=30)
    e.pack()
    btn = Button(pop, text="Save", command=get_filename).pack()
        
def select_img():
    global path
    global btn_show
    global btn_gray
    global btn_resize
    global btn_showinfo
    global btn_neg
    global btn_red
    global btn_green
    global btn_blue
    global btn_crop
    global btn_blur
    global btn_smooth
    path = filedialog.askopenfilename(initialdir="images", title="select a file", 
                                      filetypes=(("jpg files", "*.jpg"), 
                                                 ("png files", "*.png"), 
                                                 ("all files", "*.*")))
    Button(root, text="Select an Image", command=select_img).grid(
        row=0, column=0, padx=2, pady=2, sticky=W, ipadx=17)
    
    Button(root, text="Show Original Image", command=lambda:show(path)).grid(
        row=1, column=0, padx=2, pady=2, sticky=W)
    Button(root, text="Show Image Info", command=lambda:showinfo(path)).grid(
        row=1, column=1, padx=2, pady=2, sticky=W)
    Button(root, text="Resize Image", command=lambda:resize(path)).grid(
        row=1, column=2, padx=2, pady=2, sticky=W)
    Button(root, text="Crop Image", command=lambda:crop(path)).grid(
        row=1, column=3, padx=2, pady=2, sticky=W, ipadx=10)
    
    Button(root, text="Grayscale Image", command=lambda:gray(path)).grid(
        row=2, column=0, padx=2, pady=2, sticky=W, ipadx=16)
    Button(root, text="Negative Image", command=lambda:negative(path)).grid(
        row=2, column=1, padx=2, pady=2, sticky=W, ipadx=4)
    Button(root, text="Blur Image", command=lambda:blur(path)).grid(
        row=2, column=2, padx=2, pady=2, sticky=W, ipadx=8)
    Button(root, text="Smooth Image", command=lambda:smooth(path)).grid(
        row=2, column=3, padx=2, pady=2, sticky=W)
    
    Button(root, text="Red Image", command=lambda:red(path)).grid(
        row=3, column=0, padx=2, pady=2, sticky=W, ipadx=35)
    Button(root, text="Green Image", command=lambda:green(path)).grid(
        row=3, column=1, padx=2, pady=2, sticky=W, ipadx=14)
    Button(root, text="Blue Image", command=lambda:blue(path)).grid(
        row=3, column=2, padx=2, pady=2, sticky=W, ipadx=6)
    Button(root, text="Sketch Image", command=lambda:sketch(path)).grid(
        row=3, column=3, padx=2, pady=2, sticky=W, ipadx=4)

    return path

def show(path):
    img_f = cv2.imread(path)
    img = cv2_to_PIL(img_f)
    top_pop("Original", img, img_f)

def showinfo(path):
    img = cv2.imread(path)
    info = "Path: "+str(path)+"\n\nResolution: "+str(img.shape[0])+" x "+str(img.shape[1])
    response = messagebox.showinfo("Info", info)
    return response

def resize(path):
    def get_shape(img):
        global myImage
        num = e.get().split()
        x,y = int(num[0]), int(num[1])
        E.destroy()
        img_f = cv2.resize(img, (x,y))
        img = cv2_to_PIL(img_f)
        top_pop("Resize", img, img_f)

    img = cv2.imread(path)      
    E = Toplevel()
    E.title("XY")
    E.iconbitmap("icon.ico")
    e = Entry(E, width=30)
    e.insert(0, "Enter X and Y (Separate with space)")
    e.pack()
    btn = Button(E, text="Enter", command=lambda:get_shape(img)).pack()

def gray(path):
    img = cv2.imread(path)
    img_f = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2_to_PIL(img_f)
    top_pop("Grayscale", img, img_f)

def negative(path):
    img = cv2.imread(path)
    img_f = 1 - img
    img = cv2_to_PIL(img_f)
    top_pop("Negative", img, img_f)

def red(path):
    img = cv2.imread(path)
    img = img[:,:,0]
    black = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
    img_f = np.stack((black,black,img), axis=2)
    img = cv2_to_PIL(img_f)
    top_pop("Red", img, img_f)

def green(path):
    img = cv2.imread(path)
    img = img[:,:,1]
    black = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
    img_f = np.stack((black,img,black), axis=2)
    img = cv2_to_PIL(img_f)
    top_pop("Green", img, img_f)

def blue(path):
    img = cv2.imread(path)
    img = img[:,:,2]
    black = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
    img_f = np.stack((img,black,black), axis=2)
    img = cv2_to_PIL(img_f)
    top_pop("Blue", img, img_f)

def crop(path):
    img = cv2.imread(path)
    value = cv2.selectROI(img, False)
    img_f = img[value[1]:value[1]+value[3],
                value[0]:value[0]+value[2]]
    img = cv2_to_PIL(img_f)
    top_pop("Crop", img, img_f)

def blur(path):
    img = cv2.imread(path)
    img_f = cv2.blur(img, (3,3))
    img = cv2_to_PIL(img_f)
    top_pop("Blur", img, img_f)

def smooth(path):
    img = cv2.imread(path)
    img_f = cv2.edgePreservingFilter(img, cv2.RECURS_FILTER, 300, 0.6)
    img = cv2_to_PIL(img_f)
    top_pop("Smooth", img, img_f)

def sketch(path):
    img = cv2.imread(path)
    pencil, img_f = cv2.pencilSketch(img, 100, 0.1, shade_factor=0.1)
    img = cv2_to_PIL(img_f)
    top_pop("Sketch", img, img_f)

# All Buttons
btn_exit = Button(root, text="Exit", command=root.quit).grid(
    row=4, column=3, padx=2, pady=2, ipadx=37)

btn_select = Button(root, text="Select an Image", command=select_img).grid(
    row=0, column=0, padx=2, pady=2, sticky=W, ipadx=17)

btn_show = Button(root, text="Show Original Image", command=lambda:show(path), state=DISABLED).grid(
    row=1, column=0, padx=2, pady=2, sticky=W)
btn_showinfo = Button(root, text="Show Image Info", command=lambda:showinfo(path), state=DISABLED).grid(
    row=1, column=1, padx=2, pady=2, sticky=W)
btn_resize = Button(root, text="Resize Image", command=lambda:resize(path), state=DISABLED).grid(
    row=1, column=2, padx=2, pady=2, sticky=W)
btn_crop = Button(root, text="Crop Image", command=lambda:crop(path), state=DISABLED).grid(
    row=1, column=3, padx=2, pady=2, sticky=W, ipadx=10)

btn_gray = Button(root, text="Grayscale Image", command=lambda:gray(path), state=DISABLED).grid(
    row=2, column=0, padx=2, pady=2, sticky=W, ipadx=16)
btn_neg = Button(root, text="Negative Image", command=lambda:negative(path), state=DISABLED).grid(
    row=2, column=1, padx=2, pady=2, sticky=W, ipadx=4)
btn_blur = Button(root, text="Blur Image", command=lambda:blur(path), state=DISABLED).grid(
    row=2, column=2, padx=2, pady=2, sticky=W, ipadx=8)
btn_smooth = Button(root, text="Smooth Image", command=lambda:smooth(path), state=DISABLED).grid(
    row=2, column=3, padx=2, pady=2, sticky=W)

btn_red = Button(root, text="Red Image", command=lambda:red(path), state=DISABLED).grid(
    row=3, column=0, padx=2, pady=2, sticky=W, ipadx=35)
btn_green = Button(root, text="Green Image", command=lambda:green(path), state=DISABLED).grid(
    row=3, column=1, padx=2, pady=2, sticky=W, ipadx=14)
btn_blue = Button(root, text="Blue Image", command=lambda:blue(path), state=DISABLED).grid(
    row=3, column=2, padx=2, pady=2, sticky=W, ipadx=6)
btn_sketch = Button(root, text="Sketch Image", command=lambda:sketch(path), state=DISABLED).grid(
    row=3, column=3, padx=2, pady=2, sticky=W, ipadx=4)

root.mainloop()