class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # check the length
        if len(s) == len(t):
            # use hash table to count the characters
            is_valid = True
            hash_table = {}

            for character in s:
                if character not in hash_table.keys():
                    hash_table[character] = 1
                else:
                    hash_table[character] += 1

            for character in t:
                if character not in hash_table.keys() or hash_table[character] == 0:
                    is_valid = False
                    break

                hash_table[character] -= 1

            if is_valid:
                return True
            else:
                return False
        else:
            return False