import csv
import os

# Đường dẫn đến file CSV của bạn và file txt đầu ra (sửa để nhất quán)
input_csv_filename = 'AI_agents/data/pre-process/diabetes_prediction_dataset.csv'  # Đảm bảo đường dẫn chính xác
output_txt_filename = 'AI_agents/data/completed/diabetes_prediction_dataset.txt'  # Sửa để khớp với input

# Kiểm tra file input tồn tại
if not os.path.exists(input_csv_filename):
    print(f"Error: Input file '{input_csv_filename}' not found.")
    exit(1)

# Tạo thư mục output nếu chưa có
output_dir = os.path.dirname(output_txt_filename)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

try:
    # Mở file CSV để đọc và file TXT để ghi
    with open(input_csv_filename, mode='r', newline='', encoding='utf-8') as csv_file, \
         open(output_txt_filename, mode='w', encoding='utf-8') as txt_file:

        # Tạo đối tượng reader để đọc CSV
        csv_reader = csv.DictReader(csv_file)
        
        # Duyệt qua từng dòng trong CSV
        for row_num, row in enumerate(csv_reader, start=1):
            
            # Tạo một list để lưu trữ các triệu chứng có giá trị là 1
            symptoms_list = []
            
            # Danh sách các cột triệu chứng (loại bỏ các cột không phải triệu chứng)
            all_keys = list(row.keys())
            symptom_columns = [key for key in all_keys if key not in ['Age', 'Stroke Risk (%)', 'At Risk (Binary)']]
            
            # Kiểm tra từng triệu chứng (chuyển về string để so sánh an toàn)
            for symptom in symptom_columns:
                value = str(row.get(symptom, '')).strip()
                if value == '1':
                    symptoms_list.append(symptom)
            
            # Xử lý trường hợp không có triệu chứng nào
            if not symptoms_list:
                symptoms_text = "No specific symptoms reported"
            else:
                symptoms_text = ", ".join(symptoms_list)
            
            # Lấy các thông tin khác (xử lý nếu thiếu)
            age = row.get('Age', 'Unknown').strip()
            stroke_risk = row.get('Stroke Risk (%)', 'Unknown').strip()
            at_risk_binary = "At Risk" if str(row.get('At Risk (Binary)', '')).strip() == '1' else "Not At Risk"
            
            # Viết dòng mô tả vào file txt
            description_line = f"{row_num}. Patient presents with {symptoms_text}. Age: {age}. Stroke Risk: {stroke_risk}% → {at_risk_binary}.\n"
            txt_file.write(description_line)

    print(f"Conversion completed! Output saved to '{output_txt_filename}'.")

except Exception as e:
    print(f"Error during conversion: {e}")