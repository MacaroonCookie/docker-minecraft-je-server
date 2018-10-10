from distutils.core import setup

setup(
    name="MinecraftMeta",
    version="0.1dev",
    packages=["minecraftmeta"],
    license="",
    long_description=open("README.md").read(),
    entry_points={"console_scripts": ["mcmeta=minecraftmeta.cli:call"]},
)
