import fitz
from PIL import Image

class PdfProcessor:
    """
    This class facilitates the processing of PDF documents.
    
    Attributes:
    - pdf_document: The loaded PDF document.
    - images: List to store converted images.
    - num: Number of pages in the PDF document.

    Author: Adarsh Ajay
    Date: 04/03/2024
    """

    @staticmethod
    def pdf_to_images(pdf_path):
        """
        Convert each page of a PDF document to images.

        Parameters:
        - pdf_path (str): Path to the PDF file.
        - file_name (str): Name of the PDF file (without extension).

        Returns:
        - List[str]: List of image paths.
        """
        image_paths = []

        try:
            # Open the PDF file
            with fitz.open(pdf_path) as pdf_document:
                # Iterate through each page and convert it to an image
                for page_number in range(pdf_document.page_count):
                    page = pdf_document[page_number]
                    image = page.get_pixmap()
                    pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)

                    # Save the image as a PNG file
                    image_path = f"{page_number + 1}.png"
                    pil_image.save(image_path)
                    image_paths.append(image_path)

        except Exception as e:
            print(f"Error converting PDF to images: {e}")

        return image_paths