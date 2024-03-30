**Level 0**:
The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0.

> ssh -p 2220 bandit0@bandit.labs.overthewire.org

**Level 0-> Level 1**: The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

> ls

> cat readme

_password obtained: NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL_

**Level 1-> Level 2**: The password for the next level is stored in a file called - located in the home directory

> ssh -p 2220 bandit1@bandit.labs.overthewire.org

password: NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL

> cat ./-

password obtained: rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

_In scripting, the cat command is typically used to concatenate and display the content of files. When used with "-" as an argument, cat reads from standard input (stdin). On the other hand, when used with "./-" as an argument, cat interprets it as a filename in the current directory._

Ref: https://tldp.org/LDP/abs/html/special-chars.html

**Level 2-> Level 3**: The password for the next level is stored in a file called spaces in this filename located in the home directory

> ssh -p 2220 bandit2@bandit.labs.overthewire.org

password: rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

> cat spaces\ in\ this\ filename

password obtained: aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG

**Level 3-> Level 4**: The password for the next level is stored in a hidden file in the inhere directory.

> ssh -p 2220 bandit3@bandit.labs.overthewire.org

password: aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG

> ls

> cd inhere/

> ls -al

> cat .hidden

password obtained: 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

**Level 4-> Level 5**: The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

> ssh -p 2220 bandit4@bandit.labs.overthewire.org

password: 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

> cd inhere/

> ls -al

output: 

```
total 48
drwxr-xr-x 2 root    root    4096 Oct  5 06:19 .
drwxr-xr-x 3 root    root    4096 Oct  5 06:19 ..
-rw-r----- 1 bandit5 bandit4   33 Oct  5 06:19 -file00
-rw-r----- 1 bandit5 bandit4   33 Oct  5 06:19 -file01
-rw-r----- 1 bandit5 bandit4   33 Oct  5 06:19 -file02
-rw-r----- 1 bandit5 bandit4   33 Oct  5 06:19 -file03
-rw-r----- 1 bandit5 bandit4   33 Oct  5 06:19 -file04
-rw-r----- 1 bandit5 bandit4   33 Oct  5 06:19 -file05
-rw-r----- 1 bandit5 bandit4   33 Oct  5 06:19 -file06
-rw-r----- 1 bandit5 bandit4   33 Oct  5 06:19 -file07
-rw-r----- 1 bandit5 bandit4   33 Oct  5 06:19 -file08
-rw-r----- 1 bandit5 bandit4   33 Oct  5 06:19 -file09
```

> file ./* | grep text

_The ./ is used to specify that the filenames are starting with - which is a part of filename but not a special character. **grep** is a command-line utility for searching plain-text data sets for lines that match a regular expression pattern. when text is used alongwith, searches for plain text files, scripts, source code files, configuration files, and similar types of files that are typically human-readable. * is used for listing out all files in current directory_

> cat ./-file07

password obtained: lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

**Level 5-> Level 6**: The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

> ssh -p 2220 bandit5@bandit.labs.overthewire.org

password: lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

> cd inhere/

> ls -al

output: 

```
total 88
drwxr-x--- 22 root bandit5 4096 Oct  5 06:19 .
drwxr-xr-x  3 root root    4096 Oct  5 06:19 ..
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere00
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere01
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere02
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere03
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere04
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere05
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere06
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere07
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere08
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere09
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere10
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere11
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere12
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere13
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere14
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere15
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere16
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere17
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere18
drwxr-x---  2 root bandit5 4096 Oct  5 06:19 maybehere19
```

> find -type f -size 1033c ! -executable -exec file {} + | grep "ASCII text"

output:
```
./maybehere07/.file2: ASCII text, with very long lines (1000)
```

_here find starts searching in the current directory. -type f tells that only regular files should be considered and -seize 1033c specifies that the file size should be 1033 bytes, c stands for bytes. ! -executbales excludes all the executable files and -exec executes the file command on current file and searches for human readable files._

> cat ./maybehere07/.file2

password obtained: P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

