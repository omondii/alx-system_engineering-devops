SFTP
Steps taken to move screenshots from my local system to the sandbox environment.

Sftp is a file transfer protocol that allows for secure file transfers over SSH.

- Installation
   snadbox: sudo apt-get install openssh-server
   local: enable OpenSSH Client via settings.

- Start sftp
  sftp username@hostname
  Authenticate with password
  if correct;
	sftp>

- copy files
  put </path/to/file.txt> <file.txt>
      (local path)            (remote file name)