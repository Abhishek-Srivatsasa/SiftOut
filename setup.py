from setuptools import setup , find_packages 

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="siftout",
    version="0.1",
    packages=find_packages(),
    author="Abhishek Srivatsasa Guntur",
    author_email="gabhisheksrivatsasa@gmail.com",
    description="A smart, automated workspace cleaner and security hardener for Python projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Abhishek-Srivatsasa/SiftOut",
)