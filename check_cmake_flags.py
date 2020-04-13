import os

import pdb


def get_matching_files(top_dir, wanted_filename):
    out_files = []

    for r, d, f in os.walk(top_dir):
        for file in f:
            if file == wanted_filename:
                final_filename = os.path.join(r, file)
                out_files.append(final_filename)
                #print(final_filename)
    
    return out_files


def read_unique_include_flags(files_in):
    unique_flags = set()

    # First, load everything in...
    for cur_flag_file in files_in:
        with open(cur_flag_file) as fp:
            for cur_line in fp:
                cur_line = cur_line.rstrip('\n')
                if cur_line.startswith("CXX_FLAGS"):
                    if cur_line not in unique_flags:
                        unique_flags.add(cur_line)
                        print("")
                        print(cur_flag_file)
                        print(cur_line)
                    
    


if __name__ == '__main__':
    check_dir = "/home/sniyaz/my-workspace"
    include_out_file = "/home/sniyaz/Desktop/cmake_includes.txt"

    include_flag_files = get_matching_files(check_dir, "flags.make")
    read_unique_include_flags(include_flag_files)
