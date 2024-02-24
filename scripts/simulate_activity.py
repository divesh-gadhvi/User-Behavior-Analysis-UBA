import requests
import time

base_url = "http://127.0.0.1:5000"

def simulate_legitimate_user_activity(user_id):

    login_response = requests.post(f"{base_url}/login", params={'user_id': user_id})
    print(login_response.text)

    data_access_response = requests.get(f"{base_url}/data", params={'user_id': user_id})
    print(data_access_response.text)
    
    for _ in range(0,3):
        transaction_response = requests.post(f"{base_url}/transaction", params={'user_id': user_id})
        print(transaction_response.text)

def simulate_malicious_user_activity(user_id):
    # Simulate unauthorized login attempt
    unauthorized_login_response = requests.post(f"{base_url}/login", params={'user_id': user_id})
    print(unauthorized_login_response.text)
    
    injection_response = requests.get(f"{base_url}/data", params={'user_id': user_id, 'payload': '...'})
    print(injection_response.text)

    #for _ in range(0,4):
    #    # Simulate injection attempt
    #    injection_response = requests.get(f"{base_url}/data", params={'user_id': 'malicious_user', 'payload': '...'})
    #    print(injection_response.text)

    #for _ in range(0,12):
    #    # Simulate abnormal transaction pattern
    #    abnormal_transaction_response = requests.post(f"{base_url}/transaction", params={'user_id': 'malicious_user'})
    #    print(abnormal_transaction_response.text)

if __name__ == "__main__":
    # Simulate legitimate user activities
    #simulate_legitimate_user_activity('user1')

    # Simulate malicious user activities
    simulate_malicious_user_activity('user3')
