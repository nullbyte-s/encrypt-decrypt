# Encrypt and Decrypt Messages

Input a 'password' and use it to encrypt or decrypt text.

[Demo](https://mcnamee.github.io/encrypt-decrypt/index.html)

## Install

```bash
npm i
```

## Run
```bash
npm start

# Then open your browser at http://127.0.0.1:8080
```

## Deploy to Github Pages
```bash
sh gh-deploy.sh
```

## Sobre a chave secreta
O programa "secret-key-renewer.py" serve para gerar uma chave aleatória e armazenar no próprio index, evitando a necessidade de informar a chave escolhida. Isso foi feito para cenários onde somente as pessoas autorizadas têm acesso ao serviço (por exemplo, usando lista branca em um proxy reverso para limitar o acesso, bem como um sistema de login complementar, como o Authelia).

Como sugestão, para tornar as mensagens criptografadas temporárias, pode-se agendar uma tarefa no cron ou anacron, para que a chave secreta seja atualizada automática e periodicamente.

```bash
30      10       encrypt-decrypt-renewer       python3 ~/Projects/encrypt-decrypt/secret-key-renewer.py
```

Se essa sugestão for implementada, como "plano B", o programa armazena a última chave usada num arquivo "log.txt", para lidar com situações onde o texto foi criptografado com uma chave e, antes de ser descriptografado pelo destinatário, a chave foi renovada.
