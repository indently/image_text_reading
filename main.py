from PIL import Image
from pytesseract import pytesseract
import enum


class OS(enum.Enum):
    Mac = 0
    Windows = 1


class Language(enum.Enum):
    ENG = 'eng'
    RUS = 'rus'
    ITA = 'ita'


class ImageReader:
    # We provide the setup in our initializer
    def __init__(self, os: OS):
        if os == OS.Mac:
            # Tesseract is already installed via Homebrew
            print('Running on: MAC\n')

        if os == OS.Windows:
            # This should be replaced with your own path to: tesseract.exe
            windows_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            pytesseract.tesseract_cmd = windows_path
            print('Running on: WINDOWS\n')

    # Specify the image and language for the text you want to extract
    def extract_text(self, image: str, lang: Language) -> str:
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img, lang=lang.value)
        return extracted_text


if __name__ == '__main__':
    ir = ImageReader(OS.Mac)
    # Multiple languages can be used with: 'eng+ita+rus'
    text = ir.extract_text(image='images/kings.png', lang=Language.ENG)

    # Do some light processing before printing the text
    processed_text = ' '.join(text.split())
    print(processed_text)
