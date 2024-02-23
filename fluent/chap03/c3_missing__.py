#Implementing a dictionary that handles the missing key thing

class StrKeyDict(dict):
    '''A dictionary that converts the integer key to string one or else handles the missing key'''
    def __missing__(self, key):
        print("StrKeyDict:__missing__")
        if isinstance(key, str):
            # If the missing is is already an string we cannot handle it since str keys "need to be present if mentioned else KeyError
            raise KeyError(key)
        return self[str(key)]


    def get(self, key, default=None):
        print("StrKeyDict: __get__")
        try:
            return self[key]
        except KeyError:
            print("StrKeyDict: __caught__KeyError_")
            return default


    def __contains__(self, key):
        print("StrKeyDict: callback invoked __contains__")
        return key in self.keys() or str(key) in self.keys()
