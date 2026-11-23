package main

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/md5"
	"crypto/mlkem"
	"crypto/rand"
	"crypto/rsa"
	"crypto/tls"
)

func main() {
	k, _ := rsa.GenerateKey(rand.Reader, 4096)
	e, _ := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
	d, _ := mlkem.GenerateKey768()
	_ = md5.Sum([]byte("x"))
	cfg := &tls.Config{
		MinVersion:       tls.VersionTLS10,
		CurvePreferences: []tls.CurveID{tls.X25519MLKEM768, tls.X25519},
	}
	_, _, _, _ = k, e, d, cfg
}
