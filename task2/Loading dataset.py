# Load the dataset
file_path = r"D:\User\Downloads\Unemployment in India (1).csv"

try:
    # Load CSV file with appropriate encoding to handle BOM
    df = pd.read_csv(file_path, encoding='utf-8-sig')