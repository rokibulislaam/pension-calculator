from data.commutation_factor_table import commutation_factor_table


def get_commutation_value(age):
    return commutation_factor_table().get(int(age))
