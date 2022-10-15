from tkinter import*
import fitz
from tkinter.ttk import Progressbar
from threading import Thread
import math

"""
The ShowPDF class was taken from the PyPi module tkPDFViewer. This class, however, was outdated and no longer 
functional, so I copied the class into its own file and modified it to work with my CertHelper project.
"""


class ShowPDF:

    def __init__(self):
        self.frame = ''
        self.display_msg = Label()
        self.text = Text()
        self.img_object_li = []

    def pdf_view(self, master, width=1200, height=600, pdf_location="", bar=True, load="after"):

        self.frame = Frame(master, width=width, height=height, background="#F1F1F1")

        scroll_y = Scrollbar(self.frame, orient="vertical")
        scroll_x = Scrollbar(self.frame, orient="horizontal")

        scroll_x.pack(fill="x", side="bottom")
        scroll_y.pack(fill="y", side="right")

        percentage_load = StringVar()

        if bar and load == "after":
            self.display_msg = Label(textvariable=percentage_load)
            self.display_msg.place(anchor='n', y=540, x=480)

            loading = Progressbar(self.frame, orient=HORIZONTAL, length=100, mode='determinate')
            loading.pack(side=TOP, fill=X)

        self.text = Text(self.frame, background='#F1F1F1', yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set,
                         width=width, height=height)
        self.text.pack(side="left")

        scroll_x.config(command=self.text.xview)
        scroll_y.config(command=self.text.yview)

        def add_img():
            percentage = 0
            # noinspection PyUnresolvedReferences
            open_pdf = fitz.open(pdf_location)

            for page in open_pdf:
                pix = page.get_pixmap(dpi=113)
                pix1 = fitz.Pixmap(pix, 0) if pix.alpha else pix
                img = pix1.tobytes("ppm")
                timg = PhotoImage(data=img)
                self.img_object_li.append(timg)
                if bar and load == "after":
                    percentage += 1
                    percentage_view = (float(percentage)/float(len(open_pdf))*float(100))
                    loading['value'] = percentage_view
                    percentage_load.set(f"PDF loading {int(math.floor(percentage_view))}%")
            if bar and load == "after":
                loading.pack_forget()
                self.display_msg.place_forget()

            for i in self.img_object_li:
                self.text.image_create(END, image=i)
                self.text.insert(END, "\n\n")
            self.text.configure(state="disabled")

        def start_pack():
            t1 = Thread(target=add_img)
            t1.start()

        if load == "after":
            master.after(250, start_pack)
        else:
            start_pack()

        return self.frame
