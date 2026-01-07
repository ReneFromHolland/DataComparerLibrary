#!/usr/bin/env python

from .datacomparer import DataComparer
from .datasorter import DataSorter
from .fileconverter import FileConverter


class DataComparerLibrary(DataComparer, DataSorter, FileConverter):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
