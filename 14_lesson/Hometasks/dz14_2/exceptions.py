class MaxStudentsExceeded(Exception):
    """Exception raised when adding more than the allowed number of students in a group."""
    def __init__(self, message="Cannot add more than 10 students to the group"):
        self.message = message
        super().__init__(self.message)
