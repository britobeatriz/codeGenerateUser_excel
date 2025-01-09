import random
import string
import json
import pandas as pd

# json data users(cpf and matricula)
pathUsers = 'users.json'
with open(pathUsers, 'r') as file:
    data = json.load(file)
# print(data)

# this class receive data of user
class User:
    def __init__(self, cpf, matricula, code):
        self.cpf = cpf,
        self.matricula = matricula
        # self.code = codeGenerator()
        self.code = code

    def __str__(self):
        # return f"Cpf: {self.cpf}, Matricula:{self.matricula}, Codigo: {self.code}"
        return f"{self.cpf},{self.matricula},{self.code}"
    
# this function generates a for digit randon code 
def codeGenerator():
    code = []
    cd = random.choice([random.choice(string.ascii_uppercase)])
    for _ in range(3):
        choice = random.choice([random.choice(string.ascii_uppercase), random.randint(0, 9)])
        cd += str(choice)
        code.append(cd)

    code = code[-1]
    # print(codigo)
    return code

# stores the data with the code in the variable(codeWithCpf)
codeWithCpf = []
for line in data:
    newCode = codeGenerator()
    exists = any(item['code'] == newCode for item in codeWithCpf)
    user = User(cpf=line['cpf'], matricula=line['matricula'], code=newCode) # check if the codes alredy exists(any)
    # print(usuario)
    codeWithCpf.append({"cfp":user.cpf[0], "matricula":user.matricula, "code":user.code})
# print(codeWithCpf)

# save the data in xlsx file
df = pd.DataFrame(codeWithCpf) # dataframe
df.to_excel('arquivo.xlsx', index=False)
print(df)
