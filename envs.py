from os import getenv


def get_sftp_host() -> str:
    return getenv('SFTP_HOST', 'localhost')

def get_sftp_user() -> str:
    return getenv('SFTP_USER', '')

def get_sftp_password() -> str:
    return getenv('SFTP_PASSWORD')

def get_object_to_backup() -> str:
    return getenv('OBJECT_TO_BACKUP', '')

def get_tmp_backup_directory() -> str:
    return getenv('TMP_BACKUP_DIRECTORY', '')

def get_backup_directory() -> str:
    return getenv('BACKUP_DIRECTORY', '')

def get_max_backup_amount() -> int:
    return int(getenv('MAX_BACKUP_AMOUNT', 5))
