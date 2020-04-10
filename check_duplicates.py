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
                cur_line = cur_line.rstrip('\n')
                line_parts = cur_line.split(" ")
                true_file_name = line_parts[-1]
                cleaned_files_out.add(true_file_name)
                # print(true_file_name)
            fp.close()

    return cleaned_files_out

def get_find_files():
    cleaned_files_out = set()

    find_output_files = get_output_files(find_output_dir)
    for cur_file in find_output_files:
        with open(cur_file) as fp:
            for cur_line in fp:
                cur_line = cur_line.rstrip('\n')
                true_file_name = cur_line
                cleaned_files_out.add(true_file_name)
                print(true_file_name)
            fp.close()

    return cleaned_files_out


def check_grouped_find_files():
    grouped_files = {}
    find_output_files = get_output_files(find_output_dir)

    # First, load everything in...
    for cur_output_file in find_output_files:
        # NOTE: Also strip ".txt"
        dir_basename = os.path.basename(cur_output_file)[:-4]
        true_dir_name = dir_basename.replace("_", "/")
        print("Find Dir: " + true_dir_name)

        grouped_files[true_dir_name] = set()

        with open(cur_output_file) as fp:
            for cur_line in fp:
                cur_line = cur_line.rstrip('\n')
                true_file_name = cur_line
                grouped_files[true_dir_name].add(true_file_name)
                # print(true_file_name)
            fp.close()

    # Then, check for any duplicates.
    for cur_check_dir in grouped_files.keys():
        for cur_dir_member in grouped_files[cur_check_dir]:
            other_dirs = [i for i in grouped_files.keys() if i != cur_check_dir]
            for cur_other_dir in other_dirs:
                if cur_dir_member in grouped_files[cur_other_dir]:
                    print("")
                    print("DUP: ")
                    print(os.path.normpath(os.path.join(cur_check_dir, cur_dir_member)))
                    print(os.path.normpath(os.path.join(cur_other_dir, cur_dir_member)))

              

check_grouped_find_files()
