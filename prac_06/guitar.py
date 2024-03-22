class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialize Guitar object"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Format of the Guitar object"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age pf the guitar"""
        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        """Check the guitar is vintage or not"""
        return self.get_age() >= 50
