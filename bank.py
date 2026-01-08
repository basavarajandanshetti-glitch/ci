def bank_details(account_number, holder_name, account_type):
    result = {
        "Account Number": account_number,
        "Holder Name": holder_name,
        "Account Type": account_type
    }
    return result

if __name__ == "__main__":
    account_number = "123456789"
    holder_name = "John Doe"
    account_type = "Savings"
    print(bank_details(account_number, holder_name, account_type))
