import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='mindpowered-iptools',
    version='0.0.14',
    author="Mind Powered Corporation",
    author_email="support@mindpowered.dev",
    license="CPAL-1.0",
    url="https://mindpowered.dev/",
    description="Tools for working with IP Addresses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['iptools'],
    packages=['mindpowered_iptools'],
    package_dir={'mindpowered_iptools': 'wrappers'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'mindpowered-maglev',
    ],
)
