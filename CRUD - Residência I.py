#Create
usuarios = []
def cadastrar_usuario():
   nome = (input('Nome:'))
   idade = int(input('Idade:'))
   usuarios.append({'nome': nome, 'idade': idade})
   print('Usuário cadastrado!')
#Read
def listar_usuarios():
   for usuario in usuarios:
      print(f'Nome: {usuario["nome"]} | Idade: {usuario["idade"]}')
#Update
def atualizar_usuario():
   nome = str(input('Digite o nome do usuário que deseja alterar:'))
   encontrado = False
   for usuario in usuarios:
      if usuario['nome'] == nome:
         nova_idade = int(input('Digite a nova idade:'))
         usuario['idade']= nova_idade
         print('Idade atualizada com sucesso!')
         encontrado = True
         break
   if not encontrado:
      print('Usuário não encontrado.')
#Delete
def excluir_usuario():
   nome = str(input('Digite o nome do usuário que deseja excluir:'))
   encontrado = False
   for usuario in usuarios:
      if usuario['nome'] == nome:
         usuarios.remove(usuario)
         print('Usuário excluído com sucesso!')
         encontrado = True
         break
   if not encontrado:
      print('Usuário não encontrado.')
opcao = 0
while True:
   print(''' 1 - Cadastrar usuário
2-Listar usuários
3 - Atualizar usuário
4 - Excluir usuário
5 - Sair''')
   opcao = int(input('Digite a opção desejada:'))
   if opcao == 1:
      cadastrar_usuario()
   elif opcao == 2:
      listar_usuarios()
   elif opcao == 3:
      atualizar_usuario()
   elif opcao == 4:
      excluir_usuario()
   elif opcao == 5:
