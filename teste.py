from pprint import pprint

contatos = {
    "Ana" : "(11) 91234-5678",
    "Bruno": "(21) 99876-5432",
    "Clara": "(31) 98765-4321",
}

print(contatos["Ana"])

print()
print()
contatos1 = {}
contatos["Ana"]   = "(11) 91234-5678"
contatos["Bruno"] = "(21) 99876-5432"
contatos["Clara"] = "(31) 98765-4321"
#Abaixo esta sobrescrevendo Ana, ou seja, mudará o valor
contatos["Ana"] = "(31) 98765-4321"

print(contatos["Clara"])
pprint(contatos)


contatos2 = {"Ana": "(11) 91234-5678", "Bruno": "(21) 99876-5432"}
#O operador in verifica se uma chave está presente no dicionário.
"Clara" in contatos2

"Ana" in contatos2

contatos3 = {"Ana": "(11) 91234-5678", "Bruno": "(21) 99876-5432"}
print(contatos3.get("Pedro", "não definido"))
