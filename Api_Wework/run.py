import os
import sys

import pytest


if __name__ == '__main__':
    pytest.main(['./TestCases/test_member.py', '-vs', '--alluredir', './allure-results'])
    os.system('allure serve ./allure-results -o ./report --clean')
