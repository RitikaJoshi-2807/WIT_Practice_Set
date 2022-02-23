def get_coordinate(data):
    return data[1]
    
    """

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    pass


def convert_coordinate(coordinate):
    new=(coordinate[0], coordinate[1])
    return new
    """

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """



def compare_records(azara_record, rui_record):
    
    if(convert_coordinate(azara_record[-1])==rui_record[1]):
        return True
    else: 
        return False

        
    """
    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """

    pass
    


def create_record(azara_record, rui_record):
    if(compare_records(azara_record,rui_record)):
        return azara_record+rui_record
    else:
        return "not a match"
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """



def clean_up(combined_record_group):
    result=""
    for i in combined_record_group:
        i=list(i)
        del(i[1])
        i=tuple(i)
        result+=str(i)+"\n"
    return result

            

"""

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned". Excess coordinates and information removed.
"""
