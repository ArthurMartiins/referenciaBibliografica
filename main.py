# com autor: SOBRENOME, Nome. Título da matéria. Nome do site, ano. Disponível em: <URL>. Acesso em: dia, mês e ano.
# sem autor: TÍTULO da matéria. Nome do site, ano. Disponível em: <URL>. Acesso em: dia, mês e ano.

print("*********************************************************")
titulo = input("Nome da matéria: ")
nomeSite = input("Nome do Site: ")
data = input("Quando foi acessado?: ")
nome = input("Nome do Autor do texto: ")
sobrenome = input("sobrenome do Autor do texto: ")
link = input("Link da matéria: ")
print("*********************************************************")

print(sobrenome + ', ' + nome + '. ' + titulo + '. ' + nomeSite + '. Disponível em: <' + link +'>. Acesso em: ' + data)
print("____________________________________________________________________________________")
