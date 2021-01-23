
iptools
=======
Tools for working with IP Addresses

![Build Status](https://mindpowered.dev/assets/images/github-badges/build-passing.svg)

Contents
========

* [Source Code and Documentation](#source-code-and-documentation)
* [Licensing](#licensing)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Support](#support)

# Source Code and Documentation
- Source Code: [https://github.com/mindpowered/ip-tools-python](https://github.com/mindpowered/ip-tools-python)
- Documentation: [https://mindpowered.github.io/ip-tools-python](https://mindpowered.github.io/ip-tools-python)

# Licensing
This package is dual-licensed under the MIT and CPAL-1.0 licenses.

To obtain a version licensed under the MIT License, follow the instructions at [get a license][purchase].

# Requirements
- Requires Python 3.x. Due to security fixes and new features Python 3.7 or later is recommended.
- pip


Third-party dependencies may have additional requirements.

# Installation
You can retrieve the iptools package from the Python Package Index https://pypi.org/ using pip. First make sure you have python3 and python3-pip installed. Then you can start by making a `requirements.txt` file in your working directory with the iptools requirement in it. You can add any other packages to your requirements here, each as a separate line.

requirements.txt:
```
mindpowered-iptools>0
```
Now you can use pip to install the iptools package: `python3 -m pip install -r requirements.txt`
If you would like to update the package, simply run the above command again.


# Usage
```python
from mindpowered_iptools import *

ipt = IPTools()
decimal = ipt.IPToDecimal("192.168.1.1")

```


# Support
We are here to support using this package. If it doesn't do what you're looking for, isn't working, or you just need help, please [Contact us][contact].

There is also a public [Issue Tracker][bugs] available for this package.



[bugs]: https://github.com/mindpowered/ip-tools-python/issues
[contact]: https://mindpowered.dev/support.html?ref=ip-tools-python/
[docs]: https://mindpowered.github.io/ip-tools-python/
[licensing]: https://mindpowered.dev/?ref=ip-tools-python
[purchase]: https://mindpowered.dev/purchase/ip-tools-python
