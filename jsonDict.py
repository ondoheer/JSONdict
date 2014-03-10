__author__ = 'ondoheer'


class JSONDictionary(object):

    """Creates an dictionary Object that works with JSON structured
    dictionaries it takes one such argument as an inialization parameter.
    It adds extra dictionary functionalities like key seaching and
    specific key value retrieval (no matters how nested or what kind
    of object the value is)"""

    dictionary = None

    def __init__(self, dictionary):
        '''initializes with a dictionary as argument'''
        self.dictionary = dictionary

    def listKeys(self, *args):
        '''lists every key in the object,
        it does not matter how nested it is'''
        if len(args) < 1:
            innerDict = self.dictionary
        else:
            innerDict = args[0]
        dictKeys = []
        for key, value in innerDict.iteritems():
            try:
                dictKeys.append(key)
            except TypeError:
                pass
            try:
                results = self.listKeys(value)
                for result in results:
                    dictKeys.append(result)
            except AttributeError:
                pass
        return dictKeys

    def getKeyValue(self, keyToSearch, *args):
        '''search all the tree for a specific dictionary,
        there cannot be repeated keys in the object or you will
        never know which one has been returned'''
        if len(args) < 1:
            dictionary = self.dictionary
        else:
            dictionary = args[0]
        if keyToSearch in dictionary:
            return dictionary[keyToSearch]
        for key, value in dictionary.iteritems():
            try:
                item = self.getKeyValue(keyToSearch, value)
                if item is not None:
                    return item
            except:
                pass

    def findKey(self, keyToSearch):
        '''Returns True if key in Object'''
        return keyToSearch in self.listKeys()
