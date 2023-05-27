from image_functions_GUI import image_functions
from tkinter import *
img_func = image_functions()
img = img_func.select_img
# All Buttons
btn_exit = Button(img_func.root, text="Exit", command=img_func.root.quit).grid(
    row=5, column=3, padx=2, pady=2, ipadx=37)

btn_select = Button(img_func.root, text="Select an Image", command=img).grid(
    row=0, column=0, padx=2, pady=2, sticky=W, ipadx=19)

btn_show = Button(img_func.root, text="Show Original Image", command=lambda:img_func.show(img), state=DISABLED).grid(
    row=1, column=0, padx=2, pady=2, sticky=W, ipadx=2)
btn_showinfo = Button(img_func.root, text="Show Image Info", command=lambda:img_func.showinfo(img), state=DISABLED).grid(
    row=1, column=1, padx=2, pady=2, sticky=W)
btn_resize = Button(img_func.root, text="Resize Image", command=lambda:img_func.resize(img), state=DISABLED).grid(
    row=1, column=2, padx=2, pady=2, sticky=W, ipadx=6)
btn_crop = Button(img_func.root, text="Crop Image", command=lambda:img_func.crop(img), state=DISABLED).grid(
    row=1, column=3, padx=2, pady=2, sticky=W, ipadx=10)

btn_gray = Button(img_func.root, text="Grayscale Image", command=lambda:img_func.gray(img), state=DISABLED).grid(
    row=2, column=0, padx=2, pady=2, sticky=W, ipadx=18)
btn_neg = Button(img_func.root, text="Negative Image", command=lambda:img_func.negative(img), state=DISABLED).grid(
    row=2, column=1, padx=2, pady=2, sticky=W, ipadx=4)
btn_blur = Button(img_func.root, text="Blur Image", command=lambda:img_func.blur(img), state=DISABLED).grid(
    row=2, column=2, padx=2, pady=2, sticky=W, ipadx=14)
btn_smooth = Button(img_func.root, text="Smooth Image", command=lambda:img_func.smooth(img), state=DISABLED).grid(
    row=2, column=3, padx=2, pady=2, sticky=W)

btn_red = Button(img_func.root, text="Red Image", command=lambda:img_func.red(img), state=DISABLED).grid(
    row=3, column=0, padx=2, pady=2, sticky=W, ipadx=37)
btn_green = Button(img_func.root, text="Green Image", command=lambda:img_func.green(img), state=DISABLED).grid(
    row=3, column=1, padx=2, pady=2, sticky=W, ipadx=14)
btn_blue = Button(img_func.root, text="Blue Image", command=lambda:img_func.blue(img), state=DISABLED).grid(
    row=3, column=2, padx=2, pady=2, sticky=W, ipadx=12)
btn_sketch = Button(img_func.root, text="Sketch Image", command=lambda:img_func.sketch(img), state=DISABLED).grid(
    row=3, column=3, padx=2, pady=2, sticky=W, ipadx=4)

btn_rotate = Button(img_func.root, text="Rotate Image", command=lambda:img_func.rotate(img), state=DISABLED).grid(
    row=4, column=0, padx=2, pady=2, sticky=W, ipadx=28)
btn_flip = Button(img_func.root, text="Flip Image", command=lambda:img_func.flip(img), state=DISABLED).grid(
    row=4, column=1, padx=2, pady=2, sticky=W, ipadx=22)
btn_border = Button(img_func.root, text="Border Image", command=lambda:img_func.border(img), state=DISABLED).grid(
    row=4, column=2, padx=2, pady=2, sticky=W, ipadx=5)
btn_text = Button(img_func.root, text="Text Image", command=lambda:img_func.text(img), state=DISABLED).grid(
    row=4, column=3, padx=2, pady=2, sticky=W, ipadx=12)

btn_color = Button(img_func.root, text="Brightness & Contrast", command=lambda:img_func.bright_contrast(img), state=DISABLED).grid(
    row=5, column=0, padx=2, pady=2, sticky=W)
btn_edge = Button(img_func.root, text="Image Edge", command=lambda:img_func.edge(img), state=DISABLED).grid(
    row=5, column=1, padx=2, pady=2, sticky=W, ipadx=17)
btn_sharp = Button(img_func.root, text="Sharpen Image", command=lambda:img_func.sharpen(img), state=DISABLED).grid(
    row=5, column=2, padx=2, pady=2, sticky=W)

img_func.root.mainloop()
