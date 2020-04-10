import os

import pdb

# NOTE: Keep these updated!
dpkg_output_dir = "data/dpkg_search/"
find_output_dir = "data/find_outputs/"

def get_output_files(cur_dir):
    files_out = []
    for file in os.listdir(cur_dir):
        if file.endswith(".txt"):
           files_out.append(os.path.join(cur_dir, file))

    return(files_out)


def get_dpkg_files():
    cleaned_files_out = set()

    dpkg_output_files = get_output_files(dpkg_output_dir)
    for cur_file in dpkg_output_files:
        with open(cur_file) as fp:
            for cur_line in fp:
                line_parts = cur_line.split(" ")
                true_file_name = line_parts[-1]
                cleaned_files_out.add(true_file_name)
                # print(true_file_name)

    return cleaned_files_out

def get_find_files():
    cleaned_files_out = set()

    find_output_files = get_output_files(find_output_dir)
    for cur_file in find_output_files:
        with open(cur_file) as fp:
            for cur_line in fp:
                true_file_name = cur_line
                cleaned_files_out.add(true_file_name)
                # print(true_file_name)

    return cleaned_files_out
              

get_dpkg_files()
