# Includes.
cd /usr/lib/gcc/x86_64-linux-gnu/4.8/include
sudo find . ! -type d > ~/Desktop/find_outputs/usr_lib_gcc_x86_64-linux-gnu_4.8_include.txt

cd /usr/local/include
sudo find . ! -type d > ~/Desktop/find_outputs/usr_local_include.txt

cd /usr/lib/gcc/x86_64-linux-gnu/4.8/include-fixed
sudo find . ! -type d > ~/Desktop/find_outputs/usr_lib_gcc_x86_64-linux-gnu_4.8_include-fixed.txt

cd /usr/include/x86_64-linux-gnu
sudo find . ! -type d > ~/Desktop/find_outputs/usr_include_x86_64-linux-gnu.txt

cd /usr/include
sudo find . ! -type d > ~/Desktop/find_outputs/usr_include.txt

cd /opt/ros/indigo/include
sudo find . ! -type d > ~/Desktop/find_outputs/opt_ros_indigo_include.txt

# Libs.
cd /usr/local/lib/x86_64-linux-gnu
sudo find . ! -type d > ~/Desktop/find_outputs/usr_local_lib_x86_64-linux-gnu.txt

cd /lib/x86_64-linux-gnu
sudo find . ! -type d > ~/Desktop/find_outputs/lib_x86_64-linux-gnu.txt

cd /lib64
sudo find . ! -type d > ~/Desktop/find_outputs/lib64.txt

cd /usr/lib/x86_64-linux-gnu
sudo find . ! -type d > ~/Desktop/find_outputs/usr_lib_x86_64-linux-gnu.txt

cd /usr/local/lib
sudo find . ! -type d > ~/Desktop/find_outputs/usr_local_lib.txt

cd /lib 
sudo find . ! -type d > ~/Desktop/find_outputs/lib.txt

cd /usr/lib
sudo find . ! -type d > ~/Desktop/find_outputs/usr_lib.txt

cd /opt/ros/indigo/lib
sudo find . ! -type d > ~/Desktop/find_outputs/opt_ros_indigo_lib.txt

# And something extra.
cd /usr/share
sudo find . ! -type d > ~/Desktop/find_outputs/usr_share.txt
