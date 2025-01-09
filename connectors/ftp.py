from ftplib import FTP

from ftplib import FTP

# Connect to the FTP server
ftp = FTP('ftp.example.com')
ftp.login(user='username', passwd='password')

# Change directory
ftp.cwd('/path/to/directory')

# List files in the current directory
ftp.retrlines('LIST')

# Upload a file
with open('localfile.txt', 'rb') as file:
    ftp.storbinary('STOR remotefile.txt', file)

# Download a file
with open('localfile.txt', 'wb') as file:
    ftp.retrbinary('RETR remotefile.txt', file.write)

# Close the connection
ftp.quit()
