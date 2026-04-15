class Patient:
    def __init__(self, name, age, id, disease):
        self.name = name
        self.age = age
        self.id = id
        self.disease = disease


    def get_info(self):
        return f"Patient Name: {self.name}, Age: {self.age}, ID: {self.id}, Disease: {self.disease}"