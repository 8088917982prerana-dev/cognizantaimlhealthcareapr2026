class Doctor:
    def __init__(self, name, specialization, id):
        self.name = name
        self.specialization = specialization
        self.id = id

    def get_info(self):
        return f"Dr. {self.name}, Specialization: {self.specialization}, ID: {self.id}"