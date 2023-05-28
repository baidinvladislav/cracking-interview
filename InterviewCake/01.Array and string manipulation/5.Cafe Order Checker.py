# my iterative solution
# Time complexity: O(n)
# Space complexity: O(1)
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    take_out_counter = dine_in_counter = 0
    for order in served_orders:
        if take_out_counter <= len(take_out_orders) - 1 and order == take_out_orders[take_out_counter]:
            take_out_counter += 1

        elif dine_in_counter <= len(dine_in_orders) - 1 and order == dine_in_orders[dine_in_counter]:
            dine_in_counter += 1

        else:
            return False

    if take_out_counter != len(take_out_orders) or dine_in_counter != len(dine_in_orders):
        return False

    return True


# my recursive solution without slicing
# Time complexity: O(n)
# Space complexity: O(n)
def is_first_come_first_served(
        take_out_orders, dine_in_orders, served_orders,
        first_counter=0, second_counter=0, third_counter=0,
):
    if len(served_orders) - 1 == third_counter:
        return True

    if first_counter < len(take_out_orders) and served_orders[third_counter] == take_out_orders[first_counter]:
        first_counter += 1

    elif second_counter < len(dine_in_orders) and served_orders[third_counter] == dine_in_orders[second_counter]:
        second_counter += 1

    else:
        return False

    third_counter += 1

    return is_first_come_first_served(
        take_out_orders, dine_in_orders, served_orders,
        first_counter, second_counter, third_counter
    )


# my recursive solution
# Time complexity: O(n^2)
# Space complexity: O(n^2)
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    if len(served_orders) == 0:
        return True

    if take_out_orders and take_out_orders[0] == served_orders[0]:
        return is_first_come_first_served(take_out_orders[1:], dine_in_orders, served_orders[1:])
    elif dine_in_orders and dine_in_orders[0] == served_orders[0]:
        return is_first_come_first_served(take_out_orders, dine_in_orders[1:], served_orders[1:])
    else:
        return False


# their third solution (iterative)
# Time complexity: O(n)
# Space complexity: O(1)
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    take_out_orders_index = 0
    dine_in_orders_index = 0
    take_out_orders_max_index = len(take_out_orders) - 1
    dine_in_orders_max_index = len(dine_in_orders) - 1

    for order in served_orders:
        # If we still have orders in take_out_orders
        # and the current order in take_out_orders is the same
        # as the current order in served_orders
        if take_out_orders_index <= take_out_orders_max_index and order == take_out_orders[take_out_orders_index]:
            take_out_orders_index += 1

        # If we still have orders in dine_in_orders
        # and the current order in dine_in_orders is the same
        # as the current order in served_orders
        elif dine_in_orders_index <= dine_in_orders_max_index and order == dine_in_orders[dine_in_orders_index]:
            dine_in_orders_index += 1

        # If the current order in served_orders doesn't match the current
        # order in take_out_orders or dine_in_orders, then we're not serving first-come,
        # first-served.
        else:
            return False

    # Check for any extra orders at the end of take_out_orders or dine_in_orders
    if dine_in_orders_index != len(dine_in_orders) or take_out_orders_index != len(take_out_orders):
        return False

    # All orders in served_orders have been "accounted for"
    # so we're serving first-come, first-served!
    return True


# their second solution (recursive) without slicing so O(n) time instead of O(n^2)
# Time complexity: O(n)
# Space complexity: O(n)
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders,
                               take_out_orders_index=0, dine_in_orders_index=0,
                               served_orders_index=0):
    # Base case we've hit the end of served_orders
    if served_orders_index == len(served_orders):
        return True

    # If we still have orders in take_out_orders
    # and the current order in take_out_orders is the same
    # as the current order in served_orders
    if ((take_out_orders_index < len(take_out_orders)) and
            take_out_orders[take_out_orders_index] == served_orders[served_orders_index]):
        take_out_orders_index += 1

    # If we still have orders in dine_in_orders
    # and the current order in dine_in_orders is the same
    # as the current order in served_orders
    elif ((dine_in_orders_index < len(dine_in_orders)) and
          dine_in_orders[dine_in_orders_index] == served_orders[served_orders_index]):
        dine_in_orders_index += 1

    # If the current order in served_orders doesn't match
    # the current order in take_out_orders or dine_in_orders, then we're not
    # serving in first-come, first-served order.
    else:
        return False

    # The current order in served_orders has now been "accounted for"
    # so move on to the next one
    served_orders_index += 1
    return is_first_come_first_served(
        take_out_orders, dine_in_orders, served_orders,
        take_out_orders_index, dine_in_orders_index, served_orders_index)


# their first solution (recursive)
# Time complexity: O(n^2)
# Space complexity: O(n^2)
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    # Base case
    if len(served_orders) == 0:
        return True

    # If the first order in served_orders is the same as the
    # first order in take_out_orders
    # (making sure first that we have an order in take_out_orders)
    if len(take_out_orders) and take_out_orders[0] == served_orders[0]:
        # Take the first order off take_out_orders and served_orders and recurse
        return is_first_come_first_served(take_out_orders[1:], dine_in_orders, served_orders[1:])

    # If the first order in served_orders is the same as the first
    # in dine_in_orders
    elif len(dine_in_orders) and dine_in_orders[0] == served_orders[0]:
        # Take the first order off dine_in_orders and served_orders and recurse
        return is_first_come_first_served(take_out_orders, dine_in_orders[1:], served_orders[1:])

    # First order in served_orders doesn't match the first in
    # take_out_orders or dine_in_orders, so we know it's not first-come, first-served
    else:
        return False
