import ftplib

def create_and_change_directory(ftp, directory_name):
    try:
        # Attempt to create the directory
        ftp.mkd(directory_name)

        # Change to the newly created directory
        ftp.cwd(directory_name)

        print(f"Changed to directory: {directory_name}")
    except ftplib.error_perm as e:
        print(f"FTP Error: {e}")

# Usage:
ftp = ftplib.FTP('192.168.92.128')
ftp.login("kali", "kali")

# Call the function to create and change to the "pub" directory
create_and_change_directory(ftp, 'pub')
