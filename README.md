# desafio-QA-LASIC
Repositório destinado ao desafio de QA do laboratório LASIC IFCE Maracanaú

## Desafio:
Crie um arquivo chamado usuarios.json com o seguinte conteúdo:
```json
{
    "quantidade": 0,
    "usuarios": [
    ]
}
```

1. Escreva um programa em python que leia informaçães de um usuário e os organize em um
dicionário no seguinte formato (o id deve ser gerado aleatoriamente e possuir um tamanho de
10 caractes numéricos e alfanuméricos ex:52f321s2s1):
```json
{
    "nome": "Luiz",
    "sobrenome": "Vitorino",
    "idade": 28,
    "curso": "Ciência da Computação",
    "instituição": "IFCE",
    "_id": "52f321s2s1"
}
```

onde não poderemos ter dois ids iguais. Após isso, adicione este usuário ao arquivo
usuários.json e intere a quantidade em +1, assim:
```json
{
    "quantidade": 1,
    "usuarios": [
        {
            "nome": "Luiz",
            "sobrenome": "Vitorino",
            "idade": 28,
            "curso": "Ciência da Computação",
            "instituição": "IFCE",
            "_id": "52f321s2s1"
        }
    ]
}
```

2. Escreva um programa em python que receba um id no formato da questão anterior,
pesquise este id no arquivo usuarios.json e retorne as informações do usuário:
exemplo:
entrada: 52f321s2s1
saída:
```json
{
    "nome": "Luiz",
    "sobrenome": "Vitorino",
    "idade": 28,
    "curso": "Ciência da Computação",
    "instituição": "IFCE",
    "_id": "52f321s2s1"
}
```
3. Escreva um programa em python que receba um id no formato das questões anteriores,
pesquise este id no arquivo usuarios.json, exclua o usuário do arquivo e decremente o valor
da chave 'quantidade' em -1.
4. Escreva um programa em python que receba um id conforme as questões anteriores e
permita ao usuário modificar o nome ou sobrenome do usuário.