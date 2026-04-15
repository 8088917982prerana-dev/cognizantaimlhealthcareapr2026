from models.patient import Patient
from models.doctor import Doctor


class HealthcareView:

    @staticmethod
    def show_doctors(doctors):
        print("Doctors List:")
        for doctor in doctors:
            print(doctor.get_info())

    @staticmethod
    def show_patients(patients):
        print("Patients List:")
        for patient in patients:
            print(patient.get_info())

    @staticmethod
    def show_assignment(patient: Patient, doctor: Doctor):
        if doctor:
            print(
                f"Patient {patient.name} (Disease: {patient.disease}) "
                f"is assigned to Dr. {doctor.name} ({doctor.specialization})"
            )
        else:
            print(
                f"Patient {patient.name} (Disease: {patient.disease}) "
                f"has no available doctor"
            )
