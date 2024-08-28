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
                        help="The key in the version file you wish to update. E.g II_BASELINE_INT_CHART_VERSION")
    parser.add_argument("-v", "--new_baseline_version", required=True,
                        help="The new version of the baseline to update to in the file")

    return parser.parse_args()


def execute_script_functions(args):
    """
    This function is used to execute the functions of the script
    """
    update_version_file(args.path_to_baseline_version_file, args.key_in_version_file_to_update, args.new_baseline_version)


def update_version_file(path_to_baseline_version_file, key_in_version_file_to_update, new_baseline_version):
    """
    This function will modify the version file passed in
    The goal of this function is to update the specified key value pair mentioned in the input file
    :param: path_to_baseline_version_file
    :param: key_in_version_file_to_update
    :param: new_baseline_version
    :return: None
    """
    print(f'INFO: Updating key {key_in_version_file_to_update} to {new_baseline_version} in the file {path_to_baseline_version_file}')
    try:
      with open(path_to_baseline_version_file) as version_file:
          data_from_version_file = version_file.read()
      data_from_version_file_json = json.loads(data_from_version_file)
      data_from_version_file_json[key_in_version_file_to_update] = new_baseline_version
      with open(path_to_baseline_version_file, 'w') as version_file:
          version_file.write(json.dumps(data_from_version_file_json))
    except Exception:
      print('ERROR: Unknown exception occured. Please investigate')
      raise

if __name__ == "__main__":
    execute_script_functions(parse_args())
