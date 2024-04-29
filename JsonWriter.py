import os
import json
import shutil





class JsonWriter:
    """
    A class to create a JSON file.
    """

    @staticmethod
    def write_to_json(  output_file, output_file_name, data_dict):
        """
        Write a dictionary to a JSON file.

        Parameters:
        - output_file (str): Path to the output JSON file.
        - data_dict (dict): Dictionary to be written to the JSON file.
        """
        try:
            output_file_name = JsonWriter.get_file_name_without_extension(output_file_name) + '.json'
            with open(output_file_name, 'w') as json_file:
                json.dump(data_dict, json_file, indent=4)
            
            shutil.move(output_file_name , os.path.join(output_file , output_file_name))

            print(f"JSON file '{output_file_name}' created successfully.")
        except Exception as e:
            print(f"Error creating JSON file: {e}")

    
    @staticmethod
    def get_file_name_without_extension(file_name):
        """
        Get the file name without the extension.

        Parameters:
        - file_name (str): The name of the file.

        Returns:
        - str: The file name without the extension.
        """
        last_period_index = file_name.rfind('.')
    
        if last_period_index != -1:  # Check if a period was found in the filename
            return file_name[:last_period_index]  # Return the substring before the last period
        else:
            return file_name

