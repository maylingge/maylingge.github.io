# TLS / SSL
public key infrastructure
[pki](https://en.wikipedia.org/wiki/Public_key_infrastructure)

[how it works with tcp](https://security.stackexchange.com/questions/20803/how-does-ssl-tls-work)

[TLS handshake](https://www.ibm.com/support/knowledgecenter/en/SSFKSJ_7.1.0/com.ibm.mq.doc/sy10660_.htm)
[overview of handshake](https://www.ssl.com/article/ssl-tls-handshake-overview/)

# self-signed certificate
[how to create](https://devcenter.heroku.com/articles/ssl-certificate-self)

# openssl
[openssl](https://www.openssl.org/)

# CA

# python simple server with ssl enabled.
[simple server with ssl](http://code.activestate.com/recipes/442473-simple-http-server-supporting-ssl-secure-communica/)

# asymmetric and symmetric encryption 
asymmetric is expensive than symmetric encryption

so TLS uses public/private key to exchange a symmetric secret key.

And then client/server will use the shared secret key to exchange message

Symmetric Encryption
Symmetric encryption is the oldest and best-known technique. A secret key, which can be a number, a word, or just a string of random letters, is applied to the text of a message to change the content in a particular way. This might be as simple as shifting each letter by a number of places in the alphabet. As long as both sender and recipient know the secret key, they can encrypt and decrypt all messages that use this key.

Asymmetric Encryption
The problem with secret keys is exchanging them over the Internet or a large network while preventing them from falling into the wrong hands. Anyone who knows the secret key can decrypt the message. One answer is asymmetric encryption, in which there are two related keys--a key pair. A public key is made freely available to anyone who might want to send you a message. A second, private key is kept secret, so that only you know it.

Any message (text, binary files, or documents) that are encrypted by using the public key can only be decrypted by applying the same algorithm, but by using the matching private key. Any message that is encrypted by using the private key can only be decrypted by using the matching public key.


This means that you do not have to worry about passing public keys over the Internet (the keys are supposed to be public). A problem with asymmetric encryption, however, is that it is slower than symmetric encryption. It requires far more processing power to both encrypt and decrypt the content of the message.

About Digital Certificates
To use asymmetric encryption, there must be a way for people to discover other public keys. The typical technique is to use digital certificates (also known simply as certificates). A certificate is a package of information that identifies a user or a server, and contains information such as the organization name, the organization that issued the certificate, the user's e-mail address and country, and the user's public key.

When a server and client require a secure encrypted communication, they send a query over the network to the other party, which sends back a copy of the certificate. The other party's public key can be extracted from the certificate. A certificate can also be used to uniquely identify the holder.

# TLS Session Resumption
resume tls session over different tcp connection

# HTTP Persistent connection 
[keep alive](http://51write.github.io/2014/04/09/keepalive/)


# SSL certificate
## how to apply for an official certificate
### create csr and private key and then pass the csr to the CA
    openssl req -new -newkey rsa:2048 -nodes -out myserver.csr -keyout myserver.key
    
    
### CA will provide a server.crt, root.crt and probably intermediate.crt
    server.crt and myserver.key is for your server to start up with SSL enabled.
    root.crt and intermediate.crt are to be import in browser and install on your system.
    for redhat, the following command will update the issuer to the host:
      cp root.crt /etc/pki/ca-trust/source/anchors/
      cp intermediate.crt /etc/pki/ca-trust/source/anchors/
      update-ca-trust extract
      
    The following command will verfiy whether the certificate is installed correctly:
      penssl verify server.crt
      server.crt: OK
