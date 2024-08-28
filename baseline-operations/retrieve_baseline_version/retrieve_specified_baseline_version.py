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
                        help="The key in the version file you wish to retrieve the value for. E.g II_BASELINE_INT_CHART_VERSION")

    return parser.parse_args()


def execute_script_functions(args):
    """
    This function is used to execute the functions of the script
    """
    retrieve_version_from_version_file(args.path_to_baseline_version_file, args.key_in_version_file_to_retrieve)


def retrieve_version_from_version_file(path_to_baseline_version_file, key_in_version_file_to_retrieve):
    """
    This function will write the version corresponding the key specified to a file
    :param: path_to_baseline_version_file
    :param: key_in_version_file_to_retrieve
    :return: None
    """
    try:
      with open(path_to_baseline_version_file) as version_file:
          data_from_version_file = version_file.read()
      data_from_version_file_json = json.loads(data_from_version_file)
      with open(FILE_TO_WRITE_VERSION_TO, 'w') as version_file:
          version_file.write(json.dumps(data_from_version_file_json[key_in_version_file_to_retrieve]))
    except Exception as exception:
      print('ERROR: Exception occured. Please investigate', exception)
      raise

if __name__ == "__main__":
    execute_script_functions(parse_args())
