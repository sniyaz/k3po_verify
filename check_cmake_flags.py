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


def check_ignore(filename_in):
    for prefix in ignore_prefixes:
        if filename_in.startswith(prefix):
            return True
    
    return False


def read_unique_include_flags(files_in):
    unique_flags = set()

    # First, load everything in...
    for cur_flag_file in files_in:
        if check_ignore(cur_flag_file):
            continue        

        with open(cur_flag_file) as fp:
            for cur_line in fp:
                cur_line = cur_line.rstrip('\n')
                if cur_line.startswith("CXX_FLAGS"):
                    line_parts = cur_line.split()
                    for cur_part in line_parts:
                        if cur_part not in unique_flags:
                            unique_flags.add(cur_part)
                            print("")
                            
                            part_idx = line_parts.index(cur_part)
                            if part_idx > 0 and line_parts[part_idx - 1] == "-isystem":
                                print("-isystem " + cur_part)
                            else:
                                print(cur_part)
                    
    


if __name__ == '__main__':
    check_dir = "/home/sniyaz/my-workspace"
    include_out_file = "/home/sniyaz/Desktop/cmake_includes.txt"

    ignore_prefixes = [
        "/home/sniyaz/my-workspace/build/dartsim/unittests/",
        "/home/sniyaz/my-workspace/build/dartsim/examples/",
        "/home/sniyaz/my-workspace/build/dartsim/tutorials/",
        "/home/sniyaz/my-workspace/build/aikido/tests/"]

    include_flag_files = get_matching_files(check_dir, "flags.make")
    read_unique_include_flags(include_flag_files)
