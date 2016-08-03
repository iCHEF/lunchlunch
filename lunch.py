#!/usr/bin/env python3
import os
import sys
from collections import defaultdict

import yaml


def print_bar(msg, char="="):
    prefix = ">>> "
    suffix = " "
    bar_length = 120 - len(msg) - len(prefix) - len(suffix)
    print("{}{}{}".format(prefix, msg, suffix) + char * bar_length)


def main(lunch_yml_path):
    with open(lunch_yml_path, "r") as f:
        lunch_list = yaml.load(f)

    # Collect summary
    orders_by_customer = defaultdict(list)
    for customer, items in lunch_list["orders"].items():
        for item in items:
            orders_by_customer[item].append(customer)

    # Show Item summary
    print_bar("Item Summary")
    for item, customers in orders_by_customer.items():
        print("{}: {}".format(item, len(customers)))
    # Show People summary
    print_bar("Customer Summary")
    for item, customers in orders_by_customer.items():
        print("{}: {}".format(item, ", ".join(customers)))

    # Print price
    if "price" not in lunch_list:
        return
    print_bar("Price")
    summary_price = sum(lunch_list["price"][item] * len(customers) for item, customers in orders_by_customer.items())
    print("Overall price: ${}".format(summary_price))
    for customer, items in lunch_list["orders"].items():
        print("{}: ${}".format(customer, sum(lunch_list["price"][item] for item in items)))


if __name__ == "__main__":
    # Get and read the yaml file
    if len(sys.argv) > 2:
        lunch_yml_path = sys.argv[1]
    else:
        lunch_yml_path = "lunch.yaml"

    main(lunch_yml_path)
