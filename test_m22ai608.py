from typing import Union
from pathlib import Path
import relational_table_m22ai608

PATH: Path = Path("")

def is_interactive():
    import __main__ as main
    return not hasattr(main, '__file__')

if is_interactive():
    PATH =  "C:\\Users\\Admin\\OneDrive\\Desktop\\math-mod-sim-proj2-M22AI608//IRIS.csv"
else:
    PATH =  "C:\\Users\\Admin\\OneDrive\\Desktop\\math-mod-sim-proj2-M22AI608//IRIS.csv"


if __name__ == '__main__':
    # Put any other arguments that you have added in the below list
    args = []

    table1 = relational_table_m22ai608.RelationalTable(PATH, *args)
    table1._set()


    y = (10, 1);
    query_key : Union[int, str, tuple] = y ## Add the query key here
    values = table1.query(query_key, "row-col")

    y = ('petal_length', 10);
    query_key : Union[int, str, tuple] = y ## Add the query key here
    values = table1.query(query_key, "key-row")

    y = 10;
    query_key : Union[int, str, tuple] = y ## Add the query key here
    values = table1.query(query_key, "row")

    y = 1;
    query_key : Union[int, str, tuple] = y ## Add the query key here
    values = table1.query(query_key, "col")

    x = 'petal_length';
    query_key : Union[int, str, tuple] = x ## Add the query key here
    values = table1.query(query_key, "col")

    CUSTOM_DATA_PATH = Path("C:\\Users\\Admin\\OneDrive\\Desktop\\math-mod-sim-proj2-M22AI608//species.csv")
    table2 = relational_table_m22ai608.RelationalTable(CUSTOM_DATA_PATH)

    table1.relate(table2, "species")
    
    