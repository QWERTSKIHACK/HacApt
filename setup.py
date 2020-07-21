from setuptools import (
    setup,
    find_packages
)

from src.lib.settings import VERSION


setup(
    name='HacApt',
    version=VERSION,
    auth="Ekultek",
    author_email="staysalty@protonmail.com",
    license="General Public License",
    packages=find_packages(),
    scripts=['src/bin/hacapt'],
    install_requires=["requests<=2.19.1", "pyyaml==5.1", "pysocks==1.6.8"],
    keywords="package-manager hacking-tools information-security"
)