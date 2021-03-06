import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="credsleuth",
    version="0.0.19",
    author="Dave Davison",
    author_email="dave.davison@sophos.com",
    description="A rule based library to help identify credentials and secrets in files and strings.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sophos-cybersecurity/credsleuth",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    package_data={
        '': ['*']
    },
    scripts=['bin/credsleuth'],
)