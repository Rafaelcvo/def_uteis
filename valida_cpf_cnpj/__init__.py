from itertools import cycle
import re

def valida_cpf(cpf: str) -> bool:
    
    numbers = [int(digit) for digit in cpf if digit.isdigit()]
    zeros = [0 for _ in range(0, (11 - len(numbers)))]
    zeros.extend([int(digit) for digit in cpf if digit.isdigit()])
    numbers = zeros

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return ""

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return ""

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return ""

    return f"{''.join(str(i) for i in numbers[0:3])}.{''.join(str(i) for i in numbers[3:6])}.{''.join(str(i) for i in numbers[6:9])}-{''.join(str(i) for i in numbers[9:11])}"

def valida_cnpj(cnpj: str) -> bool:
    LENGTH_CNPJ = 14
    cnpj = cnpj.replace(".","").replace("/","").replace("-","")
    if len(cnpj) != LENGTH_CNPJ:
        return cnpj

    if cnpj in (c * LENGTH_CNPJ for c in "1234567890"):
        return ""

    cnpj_r = cnpj[::-1]
    for i in range(2, 0, -1):
        cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
        dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
        if cnpj_r[i - 1:i] != str(dv % 10):
            return ""

    return f"{''.join(str(i) for i in cnpj[0:2])}.{''.join(str(i) for i in cnpj[2:5])}.{''.join(str(i) for i in cnpj[5:8])}/{''.join(str(i) for i in cnpj[8:12])}-{''.join(str(i) for i in cnpj[12:14])}"

def localiza_cpfs_em_texto(texto: str):
    resultados = []
    for match in re.findall(r"[0]*[\d]{0,3}[\n\.]{0,2}[\d]{1,3}[\n\.]{0,2}[\d]{1,3}[\n-]{0,2}[\d]{1,2}", texto):
        resultado = valida_cpf(match)
        if len(resultado) > 0:
            resultados.append(resultado)
    return resultados

def localiza_cnpjs_em_texto(cnpj:str):
    resultados = []
    for match in re.findall(r"[0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2}", cnpj):
        resultado = valida_cnpj(match)
        if len(resultado) > 0:
            resultados.append(resultado)
    return resultados



