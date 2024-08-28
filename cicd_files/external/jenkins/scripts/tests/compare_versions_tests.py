"""
Test cases for compare_versions.py script
"""
import pytest
# pylint: disable=import-error
from cicd_files.external.jenkins.scripts.compare_versions \
import compare_versions

class TestCompareVersions:
    """
    Class to run unit tests for compare_versions.py
    """

    def test_compare_versions_first(self):
        """Assert for correct result when version for comparison is lower than that stored in repo (Major)"""
        assert compare_versions("1.0.0", "2.0.0") == "-1"

    def test_compare_versions_second(self):
        """Assert for correct result when version for comparison is higher than that stored in repo (Major)"""
        assert compare_versions("2.0.0", "1.0.0") == "1"

    def test_compare_versions_third(self):
        """Assert for correct result when version for comparison equals that stored in repo (Major)"""
        assert compare_versions("2.0.0", "2.0.0") == "0"

    def test_compare_versions_fourth(self):
        """Assert for correct result when version for comparison is lower than that stored in repo (Minor)"""
        assert compare_versions("1.39.0", "2.23.0") == "-1"

    def test_compare_versions_fifth(self):
        """Assert for correct result when version for comparison is higher than that stored in repo (Minor)"""
        assert compare_versions("1.23.0", "1.11.0") == "1"

    def test_compare_versions_sixth(self):
        """Assert for correct result when version for comparison equals that stored in repo (Minor)"""
        assert compare_versions("3.17.0", "3.17.0") == "0"

    def test_compare_versions_seventh(self):
        """Assert for correct result when version for comparison is lower than that stored in repo (Patch)"""
        assert compare_versions("2.23.0-17", "2.23.0-101") == "-1"

    def test_compare_versions_eighth(self):
        """Assert for correct result when version for comparison is higher than that stored in repo (Patch)"""
        assert compare_versions("1.23.11-219", "1.23.11-38") == "1"

    def test_compare_versions_ninth(self):
        """Assert for correct result when version for comparison equals that stored in repo (Patch)"""
        assert compare_versions("3.17.0-84", "3.17.0-84") == "0"

    def test_compare_versions_tenth(self):
        """Assert for correct result when version for comparison is lower than that stored in repo (Pre-release/Build)"""
        assert compare_versions("1.99.4-101", "2.60.4-79") == "-1"

    def test_compare_versions_eleventh(self):
        """Assert for correct result when version for comparison is higher than that stored in repo (Pre-release/Build)"""
        assert compare_versions("2.60.4-101", "2.60.4-79") == "1"

    def test_compare_versions_twelfth(self):
        """Assert for correct result when version for comparison equals that stored in repo (Pre-release/Build)"""
        assert compare_versions("4.11.16-97", "4.11.16-97") == "0"

    def test_compare_versions_thirteenth(self):
        """Assert for exception being thrown if version for comparison is not valid semver"""
        with pytest.raises(Exception):
            assert compare_versions("1.ab.x7", "2.0.0")

    def test_compare_versions_fourteenth(self):
        """Assert for exception being thrown if baseline version is not valid semver"""
        with pytest.raises(Exception):
            assert compare_versions("1.0.0", "2.ab.x7")
