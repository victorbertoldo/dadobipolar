// Pesquisa geral

db.testes.find()

// Pesquisa 1 registro

db.testes.findOne({_id: "5e6fc00467d117556423bab7"})

// Deleta 1 registro -- este delete requer um criterio de filtro

db.testes.deleteOne({_id: ObjectId("5e6fc00467d117556423bab7")})

// deleta vários registros

db.testes.deleteMany({intercontinental: false})

// delete sem "where"

db.testes.deleteMany({})

