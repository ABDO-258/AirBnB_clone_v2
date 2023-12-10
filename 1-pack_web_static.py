#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack"""

from fabric.api import local, task
from datetime import datetime


@task
def do_pack():
    """Create a .tgz archive from the contents of the web_static folder."""
    folder_to_compress = "web_static"
    folder_of_compressed = "versions"
    try:
        # Create the versions folder if it doesn't exist
        #local('mkdir -p "versions"')
        # Create the archive
        now = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        archive_name = f'web_static_{now}.tgz'
        tar_command = f'tar -czvf {folder_of_compressed}/{archive_name} {folder_to_compress}'
        local(tar_command)
        return f'{folder_of_compressed}/{archive_name}'
    except Exception:
        return None
