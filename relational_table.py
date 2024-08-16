from __future__ import annotations
from pathlib import Path
from typing import Union, Any, DefaultDict, Dict, Tuple
from .utils import read_csv


class RelationalTable:
    def __init__(self, src: Union[str, Path, DefaultDict]) -> None:
        if isinstance(src, str) or isinstance(src, Path):
            self.src = read_csv(src)
        else:
            self.src = src

        self.relations = {} 

    def _set(self) -> None:
        """
        This function Tabularizes the data which can be indexed using rows and columns just like a Dataframe in pandas.

        -> Complete this function to create a realtional database out of this data. 
        -> You need to have a PRIMARY KEY in the database and a `checker` to ensure that the key is always unique.
        -> The data can be queried using (row, col) indices or (key, row) indices.
        """
        ...

    def query(self, key: Union[Tuple[Any, Any], int, str], method="key-row") -> Any:
        """Complete this function so that the data can be queried using keys"""
        if method not in ["key-row", "row-col", "row", "col"]:
            raise ValueError("Invalid Argument `method`")
        
        if method == 'key-row':
            ...
        elif method == 'row-col':
            ...
        elif method == 'row':
            ...
        elif method == 'col':
            """Do Note that col can have an `int` or a `string` value"""
            ...

    def relate(self, other_table: RelationalTable, key):
        """Complete this function so that it can relate this table to another using a provided key"""
        ...