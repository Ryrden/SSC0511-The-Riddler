import sys

caracteres_invalidos = ['"', '^']

nome_linhas = str(input("Digite o nome das linhas\nExemplo: TelaLinha -> "))
ascii_art = open(sys.argv[1], "r")
lines = ascii_art.read().split("\n")
result = f"{nome_linhas+'0'}:string \""+"#"*40 + "\"" + "\n"

for i, line in enumerate(lines, start=1):
	if (len(line) > 40):
		print("Warning : draw extends 40 char limits")
		continue
	for invalid in caracteres_invalidos:
		line = line.replace(invalid, '#')
	nome_linha_atual = nome_linhas + str(i)
	espaco_entre = (40-len(line)-2)*" "
	line = line.upper()
	result += f"{nome_linha_atual}:string \"#{line}{espaco_entre}#\"" + "\n"

result += f"{nome_linhas+str(len(lines)+1)}:string \""+"#"*40 + "\"" + "\n"
print(f"Linhas : {len(lines)+2}")
print(result)
