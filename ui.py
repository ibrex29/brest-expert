import tkinter as tk
from tkinter import ttk, messagebox
from diagnosis import rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25

class BreastCancerExpertSystemUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Breast Cancer Expert System")
        
        # Create labels and entry fields for patient information
        ttk.Label(root, text="Gender:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.gender_entry = ttk.Combobox(root, values=["Male", "Female"])
        self.gender_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(root, text="Age:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.age_entry = ttk.Entry(root)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(root, text="Family History:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.family_history_entry = ttk.Combobox(root, values=["Yes", "No"])
        self.family_history_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(root, text="Mammogram Findings:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.mammogram_entry = ttk.Combobox(root, values=["Normal", "Suspicious", "Abnormal"])
        self.mammogram_entry.grid(row=3, column=1, padx=5, pady=5)
        
        ttk.Label(root, text="Biopsy Result:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.biopsy_entry = ttk.Combobox(root, values=["Benign", "Malignant"])
        self.biopsy_entry.grid(row=4, column=1, padx=5, pady=5)
        
        # Button to submit patient information
        ttk.Button(root, text="Submit", command=self.submit_info).grid(row=5, column=0, columnspan=2, pady=10)

    def submit_info(self):
        # Get patient information from entry fields
        patient_info = {
            'gender': self.gender_entry.get(),
            'age': int(self.age_entry.get()),
            'family_history': self.family_history_entry.get(),
            'mammogram_findings': self.mammogram_entry.get(),
            'biopsy_result': self.biopsy_entry.get()
        }
        
        # Perform some validation on patient_info here if needed
        
        # Call a function to handle the patient_info, for example:
        self.handle_patient_info(patient_info)

    def handle_patient_info(self, patient_info):
        # Diagnose the patient
        diagnosis = None
        for rule in [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25]:
            result = rule(patient_info)
            if result is not None:
                diagnosis = result
                break

        # Treat the patient based on the diagnosis
        if diagnosis is not None:
            treatment = f"Treat the patient: {diagnosis}"
        else:
            treatment = "No treatment recommendation found."

        # Display diagnosis and treatment results
        messagebox.showinfo("Diagnosis and Treatment", f"Diagnosis: {diagnosis}\nTreatment: {treatment}")

def main():
    root = tk.Tk()
    app = BreastCancerExpertSystemUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
