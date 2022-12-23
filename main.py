from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont

window = Tk()
window.title('Apply your Watermark to an Image')

canvas = Canvas(width=200, height=300, bg='#EAFDFC', highlightthickness=0)

pic_path = tk.Label(canvas, text='Image Path:', padx=25, pady=25,
                    font=('verdana', 16), bg='#EAFDFC')
show_pic = tk.Label(canvas, bg='#EAFDFC')
entry_path = tk.Entry(canvas, font=('#82AAE3', 16))
btn_browse = tk.Button(canvas, text='Select Image', bg='#BFEAF5', fg='#82AAE3',
                       font=('verdana', 16))


def findPic():
    global img
    global filename
    filename = filedialog.askopenfilename(initialdir="/images", title="Select Image",
                                          filetypes=(("png images", "*.png"), ("jpg images", "*.jpg")))

    img = Image.open(filename)
    img = img.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    show_pic['image'] = img
    entry_path.insert(0, filename)


def apply_text():
    img = Image.open(filename).convert("RGBA")
    txt = Image.new('RGBA', img.size, (255, 255, 255, 0))

    # Creating Draw Object
    draw_text = ImageDraw.Draw(txt)

    # Creating text and font object
    text = entry.get()
    font = ImageFont.truetype('arial.ttf', 82)

    # Positioning Text
    width, height = img.size
    textwidth, textheight = draw_text.textsize(text, font)
    x = width / 2 - textwidth / 2
    y = height - textheight - 300

    # Applying Text
    draw_text.text((x, y), text, fill=(255, 255, 255, 125), font=font)

    # Combining Original Image with Text and Saving
    watermarked = Image.alpha_composite(img, txt)
    watermarked.show()
    watermarked.save(r'watermarked.png')


btn_browse['command'] = findPic

label = Label(window, text="", font=('arial.ttf', 82))

canvas.pack()

pic_path.grid(row=0, column=0)
entry_path.grid(row=0, column=1, padx=(0, 20))
show_pic.grid(row=1, column=0, columnspan=2)
btn_browse.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create an Entry widget to accept User Input


entry = Entry(window, bg='#EAFDFC', fg='blue', width=40)

entry.focus_set()
entry.pack()

ttk.Button(window, text="Enter your watermark", width=20, command=apply_text).pack(pady=20)

window.mainloop()
