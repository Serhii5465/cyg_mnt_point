import subprocess
from typing import Union

def get_cygwin_mount_point(uuid_drive: str) -> Union[None, str]:
    """
    Converts UUID partition to Cygwin format path's mount point.
    If disk not mounted, script will be stops his work.
    Args:
        uuid_drive: Universal Unique Identifier of HDD partition.

    Returns:
        If HDD not mounted, returns None. Otherwise, path to the HDD partition.
    """

    block_dev = subprocess.run(['blkid', '--uuid', uuid_drive], capture_output=True, text=True) #stdout: /dev/sda1\n

    """
    Checking if partition is mounted
    Output: CompletedProcess(args=['blkid', '--uuid', 'A0AACF26AACEF7B41'], returncode=2, stdout='', stderr='')
    """
    if block_dev.returncode != 0:
        return None
    else:
        # param: /dev/sda1
        # output: sda1
        part_blk_dev = block_dev.stdout.strip('\n').split('/dev/')[1]
        print(part_blk_dev)
