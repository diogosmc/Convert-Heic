import os
import tkinter as tk
from tkinter import filedialog
from heic2png import HEIC2PNG

class ImageConverterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Conversor de Imagens HEIC para PNG")

        self.label = tk.Label(master, text="Selecione o diretório com imagens HEIC")
        self.label.pack()

        self.select_button = tk.Button(master, text="Selecionar diretório", command=self.select_directory)
        self.select_button.pack()

        self.convert_button = tk.Button(master, text="Converter para PNG", command=self.convert_images, state=tk.DISABLED)
        self.convert_button.pack()

    def select_directory(self):
        self.directory = filedialog.askdirectory()
        if self.directory:
            self.convert_button['state'] = tk.NORMAL

    def convert_images(self):
        output_directory = os.path.join(self.directory, "converted_images")
        os.makedirs(output_directory, exist_ok=True)

        for filename in os.listdir(self.directory):
            if filename.strip().lower().endswith(".heic"):
                heic_img = HEIC2PNG(os.path.join(self.directory, filename), quality=90)
                output_filename = os.path.join(output_directory, os.path.splitext(filename)[0] + ".png")
                heic_img.save(output_filename)

        tk.messagebox.showinfo("Conversão concluída", "Todas as imagens HEIC foram convertidas para PNG e salvas em '{}'!".format(output_directory))

root = tk.Tk()
gui = ImageConverterGUI(root)
root.mainloop()
