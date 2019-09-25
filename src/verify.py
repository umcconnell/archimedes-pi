"""Pi verification"""
from decimal import Decimal as D


def correct_decimal_points(pi: D, file_name: str = "src/pi.txt") -> int:
    """Counts correct decimal points of approximated pi based on verification file

    :param pi: approximated pi
    :type pi: Decimal
    :param file_name: path to verification file (decimal points seperated by
    newline)
    :type file_name: str
    :returns: correct decimal points
    :rtype: int
    """
    decimal_points = str(pi)[2:]  # remove "3."

    index = 0
    correct = 0

    with open(file_name) as f:
        for line in f:
            line = line[:1]  # remove line break

            if index < len(decimal_points) and line == decimal_points[index]:
                correct += 1
                index += 1
            else:
                break

    return correct
