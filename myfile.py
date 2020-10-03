import myjson
import os


def to_file(file_name, text):
    try:
        os.remove(file_name)
    except FileNotFoundError as e:
        pass

    if isinstance(text, str):
        mode = 'wt'
    else:
        mode = 'wb'
    with open(file_name, mode) as f:
        try:
            f.write(text)
        finally:
            f.close()


def from_file(file_name):
    with open(file_name, 'rb') as f:
        return f.read()


def txt_from_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def json_from_file(file_name, err_msg=None):
    data = None
    with open(file_name, 'rb') as f:
        data = myjson.json.load(f)
    if not data:
        raise Exception(err_msg if err_msg else "No data loaded.")
    return data


def json_to_file(file_name, data):
    to_file(file_name, myjson.json.dumps(data, ensure_ascii=False, indent=2, cls=myjson.MYJSONEncoder))