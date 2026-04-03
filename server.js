const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
const MENSAGENS_FILE = path.join(__dirname, 'mensagens.json');

app.use(express.json());
app.use(express.static(__dirname));

// Garante que o arquivo de mensagens existe
if (!fs.existsSync(MENSAGENS_FILE)) {
  fs.writeFileSync(MENSAGENS_FILE, '[]', 'utf8');
}

// POST /contato — salva a mensagem
app.post('/contato', (req, res) => {
  const { nome, email, mensagem } = req.body;

  if (!nome || !email || !mensagem) {
    return res.status(400).json({ erro: 'Preencha todos os campos.' });
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    return res.status(400).json({ erro: 'E-mail inválido.' });
  }

  const mensagens = JSON.parse(fs.readFileSync(MENSAGENS_FILE, 'utf8'));
  mensagens.push({
    id: Date.now(),
    nome,
    email,
    mensagem,
    data: new Date().toISOString(),
  });
  fs.writeFileSync(MENSAGENS_FILE, JSON.stringify(mensagens, null, 2), 'utf8');

  res.json({ ok: true, mensagem: 'Mensagem recebida! Em breve entrarei em contato.' });
});

// GET /mensagens — lista mensagens salvas (uso privado)
app.get('/mensagens', (req, res) => {
  const mensagens = JSON.parse(fs.readFileSync(MENSAGENS_FILE, 'utf8'));
  res.json(mensagens);
});

app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});
