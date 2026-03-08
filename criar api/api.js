// REST == CRIAR API ESCALAVEIS 

// REQUISIÇÕES 
 
// GET  == PEGA INFORMAÇÕES 
// POST  == CRIAR INFORMAÇÕES 
// PUT / PATCH  == ALTERAR ALGO QUE JA EXISTE 
// DELETE 

import express from "express"; 

const app = express();
const PORT = 3000;

app.get("/", (request,response)=>{
    // requisição 
    // response resposta 
    response.send("Olá mundo")

})

app.listen(PORT, () => {
    console.log(`O servidor está running on the DOOR ${PORT}`);
}  );


// porta que api esta escutando
// colocar uma função que irá executar quando estiver esc
// requisição get é sempre no navegador 
// você pode mandar varias respostas pela api 