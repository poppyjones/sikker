# Week 5

## 0

1. 148
2. 129
3. 135

## 1

The key is shared publicly since alice's message is not encrypted simply signed.

## 2

The protocol does not ensure mutual authentication since Bob can't authenticate Alice. ALice never returns Nb to bob.

## 3

Use kerberos.

## 4

### 23.3

**a. Identify the key elements in this certificate, including the owner’s name and public key, its validity dates, the name of the CA that signed it, and the type and value of signature.**

- Owners name: John Doe (VeriSign)
- pk: rsa encryption
  - 00:98:f2:89:c4:48:e1:3b:2c:c5:d1:48:67:80:53:d8:eb:4d:4f:ac:31:a9:fd:11:68:94:ba:44:d8:48:46:0d:fc:5c:6d:89:47:3f:9f:d0:c0:6d:3e:9a:8e:ec:82:21:48:9b:b9:78:cf:aa:09:61:92:f6:d1:cf:45:ca:ea:8f:df
- validity dates:
  - Not Before: Jan 13 00:00:00 2000 GMT
  - Not After : Mar 13 23:59:59 2000 GMT
- CA name: VeriSign
  - type: md5WithRSAEncryption
  - value: 5a:71:77:c2:ce:82:26:02:45:41:a5:11:68:d6:99:f0:4c:ce:
7a:ce:80:44:f4:a3:1a:72:43:e9:dc:e1:1a:9b:ec:64:f7:ff:
21:f2:29:89:d6:61:e5:39:bd:04:e7:e5:3d:7b:14:46:d6:eb:
8e:37:b0:cb:ed:38:35:81:1f:40:57:57:58:a5:c0:64:ef:55:
59:c0:79:75:7a:54:47:6a:37:b2:6c:23:6b:57:4d:62:2f:94:
d3:aa:69:9d:3d:64:43:61:a7:a3:e0:b8:09:ac:94:9b:23:38:
e8:1b:0f:e5:1b:6e:e2:fa:32:86:f0:c4:0b:ed:89:d9:16:e4:
a7:77

b. State whether this is a CA or end-user certificate, and why.

end-user: CA:FALSE

c. Indicate whether the certificate is valid or not, and why.

yeah, although the persona is not validated.

d. State whether there are any other obvious problems with the algorithms used in this certificate

self-sign, RSA is questionable but 512 should be enough, 

## 5

Using your Web browser, visit any secure Web site (i.e., one whose URL starts with “https”). Examine the details of the X.509 certificate used by that site. This is usually accessible by selecting the padlock symbol. Answer the same questions as for
Problem 23.3.

- Owners name: www.besoeglaegen.dk
- pk: rsa 4096 bits
- validity dates:
  - ‎13 ‎June ‎2017 07:46:48
  - ‎06 ‎September ‎2020 00:59:59
- CA name: AlphaSSL CA - SHA256 - G2
  - type: 
  - value:

## 6
