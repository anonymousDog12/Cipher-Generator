# Cipher Generator

How to use: 	

Run ```CipherGenerator.py```, then enter your text

## RSA cipher
Support encrypt of message up to 1024bits

Generate:

Generate a pair of public key `e`,`n` and private key `d`,`n`

Encrypt text: 

Use public key `e`,`n` to encrypt

Decrypt text:

Use public key `e`,`n` to encrypt

Warning:
 - Ascii characters only. 
 - A restrction of length of encrypt text applies.

More ciphers will be supported soon! 	

TODO:
- Exclude some combinition of e and n which may crack this algorithm. 
- try to demonstrate to crack this algorithm when bits for `n` is small.