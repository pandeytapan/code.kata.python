#Implementing a dictionary that handles the missing key thing

class StrKeyDict(dict):
    '''A dictionary that converts the integer key to string one or else handles the missing key'''
    def get(self, key, default=None):
        print("StrKeyDict: __get__")
        try:
            return self[key]
        except KeyError:
            print("StrKeyDict: __caught__KeyError_")
            return default

