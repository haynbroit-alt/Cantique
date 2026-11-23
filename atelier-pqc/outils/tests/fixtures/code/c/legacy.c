#include <openssl/evp.h>
#include <openssl/rsa.h>

void f(void) {
    EVP_PKEY_CTX *ctx = EVP_PKEY_CTX_new_id(EVP_PKEY_RSA, NULL);
    EVP_PKEY_CTX_set_rsa_keygen_bits(ctx, 1024);
    const EVP_CIPHER *c = EVP_des_ede3_cbc();
    const EVP_MD *m = EVP_md5();
    EC_KEY *k = EC_KEY_new_by_curve_name(NID_X9_62_prime256v1);
}
