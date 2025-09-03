import csv
import os

def convert_csv_to_txt(csv_file_path, txt_file_path):
    # Kiểm tra file input tồn tại
    if not os.path.exists(csv_file_path):
        print(f"Error: Input file '{csv_file_path}' not found.")
        return
    
    # Tạo thư mục output nếu chưa có
    output_dir = os.path.dirname(txt_file_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                for row in csv_reader:
                    # Chuyển đổi các giá trị
                    hypertension = "Yes" if row['hypertension'] == '1' else "No"
                    heart_disease = "Yes" if row['heart_disease'] == '1' else "No"
                    stroke = "Yes" if row['stroke'] == '1' else "No"
                    
                    # Format dòng dữ liệu
                    formatted_line = (
                        f"Patient: id_{row['id']} | "
                        f"Gender: {row['gender']} | "
                        f"Age: {row['age']} | "
                        f"Hypertension: {hypertension} | "
                        f"Heart Disease: {heart_disease} | "
                        f"Ever Married: {row['ever_married']} | "
                        f"Work Type: {row['work_type']} | "
                        f"Residence Type: {row['Residence_type']} | "
                        f"Avg Glucose Level: {row['avg_glucose_level']} | "
                        f"BMI: {row['bmi']} | "
                        f"Smoking Status: {row['smoking_status']} | "
                        f"Stroke: {stroke}\n"
                    )
                    
                    # Ghi vào file text
                    txt_file.write(formatted_line)
                    
        print(f"Chuyển đổi thành công! File đã được lưu tại: {txt_file_path}")
        
    except Exception as e:
        print(f"Có lỗi xảy ra: {str(e)}")

# Sử dụng hàm
csv_file_path = 'AI_agents/data/pre-process/healthcare-dataset-stroke-data.csv'  # Thay đổi đường dẫn nếu cần
txt_file_path = 'AI_agents/data/completed/healthcare-dataset-stroke-data.txt'

convert_csv_to_txt(csv_file_path, txt_file_path)