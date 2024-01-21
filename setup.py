# setup.py

from setuptools import setup, find_packages

install_requires=["numpy", "scipy", "matplotlib", "pandas"]

setup(
    name="prime_sieve",
    install_requires=install_requires,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True
)