import pyttsx3
from PyPDF2 import PdfReader

def pdf_to_speech(pdf_file):
    # Open the PDF file
    with open(pdf_file, 'rb') as file:
        # Initialize the PDF reader object
        reader = PdfReader(file)

        # Extract text from each page of the PDF
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Convert text to speech
    engine.say(text)

    # Play the speech
    engine.runAndWait()


# Example usage
pdf_file ="pdf file path"
pdf_to_speech(pdf_file)
