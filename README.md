# gif2mp4
GIF to MP4 Converter
Overview
This is a simple, easy-to-use converter that transforms GIF files into MP4 videos. Built with Python and Tkinter, the tool offers a GUI for added convenience. Whether you need to convert a single file or an entire folder of GIFs, this script has got you covered.

Dependencies
Python 3.x
Tkinter
MoviePy
Setup
For Windows users, the project includes a .bat file that automates the environment setup. Just double-click to run and it will:

Create a Python virtual environment
Activate the virtual environment
Install the required packages
For others, you can manually set up the virtual environment and install dependencies using pip.

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
Usage
Run the script.
Select the conversion mode. You can choose to convert either a single file or all GIFs within a folder.
Click the 'Browse' button to select your input GIF(s).
Click 'Start Conversion'.
The converted MP4 files will be saved in the same directory as the input GIFs.

How it Works
The tool leverages the MoviePy library to handle the conversion, ensuring that the output retains the quality of the original GIFs.

That's it! Happy converting.
