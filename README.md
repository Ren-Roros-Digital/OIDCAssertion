# Assertion

A python / poetry application designed to create:

- A signing authority
- domain specific certs and keys
- A assertion that conforms with MS OIDC

## Install

This application requires python ^3.11 and the openssl binary.
Any moderately modern MacOS and / or linux installation should provide this out of the box.

### Install poetry

```sh
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

```sh
$ git@github.com:Ren-Roros-Digital/OIDCAssertion.git
```

### Install app

```sh
$ cd path/to/OIDCAssertion
$ poetry install
$ poetry shell
(assertion) $
```

The application provides several command line methods
As of now they are:

- **ca**
  - Create signing authority
- **pubcert**
  - create public certificate with signing authority
- **fingerprint**
  - print the fingerprint of the given [crt | pfx]
- **assertion**
  - print the computed assertion
- **token**
  - try to fetch access token based on assertion and .env
- **decode**
  - decode and print a given [crt | pfx]

The commands  can either be invoked with 

```sh
(assertion) $ poetry run <CMD>
  or
(assertion) $ <CMD>
```

> Note. 
> When creating self signed certificates it seems that most services needs the **ISSUER** and **SUBJECT** to be equal.
> You can check the **ISSUER** and **SUBJECT** of your ca/ca.crt and <domain>/<domain>.crt with

```sh
(assertion) $ poetry run decode --cert ca/ca.crt
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            18:78:e0:2e:bb:db:f6:d1:e4:4f:97:56:53:ea:f1:98:bd:e5:c2:16
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = NO, O = Ren R\C3\83\C2\B8ros Digital AS, CN = Development Certificate
        Validity
            Not Before: Aug 30 08:56:50 2023 GMT
            Not After : Aug 29 08:56:50 2026 GMT
        Subject: C = NO, O = Ren R\C3\83\C2\B8ros Digital AS, CN = Development Certificate
        ...

(assertion) $ poetry run decode --cert renroros/renroros.no.crt
Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number:
            79:a4:45:9f:0a:07:af:65:9b:55:3f:80:c4:e5:bc:81:75:92:b8:6e
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = NO, O = Ren R\C3\83\C2\B8ros Digital AS, CN = Development Certificate
        Validity
            Not Before: Aug 30 08:56:54 2023 GMT
            Not After : Aug 29 08:56:54 2026 GMT
        Subject: C = NO, O = Ren R\C3\83\C2\B8ros Digital AS, CN = Development Certificate
```

### Create CA

```sh
(assertion) $ poetry run ca --help
Usage: ca [OPTIONS]

  Create signing auth.

  Cowardly refuse to overwrite existing signing auth unless forced.

Options:
  --authname TEXT      [default: ca]
  --force
  --bits INTEGER       [default: 2048]
  --cipher TEXT        [default: sha256]
  --days TEXT          [default: 1095]
  --country TEXT
  --organization TEXT
  --commonname TEXT
  --help               Show this message and exit.
```

The command will create all necessary signing authority files. You will get a question to give the .pfx file a password.
You may or may not do this. It's entirely up to you.

### Create domain certificates

```sh
(assertion) $ poetry run pubcert --help
Usage: pubcert [OPTIONS] DOMAIN

Options:
  --authname TEXT      [default: ca]
  --bits INTEGER       [default: 2048]
  --cipher TEXT        [default: sha256]
  --days INTEGER       [default: 1095]
  --country TEXT
  --organization TEXT
  --commonname TEXT
  --help               Show this message and exit.
```

The command will create a folder *renroros* where the cert, key and pfx file for the domain will be placed.
You will get a question to give the .pfx file a password.
You may or may not do this. It's entirely up to you.

### Helper methods

```sh
(assertion) $ poetry run fingerprint
```

Will print the fingerprint (x5t) of the signing authority. This for debugging purposes only.
Calling **assertion.fingerprint:get_fingerprint** will programatically get the fingerprint

```sh
(assertion) $ poetry run assertion
```

Will print the assertion to the commandline.
Calling **assertion.create_assertion:get_authlib_payload** will programatically get the assertion 

To verify the assertion, you can use https://jwt.io

```sh
(assertion) $ poetry run decode --cert path/to/cert.[crt | pfx]
```

Will decode and print the sertificate.

```sh
(assertion) $ poetry run token --help 
Usage: token [OPTIONS]

  Print the response from a token request given fingerprint, assertion and
  scope.

  This method uses the .env file.

Options:
  --cert TEXT
  --client-id TEXT
  --print-header
  --print-payload
  --help            Show this message and exit.
```

## The .env file

The placeholder ENV must be filled in and renamed **.env**
Be sure to never add this file to git.

The same goes for your signing authority files (default ca.[crt | key | cer | pfx]) and 
your domains private keys. It's really no big deal if they end up in git.. it's just a pain to issue new sertificates for all services.
