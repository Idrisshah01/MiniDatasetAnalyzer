def average_column(data,column):
    """
    calculate average of a numeric column
    """
    try:
        values = [float(row[column]) for row in data if row[column].replace(".","",1).isdigit()]
        return sum(values) / len(values) if values else None
    except KeyError:
        print(f"column '{column}' not found")
        return None

def max_column(data,column):
    """
    find the maximum value in a numeric column"""
    try:
        values = [float(row[column]) for row in data if row[column].replace(".","",1).isdigit()]
        return max(values) if values else None
    except KeyError :
        print(f" column '{column}' not found ")
        return None
    
def min_column(data,column):
    """ find the minimun value in the numeric column """
    try:
        valuse = [float(row[column]) for row in data if row[column].replace(".","",1).isdigit()]
        return min(valuse) if valuse else None
    except KeyError:
        print(f" column '{column}' not found ")
        return None
    
def frequency_count(data,column):
    """
    count frequency of each unique value in a column """
    try :
        freq = {}
        for row in data:
            value = row[column]
            freq[value] = freq.get(value,0) + 1
        return freq 
    except KeyError:
        print(f" column '{column}' not found ")
        return None
    
def search_rows(data,column,value):
    """ search rowa where column == value """
    try:
        return [row for row in data if row[column] == value]
    except KeyError:
        print(f" column '{column}' not found ")
        return None

def search_by_id(data,id_value,id_column="id"):
    for row in data:
        if row[id_column] == id_value:
            return row 
    return None

def search_by_name(data,name_value,name_column ="name"):
    return [row for row in data if row[name_column].lower() == name_value.lower()]

