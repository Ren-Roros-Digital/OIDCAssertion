# Assertion

A python / poetry application designed to create:

- domain specific certs and keys
- A assertion that conforms with MS OIDC

## Install

This application requires python ^3.11 and the openssl binary.
Any moderately modern MacOS and / or linux installation should provide this out of the box.

### Install poetry

```shell
$ curl -sSL https://install.python-poetry.org | python3 -
```

Add poetry to your PATH

- $HOME/.local/bin on Unix.
- %APPDATA%\Python\Scripts on Windows.

Alternatively, the full path to the poetry binary can always be used:

- ~/Library/Application Support/pypoetry/venv/bin/poetry on MacOS.
- ~/.local/share/pypoetry/venv/bin/poetry on Linux/Unix.
- %APPDATA%\pypoetry\venv\Scripts\poetry on Windows.

### Clone the repo

```shell
$ git@github.com:Ren-Roros-Digital/OIDCAssertion.git
```

### Install app

```shell
$ cd path/to/OIDCAssertion
$ poetry install
$ poetry shell
(assertion) $
```

The application provides several command line methods
As of now they are:

- **newcert**
  - create public certificate
- **fingerprint**
  - print the fingerprint of the given [crt | pfx]
- **assertion**
  - print the computed assertion
- **token**
  - try to fetch access token based on assertion and .env
- **decode**
  - decode and print a given [crt | pfx]

The commands  can either be invoked with 

```shell
(assertion) $ poetry run <CMD>
  or
(assertion) $ <CMD>
```

> Note. 
> When creating self signed certificates it seems that most services needs the **ISSUER** and **SUBJECT** to be equal.
> You can check the **ISSUER** and **SUBJECT** of your ca/ca.crt and <domain>/<domain>.crt with

```shell
(assertion) $ decode --help
Usage: decode [OPTIONS]

Options:
  --cert TEXT
  --help       Show this message and exit.

(assertion) $ decode --cert <domain>/<domain>.<ext>.cert.pem
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            1f:e4:b9:ea:30:15:b8:8d:48:cf:ed:11:dd:9f:52:33:1f:9c:34:7d
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = NO, L = Default City, O = Ren Roros Digital AS, CN = Ren Roros Digital AS
        Validity
            Not Before: Sep 12 11:23:15 2023 GMT
            Not After : Sep 11 11:23:15 2026 GMT
        Subject: C = NO, L = Default City, O = Ren Roros Digital AS, CN = Ren Roros Digital AS
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:be:75:27:cc:02:17:7f:ff:b2:2c:99:cf:38:e1:
                    97:57:e3:5f:da:22:6b:ab:e8:48:96:e9:58:38:38:
                    f6:9d:7a:d9:0b:ff:35:86:f8:6a:19:22:77:d2:6c:
                    6a:5f:5d:18:38:d2:8d:38:ed:de:bd:09:32:cf:3f:
                    ac:e6:0d:8e:a8:90:85:5c:77:10:bf:99:3c:63:c2:
                    13:f7:27:53:14:69:ce:42:ac:8e:8a:e4:9d:c7:a8:
                    a4:f0:79:d4:0a:ce:c9:50:95:90:24:26:2c:da:df:
                    c4:5b:67:b2:43:3d:dc:cb:e8:be:c4:e9:60:2b:cb:
                    a6:43:5e:cc:d2:bd:21:6b:6c:08:57:15:5f:24:06:
                    e1:01:b6:f6:f8:64:2e:46:cc:4d:95:e9:71:5d:3b:
                    e2:f0:ad:98:ac:45:a4:08:f4:e6:e6:d7:6e:76:96:
                    28:fb:b2:c1:fe:4a:b3:91:93:73:67:ae:1d:a9:da:
                    89:af:76:79:3f:fa:39:88:ac:7d:17:a7:41:1f:2c:
                    92:d4:79:31:17:03:d9:52:2b:88:9c:5a:e9:e3:9a:
                    a5:6e:5d:00:68:cb:17:3d:18:da:b5:f5:47:41:f7:
                    40:04:d9:69:2a:f7:26:d5:0f:38:68:73:e7:27:d3:
                    77:b9:ad:bd:78:74:3a:5b:07:fb:76:82:12:cd:50:
                    bf:f9
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Subject Key Identifier: 
                22:9E:ED:19:48:37:4E:0E:0F:0B:B8:E0:BB:DB:6E:63:FF:52:E9:09
            X509v3 Authority Key Identifier: 
                22:9E:ED:19:48:37:4E:0E:0F:0B:B8:E0:BB:DB:6E:63:FF:52:E9:09
            X509v3 Basic Constraints: critical
                CA:TRUE
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        11:b2:4b:31:09:df:48:38:66:38:ac:a4:c6:ff:64:60:cd:f0:
        57:41:31:8f:7b:29:a6:a3:b8:59:50:5f:e0:2d:2c:29:1c:54:
        c5:a9:8d:a9:75:ee:4b:5c:08:05:94:31:74:db:f0:15:5d:6b:
        9c:ad:f8:90:b1:a8:f4:2f:d5:ee:d7:3f:ea:f6:76:e1:0c:62:
        f0:5e:23:7c:68:7f:c4:98:b1:cd:b4:43:ad:e8:05:b3:73:26:
        52:9c:68:da:e4:a6:f2:4d:8f:f4:99:4c:af:79:4d:36:8f:21:
        e8:85:88:3b:cb:9e:fe:27:78:47:10:d3:32:3d:43:73:ad:53:
        8a:59:47:93:12:b4:61:d4:ce:f5:ba:29:d6:2b:61:14:00:02:
        82:98:33:7e:94:63:75:57:9d:8c:e3:91:f6:90:ed:d4:ce:e0:
        1f:8c:e8:b7:dc:19:8b:dd:06:5c:22:c3:42:57:e2:be:18:d2:
        1f:4b:0b:5e:b1:9c:8c:89:46:a9:a8:a2:99:78:20:66:2f:5c:
        7a:af:1b:e0:65:e6:75:d3:49:64:e2:55:f3:84:92:a6:a7:e3:
        7f:b1:ee:26:bd:75:f5:b7:91:7a:c6:06:ac:a7:db:f8:89:3b:
        84:a3:be:d2:74:e8:ad:36:ad:54:7a:8b:95:b1:a9:d9:af:bd:
        af:0c:93:b5
-----BEGIN CERTIFICATE-----
MIIDpTCCAo2gAwIBAgIUH+S56jAVuI1Iz+0R3Z9SMx+cNH0wDQYJKoZIhvcNAQEL
BQAwYjELMAkGA1UEBhMCTk8xFTATBgNVBAcMDERlZmF1bHQgQ2l0eTEdMBsGA1UE
CgwUUmVuIFJvcm9zIERpZ2l0YWwgQVMxHTAbBgNVBAMMFFJlbiBSb3JvcyBEaWdp
dGFsIEFTMB4XDTIzMDkxMjExMjMxNVoXDTI2MDkxMTExMjMxNVowYjELMAkGA1UE
BhMCTk8xFTATBgNVBAcMDERlZmF1bHQgQ2l0eTEdMBsGA1UECgwUUmVuIFJvcm9z
IERpZ2l0YWwgQVMxHTAbBgNVBAMMFFJlbiBSb3JvcyBEaWdpdGFsIEFTMIIBIjAN
BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvnUnzAIXf/+yLJnPOOGXV+Nf2iJr
q+hIlulYODj2nXrZC/81hvhqGSJ30mxqX10YONKNOO3evQkyzz+s5g2OqJCFXHcQ
v5k8Y8IT9ydTFGnOQqyOiuSdx6ik8HnUCs7JUJWQJCYs2t/EW2eyQz3cy+i+xOlg
K8umQ17M0r0ha2wIVxVfJAbhAbb2+GQuRsxNlelxXTvi8K2YrEWkCPTm5tdudpYo
+7LB/kqzkZNzZ64dqdqJr3Z5P/o5iKx9F6dBHyyS1HkxFwPZUiuInFrp45qlbl0A
aMsXPRjatfVHQfdABNlpKvcm1Q84aHPnJ9N3ua29eHQ6Wwf7doISzVC/+QIDAQAB
o1MwUTAdBgNVHQ4EFgQUIp7tGUg3Tg4PC7jgu9tuY/9S6QkwHwYDVR0jBBgwFoAU
Ip7tGUg3Tg4PC7jgu9tuY/9S6QkwDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0B
AQsFAAOCAQEAEbJLMQnfSDhmOKykxv9kYM3wV0Exj3sppqO4WVBf4C0sKRxUxamN
qXXuS1wIBZQxdNvwFV1rnK34kLGo9C/V7tc/6vZ24Qxi8F4jfGh/xJixzbRDregF
s3MmUpxo2uSm8k2P9JlMr3lNNo8h6IWIO8ue/id4RxDTMj1Dc61TillHkxK0YdTO
9bop1ithFAACgpgzfpRjdVedjOOR9pDt1M7gH4zot9wZi90GXCLDQlfivhjSH0sL
XrGcjIlGqaiimXggZi9ceq8b4GXmddNJZOJV84SSpqfjf7HuJr119beResYGrKfb
+Ik7hKO+0nTorTatVHqLlbGp2a+9rwyTtQ==
-----END CERTIFICATE-----


```

### Create domain certificates

```shell
(assertion) $ newcert --help
Usage: newcert [OPTIONS] DOMAIN

Options:
  --bits INTEGER  [default: 2048]
  --days INTEGER  [default: 1095]
  --help          Show this message and exit.

(assertion) $ newcert renroros.no
```

The command will create a folder *renroros* where the cert.pem, key.pem and pfx file for the domain will be placed. You will be given a lot of questions. You may or may not answer them. It's entirely up to you.

### Helper methods

```shell
(assertion) $ fingeprint --help
Usage: fingerprint [OPTIONS]

  Print the fingerprint of the given <path/to/certificate.crt> .

Options:
  --cert TEXT
  --help       Show this message and exit.

(assertion) $ fingerprint --cert renroros/renroros.no.cert.pem
EgzZG0O+aLmtIURu/o8QXJfCSys=

```

Will print the fingerprint (x5t) of the certificate. This for debugging purposes only.
Calling **assertion.fingerprint:get_fingerprint** will programatically get the fingerprint for inclusion in the **jwt** header.

```shell
(assertion) $ assertion --help
Usage: assertion [OPTIONS]

Options:
  --help  Show this message and exit.

```

Calling **asertion** uses the settings sub system. The settings sub system reads your **.env** file and prints the assertion based off of this to the command line.

An example **.env** file might look something like this.

```ini
fingerprint=renroros/renroros.no.cert.pem
public_key=renroros/renroros.no.key.pem
client_id=<xyz>
subscription_id=<zxy>
grant_type="urn:ietf:params:oauth:grant-type:jwt-bearer"
scope=https://test-api.helseplattformen.no/lws
token_url=https://oauth-iam-uat.helseplattformen.no/mga/sps/oauth/oauth20/token

```

Calling **assertion.create_assertion:get_authlib_payload** will programatically get the assertion 

To verify the assertion, you can use https://jwt.io

To get the token, mostly for testing purposes with *postman* you can use the **token** command.

```shell
(assertion) $ token --cert renroros/renroros.no.cert.pem
Usage: token [OPTIONS]

  Print the response from a token request.

  The default behaviour is that the command reads the .env file. Setting the
  options will override options from .env file.

Options:
  --cert TEXT
  --client-id TEXT
  --statuscode / --no-statuscode  [default: statuscode]
  --print-header
  --print-payload
  --print-token-string
  --help                          Show this message and exit.


(assertion) $ token --cert renroros/renroros.no.cert.pem --print-token-string
```
