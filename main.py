from image_functions_GUI import image_functions
from tkinter import *
img_func = image_functions()

# All Buttons
btn_exit = Button(img_func.root, text="Exit", command=img_func.root.quit).grid(
    row=5, column=3, padx=2, pady=2, ipadx=37)

btn_select = Button(img_func.root, text="Select an Image", command=img_func.select_img).grid(
    row=0, column=0, padx=2, pady=2, sticky=W, ipadx=17)

btn_show = Button(img_func.root, text="Show Original Image", command=lambda:img_func.show(img_func.select_img), state=DISABLED).grid(
    row=1, column=0, padx=2, pady=2, sticky=W)
btn_showinfo = Button(img_func.root, text="Show Image Info", command=lambda:img_func.showinfo(img_func.select_img), state=DISABLED).grid(
    row=1, column=1, padx=2, pady=2, sticky=W)
btn_resize = Button(img_func.root, text="Resize Image", command=lambda:img_func.resize(img_func.select_img), state=DISABLED).grid(
    row=1, column=2, padx=2, pady=2, sticky=W, ipadx=1)
btn_crop = Button(img_func.root, text="Crop Image", command=lambda:img_func.crop(img_func.select_img), state=DISABLED).grid(
    row=1, column=3, padx=2, pady=2, sticky=W, ipadx=10)

btn_gray = Button(img_func.root, text="Grayscale Image", command=lambda:img_func.gray(img_func.select_img), state=DISABLED).grid(
    row=2, column=0, padx=2, pady=2, sticky=W, ipadx=16)
btn_neg = Button(img_func.root, text="Negative Image", command=lambda:img_func.negative(img_func.select_img), state=DISABLED).grid(
    row=2, column=1, padx=2, pady=2, sticky=W, ipadx=4)
btn_blur = Button(img_func.root, text="Blur Image", command=lambda:img_func.blur(img_func.select_img), state=DISABLED).grid(
    row=2, column=2, padx=2, pady=2, sticky=W, ipadx=9)
btn_smooth = Button(img_func.root, text="Smooth Image", command=lambda:img_func.smooth(img_func.select_img), state=DISABLED).grid(
    row=2, column=3, padx=2, pady=2, sticky=W)

btn_red = Button(img_func.root, text="Red Image", command=lambda:img_func.red(img_func.select_img), state=DISABLED).grid(
    row=3, column=0, padx=2, pady=2, sticky=W, ipadx=35)
btn_green = Button(img_func.root, text="Green Image", command=lambda:img_func.green(img_func.select_img), state=DISABLED).grid(
    row=3, column=1, padx=2, pady=2, sticky=W, ipadx=14)
btn_blue = Button(img_func.root, text="Blue Image", command=lambda:img_func.blue(img_func.select_img), state=DISABLED).grid(
    row=3, column=2, padx=2, pady=2, sticky=W, ipadx=7)
btn_sketch = Button(img_func.root, text="Sketch Image", command=lambda:img_func.sketch(img_func.select_img), state=DISABLED).grid(
    row=3, column=3, padx=2, pady=2, sticky=W, ipadx=4)

btn_rotate = Button(img_func.root, text="Rotate Image", command=lambda:img_func.rotate(img_func.select_img), state=DISABLED).grid(
    row=4, column=0, padx=2, pady=2, sticky=W, ipadx=26)
btn_flip = Button(img_func.root, text="Flip Image", command=lambda:img_func.flip(img_func.select_img), state=DISABLED).grid(
    row=4, column=1, padx=2, pady=2, sticky=W, ipadx=22)
btn_border = Button(img_func.root, text="Border Image", command=lambda:img_func.border(img_func.select_img), state=DISABLED).grid(
    row=4, column=2, padx=2, pady=2, sticky=W)
btn_text = Button(img_func.root, text="Text Image", command=lambda:img_func.text(img_func.select_img), state=DISABLED).grid(
    row=4, column=3, padx=2, pady=2, sticky=W, ipadx=12)



img_func.root.mainloop()
