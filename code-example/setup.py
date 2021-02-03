# coding: utf-8

"""
    Vipps signup API

    Vipps Signup API enables a partner to initiate Vipps onboarding process on behalf of a merchant. The merchant needs to complete Vipps signup form to sign the merchant agreement with Vipps. After the signup form has been processed, Vipps will send the API keys to the defined callback endpoint. In order to complete the integration there is a need to: 1. Initiate the Signup to the Initiate endpoint 2. Accept the callback sent to the callback endpoint 3. Return a 202 response to acknowledge that the callback has been accepted.    # noqa: E501

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Vipps signup API",
    author_email="",
    url="",
    keywords=["Swagger", "Vipps signup API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Vipps Signup API enables a partner to initiate Vipps onboarding process on behalf of a merchant. The merchant needs to complete Vipps signup form to sign the merchant agreement with Vipps. After the signup form has been processed, Vipps will send the API keys to the defined callback endpoint. In order to complete the integration there is a need to: 1. Initiate the Signup to the Initiate endpoint 2. Accept the callback sent to the callback endpoint 3. Return a 202 response to acknowledge that the callback has been accepted.    # noqa: E501
    """
)
