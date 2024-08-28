"""
Test cases for retrieve_version_from_version_file.py script
"""
import json
import pytest
# pylint: disable=import-error
from cicd_files.external.jenkins.scripts.retrieve_specified_baseline_version \
import retrieve_version_from_version_file

class TestRetrieveSpecifiedBaselineVersion:
    """
    Class to run unit tests for retrieve_specified_baseline_version.py
    """

    @pytest.fixture
    def test_data(self):
        """This fixture returns a sample test data"""
        return json.loads('{"CHART_VESION_1": "1.0.0-test", "CHART_VESION_2": "2.0.0-test" }')


    def test_retrieve_specified_baseline_version_first(self, test_data):
        """Assert for correct version retrieved from test data"""
        assert retrieve_version_from_version_file(test_data, 'CHART_VESION_1') == '"1.0.0-test"'


    def test_retrieve_specified_baseline_version_second(self, test_data):
        """Assert for correct version retrieved from test data"""
        assert retrieve_version_from_version_file(test_data, 'CHART_VESION_2') == '"2.0.0-test"'


    def test_retrieve_specified_baseline_version_third(self, test_data):
        """Assert for exception being thrown if the key does not exist"""
        with pytest.raises(KeyError):
            assert retrieve_version_from_version_file(test_data, 'DOES_NOT_EXIST')
