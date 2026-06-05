#!/usr/bin/env python

from .datacomparer import DataComparer
from .datasorter import DataSorter
from .fileconverter import FileConverter
from .templatecreator import TemplateCreator


class DataComparerLibrary(DataComparer, DataSorter, FileConverter, TemplateCreator):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
