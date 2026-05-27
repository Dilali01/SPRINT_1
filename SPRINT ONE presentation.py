class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Patient(Person):
    def __init__(self, name, age, patient_id, disease):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.disease = disease

    def display_info(self):
        return (
            f"Patient ID: {self.patient_id}, "
            f"{super().display_info()}, "
            f"Disease: {self.disease}"
        )


class Doctor(Person):
    def __init__(self, name, age, doctor_id, specialization):
        super().__init__(name, age)
        self.doctor_id = doctor_id
        self.specialization = specialization

    def display_info(self):
        return (
            f"Doctor ID: {self.doctor_id}, "
            f"{super().display_info()}, "
            f"Specialization: {self.specialization}"
        )


class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def show_appointment(self):
        return (
            f"Appointment Date: {self.date}\n"
            f"Patient: {self.patient.name}\n"
            f"Doctor: {self.doctor.name}"
        )


class HealthRecord:
    def __init__(self, patient, blood_pressure, sugar_level):
        self.patient = patient
        self.blood_pressure = blood_pressure
        self.sugar_level = sugar_level

    def analyze_health(self):
        if self.sugar_level > 140:
            status = "High Sugar Level"
        else:
            status = "Normal Sugar Level"

        return (
            f"Health Record for {self.patient.name}\n"
            f"Blood Pressure: {self.blood_pressure}\n"
            f"Sugar Level: {self.sugar_level}\n"
            f"Status: {status}"
        )


class HealthAnalyticsSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def show_all_patients(self):
        print("\nAll Patients:")
        for patient in self.patients:
            print(patient.display_info())

    def show_all_doctors(self):
        print("\nAll Doctors:")
        for doctor in self.doctors:
            print(doctor.display_info())


# Main Program
if __name__ == "__main__":

    system = HealthAnalyticsSystem()

    patient1 = Patient("Allan", 22, "P101", "Malaria")
    doctor1 = Doctor("Dr. James", 40, "D201", "General Medicine")

    system.add_patient(patient1)
    system.add_doctor(doctor1)

    appointment1 = Appointment(patient1, doctor1, "25 April 2026")
    record1 = HealthRecord(patient1, "120/80", 150)

    system.show_all_patients()
    system.show_all_doctors()

    print("\nAppointment Details:")
    print(appointment1.show_appointment())

    print("\nHealth Analysis:")
    print(record1.analyze_health())