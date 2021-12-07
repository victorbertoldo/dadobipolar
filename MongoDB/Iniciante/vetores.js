db.funcionarios.insertOne(
    {
        nome: 'João',
        idade: 29,
        filhos: ['Mariana','Raul']
    }
);

db.funcionarios.find().pretty();

db.funcionarios.insertMany([
    {
        nome: 'João',
        idade: 29,
        filhos: ['Mariana','Raul']
    },
    {
        nome: 'Flávia',
        idade: 29,
        filhos: ['Alan','José']
    },
    {
        nome: 'Livia',
        idade: 29,
        filhos: ['Laura','Eva']
    }
])