
iptools
=======
Tools for working with IP4/IP6 IP Addresses including IPv4, IPv6, CIDR, and Subnet Masks

![Build Status](https://mindpowered.dev/assets/images/github-badges/build-passing.svg)

Contents
========

* [Source Code and Documentation](#source-code-and-documentation)
* [About](#about)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Support](#support)
* [Licensing](#licensing)

# Source Code and Documentation
- Source Code: [https://github.com/mindpowered/ip-tools-python](https://github.com/mindpowered/ip-tools-python)
- Documentation: [https://mindpowered.github.io/ip-tools-python](https://mindpowered.github.io/ip-tools-python)

# About
IPv4 uses a 32-bit address for its Internet addresses. All IPv4 addresses are now assigned. IPv6 utilizes 128-bit Internet addresses so there are 1028 times more addresses. Mappings exist for converting from an IPv4 address to an IPv6 addresses. This allows interoperability.

An IP address consists of octets delimited by dots (".") for IPv4 or colons (":") for IPv6. We can compress IPv6 addresses by removing extra zeros to make the address shorter. Computers store IP addresses as their corresponding integer values. The number represented by this integer is its decimal representation.

Subnetting is the process of dividing a network into smaller network sections. A part of the IP address is *masked* off to define a network. The remaining part of the address identifies a device on the network. CIDR is an alternative way of representing a subnet mask and IP address range.

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

# Licensing
This package is released under the MIT License.



[bugs]: https://github.com/mindpowered/ip-tools-python/issues
[contact]: https://mindpowered.dev/support/?ref=ip-tools-python/
[docs]: https://mindpowered.github.io/ip-tools-python/
[licensing]: https://mindpowered.dev/?ref=ip-tools-python
[purchase]: https://mindpowered.dev/purchase/
