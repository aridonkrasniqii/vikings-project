from tv_series.base.validators import BaseValidator


class NorsemanValidator(BaseValidator):
    def __init__(self, name, photo, actor_name):
        super().__init__(name=name, photo=photo)
        self.actor_name = actor_name

    def validate_actor_name(self):
        if not self.actor_name:
            self.errors.append("Actor name is required")
        if re.search(r'[<>/{}[\]$&*^%#@!]', self.actor_name):
            self.errors.append("Actor name contains invalid characters")

    def validate(self):
        self.errors = []
        self.validate_name()
        self.validate_photo_url()
        self.validate_actor_name()

        if self.errors:
            return False, self.errors
        return True, None