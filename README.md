
  

# Simemens HMI Screenshots Processing

  

  

This Python script is designed for processing Simemens HMI (Human-Machine Interface) screenshots. It allows you to convert PDF files to images and crop them to a specific size. Follow the instructions below to install and use the script.

  

![image](program.PNG)

  

## Installation

  

1.  **Install Python**:

Ensure that you have Python installed on your system. If not, download and install it from the official Python website: [Python Downloads](https://www.python.org/downloads).

  

  

3.  **Install Required Packages**:
Open a command prompt.
Install the necessary Python packages using `pip` by running the following commands:
-  `pdf2image`: Run `pip install pdf2image`.
-  `PIL`: Run `pip install pillow`.
3.  **Download the Source Folder of Script**:

## Usage
4.  **Running the Script**

Comand Promt

-  **Open a Command Prompt**

-  **Navigate to the Script Directory**

Use the `cd` command to navigate to the directory where you saved the `program.py` file.

-  **Run the Script**

Execute the script by running the following command:

```

python program.py

```

OR

-  **Open the Source Folder of Script**

-  **Run the Script**

Execute the script by double-clicking on `program.py` file.

5.  **Using the GUI**:

  

The script will open a graphical user interface (GUI) window with the following steps for processing Siemens HMI screenshots:

  

  

-  **Step 1: Select the PDF Directory**

  

Click on the "PDF Directory" button to choose the directory containing the PDF files you want to convert to images.

The selected directory path will be displayed in the GUI.

  

-  **Step 2: Enter the Reduction Ratio**

  

In the text entry box, enter the desired reduction ratio, e.g., 3.5 (a higher ratio will result in smaller images).

  

-  **Step 3: Perform the Processing**

  

Click on the "Crop" button to start the conversion and cropping process.

The script will convert the PDF files to images and crop them based on the specified ratio.

The progress will be displayed in the command prompt or terminal.

 Once the process is complete, a message will appear in the GUI indicating the completion.

6.  **Processed Images**:

  The processed images will be saved in the same directory as the PDF files:

  Cropped images: The original images will be replaced with the cropped versions, suffixed with "_screen_big.jpg".

 Small images: Additional resized images will be saved with the suffix "_screen_small.jpg".

  

  

7.  **Exit the Script**:

Close the GUI window to exit the script.

  

  #
**Note**: Ensure you have the necessary permissions to access and modify the files in the selected directories.
##
  

 

That's it! You can now use this script to process Siemens HMI screenshots and automate the conversion and cropping process.
