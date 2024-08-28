"""
This script compares two supplied versions and writes the
result to a file.
"""

import semver
from argparse import ArgumentParser

FILE_TO_WRITE_COMPARISON_RESULT_TO = '/usr/src/app/out/comparison_result.txt'

def parse_args():
    """
    This function is used to handle arguments passed into the script
    """
    parser = ArgumentParser()
    parser.add_argument("-vc", "--version_for_comparison", required=True,
                        help="The version which is to be compared against the baseline version stored in the baseline-versions repo.")
    parser.add_argument("-bv", "--baseline_version_in_repo", required=True,
                        help="The baseline version currently stored in the baseline-versions repo.")

    return parser.parse_args()


def execute_script_functions(args):
    """
    This function is used to execute the functions of the script
    """
    version_to_compare = args.version_for_comparison
    baseline_version_in_repo = args.baseline_version_in_repo
    result_of_comparison = compare_versions(version_to_compare, baseline_version_in_repo)
    write_to_artifact_file(result_of_comparison)


def compare_versions(version_to_compare, baseline_version_in_repo):
    """
    This function checks that versions passed are valid semver
    then compares the two versions (returning -1, 1 or 0)
    :param: version_to_compare
    :param: baseline_version_in_repo
    :return: comparison_result
    """
    is_version_to_compare_valid_semver = semver.VersionInfo.is_valid(version_to_compare)
    is_baseline_version_in_repo_valid_semver = semver.VersionInfo.is_valid(baseline_version_in_repo)

    if is_version_to_compare_valid_semver == False:
        raise Exception("Version for comparison is invalid!")
    elif is_baseline_version_in_repo_valid_semver == False:
        raise Exception("Baseline version is invalid!")

    version_to_compare_semver = semver.VersionInfo.parse(version_to_compare)
    baseline_version_in_repo_semver = semver.VersionInfo.parse(baseline_version_in_repo)

    comparison_result = str(semver.VersionInfo.compare(version_to_compare_semver, baseline_version_in_repo_semver))

    return comparison_result


def write_to_artifact_file(comparison_result):
    """
    This function will write the result of comparison to a file
    :param: comparison_result
    :return: None
    """
    try:
        with open(FILE_TO_WRITE_COMPARISON_RESULT_TO, 'w+', encoding="utf-8") as result_file:
            print(result_file.name)
            result_file.write(comparison_result)
    except Exception as exception:
        print('ERROR: Exception occured. Please investigate', exception)
        raise


if __name__ == "__main__":
    execute_script_functions(parse_args())
