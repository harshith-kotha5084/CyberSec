First setup a GitHub account. create a token to push your code into it. 

we need a basic structure of our repo which our trojan uses. The config directory
holds unique configuration files for each trojan. As you deploy trojans, you
want each one to perform different tasks, so each trojan will check a separate
configuration file. The modules directory contains any modular code that the
trojan should pick up and then execute. We’ll implement a special import
hack to allow our trojan to import libraries directly from our GitHub repo.
This remote load capability will also allow you to stash third-party libraries in
GitHub so you don’t have to continually recompile your trojan every time you
want to add new functionality or dependencies. The data directory is where
the trojan will check in any collected data.

so we creae and push the same
> $ mkdir trojan
> 
> $ cd trojan
> 
> $ git init
> 
> $ mkdir modules
> 
> $ mkdir config
>
> $ mkdir data
> 
> $ touch .gitignore
> 
> $ git add .
> 
> $ git commit -m "Adds repo structure for trojan."
> 
> $ git remote add origin htps://github.com/-username-/trojan.git

Now we create modules (check in the trojan zip file.) and then push them into the repo. 
and we create a configuration file 'abc.json' where abc is the trojan id of our trojan we are going to create. 

we push everything and create the trojan on the target machine, with the name _git_trojan.py_

we run the file normally and notice that the trojan connects to the repo, gets the config file and then the modules and run it. then all the data is pushed into the data folder. 

Note: do not forget to change the username and password of your github account in the file. 

link to slides: https://docs.google.com/presentation/d/1UTs_lQGyKFMOdSBiloV6ThCNzEGHJU21Dd8zCxYEIyc/edit?usp=sharing
