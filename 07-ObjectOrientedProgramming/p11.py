class Arrays():
    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    @staticmethod
    def print_in_row(array):
        dl = len(array)
        for x in range(0,dl):
            if x<dl-1:
                print(str(array[x])+",",end="")
            else:
                print(array[x])

my_array = [4,1,8,7,2]
#Arrays.print_in_col(my_array)
Arrays.print_in_row(my_array)