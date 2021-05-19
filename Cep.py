import requests,os
def main():
		os.system('clear')
		print('\033[1;30;m                          ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print('\033[1;35;m                                  𝘽𝙔:Ｃｒｏｗｌｅｙ')
		print('\033[1;30;m                  ━━━━━━━━━━━                          ━━━━━━━━━━━')
		print(' \033[1;35;m                             𝘾𝙤𝙣𝙩𝙖𝙩𝙤: +55 67 9696-8737\033[m')
		print('\033[1;30;m                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[m')
		print('\033[1;30;m         ━━━━━━━━━━━━━━━━━━━                            ━━━━━━━━━━━━━━━━━━━')
		print('\033[1;30;m                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print('\033[1;35;m                                            ')
		print('\033[1;30;m                  ━━━━━━━━━━━\033[m       \033[1;35mCorporation\033[m      \033[1;30;m  ━━━━━━━━━━━')
		print(' \033[1;35;m                                           \033[m')
		print('\033[1;30;m                          ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[m')
		print('')
		print('')
		cep = input('\033[1;34mDigite o CEP que deseja consultar:\033[m\033[1;36m ')
		
		
		if len(cep) != 8:
			print('\033[1;33mQuantidade de digitos invalida!\033[m')
			exit()
			
		data = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep)).json()
		
		print(f"""
\033[1;31mResultados: \033[m'

\033[1;34mCep:\033[m \033[1;36m{data['cep']}\033[m
\033[1;34mLogradouro:\033[m \033[1;36m{data['logradouro']}\033[m
\033[1;34mComplemento:\033[m \033[1;36m{data['complemento']}\033[m
\033[1;34mBairro:\033[m \033[1;36m{data['bairro']}\033[m
\033[1;34mLocalidade:\033[m \033[1;36m{data['localidade']}\033[m
\033[1;34mEstado:\033[m \033[1;36m{data['uf']}\033[m
		""")
		opção = int(input('\033[7;35;97mDeseja realizar uma nova consulta? \033[m\n\n\033[1;30m[ 1 ]\033[m \033[1;97mSim\n\033[1;30m[ 2 ]\033[m \033[1;97mSair\n\n\033[1;31mR:\033[m\033[1;33m '))
		print('\033[m')
		os.system('clear')
	
		if  opção == 1:
			main()

if __name__ == '__main__':
	main()
