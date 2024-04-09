#!/usr/bin/env python3


class Solution(object):
    def isIsomorphic(self, s: str, t: str) -> bool:
        length = len(s)
        if len(t) != length:
            return False

        mapping_s = {}
        mapping_t = {}

        for i in range(length):
            char_s = s[i]
            char_t = t[i]

            if char_s not in mapping_s:
                mapping_s[char_s] = char_t
            else:
                if mapping_s[char_s] != char_t:
                    return False
            
            if char_t not in mapping_t:
                mapping_t[char_t] = char_s
            else:
                if mapping_t[char_t] != char_s:
                    return False
        return True

