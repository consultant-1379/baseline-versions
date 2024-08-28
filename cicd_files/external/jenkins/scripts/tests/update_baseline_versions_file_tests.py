"""
Test cases for update_baseline_versions_file.py script
"""
import json
import pytest
# pylint: disable=import-error
from cicd_files.external.jenkins.scripts.update_baseline_versions_file \
import update_version_in_version_file

class TestUpdateBaselineVersionsFile:
    """
    Class to run unit tests for update_baseline_versions_file.py
    """

    @pytest.fixture
    def test_data(self):
        """This fixture returns a sample test data"""
        return json.loads('{"CHART_VESION_1": "1.0.0-test", "CHART_VESION_2": "2.0.0-test" }')


    def test_update_baseline_versions_file_first(self, test_data):
        """Assert for correct version retrieved from test data"""
        assert update_version_in_version_file(test_data, 'CHART_VESION_1', '1.1.1-test') == \
            json.loads('{"CHART_VESION_1": "1.1.1-test", "CHART_VESION_2": "2.0.0-test"}')


    def test_update_baseline_versions_file_second(self, test_data):
        """Assert for correct version retrieved from test data"""
        assert update_version_in_version_file(test_data, 'CHART_VESION_2', '2.2.2-test') == \
            json.loads('{"CHART_VESION_1": "1.0.0-test", "CHART_VESION_2": "2.2.2-test"}')


    def test_update_baseline_versions_file_third(self, test_data):
        """Assert for exception being thrown if the key does not exist"""
        with pytest.raises(Exception):
            assert update_version_in_version_file(test_data, 'DOES_NOT_EXIST', 'FAKE')
