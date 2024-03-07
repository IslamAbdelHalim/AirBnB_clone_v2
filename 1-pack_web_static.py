#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """archive file"""

    directory = local("mkdir -p versions")
    if directory.failed:
        return None

    time = datetime.utcnow()

    arc_file = 'versions/web_static_{}{}{}{}{}.tgz'
    .format(time.year, time.month, time.day,
            time.hour, time.minute, time.second)

    compress = local("tar -czf {} web_static".format(arc_file))

    if compress.failed:
        return None

    return arc_file
