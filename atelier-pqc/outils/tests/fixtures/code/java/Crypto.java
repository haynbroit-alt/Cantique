import java.security.KeyPairGenerator;
import java.security.MessageDigest;
import javax.crypto.Cipher;
import org.bouncycastle.crypto.engines.DESedeEngine;

public class Crypto {
    void exemple() throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(2048);
        Cipher c = Cipher.getInstance("AES/GCM/NoPadding");
        MessageDigest md = MessageDigest.getInstance("SHA-1");
        KeyPairGenerator ec = KeyPairGenerator.getInstance("EC");
        ec.initialize(new java.security.spec.ECGenParameterSpec("secp256r1"));
        DESedeEngine moteur = new DESedeEngine();
        String rsaKeyAlias = "cle-principale";
    }
}
