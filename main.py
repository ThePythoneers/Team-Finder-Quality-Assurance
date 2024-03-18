from test import sign_up

credentials = {
    'username': "testuser",
    'email': "test@example.com",
    'password': "password123",
    'organization_name': "TestOrg",
    'hq_address': "123 Test St"
}


def test_invalid_emails():
    # List of invalid email addresses to test registration with
    invalid_emails = [
        "invalid!email",
        "email$invalid",
        "invalid?email",
        "invalid_email!",
        "user",
        "invalid email",
        "email123456789012345678901234567890123456789012345678901@example.com"  # Too long
    ]

    # Common credentials for registration
    common_credentials = {
        'username': 'TestUsername',
        'password': 'TestPassword122!',
        'organization_name': 'TestOrg',
        'hq_address': 'TestHQAddress'
    }

    # Run registration test for each invalid email
    for email in invalid_emails:
        # Assign email to credentials
        credentials = common_credentials.copy()
        credentials['email'] = email

        # Run signup test with current credentials
        print(f"Testing registration with invalid email: {email}")
        sign_up.run_signup_test(credentials)


if __name__ == "__main__":
    test_invalid_emails()
