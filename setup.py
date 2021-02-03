import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='mindpowered-iptools',
    version='0.0.17',
    author="Mind Powered Corporation",
    author_email="support@mindpowered.dev",
    license="MIT",
    url="https://mindpowered.dev/",
    description="Tools for working with IP4/IP6 IP Addresses including IPv4, IPv6, CIDR, and Subnet Masks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['iptools'],
    packages=['mindpowered_iptools'],
    package_dir={'mindpowered_iptools': 'wrappers'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'mindpowered-maglev',
    ],
)
