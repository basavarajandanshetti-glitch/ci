from bank import bank_details
def test_bank_details():
    account_number = "987654321"
    holder_name = "Jane Smith"
    account_type = "Checking"
    expected_result = {
        "account_number": "987654321",
        "holder_name": "Jane Smith",
        "account_type": "savings"
    }
    assert bank_details(account_number, holder_name, account_type) == expected_result
