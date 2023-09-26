"""Setup file for CryptoFuzz. Programmer and Owner: Mmdrza.Com / Email: PyMmdrza@gmail.com"""
import os, subprocess, platform
from setuptools import setup, find_packages
import datetime as dt
import os

PACK_NAME = "CryptoFuzz"
PACK_DESCRIPTION = "Generated and Converted Keys with any Type Foundation from Private Key [WIF Hexed Mnemonic and Binary Bytes seed] in Python"
PACK_VERSION = "2.6.9"
PACK_LICENSE = "MIT"
PACK_AUTHOR = "Mohammadreza (Mmdrza.Com)"
PACK_EMAIL = "Pymmdrza@gmail.com"
PACK_URL = "https://github.com/Pymmdrza/cryptofuzz"
PACK_ISSUES = 'https://github.com/Pymdrza/CryptoFuzz/issues'
PACK_DOCS_URL = 'https://github.com/Pymdrza/CryptoFuzz'
PACK_TYPE_README = 'text/markdown'

PACK_KEYWORD = ["CryptoFuzz", "Wif", "Mnemonic", "Binary", "seed", "Foundation", "Private", "Key", "HEX", "Mnemonic",
                "Binary", "Bytes", "bitcoin", "ethereum", "tron", "dogecoin", "zcash", "digibyte", "bitcoin gold",
                "wallet", "bip32", "bip39", "litecoin", "qtum", "ravencoin", "BTC", "ETH", "TRX", "DOGE", "BTG",
                "LTC", "ZEC", "AXE", "DASH"]
PACK_CLASSIFIERS = ["Development Status :: 5 - Production/Stable",
                    "Intended Audience :: Developers",
                    "Intended Audience :: Information Technology",
                    "Topic :: Security :: Cryptography",
                    "License :: OSI Approved :: MIT License",
                    "Programming Language :: Python :: 3",
                    "Programming Language :: Python :: 3.6",
                    "Programming Language :: Python :: 3.7",
                    "Programming Language :: Python :: 3.8",
                    "Programming Language :: Python :: 3.9",
                    "Programming Language :: Python :: 3.10",
                    "Programming Language :: Python :: 3.11",
                    "Programming Language :: Python :: Implementation :: CPython",
                    "Operating System :: OS Independent"]
PACK_COPYRIGHT = f"Copyright (C) 2023-{dt.date.today().year} - {PACK_AUTHOR}"
PACK_CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
PACK_README = "README.md"
PACK_PROJECT_URLS = {
    "Bug Tracker": PACK_ISSUES,
    "Documentation": PACK_DOCS_URL,
    "Source Code": PACK_URL,
    "Website": "https://mmdrza.com"
}
PACK_SCRIPTS_CONSOLE = {
    'console_scripts': [
        'cryptofuzz=cryptofuzz.CLI:__main__',
        'cryptofuzz-example=cryptofuzz.example:__main__'
    ]
}

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    PACK_README_DESCRIPTION = readme.read()


def installpackages():
    if 'win' in platform.platform().lower():
        subprocess.run(['pip', 'install', 'hdwallet'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(['pip', 'install', 'setuptools', 'wheel'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(['pip', 'install', 'ecdsa'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif 'linux' in platform.platform().lower():
        subprocess.run(['pip3', 'install', 'hdwallet'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(['pip3', 'install', 'setuptools', 'wheel'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(['pip3', 'install', 'ecdsa'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif 'mac' in platform.platform().lower():
        subprocess.run(['pip3', 'install', 'hdwallet'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(['pip3', 'install', 'setuptools', 'wheel'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(['pip3', 'install', 'ecdsa'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

installpackages()

setup(
    name=PACK_NAME,
    description=PACK_DESCRIPTION,
    long_description=PACK_README_DESCRIPTION,
    long_description_content_type=PACK_TYPE_README,
    url=PACK_URL,
    packages=find_packages(),
    project_urls=PACK_PROJECT_URLS,
    classifiers=PACK_CLASSIFIERS,
    entry_points=PACK_SCRIPTS_CONSOLE,
    version=PACK_VERSION,
    author=PACK_AUTHOR,
    author_email=PACK_EMAIL,
    license=PACK_LICENSE,
    keywords=PACK_KEYWORD,
    include_package_data=True,
    zip_safe=True
)