import pysftp
from envs import *


class Sftp:

    def __init__(self, file) -> None:
        self.srv = pysftp.Connection(host=get_sftp_host(), username=get_sftp_user(), password=get_sftp_password())
        self.file = file

    def send_file_to_server(self) -> None:
        self.srv.chdir(get_backup_directory())
        self.srv.put(self.file) # upload file
        # Closes the connection
        self.srv.close()