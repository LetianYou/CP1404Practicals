class ProgrammingLanguage:
    """Represent the ProgrammingLanguage object."""
    def __init__(self, name, typing, reflection, year):
        """Initialise the ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the ProgrammingLanguage is dynamically typed."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Returns the string representation of the ProgrammingLanguage object."""
        reflection_str = "Reflection=True" if self.reflection else "Reflection=False"
        return f"{self.name}, {self.typing} Typing, {reflection_str}, First appeared in {self.year}"
