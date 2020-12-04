#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# staticObject.py

"""
    The staticObject module is used to explore ICOS CP StaticObjects' metadata.

    Example usage:

    From staticObject import StaticObject

    staticobjects = StaticObject()  # initialise ICOS CP StaticObject object
    staticobjects.get_meta()        # get staticobjects' metadata from ICOS CP
    staticobjects.show()            # print staticobjects' metadata
"""

# --- import -----------------------------------
# import from standard lib
import logging
# import from other lib
# import from my project
from icp2edd.icpObj import ICPObj

# --- module's variable ------------------------
# load logger
_logger = logging.getLogger(__name__)

# object attributes' dictionary with RDF 'property' as key and RDF 'object' as value
#   RDF triples: 'subject' + 'property/predicate' + 'object/value'
# {'property/predicate': 'object/value'}
# Note: 'object/value' will be the output attribute name
_attr = {
    'cpmeta:hasSizeInBytes': 'sizeInBytes',
    'cpmeta:hasSha256sum': 'sha256sum',
    'cpmeta:hasCitationString': 'citation',
    'cpmeta:hasName': 'name',
    'cpmeta:hasDoi': 'doi',
    'cpmeta:isNextVersionOf': 'StaticObject',
    'cpmeta:wasSubmittedBy': 'DataSubmission'
}


# ----------------------------------------------
class StaticObject(ICPObj):
    """
    >>> t.getMeta()
    >>> t.show()

    """

    def __init__(self, limit=None, lastupdate=None, endupdate=None, lastversion=None, uri=None):
        """ initialise instance of StaticObject(ICPObj).

        It will be used to set up a sparql query, and get all metadata of StaticObject from ICOS CP.

        Optionally we could limit the number of output:
        - limit the amount of returned results

        and/or select StaticObject:
        - submitted since 'lastupdate'
        - submitted until 'endupdate'
        - only from the 'lastversion'
        - with ICOS CP 'uri'

        Example:
            StaticObject(limit=5)

        :param limit: number of returned results
        :param lastupdate: submitted since last update ( '2020-01-01T00:00:00.000Z' )
        :param endupdate: submitted until end update ( '2020-01-01T00:00:00.000Z' )
        :param lastversion: select only last release [True,False]
        :param uri: ICOS CP URI ('https://meta.icos-cp.eu/objects/uwXo3eDGipsYBv0ef6H2jJ3Z')
        """
        super().__init__()
        # set up class/instance variables
        self._uri = uri
        self._limit = limit
        self._lastupdate = lastupdate
        self._endupdate = endupdate
        self._lastversion = lastversion

        # object attributes' dictionary
        if isinstance(_attr, dict):
            self._attr = {**_attr, **self._attr}

        # object type URI
        self._object = 'http://meta.icos-cp.eu/ontologies/cpmeta/StaticObject'


if __name__ == '__main__':
    import doctest

    doctest.testmod(extraglobs={'t': StaticObject(limit=10)},
                    optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/