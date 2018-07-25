import os


def get_image_path(path):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "../images/" + path
    abs_file_path = os.path.join(script_dir, rel_path)
    return abs_file_path
