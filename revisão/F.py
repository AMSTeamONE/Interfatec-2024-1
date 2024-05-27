# PROBLEMA F
import re
placa = input()
patterns = [
    (r"^[AP]\d{1,5}$", "muito antiga"),
    (r"^\d{,7}$", "numerica"),
    (r"^[A-Z]{2}\d{4}$", "AA-9999"),
    (r"^[A-Z]{3}\d{4}$", "AAA-9999"),
    (r"^[A-Z]{3}\d{1}[A-Z]{1}\d{2}$", "Mercosul")
]

def get_type(placa):
    for p, name in patterns:
        if re.search(p, placa) is not None:
            return f"Placa {name}"
    
    return "Placa invalida"

print(get_type(placa))