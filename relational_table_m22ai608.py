from __future__ import annotations
from pathlib import Path
from typing import Union, Any, DefaultDict, Dict, Tuple
import modified_utils 
import pandas as pd
from tabulate import tabulate

class RelationalTable:
    def __init__(self, src: Union[str, Path, DefaultDict]) -> None:
        if isinstance(src, str) or isinstance(src, Path):
            self.src = modified_utils.read_data(src)
        else:
            self.src = src

        self.relations = {} 

    def _set(self) -> None:
        #Creating an empty dictionary to storing table data
        self.data = {}

        # Loop over the Row labels & creating an empty dictionary for each row in Table
        for key, items in self.src.items():
            # Loop over the column labels & setting a value for each column in the row in The Table
            dataCol = {}
            for index, item in enumerate(items):
                dataCol[self.src.get('columns')[index]] =  item
                
            self.data [key] = list(dataCol.items())
   

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
            if type(key) is tuple:
                row = key[0]
                col = key[1]
            else:
                raise ValueError("correct value not provided")
            print("value at ",key," is: ",dict(self.data[str(col)])[row])


            ...
        elif method == 'row-col':
            if type(key) is tuple:
                row = key[0]
                col = key[1]
            else:
                raise ValueError("correct value not provided")

            print("value at ",key," is: ",self.data[str(row)][col][1])
            
            ...
        elif method == 'row':
            if type(key) is int:
                row = key
            else:
                raise ValueError("correct value not provided")
            print("value at ",key," is: ",self.data[str(row)])

            ...
        elif method == 'col':
            """column has `int` or `string` value"""
            if type(key) is int:
                row = key
                print("value at col ",key," is: ",[j[key][1] for i,j in self.data.items()])
            elif type(key) is str:
                row = key
                print("value at col ",key," is: ",[dict(j)[key] for i,j in self.data.items()])
            else:
                raise ValueError("correct value not provided")

            ...

    def relate(self, other_table: RelationalTable, key):
        """Complete this function so that it can relate this table to another using a provided key"""
        other_table._set()
        print('another table data')
        print(other_table.data)
        for k, item in self.data.copy().items():
            for key2, item2 in other_table.data.items():
                print(dict(item)[key])
                if(dict(item)[key] == dict(item2)[key]):
                    
                    self.data[k] = item + item2

        print(self.data)
        