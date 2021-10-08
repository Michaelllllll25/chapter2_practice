car = {
    "model": "Prius",
    "make": "Toyota",
    "color": "grey"
}
print("  make     model     color")
print(" -----     -----     -----")
print(f"{car['make']}     {car['model']}     {car['color']}")
def print_row() -> None:
    """Print out a dictionary's fields in a single row.

    Args:
        dictionary (dict): The dictionary to print out.
        fields (List[str]): A list of field names to print out
            in order.
    """
    pass




fields = ["make", "model"]

# print table header
# print("\t".join(fields))
# print("\t".join(["-" * len(title) for title in fields]))

# # print single row
# print_row(car, fields)
