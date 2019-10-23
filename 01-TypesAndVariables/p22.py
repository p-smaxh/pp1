#pole trojkata z herona
import math;
a = int(input("Podaj długość boku a"));
b = int(input("Podaj długość boku b"));
c = int(input("Podaj długość boku c"));
p = 0.5*(a+b+c);
pole = math.sqrt(p*(p-a)*(p-b)*(p-c));
            
print("pole trojkata wynosi",pole);