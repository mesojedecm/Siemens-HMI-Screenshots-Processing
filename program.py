import glob, os, PIL.Image, PIL.ImageTk
from pdf2image import convert_from_path
from tkinter import *
from tkinter import filedialog

window = Tk()
window.geometry ("600x210")
window.title("Obdelava HMI screenshotov")

current_directory = os.getcwd()
poppler_directory = "\\poppler-23.08.0\\Library\\bin"
logo_directory = "\\pic\\pio_logo.jpg"
poppler_directory =  current_directory + poppler_directory
logo_directory = current_directory + logo_directory


def openDirectoryPDF():
    global pdf_directory
    pdf_directory = filedialog.askdirectory()
    pdf_directory = pdf_directory.replace('/', '\\')
    print('Lokacija PDF: ' + pdf_directory + '\n')
    print('Lokacija poppler: ' + poppler_directory + '\n')
    D1 = Label(window, text = pdf_directory)
    D1.place(x=0, y=40)
    return pdf_directory

def pdfToImage():
    pdf_filenames = glob.glob(pdf_directory + '/*.pdf')
    for pdf_filename in pdf_filenames:
        images = convert_from_path(pdf_filename, poppler_path=poppler_directory)
        for i, image in enumerate(images):
            image.save(f"{pdf_filename[:-4]}_{i}.png", 'PNG')

def crop():
    jpg_filenames = glob.glob(pdf_directory + '/*.png')  
    ratio = float(E1.get())
    width_small = 1574/ratio
    height_small = 935/ratio
    small_size = int(width_small), int(height_small)
    print(ratio)
    for jpg_file in jpg_filenames:
        img = PIL.Image.open(jpg_file)
        width, height = img.size
        left = 42
        top = 35
        right = width - 37
        bottom = 970
        crop = img.crop((left, top, right, bottom))
        crop.save(jpg_file[:-4] + '_screen_big.png', 'PNG')
        resize = crop.resize(small_size)
        resize.save(jpg_file[:-4] + '_screen_small.png', 'PNG')
        os.remove(jpg_file)
        L3 = Label(window, text='Končano!', fg="blue", font=('Poppins bold', 15))
        L3.place(x=150, y=150)
        print(f"{jpg_file} je obdelan.")

def process():
    pdfToImage()
    crop()
        

button1 = Button(window, text="PDF mapa", command=openDirectoryPDF, bg="brown", fg="white", font=('Poppins bold', 15))
button1.place(x=215, y=0)
L1 = Label(window, text="1. Izberi mapo s PDF-ji", font=('Poppins bold', 15))
L1.place(x=0, y=5)


L2 = Label(window, text="2. Vpiši stopnjo pomanjšanja, npr. 3.5", font=('Poppins bold', 15))
L2.place(x=0, y=63)
E1 = Entry(window, width=3, font=('Poppins bold', 15))
E1.place(x=340, y=65)

L3 = Label(window, text="3. Izvedi proces", font=('Poppins bold', 15))
L3.place(x=0, y=98)
button2 = Button(text="Obreži", command=process, bg="brown", fg="white", font=('Poppins bold', 15))
button2.place(x=150, y=95)


frame = Frame(window)
frame.pack(side=RIGHT)

img1 = PIL.ImageTk.PhotoImage(PIL.Image.open(logo_directory)) 
label = Label(frame, image = img1) 
label.pack()

window.mainloop()
