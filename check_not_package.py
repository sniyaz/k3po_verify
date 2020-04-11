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


if __name__ == '__main__':
    dpkg_file_set = get_dpkg_files()
    find_file_set = get_find_files()

    pdb.set_trace()