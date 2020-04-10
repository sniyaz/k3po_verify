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

def check_if_ignored(cur_filename, ignore_prefixes):
    for cur_prefix in ignore_prefixes:
        if cur_filename.startswith(cur_prefix):
            return True
    return False


def check_grouped_find_files():
    ignore_prefixes = [
        "/usr/lib/node_modules", 
        "/usr/local/lib/node_modules", 
        "/usr/local/lib/python2.7/dist-packages",
        "/usr/lib/python2.7/dist-packages"]

    grouped_files = {}
    find_output_files = get_output_files(find_output_dir)

    # First, load everything in...
    for cur_output_file in find_output_files:
        # NOTE: Also strip ".txt"
        dir_basename = os.path.basename(cur_output_file)[:-4]
        true_dir_name = dir_basename.replace("_", "/")
        # Need to fix this too.
        true_dir_name = true_dir_name.replace("x86/64", "x86_64")
        # Let's add that slash in front as well.
        true_dir_name = "/" + true_dir_name
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
                    full_dup_first = os.path.normpath(os.path.join(cur_check_dir, cur_dir_member))
                    full_dup_second = os.path.normpath(os.path.join(cur_other_dir, cur_dir_member))

                    # Check if we're ignorning duplicates from certain dirs.
                    if check_if_ignored(full_dup_first, ignore_prefixes) and check_if_ignored(full_dup_second, ignore_prefixes):
                        continue

                    print("")
                    print("DUP: ")
                    print(full_dup_first)
                    print(full_dup_second)

              

check_grouped_find_files()
