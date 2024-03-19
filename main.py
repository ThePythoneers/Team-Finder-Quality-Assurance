from testcases import invalid_passwords


def test_invalid_passwords():
    # List of invalid passwords to test sign-in with
    invalid_passwords = [
        "short",
        "no_uppercase",
        "no_number",
        "no_specialchar",
        "onlylowercase123",
        "ONLYUPPERCASE123",
        "123456789012345678901234567890123456789012345678901"  # Too long
    ]

    # Common credentials for sign-in
    common_credentials = {
        'email': 'miclaush@gmail.com'  # Email address to test
    }

    # Run sign-in test for each invalid password
    for password in invalid_passwords:
        # Assign password to credentials
        credentials = common_credentials.copy()
        credentials['password'] = password

        # Run sign-in test with current credentials
        print(f"Testing sign-in with invalid password: {password}")
        sign_in.run_signin_test(credentials)


def test_invalid_emails():
    # List of invalid emails to test sign-in with
    invalid_emails = [
        "invalid!email",
        "email$invalid",
        "invalid?email",
        "invalid_email!",
        "user",
        "invalid email",
        "email123456789012345678901234567890123456789012345678901@example.com"  # Too long
    ]

    # Common password for sign-in
    common_password = "Miclaush1@"
    credentials = { "password": "Miclaush1@"}
    # Run sign-in test for each invalid email
    for email in invalid_emails:
        # Run sign-in test with current email and common password
        credentials["email"] = email
        print(f"Testing sign-in with invalid email: {email}")
        sign_in.run_signin_test(credentials)


if __name__ == "__main__":
    #test_invalid_emails()
    #test_invalid_passwords()
    invalid_passwords.test_invalid_passwords()
