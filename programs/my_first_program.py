from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    # Start date of the event
    HackerHouse = SecretInteger(Input(name="HackerHouse", party=party1, value=200))
    Rocks = SecretInteger(Input(name="Rocks", party=party1, value=208))

    # Computation for sum and product of HackerHouse and Rocks
    sum_result = HackerHouse + Rocks
    product_result = HackerHouse * Rocks

    # Outputs the sum and product to party1 with new labels
    return [
        Output(sum_result, "HackerHouse", party1),
        Output(product_result, "WillRock", party1)
    ]
