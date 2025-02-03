from tv_series.base.validators import BaseValidator


class VikingValidator(BaseValidator):
    def __init__(self, name, description, photo, actor_name):
        super().__init__(name=name, photo=photo)
        self.description = description
        self.actor_name = actor_name

    def validate_description(self):
        if not self.description:
            self.errors.append("Description is required")
        if re.search(r'<script.*?>.*?</script>', self.description, re.IGNORECASE):
            self.errors.append("Description contains dangerous script tags")

    def validate_actor_name(self):
        if not self.actor_name:
            self.errors.append("Actor name is required")
        if re.search(r'[<>/{}[\]$&*^%#@!]', self.actor_name):
            self.errors.append("Actor name contains invalid characters")

    def validate(self):
        self.errors = []
        self.validate_name()
        self.validate_description()
        self.validate_photo_url()
        self.validate_actor_name()

        if self.errors:
            return False, self.errors
        return True, None