from typing import List

def longestCommonPrefix(strs: List[str]) -> str:

    if len(strs) == 0:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[0 : len(prefix) - 1]
            if prefix == "":
                return ""
    return prefix

longest_pref = longestCommonPrefix(["flower","flow","flight"])

print(longest_pref)