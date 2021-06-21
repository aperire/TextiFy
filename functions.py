import pytesseract
from gingerit.gingerit import GingerIt

def img_to_txt(file):
    #Windows--
    #pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
    #Mac--
    #brew install tesseract
    return pytesseract.image_to_string(file)

def write_txt(name, string):
    f = open(f"{name}.txt", "w+")
    f.write(string)
    f.close()

def fix_grammar(text):
    res = GingerIt().parse(text)
    return res["result"]

