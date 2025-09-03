import pandas as pd
import os

# Đường dẫn input và output
input_csv = 'AI_agents/data/pre-process/hypertension_dataset.csv'
output_txt = 'AI_agents/data/pre-process/hypertension_dataset.txt'

# Kiểm tra file input tồn tại
if not os.path.exists(input_csv):
    print(f"Error: Input file '{input_csv}' not found.")
    exit(1)

# Tạo thư mục output nếu chưa có
output_dir = os.path.dirname(output_txt)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Đọc file CSV
df = pd.read_csv(input_csv)

# Tạo file output
with open(output_txt, 'w', encoding='utf-8') as f:
    for _, row in df.iterrows():
        # Tạo chuỗi mô tả cho mỗi bệnh nhân
        patient_data = "Patient data: "
        patient_data += f"Country: {row['Country']} | "
        patient_data += f"Age: {row['Age']} | "
        patient_data += f"BMI: {row['BMI']} | "
        patient_data += f"Cholesterol: {row['Cholesterol']} | "
        patient_data += f"Systolic_BP: {row['Systolic_BP']} | "
        patient_data += f"Diastolic_BP: {row['Diastolic_BP']} | "
        patient_data += f"Smoking_Status: {row['Smoking_Status']} | "
        patient_data += f"Alcohol_Intake: {row['Alcohol_Intake']} | "
        patient_data += f"Physical_Activity_Level: {row['Physical_Activity_Level']} | "
        patient_data += f"Family_History: {row['Family_History']} | "
        patient_data += f"Diabetes: {row['Diabetes']} | "
        patient_data += f"Stress_Level: {row['Stress_Level']} | "
        patient_data += f"Salt_Intake: {row['Salt_Intake']} | "
        patient_data += f"Sleep_Duration: {row['Sleep_Duration']} | "
        patient_data += f"Heart_Rate: {row['Heart_Rate']} | "
        patient_data += f"LDL: {row['LDL']} | "
        patient_data += f"HDL: {row['HDL']} | "
        patient_data += f"Triglycerides: {row['Triglycerides']} | "
        patient_data += f"Glucose: {row['Glucose']} | "
        patient_data += f"Gender: {row['Gender']} | "
        patient_data += f"Education_Level: {row['Education_Level']} | "
        patient_data += f"Employment_Status: {row['Employment_Status']} | "
        patient_data += f"Hypertension: {row['Hypertension']}"
        
        # Ghi vào file
        f.write(patient_data + '\n\n')

print(f"Conversion completed! File saved as '{output_txt}'")