"""Some functions about input text convert."""
def apply_rule(column: int, delimiter: str, intext):
    """_summary_
    Desc: Convert multiple lines to a table. Each line is an element.
    Args:
        column (int): _description_
        delimiter (str): _description_
        intext (_type_): _description_

    Returns:
        _type_: _description_
    """

    lst_input = intext.strip().split("\n")
    if delimiter == 'tab':
        lst_row = ['\t'.join(map(str, lst_input[i:i+column])) for i in range(0, len(lst_input), column)]
    else:
        lst_row = [delimiter.join(map(str, lst_input[i:i+column])) for i in range(0, len(lst_input), column)]

    
    str_output = '\n'.join(x for x in lst_row)
    print(str_output)
    return str_output