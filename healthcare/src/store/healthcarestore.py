import typing
import faker
from models.doctor import Doctor
from models.patient import Patient


class HealthcareStore:
    def __init__(self, num_doctors: int, num_patients: int):
        self.doctors: typing.List[Doctor] = []
        self.patients: typing.List[Patient] = []
        self.generate_doctors(num_doctors)
        self.generate_patients(num_patients)

    def generate_doctors(self, num_doctors: int):
        fake = faker.Faker()
        specializations = ["cardiology", "neurology", "orthopedic", "dermatology"]

        for i in range(1, num_doctors + 1):
            name = fake.name()
            specialization = fake.random_element(specializations)
            doctor = Doctor(name, specialization, i)
            self.doctors.append(doctor)

    def generate_patients(self, num_patients: int):
        fake = faker.Faker()
        diseases = ["cardiology", "neurology", "orthopedic", "dermatology"]

        for i in range(1, num_patients + 1):
            name = fake.name()
            age = fake.random_int(min=1, max=90)
            disease = fake.random_element(diseases)
            patient = Patient(name, age, i, disease)
            self.patients.append(patient)

    def assign_doctor(self, patient: Patient) -> typing.Optional[Doctor]:
        for doctor in self.doctors:
            if doctor.specialization == patient.disease:
                return doctor
        return None

    def get_all_doctors(self) -> typing.List[Doctor]:
        return self.doctors

    def get_all_patients(self) -> typing.List[Patient]:
        return self.patients
