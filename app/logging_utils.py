import pandas as pd
from datetime import datetime

def log_request_to_excel(request):
    user_id = request.args.get('user_id')
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_address = request.remote_addr
    endpoint = request.endpoint
    method = request.method

    log_entry = {'Timestamp': current_time, 'User ID': user_id, 'IP Address': ip_address, 'Endpoint': endpoint, 'Method': method}
    log_df = pd.DataFrame([log_entry])

    try:
        existing_log_df = pd.read_excel('api_logs.xlsx')
        combined_df = pd.concat([existing_log_df, log_df], ignore_index=True)
    except FileNotFoundError:
        combined_df = log_df

    combined_df.to_excel('api_logs.xlsx', index=False)
    return log_entry
