squares={a:a * a for a in range(5,11)}
print(squares)

l=['John', 'Samuel', 'Eke', 'Tobi']

result = {len(x): x for x in l}
capital = {x[1].upper(): x for x in l}
print(result)
print(capital)