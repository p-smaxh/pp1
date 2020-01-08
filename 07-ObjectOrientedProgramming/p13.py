import random
class Arrays():
    separator = ","
    @staticmethod
    def change_sep(sep):
        Arrays.separator= sep
    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    @staticmethod
    def print_in_row(array):
        dl = len(array)
        for x in range(0,dl):
            if x<dl-1:
                print(str(array[x])+Arrays.separator,end="")
            else:
                print(array[x])
    @staticmethod
    def create_arr(x,n):
        array = [x]*n
        return array
    @staticmethod
    def create_arr_random(n,x,y):
        array = []
        for x in range(0,n):
            a = random.randint(x,y)
            array.append(a)
        return array
    @staticmethod
    def how_many(array,x,y):
        count = 0
        dl = len(array)
        for i in range(dl):
            if array[i]>=x and array[i]<=y:
                count = count+1
        return count
my_array = [4,1,8,7,2]
#Arrays.print_in_col(my_array)
Arrays.print_in_row(my_array)
Arrays.change_sep(" | ")
Arrays.print_in_row(my_array)