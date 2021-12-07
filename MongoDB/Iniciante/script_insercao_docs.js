// inserindo apenas 1 documento


db.testes.insertOne( {
        aeroPartida: "SDU",
        aeroChegada: "YYZ",
        aviao: "Airbus",
        distancia: 30000,
        intercontinental: true
    })

//////////////////////

db.testes.insertOne( {
        aeroPartida: "GRU",
        aeroChegada: "GIG",
        aviao: "Airbus A320",
        distancia: 550,
        intercontinental: false
    })

/////////// consulta somente 1 registro

db.testes.findOne() // seletc * from tb limit 1

db.testes.find().pretty()

/// add campo e valor em um doc existente




