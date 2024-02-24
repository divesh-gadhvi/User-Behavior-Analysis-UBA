import pandas as pd
from datetime import datetime

import logging

# Configure the logging module
logging.basicConfig(filename='anomaly_log.txt', level=logging.WARNING, format='%(levelname)s: %(message)s')

def analyze_user_activity(log_entry):
    baseline_rules = {
        'login_time_range': (9, 16),  # 9:00 AM to 5:00 PM
        'ip_address_range': ('127.0.0.1', '127.0.0.9'),
        'max_data_accessed_per_day': 3,
        'max_transactions_per_day': 10
    }
 
    # Extract relevant information from the log entry
    log_time = int(log_entry['Timestamp'].split()[1].split(':')[0])
    ip_address = log_entry['IP Address']

    if ip_address < baseline_rules['ip_address_range'][0] or ip_address > baseline_rules['ip_address_range'][1]:
            logging.warning("Anomaly: IP address outside the expected range")

    if 'login' in log_entry['Endpoint']:
        # Check against the baseline rules
        if log_time < baseline_rules['login_time_range'][0] or log_time > baseline_rules['login_time_range'][1]:
            logging.warning("Anomaly: Login time outside the expected range")

    if 'make_transaction' in log_entry['Endpoint']:
        if log_time > baseline_rules['login_time_range'][0] and log_time < baseline_rules['login_time_range'][1]:
            transactions_per_day = get_transactions_per_day(log_entry['User ID'], log_entry['Timestamp']) 
            if transactions_per_day > baseline_rules['max_transactions_per_day']:
                logging.warning("Anomaly: Excessive transactions per day")
        else:
            logging.warning("Anomaly: Transaction performed outside the expected time range")
    
    if 'access_data' in log_entry['Endpoint']:
        if log_entry['User ID'] in ['user1', 'user2', 'user5']:
            if log_time > baseline_rules['login_time_range'][0] and log_time < baseline_rules['login_time_range'][1]:
                data_accessed_per_day = get_data_accessed_per_day(log_entry['User ID'], log_entry['Timestamp']) 
                if data_accessed_per_day > baseline_rules['max_data_accessed_per_day']:
                    logging.warning("Anomaly Detected: Attempted access to data beyond the permissible limit.")
            else:
                logging.warning("Anomaly: Data access performed outside the expected time range")
        else:
            logging.warning(f"Anomaly: Unauthorized access by user {log_entry['User ID']}")
    
def get_data_accessed_per_day(user_id, timestamp):
    # Read historical data from Excel file
    try:
        api_logs = pd.read_excel('../api_logs.xlsx')
    except FileNotFoundError:
        return 0  # Return 0 if the file is not found or empty

    # Convert timestamp to datetime object
    current_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

    # Filter data based on user ID and date
    user_data = api_logs[api_logs['User ID'] == user_id]
    user_data_day = user_data[user_data['Timestamp'].dt.date == current_time.date()]
    user_data_day = user_data_day[user_data_day['Endpoint'].str.contains('login')]
    # Count the number of transactions per day
    data_accessed_per_day = user_data_day.shape[0]

    return data_accessed_per_day

def get_transactions_per_day(user_id, timestamp):
    # Read historical data from Excel file
    try:
        api_logs = pd.read_excel('../api_logs.xlsx')
    except FileNotFoundError:
        return 0  # Return 0 if the file is not found or empty

    # Convert timestamp to datetime object
    current_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

    # Filter data based on user ID and date
    user_data = api_logs[api_logs['User ID'] == user_id]
    user_data_day = user_data[user_data['Timestamp'].dt.date == current_time.date()]
    user_data_day = user_data_day[user_data_day['Endpoint'].str.contains('make_transaction')]
    # Count the number of transactions per day
    transactions_per_day = user_data_day.shape[0]

    return transactions_per_day

# Example usage:
log_entry_example = {'Timestamp': '2023-12-10 18:19:09', 'User ID': 'user1', 'IP Address': '127.0.0.1', 'Endpoint': 'make_transaction.make_transaction_route', 'Method': 'POST'}
analyze_user_activity(log_entry_example)