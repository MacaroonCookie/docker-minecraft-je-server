#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


class Versions(object):
    def __init__(self):
        mcversions_url = "https://mcversions.net"
        self.versions = {}
        self.latest = None

        with requests.get(mcversions_url) as mcversions_response:
            mcversions_soup = BeautifulSoup(mcversions_response.text, "html.parser")

        def extract_download_dict(soup, download_type):
            elements = release.div.find_all("a", class_=download_type)
            download_dict = None
            if elements:
                e = elements[0]
                download_dict = {
                    "url": e["href"],
                    "filename": e["download"],
                    "type": download_type,
                }
            return download_dict

        for release in mcversions_soup.find_all("li", class_="release"):
            self.versions[release["id"]] = {
                "version": release["id"],
                "date": release.find_all("span", class_="time")[0].text,
                "server": extract_download_dict(release, "server"),
                "client": extract_download_dict(release, "client"),
            }

        latest_element = mcversions_soup.find_all("li", class_="latest")
        if latest_element:
            self.latest = latest_element[0]["id"]

    def get_latest(self):
        return self.latest

    def _get_download_info(self, version, download_type):
        if version in self.versions:
            meta = self.versions[version]
            if meta[download_type] is not None:
                return meta[download_type]["url"], meta[download_type]["filename"]
            else:
                raise Exception(f"Minecraft {version} does not have a {download_type}")
        else:
            raise Exception(
                f"Minecraft versions {version} does not exist or is not found"
            )

    def get_server_download_info(self, version):
        return self._get_download_info(version, "server")

    def get_client_download_info(self, version):
        return self._get_download_info(version, "client")

    def has_client(self, version):
        if version in self.versions:
            if self.versions[version]["client"] is not None:
                return True
        else:
            return False

    def has(self, version):
        return version in self.versions

    def get_versions(self):
        return sorted(self.versions.keys())
