# setup.py

from setuptools import setup

install_requires=["numpy", "scipy"]

setup(
    name="prime-seive",
    install_requires=install_requires,
    packages=find_packages(where="src"),
    package_dir={"": "src"}
)