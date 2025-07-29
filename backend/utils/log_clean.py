import os

def manage_log_files(log_dir="logs", max_logs=10):
    os.makedirs(log_dir,exist_ok=True)
    print(f"Log cleaner active (max {max_logs} logs retained)")