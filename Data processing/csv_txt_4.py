import pandas as pd
import os

# Đường dẫn input và output
input_csv = 'AI_agents/data/pre-process/diabetes_prediction_dataset.csv'
output_txt = 'AI_agents/data/completed/diabetes_prediction_dataset.txt'
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

# Hàm chuyển đổi giá trị số thành Yes/No
def map_yes_no(value):
    return "Yes" if value == 1 else "No"

# Mở file để ghi
with open(output_txt, 'w', encoding='utf-8') as file:
    # Duyệt qua từng dòng trong DataFrame
    for _, row in df.iterrows():
        # Định dạng thông tin bệnh nhân
        patient_info = f"Patient: {row['gender']}, age {row['age']} | " \
                      f"Hypertension: {map_yes_no(row['hypertension'])} | " \
                      f"Heart disease: {map_yes_no(row['heart_disease'])} | " \
                      f"Smoking history: {row['smoking_history']} | " \
                      f"BMI: {row['bmi']} | " \
                      f"HbA1c level: {row['HbA1c_level']} | " \
                      f"Blood glucose level: {row['blood_glucose_level']} | " \
                      f"Diabetes: {map_yes_no(row['diabetes'])}"
        
        # Ghi thông tin vào file
        file.write(patient_info + '\n')

print("Đã chuyển đổi xong dữ liệu từ CSV sang file text!")