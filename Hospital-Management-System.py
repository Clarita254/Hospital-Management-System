

#BBIT 2.2C ADMISSION: 167753- Clara Waithaka
# A short description of the Hospital Management system
    #The Hospital Management System manages data related to:Doctors,Patients and data regarding consultation by applying Object-oriented programming concepts:Abstraction,Inheritance,Encapsulation and polymorphism
    #Person Class(Abstract class)It defines common attributes (name,age)and methods(get_details,get_name,get_age)that will be inherited by Patient and Doctor Class
    #Patient class-Manages data regarding patients in  the hospital. Has the attributes(patient_id and medical_history)and the inherited attributesIt also has a get_details method to display patient information
    #Consultation class-Manages relationships between patient and doctor based on consultation.It stores details like date,type and duration of the consultation
    #Doctor class-Manges data for doctors in the hospital with attributes doctor_id and specializatio 
    #System Class(Stored data of the patients,doctors, and consultation).There are also methods to add,view and remove patients, doctors and consultation.It includes exception handling for borrowing medical items from patients's history



#Creating an abstract class person-It defines common attributes of theclass doctor and patient

#Concept of Abstraction
from abc import ABC,abstractmethod

class Person(ABC): #Person class-Base/Parent class
    def __init__(self, name, age):  # Corrected __init__ method and removed space before age
        self.__name = name  # Private attribute
        self.__age = age
    @abstractmethod

    def get_details(self):
      pass
    def get_name(self):
      return self.__name
    def get_age(self):
      return self.__age
    
    def set_name(self,name):
      if name:
         self._name=name
      else:
        print("Name is empty")

    def set_age(self,age):
      self._age=age
      
#Patient class inheriting attributes of the parent class(Person)
class Patient(Person):
       def __init__(self, name, age, patient_id, medical_history=None):  # Static variable and variable name
        super().__init__(name, age)  #  to inheritance from Person class
        self.__patient_id = patient_id  # Private attribute
        self.medical_history = medical_history 


       def get_details(self):
          return f"PatientId:{self.__patient_id},Name:{self.get_name()},medical history:{self.medical_history}"
       
       def get_patient_id(self): #Getters
          return self.__patient_id
       def set_patient_id(self,patient_id):#setter
          self.__patient_id=patient_id #Encapsulation


#Doctor class inheriting attributes of the parent class(Person)
class Doctor(Person):
    def __init__(self, name, age, doctor_id, specialization):
        super().__init__(name, age)  # Inheritance from Person class
        self.__doctor_id = doctor_id  # Private attribute
        self.specialization = specialization

    def get_details(self):  # Overriding the get_details method
        return (f"DoctorId: {self.__doctor_id}, Name: {self.get_name()}, "
                f"Age: {self.get_age()}, Area of Specialization: {self.specialization}")

    def get_doctor_id(self):
        return self.__doctor_id

    def set_doctor_id(self, doctor_id):
        self.__doctor_id = doctor_id

        
#Consultation class-It manages the relationship between the patient and doctor(They are more specific )
class Consultation:
   def __init__(self,patient,doctor,date,type_of_consultation,duration):
      self.patient=patient #Attribute
      self.doctor=doctor  #Attribute
      self.date=date    #Attribute
      self.type_of_consultation=type_of_consultation  #Attribute
      self.duration=duration #Attribute

   def get_consultation_info(self):
      return(f"Consultation Date:{self.date}\n"
             f"Type:{self.type_of_consultation}\n"
             f"Duration:{self.duration}minutes\n"
             f"Patient:{self.patient.get_name()}(ID:{self.patient.get_patient_id()})\n"
             f"Doctor:{self.doctor.get_name()}(ID:{self.doctor.get_doctor_id()})"
            )
             
              
   
 #System usage
 #Creating of instances of patients
patient1=Patient("Mary",65,"P001","Diabetes")
patient2=Patient("Jack",20,"P002","Eczema")

#Creating instances of  doctors
doctor1=Doctor("Dr.Mundia",45,"D001","endocrine System")
doctor2=Doctor("Dr.John",50,"D002","Skin,Hair,Nails")

#Creating consultations
consultation1=Consultation(patient1,doctor1,"17/10/2024","Endocrinology consultation","30")
consultation2=Consultation(patient2,doctor2,"19/10/2024","Dermatology consultation","30")

#Display patient,doctor and consultation details

print(patient1.get_details())
print(doctor1.get_details())
print(consultation1.get_consultation_info())

print("\n")

print(patient2.get_details())
print(doctor2.get_details())
print(consultation2.get_consultation_info())

#...............................................................


class System:#Hospital System class to manage hospital records
   def __init__(self):
      self.patients=[]
      self.doctors= []
      self.consultations=[]

#Adding a new patient
   def add_patient(self,patient):
      self.patients.append(patient)
      print(f"Patient:{patient.get_name()} added successfully")

#Adding a new doctor
   def add_doctor(self,doctor):
      self.doctors.append(doctor)
      print(f"Doctor:{doctor.get_name()} added successfully")


#Schedule consultation

   def add_consultation(self,patient,doctor,date,type_of_consultation,duration):
    if patient not in self.patients or doctor not in self.doctors:
      print("Kindly register in the system")
      return
    consultation= Consultation(patient,doctor,date,type_of_consultation,duration)
    self.consultations.append(consultation)
    print("Consultation Scheduled successfully")


#Viewing all Consultation
   def view_consultations(self):
      for consultation in self.consultations:
       print(consultation.get_consultation_info())

 #Removing a patient
   def remove_patient(self,patient_id):
     self.patients=[p for p in self.patients if p.get_patient_id()!=patient_id] 
     print(f"Patient ID:{patient_id} removed successfully")


  # Removing a doctor
   def remove_doctor(self,doctor_id):
    self.doctors=[d for d in self.doctors if d.get_doctor_id()!=doctor_id] 
    print(f" Doctor ID:{doctor_id} removed successfully")

     #Exception Handling
   def borrow_medical_item(self,patient,item_name):
    try:
      if item_name  not in patient.medical_history:
        raise   ValueError ("Item not available in patient's medical history")
      print(f"Patient{patient.get_name()}borrowed item:{item_name}")
    except ValueError as e:
      print(e)


#Illustration-

#Initialize system
system=System()

#Adding patients and doctors
patient3=Patient("Alice",48,"P003","Heart Failure")
doctor3=Doctor("Dr.Tumutu",39,"D003","Cardiology")

system.add_patient(patient3)
system.add_doctor(doctor3)

#Adding consultation
system.add_consultation(patient3,doctor3,"25/10/2024","Review",20)

#Displaying the consultations
system.view_consultations()

#Borrowing a medical item
system.borrow_medical_item(patient1,"sphygmomanometer")

 #Removing a doctor and a patient
system.remove_patient("P001")
system.remove_doctor("D001")


           


  