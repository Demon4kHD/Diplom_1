
def create_data_for_test_database(current_dict: dict, current_key: str):
    len_dict = len(current_dict[current_key])
    list_with_tuple = []
    for num in range(len_dict):
        current_tuple = (num, current_dict[current_key][num])
        list_with_tuple.append(current_tuple)

    return list_with_tuple
