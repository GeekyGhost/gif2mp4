from moviepy.editor import VideoFileClip
from tkinter import filedialog, Tk, Label, Button, StringVar, Radiobutton
from pathlib import Path
import os

def browse():
    if folder_or_files.get() == 'folder':
        folder_path.set(filedialog.askdirectory())
    elif folder_or_files.get() == 'files':
        file_paths = filedialog.askopenfilenames(filetypes=[("GIF and MP4 files", "*.gif;*.mp4")])
        folder_path.set(', '.join(file_paths))
    print(f"Selected path: {folder_path.get()}")  # Debugging

def convert():
    print("Converting...")  # Debugging
    if not folder_path.get():
        print("No folder or files selected.")  # Debugging
        status_label.config(text="No folder or files selected.")
        return

    try:
        if folder_or_files.get() == 'folder':
            for filename in os.listdir(folder_path.get()):
                if filename.endswith('.gif') or filename.endswith('.mp4'):
                    convert_file(os.path.join(folder_path.get(), filename))
        elif folder_or_files.get() == 'files':
            for file_path in folder_path.get().split(', '):
                convert_file(file_path)

        status_label.config(text="Conversion completed!")
    except Exception as e:
        print(f"An error occurred: {e}")  # Debugging
        status_label.config(text=f"An error occurred: {e}")

def convert_file(input_path):
    try:
        print(f"Converting {input_path}")  # Debugging
        output_directory = Path(input_path).parent
        conversion_type = conversion_choice.get()

        if conversion_type == 'gif_to_mp4':
            output_filename = Path(input_path).stem + '.mp4'
            output_path = output_directory / output_filename
            clip = VideoFileClip(input_path)
            clip.write_videofile(str(output_path))
        elif conversion_type == 'mp4_to_gif':
            output_filename = Path(input_path).stem + '.gif'
            output_path = output_directory / output_filename
            clip = VideoFileClip(input_path)
            clip.write_gif(str(output_path))

        clip.close()
    except Exception as e:
        print(f"Error in convert_file: {e}")  # Debugging
        status_label.config(text=f"Error: {e}")

if __name__ == "__main__":
    root = Tk()
    root.title("Media Converter")

    folder_path = StringVar()
    folder_or_files = StringVar()
    folder_or_files.set('folder')  # default to folder selection
    conversion_choice = StringVar()
    conversion_choice.set('gif_to_mp4')  # default to GIF to MP4 conversion

    Label(root, text="Choose conversion mode:").pack()

    Radiobutton(root, text="Folder", variable=folder_or_files, value='folder').pack()
    Radiobutton(root, text="Files", variable=folder_or_files, value='files').pack()

    Label(root, text="Choose conversion type:").pack()

    Radiobutton(root, text="GIF to MP4", variable=conversion_choice, value='gif_to_mp4').pack()
    Radiobutton(root, text="MP4 to GIF", variable=conversion_choice, value='mp4_to_gif').pack()

    Button(root, text="Browse", command=browse).pack()
    Label(root, textvariable=folder_path).pack()

    Button(root, text="Start Conversion", command=convert).pack()
    status_label = Label(root, text="")
    status_label.pack()

    root.mainloop()
