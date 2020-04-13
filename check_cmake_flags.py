import os

import pdb


def get_matching_files(top_dir, wanted_filename):
	out_files = []

	for r, d, f in os.walk(top_dir):
    for file in f:
        if file = wanted_filename:
            out_files.append(os.path.join(r, file))

    return out_files





if __name__ == '__main__':
    check_dir = "/home/sniyaz/my-workspace"
    include_out_file = "/home/sniyaz/Desktop/cmake_includes.txt"