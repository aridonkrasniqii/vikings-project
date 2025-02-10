import re
from urllib.parse import urlparse


class BaseValidator:
    def __init__(self, **kwargs):
        self.fields = kwargs
        self.errors = []

    @staticmethod
    def validate_id(model_id):
        if not str(model_id).isdigit():
            return False, "ID is not valid, it should be a number"
        return True, None

    def validate(self):
        self.errors = []
        for field, value in self.fields.items():
            validate_method = getattr(self, f"validate_{field}", None)
            if validate_method:
                validate_method(value)
        if self.errors:
            return False, self.errors
        return True, None

    def validate_name(self, value):
        if not value:
            self.errors.append("Name is required")
        if re.search(r'[<>/{}[\]$&*^%#@!]', value):
            self.errors.append("Name contains invalid characters")

    def validate_photo_url(self, value):
        # Allow 'N/A' as a valid value
        if value in [None, 'N/A']:
            return  # No error if value is 'N/A' or None

        if not value:
            self.errors.append("Photo URL is required")
            return

        try:
            result = urlparse(value)
            if not all([result.scheme, result.netloc]):
                self.errors.append("Invalid URL for photo")
        except ValueError:
            self.errors.append("Invalid URL format for photo")

