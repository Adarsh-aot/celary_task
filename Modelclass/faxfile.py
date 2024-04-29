from pathlib import Path as path
import os
from Modelclass.ImageProcessor import ImageProcessor
from Modelclass.PdfProcessor import PdfProcessor
from Modelclass.ModelProcessor import ModelProcessor
from Modelclass.DonutValidater import DonutValidater
from Modelclass.JsonWriter import JsonWriter


class FaxFile:
    """
    Represents a fax file. This class can process a fax file and extract relevant information from it.

    Attributes:
    - pdf_file (pathlib.Path): The path to the fax file.
    - pdf_file_name (str): The name of the fax file (without extension).
    - pages (list): A list to store the names of the images extracted from the fax file.
    - png_processor (ImageProcessor): An instance of ImageProcessor to process images.
    - model_processor (ModelProcessor): An instance of ModelProcessor to process the fax file.
    - donuut_validator (DonutValidater): An instance of DonutValidater to validate the extracted information.
    - json_writer (JsonWriter): An instance of JsonWriter to write the extracted information to a JSON file.
    """

    def __init__(self, pdf_file):
        """
        Initialize a FaxFile object.

        Parameters:
        - pdf_file (str): The path to the fax file.
        """
        self.pages = []
        self.pdf_file = path(pdf_file)
        self.pdf_file_name = os.path.basename(pdf_file)
        self.png_processor = ImageProcessor()
        self.model_processor = ModelProcessor()
        self.donuut_validator = DonutValidater()
        self.json_writer = JsonWriter()

    def process_file(self):
        """
        Process the fax file and extract relevant information from it.
        """
        image_list = PdfProcessor.pdf_to_images(self.pdf_file)
        print(image_list)

        image_extract_list = []
        for image_path in image_list:
            self.png_processor.load_image(image_path)
            image_extract = self.model_processor.load_image_and_get_predictions(image_path)
            image_extract_list.append(image_extract)
            if self.donuut_validator.validate(image_extract):
                print("Valid")
                flag = 0
            else:
                flag = 1
                break

            try:
                os.remove(image_path)
            except:
                self.png_processor.image_close()
                os.remove(image_path)

        if flag == 0:
            self.pdf_file = os.path.dirname(self.pdf_file)
            self.json_writer.write_to_json(self.pdf_file, self.pdf_file_name, image_extract_list)
        else:
            print("paddleocr")
        print(image_extract_list)

