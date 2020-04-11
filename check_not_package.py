import os
import pdb

from check_duplicates import *


def get_dpkg_files():
    cleaned_files_out = set()

    dpkg_output_files = get_output_files(dpkg_output_dir)
    for cur_file in dpkg_output_files:
        with open(cur_file) as fp:
            for cur_line in fp:
                cur_line = cur_line.rstrip('\n')
                line_parts = cur_line.split(" ")
                true_file_name = line_parts[-1]
                cleaned_files_out.add(true_file_name)
                # print(true_file_name)
            fp.close()

    return cleaned_files_out


def get_find_files():
    cleaned_files_out = set()

    # Load everything in...
    find_output_files = get_output_files(find_output_dir)
    for cur_output_file in find_output_files:
        true_dir_name = get_dir_from_find_output_file(cur_output_file)

        with open(cur_output_file) as fp:
            for cur_line in fp:
                cur_line = cur_line.rstrip('\n')
                true_file_name = os.path.normpath(os.path.join(true_dir_name, cur_line))
                cleaned_files_out.add(true_file_name)
                # print(true_file_name)
            fp.close()

    return cleaned_files_out


def find_not_package_files():
    ignore_prefixes = [
        "/usr/local/lib/python3.4/dist-packages/tensorflow/",
        "/usr/lib/node_modules", 
        "/usr/local/lib/node_modules", 
        "/usr/local/lib/python2.7/dist-packages",
        "/usr/lib/python2.7/dist-packages"]

    for cur_find_file in find_file_set:
        if cur_find_file not in dpkg_file_set:

            if check_if_ignored(cur_find_file, ignore_prefixes):
                continue

            print("")
            print("NOT PACK: ")
            print(cur_find_file)


if __name__ == '__main__':
    dpkg_file_set = get_dpkg_files()
    find_file_set = get_find_files()

    find_not_package_files()

    # pdb.set_trace()