def clip(text: str, max_len: int = 80):
    '''Clips a text at or before the max_len'''

    end = None
    if len(text) > max_len:
        space = text.rfind(' ', 0, max_len)
        if space >= 0: # There is a rightmost space within the range max_len
            end = space
        else: # We need ot search beyond the max_len
            space = text.rfind(' ', max_len)
            if space >=0 :
                end  = space
    if end is None:
        end = len(text)
    return text[:end].rstrip()
