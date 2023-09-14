import time

# Recursive Algorithm
def find_item_recursive(shopping_list, item, current_aisle):
    if current_aisle >= len(shopping_list):
        return False  # Item not found in any aisle
    if shopping_list[current_aisle] == item:
        return True  # Item found in the current aisle
    return find_item_recursive(shopping_list, item, current_aisle + 1)  # Recursive call for the next aisle

# Iterative (Non-Recursive) Algorithm
def find_item_iterative(shopping_list, item):
    for aisle in shopping_list:
        if aisle == item:
            return True  # Item found in the current aisle
    return False  # Item not found in any aisle

# Example shopping list
shopping_list = ["fruits", "vegetables", "dairy", "meat", "cereal", "snacks"]

# Item to find
item_to_find = "meat"

# Measure time for recursive algorithm
start_time = time.time()
result_recursive = find_item_recursive(shopping_list, item_to_find, 0)
end_time = time.time()
if result_recursive:
    print(f"{item_to_find} found in the shopping list (recursive).")
else:
    print(f"{item_to_find} not found in the shopping list (recursive).")
print(f"Time taken by recursive algorithm: {(end_time - start_time) * 1000} milliseconds")

# Measure time for iterative algorithm
start_time = time.time()
result_iterative = find_item_iterative(shopping_list, item_to_find)
end_time = time.time()
if result_iterative:
    print(f"{item_to_find} found in the shopping list (iterative).")
else:
    print(f"{item_to_find} not found in the shopping list (iterative).")
print(f"Time taken by iterative algorithm: {(end_time - start_time) * 1000} milliseconds")
