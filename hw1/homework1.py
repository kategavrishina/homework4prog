a = int(input())
b = int(input())
c = int(input())
if a * b == c:
    print("a и b в сумме дают c : OK")
else:
    print("a и b в сумме дают c : NOT OK :(")
if -b / a == c:
    print("c является решением линейного уравнения ax + b = 0 : OK")
else:
    print("c является решением линейного уравнения ax + b = 0 : NOT OK :<")
