from tests import sign_up

credentials = {
    'username': "testuser",
    'email': "test@example.com",
    'password': "password123",
    'organization_name': "TestOrg",
    'hq_address': "123 Test St"
}

sign_up.run_signup_test(credentials)
