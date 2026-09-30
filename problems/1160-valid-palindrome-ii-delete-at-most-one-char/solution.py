def valid_palindrome(s):
    def is_palindrome(subs: str) -> bool:
        return subs == subs[::-1]

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # Check if either of the substrings is a palindrome
            return is_palindrome(s[left + 1:right + 1]) or is_palindrome(s[left:right])

    return True  # The string is already a palindrome
            
