import pytesseract                                                      
import re
from PIL import Image  

class ImageProcessing:
    def __init__(self, image_path, regex):
        self.image = Image.open(image_path)
        # self.lang = 'eng'
        
        # download and install mcr language 
        #  https://github.com/BigPino67/Tesseract-MICR-OCR/blob/master/Tessdata/mcr.traineddata

        self.lang = 'mcr'
        self.pattern = r"{}".format(regex)
        self.compile = re.compile(self.pattern)
        self.result  = None

    def img_to_str(self):
        return pytesseract.image_to_string(self.image, lang=self.lang).split("\n")

    
    def generate_result(self):
        for text_data in self.img_to_str():
            # text_data = data.replace(" ", "")
            if self.compile.match(text_data):
                self.result = text_data
        return self.result

    def print_imagetext(self):
        print ("*" * 100)
        for data in self.img_to_str():
            print (data)
        print ("*" * 100)

if __name__ == "__main__":
    import json
    with open('input_json.json', 'r') as input:
        # Reading from file
        json_data_list = json.loads(input.read())

    for data in json_data_list:
        print (ImageProcessing(data.get('image_path'), data.get('regex')).generate_result())


