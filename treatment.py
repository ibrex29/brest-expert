def treat1(patient_info):
    if patient_info['gender'] == 'Female' and patient_info['age'] >= 40 and patient_info['family_history'] == 'Yes':
        return "Consider scheduling a mammogram."
    return None

def treat2(patient_info):
    if patient_info['mammogram_findings'] == 'Suspicious':
        return "Recommend further diagnostic tests such as a biopsy."
    return None

def treat3(patient_info):
    if patient_info['biopsy_result'] == 'Malignant':
        return "Diagnose the patient with breast cancer."
    return None

def treat4(patient_info):
    if patient_info['tumor_size'] < 2 and patient_info['lymph_node_status'] == 'Negative':
        return "Classify the cancer as stage I."
    return None

def treat5(patient_info):
    if 2 <= patient_info['tumor_size'] <= 5 and patient_info['lymph_node_status'] == 'Negative':
        return "Classify the cancer as stage II."
    return None

def treat6(patient_info):
    if patient_info['tumor_size'] > 5 or patient_info['lymph_node_status'] == 'Positive':
        return "Classify the cancer as stage III."
    return None

def treat7(patient_info):
    if 'Metastatic' in patient_info['stage']:
        return "Classify the cancer as stage IV."
    return None

def treat8(patient_info):
    if 'ER-positive' in patient_info['cancer_subtype']:
        return "Consider hormone therapy as part of the treatment plan."
    return None

def treat9(patient_info):
    if 'HER2-positive' in patient_info['cancer_subtype']:
        return "Consider targeted therapy with drugs such as trastuzumab."
    return None

def treat10(patient_info):
    if 'Triple-negative' in patient_info['cancer_subtype']:
        return "Consider chemotherapy as the primary treatment option."
    return None

def treat11(patient_info):
    if 'BRCA1' in patient_info['genetic_mutations'] or 'BRCA2' in patient_info['genetic_mutations']:
        return "Discuss the option of prophylactic mastectomy."
    return None

def treat12(patient_info):
    if 'DCIS' in patient_info['cancer_subtype']:
        return "Discuss the option of lumpectomy with radiation therapy."
    return None

def treat13(patient_info):
    if 'ILC' in patient_info['cancer_subtype']:
        return "Consider additional imaging studies to evaluate the extent of the tumor."
    return None

def treat14(patient_info):
    if 'IBC' in patient_info['cancer_subtype']:
        return "Initiate chemotherapy prior to surgery to shrink the tumor."
    return None

def treat15(patient_info):
    if 'Metastatic' in patient_info['stage']:
        return "Focus on palliative care and symptom management."
    return None

def treat16(patient_info):
    if 'pregnant' in patient_info['patient_status'] and 'Breast cancer' in patient_info['diagnosis']:
        return "Consult with a multidisciplinary team to develop a treatment plan that minimizes risks to the fetus."
    return None

def treat17(patient_info):
    if 'completed primary treatment' in patient_info['patient_status'] and 'Breast cancer' in patient_info['diagnosis']:
        return "Schedule regular follow-up appointments for surveillance."
    return None

def treat18(patient_info):
    if 'persistent pain or swelling in the breast' in patient_info['symptoms']:
        return "Consider further evaluation for recurrence."
    return None

def treat19(patient_info):
    if 'lymphedema' in patient_info['complications']:
        return "Refer to a physical therapist for lymphatic drainage massage."
    return None

def treat20(patient_info):
    if 'menopausal symptoms' in patient_info['side_effects']:
        return "Discuss strategies for symptom management."
    return None

def treat21(patient_info):
    if 'overweight or obese' in patient_info['patient_status']:
        return "Encourage lifestyle modifications such as diet and exercise to reduce the risk of recurrence."
    return None

def treat22(patient_info):
    if 'smoking' in patient_info['patient_status']:
        return "Provide resources for smoking cessation to improve overall health outcomes."
    return None

def treat23(patient_info):
    if 'depression or anxiety' in patient_info['side_effects']:
        return "Refer to a mental health professional for support."
    return None

def treat24(patient_info):
    if 'fertility preservation' in patient_info['concerns']:
        return "Discuss options such as egg or embryo freezing."
    return None

def treat25(patient_info):
    if 'completed chemotherapy' in patient_info['patient_status']:
        return "Consider referral to a fertility specialist for assessment of ovarian function."
    return None
