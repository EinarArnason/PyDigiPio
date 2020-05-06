from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="PyDigiPio",
    version="0.1.2",
    description="Python module for Raspberry Pi GPIO",
    long_description_content_type="text/markdown",
    long_description=f"{readme.strip()}",
    author="Einar Arnason",
    author_email="einsiarna@gmail.com",
    url="https://github.com/EinarArnason/PyDigiPio",
    license=f"{license.strip()}",
    py_modules=["PyDigiPio"],
    test_suite="tests",
    platforms=["linux"],
)
