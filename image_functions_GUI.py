import cv2
import numpy as np
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog

class image_functions():
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Image Editor")
        self.root.iconbitmap("icon.ico")

# All Functions

    def top_pop(self,title, img, img_f):
        global myImage
        global top
        top = Toplevel()
        top.title(title)
        top.iconbitmap("icon.ico")
        myImage = Label(top, image=img)
        myImage.image = img
        myImage.pack()
        btn1 = Button(top, text="Save Image", command=lambda:self.save(img_f)).pack(fill="both")
        btn2 = Button(top, text="Close window", command=top.destroy).pack(fill="both")

    def cv2_to_PIL(self,img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_array = Image.fromarray(img)
        img_final = ImageTk.PhotoImage(img_array)
        return img_final

    def save(self,img):
        def get_filename():
            cv2.imwrite((str(e.get())+".jpg"), img)
            pop.destroy()
        pop = Toplevel()
        pop.title("File name")
        pop.iconbitmap("icon.ico")
        e = Entry(pop, width=30)
        e.pack()
        btn = Button(pop, text="Save", command=get_filename).pack()
            
    def select_img(self):
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
        Button(self.root, text="Select an Image", command=self.select_img).grid(
            row=0, column=0, padx=2, pady=2, sticky=W, ipadx=17)
        
        Button(self.root, text="Show Original Image", command=lambda:self.show(path)).grid(
            row=1, column=0, padx=2, pady=2, sticky=W)
        Button(self.root, text="Show Image Info", command=lambda:self.showinfo(path)).grid(
            row=1, column=1, padx=2, pady=2, sticky=W)
        Button(self.root, text="Resize Image", command=lambda:self.resize(path)).grid(
            row=1, column=2, padx=2, pady=2, sticky=W)
        Button(self.root, text="Crop Image", command=lambda:self.crop(path)).grid(
            row=1, column=3, padx=2, pady=2, sticky=W, ipadx=10)
        
        Button(self.root, text="Grayscale Image", command=lambda:self.gray(path)).grid(
            row=2, column=0, padx=2, pady=2, sticky=W, ipadx=16)
        Button(self.root, text="Negative Image", command=lambda:self.negative(path)).grid(
            row=2, column=1, padx=2, pady=2, sticky=W, ipadx=4)
        Button(self.root, text="Blur Image", command=lambda:self.blur(path)).grid(
            row=2, column=2, padx=2, pady=2, sticky=W, ipadx=8)
        Button(self.root, text="Smooth Image", command=lambda:self.smooth(path)).grid(
            row=2, column=3, padx=2, pady=2, sticky=W)
        
        Button(self.root, text="Red Image", command=lambda:self.red(path)).grid(
            row=3, column=0, padx=2, pady=2, sticky=W, ipadx=35)
        Button(self.root, text="Green Image", command=lambda:self.green(path)).grid(
            row=3, column=1, padx=2, pady=2, sticky=W, ipadx=14)
        Button(self.root, text="Blue Image", command=lambda:self.blue(path)).grid(
            row=3, column=2, padx=2, pady=2, sticky=W, ipadx=6)
        Button(self.root, text="Sketch Image", command=lambda:self.sketch(path)).grid(
            row=3, column=3, padx=2, pady=2, sticky=W, ipadx=4)

        return path

    def show(self, path):
        img_f = cv2.imread(path)
        img = self.cv2_to_PIL(img_f)
        self.top_pop("Original", img, img_f)

    def showinfo(self, path):
        img = cv2.imread(path)
        info = "Path: "+str(path)+"\n\nResolution: "+str(img.shape[0])+" x "+str(img.shape[1])
        response = messagebox.showinfo("Info", info)
        return response

    def resize(self, path):
        def get_shape(img):
            global myImage
            num = e.get().split()
            x,y = int(num[0]), int(num[1])
            E.destroy()
            img_f = cv2.resize(img, (x,y))
            img = self.cv2_to_PIL(img_f)
            self.top_pop("Resize", img, img_f)

        img = cv2.imread(path)      
        E = Toplevel()
        E.title("XY")
        E.iconbitmap("icon.ico")
        e = Entry(E, width=30)
        e.insert(0, "Enter X and Y (Separate with space)")
        e.pack()
        btn = Button(E, text="Enter", command=lambda:get_shape(img)).pack()

    def gray(self, path):
        img = cv2.imread(path)
        img_f = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = self.cv2_to_PIL(img_f)
        self.top_pop("Grayscale", img, img_f)

    def negative(self, path):
        img = cv2.imread(path)
        img_f = 1 - img
        img = self.cv2_to_PIL(img_f)
        self.top_pop("Negative", img, img_f)

    def red(self, path):
        img = cv2.imread(path)
        img = img[:,:,0]
        black = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
        img_f = np.stack((black,black,img), axis=2)
        img = self.cv2_to_PIL(img_f)
        self.top_pop("Red", img, img_f)

    def green(self, path):
        img = cv2.imread(path)
        img = img[:,:,1]
        black = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
        img_f = np.stack((black,img,black), axis=2)
        img = self.cv2_to_PIL(img_f)
        self.top_pop("Green", img, img_f)

    def blue(self, path):
        img = cv2.imread(path)
        img = img[:,:,2]
        black = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
        img_f = np.stack((img,black,black), axis=2)
        img = self.cv2_to_PIL(img_f)
        self.top_pop("Blue", img, img_f)

    def crop(self,path):
        img = cv2.imread(path)
        value = cv2.selectROI(img, False)
        img_f = img[value[1]:value[1]+value[3],
                    value[0]:value[0]+value[2]]
        img = self.cv2_to_PIL(img_f)
        self.top_pop("Crop", img, img_f)

    def blur(self, path):
        img = cv2.imread(path)
        img_f = cv2.blur(img, (3,3))
        img = self.cv2_to_PIL(img_f)
        self.top_pop("Blur", img, img_f)

    def smooth(self, path):
        img = cv2.imread(path)
        img_f = cv2.edgePreservingFilter(img, cv2.RECURS_FILTER, 300, 0.6)
        img = self.cv2_to_PIL(img_f)
        self.top_pop("Smooth", img, img_f)

    def sketch(self, path):
        img = cv2.imread(path)
        pencil, img_f = cv2.pencilSketch(img, 100, 0.1, shade_factor=0.1)
        img = self.cv2_to_PIL(img_f)
        self.top_pop("Sketch", img, img_f)
    
    def rotate(self, path):
        img = cv2.imread(path)
        def choose_function(img, value):
            if value == "rotate 90 clockwise":
                img_f = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
                img = self.cv2_to_PIL(img_f)
                self.top_pop("Rotate", img, img_f)
            if value == "rotate 180":
                img_f = cv2.rotate(img, cv2.ROTATE_180)
                img = self.cv2_to_PIL(img_f)
                self.top_pop("Rotate", img, img_f)
            if value == "rotate 90 counterclockwise":
                img_f = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
                img = self.cv2_to_PIL(img_f)
                self.top_pop("Rotate", img, img_f)      
        
        E = Toplevel()
        E.title("Function")
        E.iconbitmap("icon.ico")
        rotate_func = [("rotate 90 clockwise","rotate 90 clockwise"),
                        ("rotate 180","rotate 180"),
                        ("rotate 90 counterclockwise","rotate 90 counterclockwise")]
        selected = StringVar()
        selected.set("rotate 90 clockwise")
        for text, selections in rotate_func:
            Radiobutton(E, text=text, variable=selected, value=selections).pack(anchor=W)
        btn = Button(E, text="Enter", command=lambda:choose_function(img, selected.get())).pack()

    def flip(self, path):
            img = cv2.imread(path)
            def choose_function(img, value):
                if value == "Vertical":
                    img_f = cv2.flip(img, 0)
                    img = self.cv2_to_PIL(img_f)
                    self.top_pop("Flip", img, img_f)
                if value == "Horizontal":
                    img_f = cv2.flip(img, 2)
                    img = self.cv2_to_PIL(img_f)
                    self.top_pop("Flip", img, img_f)
            
            E = Toplevel()
            E.title("Function")
            E.iconbitmap("icon.ico")
            flip_func = [("Vertical","Vertical"),
                            ("Horizontal","Horizontal")]
            selected = StringVar()
            selected.set("Vertical")
            for text, selections in flip_func:
                Radiobutton(E, text=text, variable=selected, value=selections).pack(anchor=W)
            btn = Button(E, text="Enter", command=lambda:choose_function(img, selected.get())).pack()

    def border(self, path):
        def get_border(img):
            num = e.get().split()
            top, bottom, left, right = int(num[0]), int(num[1]), int(num[2]), int(num[3])
            E.destroy()
            img_f = cv2.copyMakeBorder(img, top,bottom,left,right, cv2.BORDER_CONSTANT,
                                      value=(255,255,255))
            img = self.cv2_to_PIL(img_f)
            self.top_pop("Border", img, img_f)

        img = cv2.imread(path)      
        E = Toplevel()
        E.title("Border set")
        E.iconbitmap("icon.ico")
        e = Entry(E, width=50)
        e.insert(0, "Top Bottom Left Right (split with space)")
        e.pack()
        btn = Button(E, text="Enter", command=lambda:get_border(img)).pack()

    def text(self, path):
        def put_text(img):
            txt = e.get()
            E.destroy()
            img_f = cv2.putText(img, str(txt), (10,30), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0,0,0))
            img = self.cv2_to_PIL(img_f)
            self.top_pop("Text Image", img, img_f)

        img = cv2.imread(path)      
        E = Toplevel()
        E.title("Text")
        E.iconbitmap("icon.ico")
        e = Entry(E, width=50)
        e.insert(0, "Enter text:")
        e.pack()
        btn = Button(E, text="Enter", command=lambda:put_text(img)).pack()
