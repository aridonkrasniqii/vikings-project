from api.base.validators import BaseValidator


class NFLPlayerValidator(BaseValidator):
    def __init__(self, name, photo, number, position, age, experience, college):
        super().__init__(name=name, photo=photo)
        self.number = number
        self.position = position
        self.age = age
        self.experience = experience
        self.college = college

    def validate_number(self):
        if not isinstance(self.number, int):
            self.errors.append("Number must be an integer")

    def validate_position(self):
        if not self.position:
            self.errors.append("Position is required")

    def validate_age(self):
        if not isinstance(self.age, int) or self.age < 18:
            self.errors.append("Age must be an integer greater than 18")

    def validate_experience(self):
        if not isinstance(self.experience, int) or self.experience < 0:
            self.errors.append("Experience must be a non-negative integer")

    def validate_college(self):
        if not self.college:
            self.errors.append("College is required")

    def validate(self):
        self.errors = []
        self.validate_name(self.fields['name'])
        self.validate_photo_url(self.fields['photo'])
        self.validate_number()
        self.validate_position()
        self.validate_age()
        self.validate_experience()
        self.validate_college()

        if self.errors:
            return False, self.errors
        return True, None


class NflPlayerStatsValidator():
    def __init__(self, season, team, games_played, receptions, receiving_yards, receiving_touchdowns, longest_reception):
        self.errors = []
        self.season = season
        self.team = team
        self.games_played = games_played
        self.receptions = receptions
        self.receiving_yards = receiving_yards
        self.receiving_touchdowns = receiving_touchdowns
        self.longest_reception = longest_reception

    def validate_season(self):
        if not isinstance(self.season, int) or self.season <= 0:
            self.errors.append("Season must be a positive integer")

    def validate_team(self):
        if not self.team:
            self.errors.append("Team is required")

    def validate_games_played(self):
        if not isinstance(self.games_played, int) or self.games_played < 0:
            self.errors.append("Games played must be a non-negative integer")

    def validate_receptions(self):
        if not isinstance(self.receptions, int) or self.receptions < 0:
            self.errors.append("Receptions must be a non-negative integer")

    def validate_receiving_yards(self):
        if not isinstance(self.receiving_yards, int) or self.receiving_yards < 0:
            self.errors.append("Receiving yards must be a non-negative integer")

    def validate_receiving_touchdowns(self):
        if not isinstance(self.receiving_touchdowns, int) or self.receiving_touchdowns < 0:
            self.errors.append("Receiving touchdowns must be a non-negative integer")

    def validate_longest_reception(self):
        if not isinstance(self.longest_reception, int) or self.longest_reception < 0:
            self.errors.append("Longest reception must be a non-negative integer")

    def validate(self):
        self.errors = []
        self.validate_season()
        self.validate_team()
        self.validate_games_played()
        self.validate_receptions()
        self.validate_receiving_yards()
        self.validate_receiving_touchdowns()
        self.validate_longest_reception()

        if self.errors:
            return False, self.errors
        return True, None
