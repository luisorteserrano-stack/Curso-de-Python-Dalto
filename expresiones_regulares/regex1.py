import re

text = "The quick brown fox jumps over the lazy dog"
x = re.search("^The.*dog$", text)
# El "*" afecedta al operador anterior, le dice que encuentre 0 ó alguna
# y en caso de ocurrencia, devolverlo, si no, lo deja pasar

if x:
    print("SI")
else:
    print("NO")