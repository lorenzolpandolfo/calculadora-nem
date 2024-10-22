from datetime import datetime

def create_log_record(log_data: dict):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("log.txt", "a", encoding="utf8") as file:
        log_entry = f"{timestamp} - {log_data}\n"
        file.write(log_entry)
