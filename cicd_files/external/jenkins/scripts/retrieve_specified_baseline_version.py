"""
The script retreives the version from
a user specified versions file and
write it to an artifact file.
"""
import json
from argparse import ArgumentParser

FILE_TO_WRITE_VERSION_TO = '/usr/src/app/out/retrieved_version.txt'

def parse_args():
    """
    This function is used to handle arguments passed into the script
    """
    parser = ArgumentParser()
    parser.add_argument("-p", "--path_to_baseline_version_file", required=True,
                        help="Path to the baseline version file to retrieve baseline version from")
    parser.add_argument("-k", "--key_in_version_file_to_retrieve", required=True,
                        help="The key in the version file you wish to retrieve the value for.")

    return parser.parse_args()


def execute_script_functions(args):
    """
    This function is used to execute the functions of the script
    """
    data_from_version_file_json = read_from_file(args.path_to_baseline_version_file)
    version_from_json = retrieve_version_from_version_file(data_from_version_file_json,
        args.key_in_version_file_to_retrieve)
    write_to_artifact_file(version_from_json)


def read_from_file(path_to_baseline_version_file):
    """
    This function will read the version file
    :param: path_to_baseline_version_file
    :return: data_from_version_file_json
    """
    try:
        with open(path_to_baseline_version_file, encoding="utf-8") as version_file:
            data_from_version_file = version_file.read()
        data_from_version_file_json = json.loads(data_from_version_file)
    except Exception as exception:
        print('ERROR: Exception occured. Please investigate', exception)
        raise
    return data_from_version_file_json


def retrieve_version_from_version_file(data_from_version_file_json,
key_in_version_file_to_retrieve):
    """
    This function will retrieve the version from the JSON
    :param: data_from_version_file_json
    :param: key_in_version_file_to_retrieve
    :return: version
    """
    try:
        version_from_json = json.dumps(data_from_version_file_json[key_in_version_file_to_retrieve])
    except Exception as exception:
        print('ERROR: Exception occured. Please investigate', exception)
        raise
    return version_from_json

def write_to_artifact_file(version_from_json):
    """
    This function will write the version to a file
    :param: version_from_json
    :return: None
    """
    try:
        with open(FILE_TO_WRITE_VERSION_TO, 'w', encoding="utf-8") as version_file:
            version_file.write(version_from_json)
    except Exception as exception:
        print('ERROR: Exception occured. Please investigate', exception)
        raise


if __name__ == "__main__":
    execute_script_functions(parse_args())
