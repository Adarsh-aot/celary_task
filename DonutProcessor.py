import transformers
from PIL import Image
from transformers import DonutProcessor, VisionEncoderDecoderModel
import torch



# Hide logs
transformers.logging.disable_default_handler()

class ModelProcessor:
    """
    This class facilitates loading a model and making predictions for values like PHN (Personal Health Number).

    Attributes:
    - processor: DonutProcessor instance for preprocessing.
    - model: VisionEncoderDecoderModel instance for prediction.
    - device: The device (GPU or CPU) on which the model is loaded.

    Author: Adarsh Ajay
    Date: 04/03/2024
    """
    def __init__(self):
        """
        Initialize the ModelProcessor by loading the model from Hugging Face and setting up the device.
        """
        model_name = "quipohealth/faxreader" 
        # Load the model from Hugging Face
        self.processor = DonutProcessor.from_pretrained(model_name)
        self.model = VisionEncoderDecoderModel.from_pretrained(model_name)
        # Move model to GPU if available
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def _load_image(self, image_path):
        """
        Load an image, tokenize, and process inputs for the model.

        Parameters:
        - image_path (str): Path to the image file.

        Returns:
        - tuple: Pixel values and decoder input IDs.
        """
        # Load image
        image = Image.open(image_path)

        # Tokenize and process inputs
        inputs = self.processor(images=image, return_tensors="pt")
        pixel_values = inputs.pixel_values.to(self.device)

        task_prompt = "<s>"
        decoder_input_ids = self.processor.tokenizer(task_prompt, add_special_tokens=False, return_tensors="pt").input_ids.to(self.device)

        return pixel_values, decoder_input_ids


    def _run_prediction(self, pixel_values, decoder_input_ids):
        """
        Run inference on the model and process the output.

        Parameters:
        - pixel_values: Pixel values of the image.
        - decoder_input_ids: Decoder input IDs.

        Returns:
        - str: Predicted value.
        """
        # Run inference
        outputs = self.model.generate(
            pixel_values.to(self.device),
            decoder_input_ids=decoder_input_ids.to(self.device),
            max_length=self.model.decoder.config.max_position_embeddings,
            early_stopping=True,
            pad_token_id=self.processor.tokenizer.pad_token_id,
            eos_token_id=self.processor.tokenizer.eos_token_id,
            use_cache=True,
            num_beams=1,
            bad_words_ids=[[self.processor.tokenizer.unk_token_id]],
            return_dict_in_generate=True,
        )

        # Process output
        prediction = self.processor.batch_decode(outputs.sequences)[0]
        prediction = self.processor.token2json(prediction)

        return prediction
    

    def load_image_and_get_predictions(self, image_path):
        pixel_values, decoder_input_ids = self._load_image(image_path)
        prediction = self._run_prediction(pixel_values, decoder_input_ids)
        return prediction