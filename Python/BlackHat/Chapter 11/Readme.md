First Install the volatility software on you host machine to analyze the image or snapshot of the vm you are running on your host machine. 

this involves creating a virtual environment and then cloning the github and then installing it 

> PS> python3 -m venv vol3
> PS> vol3/Scripts/Activate.ps1
> PS> cd vol3/
> PS> git clone https://github.com/volatilityfoundation/volatility3.git
> PS> cd volatility3/
> PS> python setup.py install
> PS> pip install pycryptodome

then you can run. this is based on Windows, but if you want to do it on Ubuntu, follow the same steps with respective commands. 

you will have to run the _vol.py_ file in order to achieve what you want. that is to run the volatility on the snapshot captured. 

Commands to run the various things:

1. General Reconnaissance. to get the general info of the vm:
   
   > Windows: vol -f WinDev2007Eval-Snapshot4.vmem windows.info

   > Ubuntu:  sudo python3 vol.py -f snapshot1.raw windows.info.Info

2.  information in the registry:

   > Windows: vol -f WinDev2007Eval-7d959ee5.vmem windows.registry.printkey --key 'ControlSet001\Services'

   > ubuntu: sudo python3 vol.py -f snapshot1.raw windows.registry.printkey.PrintKey --key 'ControlSet001\Services'

3. lists
the command line arguments for each process as they were running at the
time the snapshot was made:

> Windows: vol -f WinDev2007Eval-7d959ee5.vmem windows.cmdline

> Ubuntu: sudo python3 vol.py -f snapshot1.raw windows.cmdline.CmdLine

4. the running processes a little bit deeper with the
pslist plug-in, which lists the processes that were running at the time
of the snapshot.:

> Windows: vol -f WinDev2007Eval-7d959ee5.vmem windows.pslist

> ubuntu: sudo python3 vol.py -f snapshot1.raw windows.pslist.PsList

5. the processes as a hierarchy, so we can tell what
process started other processes:

> Windows: vol -f WinDev2007Eval-7d959ee5.vmem windows.pstree

> Ubuntu: sudo python3 vol.py -f snapshot1.raw windows.pstree.PsTree

6. Hashdump for passwords:

  >  Windows: vol -f WinDev2007Eval-7d959ee5.vmem windows.hashdump

  >  Ubuntu: sudo python3 vol.py -f snapshot1.raw windows.hashdump.Hashdump

For each of them, you can use '-v' '-vv' '-vvv' and so on to get the details of problems and provcesses running in the background. 

We will face too many issues due to version differences and syntax changes withing the volatility frameworks, but we need to adapt to them by analyzing the properties of the Volatility. 

the _aslrcheck.py_ file is a custom plugin created to know all the process which are not under the aslr protection which might be helpful to us in exploiting the vulnerabilities. 

to run this:
> sudo python3 vol.py -p /home/harshith/Desktop/BHPCode/Chapter11 -f snapshot1.raw aslrcheck.AslrCheck

link to slides with pictures: https://docs.google.com/presentation/d/1_kKWxSOB7d2KbJmdi1gIlKWycPQeoOdKuetM1n6udOo/edit?usp=sharing
