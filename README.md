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

The application provides four command line methods

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
  --country TEXT       [default: NO]
  --organization TEXT  [default: Ren Røros Digital AS]
  --commonname TEXT    [default: Development Certificate]
  --help               Show this message and exit.
```
Running 
```sh
(assertion) $ poetry run ca
```
Will create all necessary signing authority files. You will get a question to give the .pfx file a password.
You may or may not do this. It's entirely up to you.

```sh
(assertion) $ poetry run pubcert --help
Usage: pubcert [OPTIONS] DOMAIN

Options:
  --authname TEXT      [default: ca]
  --bits INTEGER       [default: 2048]
  --cipher TEXT        [default: sha256]
  --days INTEGER       [default: 1095]
  --country TEXT       [default: NO]
  --organization TEXT  [default: Ren Røros Digital AS]
  --help               Show this message and exit.
  ```
  Running
  ```sh
  (assertion) $ poetry run pubcert renroros.no
  ```
Will create a folder *renroros* where the cert and key file for the domain will be placed.

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

# The .env file

The placeholder ENV must be filled in and renamed **.env**
Be sure to never add this file to git.

The same goes for your signing authority files (default ca.[crt | key | cer | ..]) and 
your domains private keys. It's really no big deal if they end up in git.. it's just a pain to issue new
sertificates for all services.


