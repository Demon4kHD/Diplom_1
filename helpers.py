from typing import List


def create_data_for_test_database(current_dict: dict, current_key: str):
    len_dict = len(current_dict[current_key])
    list_with_tuple = []
    for num in range(len_dict):
        current_tuple = (num, current_dict[current_key][num])
        list_with_tuple.append(current_tuple)

    return list_with_tuple

def create_receipt_for_check(bun_name, list_ingredients, total_price) -> str:
    receipt: List[str] = [f'(==== {bun_name} ====)']

    for ingredient in list_ingredients:
        receipt.append(f'= {str(ingredient[0]).lower()} {ingredient[1]} =')

    receipt.append(f'(==== {bun_name} ====)\n')
    receipt.append(f'Price: {total_price}')

    return '\n'.join(receipt)