import pandas as pd
import numpy as np
import os

# Đường dẫn input và output
input_excel = 'AI_agents/data/pre-process/Patients Data Classified.xlsx'
output_txt = 'AI_agents/data/completed/Patients Data Classified.txt'

# Kiểm tra file input tồn tại
if not os.path.exists(input_excel):
    print(f"Error: Input file '{input_excel}' not found.")
    exit(1)

# Tạo thư mục output nếu chưa có
output_dir = os.path.dirname(output_txt)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Đọc file Excel
df = pd.read_excel(input_excel, sheet_name='Sheet1')

# Debug: Print column names to check
print("Column names in the Excel file:")
print(df.columns.tolist())

# Danh sách các cột triệu chứng
symptom_columns = [
    "Left sided paralysis", "Right sided paralysis", "Unable to speak", "Unconsciousness",
    "Deviation of Mouth", "Slurring of Speech", "Increased Number of Urination",
    "Increased Thirst and Dry Mouth", "Increased Hunger", "Weight Loss", "Mood Change",
    "Apathy", "Irritability", "Lethargy", "Fatigue", "Weakness", "Blurring of Vision",
    "Delay in Wound Healing", "Nausea", "Predilection to sweet food", "Headache",
    "Nosebleed", "Pounding in Neck/ Chest", "Difficulty in Breathing", "Palpitation/ Fatigue",
    "Family History of HTN", "Generalized Body Ache", "Generalized Weakness", "Severe Headache",
    "Swelling Over Multiple Body Parts", "Vertigo", "Fever", "Cough", "Gum Bleeding", "Abdominal Pain"
]

# Mở file để ghi kết quả
with open(output_txt, 'w', encoding='utf-8') as f:
    for index, row in df.iterrows():
        # Lấy thông tin cơ bản
        patient_id = row["Patient's Number"]
        gender = row["Gender"]
        age = row["Age"]
        
        # Lấy các triệu chứng có giá trị 1
        symptoms = []
        for symptom in symptom_columns:
            try:
                if row[symptom] == 1:
                    symptoms.append(symptom)
            except KeyError:
                print(f"Warning: Column '{symptom}' not found in the file.")
        
        # Lấy thông tin đường huyết nếu có
        blood_sugar = row["Blood Sugar Level"]
        blood_sugar_text = f" | Blood Sugar: {blood_sugar}" if blood_sugar != 0 else ""
        
        # Lấy thông tin BMI nếu có
        bmi = row["BMI"]
        bmi_text = f" | BMI: {bmi}" if bmi != 0 else ""
        
        # Lấy thông tin chẩn đoán và bác sĩ đề xuất
        diagnosis = row["Output"]
        doctor = row["Suggested Doctor"]
        
        # Tạo chuỗi kết quả
        result = f"Patient {patient_id} | Gender: {gender} | Age: {age}"
        
        if symptoms:
            result += f" | Symptoms: {', '.join(symptoms)}"
            
        result += blood_sugar_text + bmi_text
        result += f" | Diagnosis: {diagnosis} | Suggested Doctor: {doctor}"
        
        # Ghi vào file
        f.write(result + '\n')

print("Đã chuyển đổi xong dữ liệu sang file patients_data.txt")