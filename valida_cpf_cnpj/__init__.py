from itertools import cycle
import re

LENGTH_CNPJ = 14
def valida_cnpj(cnpj: str) -> bool:
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
def busc_cnpj(cnpj:str):
    resultados = []
    for match in re.findall(r"[0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2}", cnpj):
        resultado = valida_cnpj(match)
        if len(resultado) > 0:
            resultados.append(resultado)
    return resultados

texto = """O modelo do número segue este padrão: 82671952000100. O número do CNPJ 774375140001-33
        pode ser dividido em blocos: a inscrição, que são os primeiros 8 dígitos, a parte 
        que representa 90306453000103 se é matriz ou filial 31.049.514/0001-65 (0001 – matriz, ou 0002 – filial), e finalmente 
        dois dígitos verificadores 82671952000100. 00059549000151"""

if __name__ == "__main__":
    print(busc_cnpj(texto))
