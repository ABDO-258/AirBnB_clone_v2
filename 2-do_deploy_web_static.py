#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack"""

from fabric.api import local, task, env, put, run
from datetime import datetime
import os


env.hosts = ['35.168.8.193', '100.26.213.82']


@task
def do_pack():
    """Create a .tgz archive from the contents of the web_static folder."""
    folder_to_compress = "web_static"
    folder_of_compressed = "versions"
    try:
        # Create the versions folder if it doesn't exist
        local('mkdir -p versions')
        # Create the archive
        now = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        archive_name = f'web_static_{now}.tgz'
        path = f'{folder_of_compressed}/{archive_name}'
        tar_command = f'tar -czvf {path} {folder_to_compress}'
        local(tar_command)
        print(f'Packing web_static to {path}')
        return (path)
    except Exception:
        return None


@task
def do_deploy(archive_path):
    """Distribute an archive to your web servers."""

    try:
        if not os.path.exists(archive_path):
            return False

        put(archive_path, '/tmp/')

        file_with_extension = os.path.basename(archive_path)
        file_no_extension = os.path.splitext(file_with_extension)[0]

        path_file = f'/data/web_static/releases/{file_no_extension}'
        run(f"mkdir -p {path_file}")
        run(f'tar -zxf /tmp/{file_with_extension} -C {path_file}')
        run(f'rm /tmp/{file_with_extension}')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {path_file}/ /data/web_static/current')

        return True
    except Exception as e:
        return False
