import qrcode
from PIL import Image,ImageTk
import tkinter as tk1
from tkinter import ttk
from tkinter import filedialog
def attach_file():
    file_path="C:\\Users\\varsha\\OneDrive\\Documents\\QR Code.docx"
    file= filedialog.openfile(file_path,title="QR Code",filetypes=[("Word files", "*.docx *.doc"), ("All files", "*.*")])
m=tk1.Tk()
m.geometry("300x200")
m.title('QR Code Generator')
paragraph="""                       QR Code Generator
A QR code generator program is a software application or script that creates Quick Response (QR) codes, which are two-dimensional barcodes that can store
various types of data, such as URLs, text, contact information, or other data.
QR codes are widely used for a variety of purposes, including marketing, ticketing, authentication, and data sharing.
Overall, QR code generator programs provide a convenient and versatile way to create QR codes for a wide range of 
applications, making it easy to share information digitally in a visually compact format.
A QR code (Quick Response code) generator program is software that allows users to create QR codes quickly and easily. QR codes are two-dimensional barcodes that can store various types of information, such as URLs, text, contact information, Wi-Fi network details, and more. They are widely used in marketing, advertising, packaging, 
and various other applications to provide quick access to information or links."""
image_path="C:\\Users\\varsha\\OneDrive\\Documents\\qrcodeimage (1).jpg"
img=Image.open(image_path)
photo = ImageTk.PhotoImage(img)
image_label = tk1.Label(m, image=photo)
new_width=40
new_height=20
img = img.resize((new_width, new_height))
image_label.pack(side="top")
text_widget = tk1.Text(m, wrap=tk1.WORD)
text_widget.insert(tk1.END, paragraph)
text_widget.config(width=70,height=20)
text_widget.pack()
l1=tk1.Label(m,text="ENTER THE SITE TO ACCESS")
l1.pack(side="top")
def generate_qr():
    url= url_entry.get()    
    qr=qrcode.QRCode(version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img=qr.make_image(fill_color="Black",back_color="White")
    img.show()
url_entry = tk1.Entry(m, width=40)
url_entry.pack()    
button1=ttk.Button(m,text="Generate QR Code",command=generate_qr)
button1.pack(side="top")
m.mainloop()