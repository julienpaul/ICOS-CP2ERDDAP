# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

__author__ = ["Julien Paul"]
__credits__ = ""
__license__ = "CC BY-SA 4.0"
__version__ = "0.0.0"
__maintainer__ = "BCDC"
__email__ = ['julien.paul@uib.no']

# --- import -----------------------------------
# import from standard lib
# import from other lib
# > conda forge
# import from my project


# ----------------------------------------------
def camel(word, sep=' '):
    """ rewrite with camelCase format

    >>> words = ["Hello", "World", "Python", "Programming"]
    >>> camel(words)
    'helloWorldPythonProgramming'
    >>> words = 'toto_25_tutu'
    >>> camel(words, sep='_')
    'toto25Tutu'
    >>> camel(words)
    'toto_25_tutu'
    """
    if isinstance(word, list):
        words = word
    else:
        words = word.split(sep=sep)

    s = "".join(word[0].upper() + word[1:].lower() for word in words)
    return s[0].lower() + s[1:]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
