from moviepy.editor import *
from tkinter import filedialog, Tk, Label, Button, StringVar, Radiobutton
import os

def browse():
    if folder_or_files.get() == 'folder':
        folder_path.set(filedialog.askdirectory())
    elif folder_or_files.get() == 'files':
        file_paths = filedialog.askopenfilenames(filetypes=[("GIF files", "*.gif")])
        folder_path.set(', '.join(file_paths))

def convert():
    if folder_or_files.get() == 'folder':
        for filename in os.listdir(folder_path.get()):
            if filename.endswith('.gif'):
                convert_file(os.path.join(folder_path.get(), filename))
    elif folder_or_files.get() == 'files':
        for file_path in folder_path.get().split(', '):
            convert_file(file_path)

    status_label.config(text="Conversion completed!")

def convert_file(input_path):
    output_filename = os.path.basename(input_path).split('.gif')[0] + '.mp4'
    output_path = os.path.join(folder_path.get(), output_filename)

    clip = VideoFileClip(input_path)
    clip.write_videofile(output_path)

if __name__ == "__main__":
    root = Tk()
    root.title("GIF to MP4 Converter")

    folder_path = StringVar()
    folder_or_files = StringVar()
    folder_or_files.set('folder')  # default to folder selection

    Label(root, text="Choose conversion mode:").pack()

    Radiobutton(root, text="Folder", variable=folder_or_files, value='folder').pack()
    Radiobutton(root, text="Files", variable=folder_or_files, value='files').pack()

    Button(root, text="Browse", command=browse).pack()
    Label(root, textvariable=folder_path).pack()

    Button(root, text="Start Conversion", command=convert).pack()
    status_label = Label(root, text="")
    status_label.pack()

    root.mainloop()
