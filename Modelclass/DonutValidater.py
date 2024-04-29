import re

class DonutValidater:
    def __init__(self):
        self.check = {
            "PHN": {
                "pattern": r'^\d{10}$'  # This pattern matches a 10-digit number
            }
        }

    def validate(self, data: dict):
        """
        Validate the given data against the checks defined in the constructor.

        Parameters:
        - data (dict): The data to be validated.

        Returns:
        - bool: True if validation succeeds, False otherwise.
        """
        for key, value in self.check.items():
            if key not in data:
                return False

            # Use regular expression pattern matching
            if not re.match(value["pattern"], str(data[key])):
                return False

        return True
