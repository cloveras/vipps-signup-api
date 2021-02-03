# coding: utf-8

"""
    Vipps signup API

    Vipps Signup API enables a partner to initiate Vipps onboarding process on behalf of a merchant. The merchant needs to complete Vipps signup form to sign the merchant agreement with Vipps. After the signup form has been processed, Vipps will send the API keys to the defined callback endpoint. In order to complete the integration there is a need to: 1. Initiate the Signup to the Initiate endpoint 2. Accept the callback sent to the callback endpoint 3. Return a 202 response to acknowledge that the callback has been accepted.    # noqa: E501

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.signup_api import SignupApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSignupApi(unittest.TestCase):
    """SignupApi unit test stubs"""

    def setUp(self):
        self.api = api.signup_api.SignupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_partial_signup(self):
        """Test case for partial_signup

        Create a signup  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
