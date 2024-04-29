from PIL import Image
import os

class ImageProcessor:
    """
    This class helps to load image, convert image to RGB mode, and delete PNG files.

    Author: Adarsh Ajay
    Date: 04/03/2024
    """
    def __init__(self):
        self.image = None

    def load_image(self, image_path):
        """
        Load an image from the given file path.

        Parameters:
        - image_path (str): Path to the image file.
        """
        try:
            self.image = Image.open(image_path)
            # print(f"Image '{image_path}' loaded successfully.")
            return self.image
        except Exception as e:
            print(f"Error loading image: {e}")
            return None

    def convert_to_rgb(self):
        """
        Convert the loaded image to the RGB mode.

        Returns:
        - Image: The image in RGB mode.
        """
        if not self.image:
            print("No image loaded. Use 'load_image' method first.")
            return

        rgb_image = self.image.convert("RGB")
        # print("Image converted to RGB mode.")
        return rgb_image
    
    def image_close(self):
        """
        Close the loaded image.
        """
        if self.image:
            self.image.close()
            print("Image closed successfully.")
        else:
            print("No image loaded. Use 'load_image' method first.")