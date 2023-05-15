import os.path
from zipfile import ZipFile
from conftest import zip_archive_file, RESOURCE_PATH

def test_add_to_zip():
    with ZipFile(zip_archive_file, "w") as zip_file:
        for file_name in os.listdir(RESOURCE_PATH):
            zip_file.write(zip_archive_file, file_name)

    with ZipFile(zip_archive_file) as zip_file:
        for file_name in os.listdir(RESOURCE_PATH):
            assert file_name in zip_file.namelist()
