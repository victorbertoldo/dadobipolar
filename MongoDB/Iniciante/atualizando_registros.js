// Inserindo vários registros

db.clientes.insertMany([
    {_id: 1, nome: "Jão", sexo:"M"},
    {_id: 2, nome: "Ana", sexo:"F"},
    {_id: 3, nome: "Zé", sexo:"M"},
    {_id: 4, nome: "Maria", sexo:"F"},
    {_id: 5, nome: "Marcos", sexo:"M"}
    
 ]
    )
    
db.clientes.find().pretty()    


rs.slaveOk()

rs.stepDown() // nó primario atual voltar pra secundario

// atualizar 1 registro - db.clientes.updateOne({<FILTRO>},{<VALOR A ENTRAR>})
// tags de comando são precedidos de $

// db.clientes.updateOne({_id:1},{ativo:true}) assim não dá certo pois esta operação requer uma tag de comando ( atomic operators) pois o campo não existe
// operator $set = append

// append field ou alterar campo existente:
db.clientes.updateOne({_id:1},{$set:{ativo:true}})


//adicionar o campo em todos os registros
db.clientes.updateMany({},{$set:{active:true}})

// remover um campo
// operador $unset faz o contrário do $set


db.clientes.updateOne({_id:1},{$unset{ativo:""}})