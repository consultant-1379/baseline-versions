"""
The script retreives the version from
a user specified versions file, updates it to a new version and
write it to an artifact file.
"""
import json
from argparse import ArgumentParser


def parse_args():
    """
    This function is used to handle arguments passed into the script
    """
    parser = ArgumentParser()
    parser.add_argument("-p", "--path_to_baseline_version_file", required=True,
                        help="Path to the baseline version file to update")
    parser.add_argument("-k", "--key_in_version_file_to_update", required=True,
                        help="The key in the version file you wish to update. \
                            E.g II_BASELINE_INT_CHART_VERSION, eric-oss-5gcnr_LATEST_VERSION")
    parser.add_argument("-v", "--new_baseline_version", required=True,
                        help="The new version of the baseline to update to in the file")

    return parser.parse_args()


def execute_script_functions(args):
    """
    This function is used to execute the functions of the script
    """
    data_from_version_file_json = read_from_file(args.path_to_baseline_version_file)
    updated_data_in_version_file_json = update_version_in_version_file(data_from_version_file_json,
        args.key_in_version_file_to_update, args.new_baseline_version)
    print(f'INFO: Updating key {args.key_in_version_file_to_update} to \
{args.new_baseline_version} in the file {args.path_to_baseline_version_file}')
    write_to_version_file(args.path_to_baseline_version_file, updated_data_in_version_file_json)


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
    except Exception:
        print('ERROR: Unknown exception occured. Please investigate')
        raise
    return data_from_version_file_json


def update_version_in_version_file(data_from_version_file_json,
key_in_version_file_to_update, new_baseline_version):
    """
    This function will modify the version file passed in
    The goal of this function is to update the specified key value pair mentioned in the input file
    :param: data_from_version_file_json
    :param: key_in_version_file_to_update
    :param: new_baseline_version
    :return: None
    """
    # validate_data = json.load(data_from_version_file_json)
    if key_in_version_file_to_update not in data_from_version_file_json:
        raise Exception('ERROR: Exception occured. Please investigate',
        key_in_version_file_to_update)
    data_from_version_file_json[key_in_version_file_to_update] = new_baseline_version
    return data_from_version_file_json


def write_to_version_file(path_to_baseline_version_file, data_from_version_file_json):
    """
    This function will write the version to a file
    :param: path_to_baseline_version_file
    :param: data_from_version_file_json
    :return: None
    """
    try:
        with open(path_to_baseline_version_file, 'w', encoding="utf-8") as version_file:
            version_file.write(json.dumps(data_from_version_file_json))
    except Exception:
        print('ERROR: Unknown exception occured. Please investigate')
        raise


if __name__ == "__main__":
    execute_script_functions(parse_args())
