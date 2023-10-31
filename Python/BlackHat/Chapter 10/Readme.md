First create the BlackHat service which is vulnerable. 

open the bhservice directory and run the file bhservice.py by:

In Windows:
> pyinstaller -F --hiddenimport win32timezone bhservice.py

then open the folder _dist_ and execute:
> bhservice.exe install
> bhservice.exe start

create a process monitor:

> run the process_monitor1.py

then for windows token privileges:

> run the process_monitor2.py

for file monitoring 

> run the file file_monitor1.py

then open a second the cmd.exe shell and execute this:

> C:\Users\tim\work> cd C:\Windows\temp
> C:\Windows\Temp> echo hello > filetest.bat
> C:\Windows\Temp> rename filetest.bat file2test
> C:\Windows\Temp> del file2test

Then for the code injection:

keep the bhservice process running. 
> run the code file_monitor2.py

then after the code injection, check the netstat service. 

link to the slides: https://docs.google.com/presentation/d/1VRjKd5lh4RwvZmROA--IHyaP0gumnw4lNk76kXMl7Dk/edit?usp=sharing
