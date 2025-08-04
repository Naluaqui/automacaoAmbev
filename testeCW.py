import re

nome_arquivo = "relatorio_CW123456_final.pdf"

# Verifica se há um padrão "CW" seguido de exatamente 6 dígitos
match = re.search(r"CW\w{6}", nome_arquivo)
if match:
    print("Achou:", match.group())
    a = match.group()
    print(match)
    nome_arquivo = nome_arquivo.replace(f"{a}", "")
    print("Novo nome do arquivo:", nome_arquivo)
else:
    print("Não achou")