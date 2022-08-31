import shutil

def zip_file(output_filename: str, dir_name: str) -> None:
    shutil.make_archive(output_filename, 'zip', dir_name)


if __name__ == "__main__":
    zip_file('hello', 'plugins/hello')