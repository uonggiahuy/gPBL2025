import pandas as pd
import os

# Đường dẫn input và output
input_csv = 'AI_agents/data/pre-process/brain_stroke.csv'
output_txt = 'AI_agents/data/completed/brain_stroke.txt'

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

# Hàm chuyển đổi giá trị nhị phân thành mô tả
def convert_binary_value(value, condition_name):
    return f"with {condition_name}" if value == 1 else f"without {condition_name}"

# Hàm tạo mô tả cho mỗi bệnh nhân
def generate_patient_description(row):
    description = f"Patient: {row['gender']}, {int(row['age'])} years old, "
    description += f"{convert_binary_value(row['hypertension'], 'hypertension')}, "
    description += f"{convert_binary_value(row['heart_disease'], 'heart disease')}, "
    description += f"{'ever married' if row['ever_married'] == 'Yes' else 'not married'}, "
    description += f"working in {row['work_type']}, "
    description += f"{row['Residence_type']} residence, "
    description += f"average glucose level {row['avg_glucose_level']}, "
    description += f"BMI {row['bmi']}, "
    description += f"{row['smoking_status'].lower()}, "
    description += f"{'had a stroke' if row['stroke'] == 1 else 'did not have a stroke'}."
    
    return description

# Tạo mô tả cho tất cả bệnh nhân
descriptions = []
for index, row in df.iterrows():
    descriptions.append(generate_patient_description(row))

# Ghi vào file txt
with open(output_txt, 'w', encoding='utf-8') as f:
    for i, desc in enumerate(descriptions, 1):
        f.write(f"{i}. {desc}\n")

print(f"Đã chuyển đổi thành công! File '{output_txt}' đã được tạo.")