"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_ip_addr = address.replace('.', '[.]')
        return new_ip_addr


print(Solution().defangIPaddr(address="1.1.1.1"))
