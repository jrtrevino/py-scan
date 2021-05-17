"""
Opens up torguard VPN and qBittorent to download a given magnet link.
"""

import subprocess


def start_vpn(path):
    subprocess.Popen(['open', '/Applications/TorGuard.app'])
    # wait for program to open
    # launch qbittorent


start_vpn('')
