#!/usr/bin/env python

import argparse
import sys
from .versions import Versions

def call():
    arg_parser = argparse.ArgumentParser(description="Query Mojang's Minecraft data.")
    arg_parser.add_argument('--download-version', type=str, default='latest', help='version of Minecraft server to download')
    args = arg_parser.parse_args()

    ver = Versions()
    if( args.download_version == 'latest' ):
        server_version = ver.get_latest()
    elif( ver.has(args.download_version) ):
        server_version = args.download_version
    else:
        print("ERROR: Minecraft version does not exist")
        exit(1)

    url, filename = ver.get_server_download_info(server_version)
    print(f"{filename} {url}")
    exit(0)
