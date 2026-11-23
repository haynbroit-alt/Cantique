import hashlib
import ssl

import jwt
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec, rsa

TAILLE = 3072


def cles():
    """Docstring qui cite RSA-2048 et md5 : ne doit rien déclencher."""
    privee = rsa.generate_private_key(public_exponent=65537, key_size=TAILLE)
    courbe = ec.generate_private_key(ec.SECP384R1())
    signature = courbe.sign(b"x", ec.ECDSA(hashes.SHA256()))
    # rsa.generate_private_key(public_exponent=65537, key_size=1024)
    return privee, signature


def empreinte(donnees):
    return hashlib.md5(donnees).hexdigest()


def jeton(cle):
    return jwt.encode({"sub": "1"}, cle, algorithm="RS256")


def contexte():
    ctx = ssl.create_default_context()
    ctx.minimum_version = ssl.TLSVersion.TLSv1_1
    return ctx


resultat = "revenu RSA des bénéficiaires"  # mot « RSA » dans du texte : pas un constat
