from test import sign_up

credentials = {
    'username': "testuser",
    'email': "test@example.com",
    'password': "password123",
    'organization_name': "TestOrg",
    'hq_address': "123 Test St"
}


def test_invalid_passwords():
    invalid_passwords = [
        "passwordwith!specialchars",  # Contains special characters but no uppercase or numbers
        "password_with_upper_and_numbers",  # No special characters
        "password with spaces",  # Contains spaces
        "invalid@password",  # Contains special characters but no uppercase or numbers
        "pAssword12345",  # Uppercase not at beginning
        "12345678Aa!",  # Numbers not at end
        "PaSsWoRd!@#",  # All uppercase, lowercase, and special characters but no numbers
        "passw0rd!",  # No uppercase letters
        "PASSWORD!",  # No lowercase letters
        "password12345",  # No special characters
        "password_with_underscores",  # Contains underscores
        "pass!1",  # Too short
        "password_123",  # Contains underscore and numbers but no uppercase
        "PASSWORD_123",  # Contains underscore and numbers but no lowercase
        "P@SSWORD",  # No numbers
        "!@#$%^&*",  # Only special characters
        "password_with_tab	",  # Contains tab character
        "PasswordWithNewline\n",  # Contains newline character
        "PasswordWithCR\r",  # Contains carriage return character
        "  password_with_leading_trailing_spaces  "  # Leading and trailing spaces
    ]

    # Run registration test for each password
    for password in invalid_passwords:
        # Assign password to credentials
        credentials['password'] = password

        # Run signup test with current credentials
        print(f"Testing registration with password: {password}")
        sign_up.run_signup_test(credentials)

# List of invalid passwords to test registration with
