from flask import Blueprint, request
from .logging_utils import log_request_to_excel
from .behavior_analytics import analyze_user_activity

login = Blueprint('login', __name__)
access_data = Blueprint('access_data', __name__)
make_transaction = Blueprint('make_transaction', __name__)

@login.route('/login', methods=['POST'])
def login_route():
    # Implementation for user authentication
    # Log relevant information here
    log_entry = log_request_to_excel(request)
    analyze_user_activity(log_entry)
    return "Login successful"

@access_data.route('/data', methods=['GET'])
def access_data_route():
    # Implementation for data access
    # Log relevant information here
    log_entry = log_request_to_excel(request)
    analyze_user_activity(log_entry)
    user_id = request.args.get('user_id')
    # Check if the user is authorized
    if user_id not in ['user1', 'user2', 'user5']:
        return "Unauthorized access", 403
    return "Data accessed"

@make_transaction.route('/transaction', methods=['POST'])
def make_transaction_route():
    # Implementation for transactions
    # Log relevant information here
    log_entry = log_request_to_excel(request)
    analyze_user_activity(log_entry)
    return "Transaction successful"
