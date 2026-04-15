from store.healthcarestore import HealthcareStore
from view.healthcareview import HealthcareView


def check():
    # create store with fake data
    store = HealthcareStore(num_doctors=5, num_patients=10)

    # display doctors
    HealthcareView.show_doctors(store.get_all_doctors())

    print("\n-----------------------\n")

    # display patients
    HealthcareView.show_patients(store.get_all_patients())

    print("\n-----------------------\n")

    # assign and display doctor for each patient
    for patient in store.get_all_patients():
        doctor = store.assign_doctor(patient)
        HealthcareView.show_assignment(patient, doctor)
if __name__ == "__main__":
    check()