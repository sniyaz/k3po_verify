sudo find /usr/lib/gcc/x86_64-linux-gnu/4.8/include ! -type d > ~/Desktop/find_outputs/A.txt
sudo find /usr/local/include ! -type d > ~/Desktop/find_outputs/B.txt
sudo find /usr/lib/gcc/x86_64-linux-gnu/4.8/include-fixed ! -type d > ~/Desktop/find_outputs/C.txt
sudo find /usr/include/x86_64-linux-gnu ! -type d > ~/Desktop/find_outputs/D.txt
sudo find /usr/include ! -type d > ~/Desktop/find_outputs/E.txt

sudo find /usr/local/lib/x86_64-linux-gnu ! -type d > ~/Desktop/find_outputs/F.txt
sudo find /lib/x86_64-linux-gnu ! -type d > ~/Desktop/find_outputs/G.txt
sudo find /lib64 ! -type d > ~/Desktop/find_outputs/H.txt
sudo find /usr/lib/x86_64-linux-gnu ! -type d > ~/Desktop/find_outputs/I.txt
sudo find /usr/local/lib ! -type d > ~/Desktop/find_outputs/I.txt
sudo find /lib ! -type d > ~/Desktop/find_outputs/I.txt
sudo find /usr/lib ! -type d > ~/Desktop/find_outputs/I.txt