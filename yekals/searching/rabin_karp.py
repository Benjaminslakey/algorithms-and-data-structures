

def rolling_hash(src_str, l_idx, r_idx, prev_hash=None):
    # TODO: implement rolling hash
    new_hash = ""
    if prev_hash is None:
        pass # calc hash from scratch
    else:
        pass
    return new_hash

def rabin_karp(needle, haystack):
    """
    arg: needle - string to find
    arg: haystack - string to search through
    ret: idx in haystack where needle was found, or -1 if no match was found
    """
    needle_hash = rolling_hash(needle, 0, len(needle) - 1)
    win_left, win_right = 0, len(needle) - 1 
    prev_hash = None
    while win_right < len(haystack):
        win_hash = rolling_hash(haystack, win_left, win_right, prev_hash=prev_hash)
        # check if collision or match
        if win_hash == needle_hash:
            matches = True
            for idx, char in enumerate(needle):
                if char != haystack[win_left + idx]:
                    matches = False
                    break
            if matches:
                return win_left
        win_left, win_right = win_left + 1, win_right + 1
        prev_hash = win_hash
    return -1
