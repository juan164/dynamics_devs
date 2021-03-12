"""
    Description: This class handles the behavior of filling numbers in an array. 
                 The private method _fill_number_1 is a easy solution but it reduces complexity 
                 of the excericise.
    Create Date: 12/03/21
    Author:      Juan castro
"""

from functools import reduce

class FillNumbers:

    """ with predeterminated languages functions """ 
    def _fill_number_1(self, arr: list) -> list:
        upto = max(arr)
        arr = list(range(1, upto + 1))
        return arr

    """ delete duplicates, get max and iterate and change array directly """ 
    def _fill_number_2(self, arr : list) -> list:
        arr = list(dict.fromkeys(arr))
        upto = reduce(lambda acc, el: acc if acc >= el else el, arr)
        for el in range(1, upto):
            if el not in arr:
                arr.append(el)
        arr.sort()
        return arr

    def fill_numbers(self, arr: list) -> list:
        try:

            if not arr: raise IndexError
            if type(arr) != type(list()): raise TypeError
            if list(filter(lambda x: x < 1, arr)): raise ValueError
            
            return self._fill_number_2(arr)

        except IndexError:
            return 'Please, send a not empty array'
        except TypeError:
            return 'Please, send a list of numbers'
        except ValueError:
            return 'Please, send only a positive numbers'

    def run(self, a: list):
        print(a)
        print(self.fill_numbers(a))


