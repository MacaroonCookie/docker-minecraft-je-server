#!/usr/bin/env python

import unittest
from minecraftmeta import Versions

class TestVersions(unittest.TestCase):

    def setUp(self):
        self.versions = Versions()

    def test_downlaod_links(self):
        self.assertTrue(self.versions.has('1.12.2'))
        self.assertIn('1.12.2', self.versions.get_versions())
        self.assertTrue(self.versions.has_client('1.12.2'))
        self.assertEqual(self.versions.get_server_download_info('1.12.2'), ('https://launcher.mojang.com/v1/objects/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar', 'minecraft_server-1.12.2.jar'))
        self.assertEqual(self.versions.get_client_download_info('1.12.2'), ('https://launcher.mojang.com/v1/objects/0f275bc1547d01fa5f56ba34bdc87d981ee12daf/client.jar', 'minecraft-1.12.2.jar'))

    def test_versions(self):
        self.assertIsNotNone(self.versions.get_latest())
        self.assertTrue(self.versions.has(self.versions.get_latest()))
        self.assertFalse(self.versions.has('bad.version'))
        self.assertIsInstance(self.versions.get_versions(), type([]))
        self.assertIn(self.versions.get_latest(), self.versions.get_versions())
        self.assertFalse(self.versions.get_versions()[3] > self.versions.get_versions()[10])
        self.assertTrue(self.versions.get_versions()[5] < self.versions.get_versions()[8])
        self.assertTrue(self.versions.has_client(self.versions.get_latest()))
        self.assertFalse(self.versions.has_client('bad.version'))


if( __name__ == '__main__' ):
    unittest.main()
