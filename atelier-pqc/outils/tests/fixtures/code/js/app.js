const crypto = require('node:crypto');
const jwt = require('jsonwebtoken');

const { publicKey } = crypto.generateKeyPairSync('rsa', {
  modulusLength: 2048,
});
const h = crypto.createHash('sha1').update('x').digest('hex');
const c = crypto.createCipheriv('des-ede3-cbc', cle, iv);
jwt.verify(jeton, publicKey, { algorithms: ['RS256', 'ES256'] });
const rsaHelper = makeHelper(); // identifiant contenant « rsa » : rien
