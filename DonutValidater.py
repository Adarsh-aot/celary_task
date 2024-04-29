class DonutValidater:
    def __init__(self):
        self.check = {
            "PHN": {
                "length": 10
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

            if len(str(data[key])) != value["length"]:
                return False

        return True

