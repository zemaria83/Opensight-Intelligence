
# Script — Enumeração de Subdomínios (PoC OSINT)

Este script em Python constitui uma **prova de conceito (PoC)** desenvolvida no âmbito do projeto
**OpenSight Intelligence**, com o objetivo de demonstrar a viabilidade de automatização de tarefas
de recolha de informação OSINT.

O script realiza a **enumeração e validação de subdomínios** através de consultas DNS a fontes públicas,
sem recorrer a técnicas de intrusão ou exploração ativa.

---

## Objetivo
- Automatizar a verificação de subdomínios a partir de uma lista de entrada
- Identificar subdomínios que apresentam resolução DNS válida
- Demonstrar um exemplo simples de automação aplicável a serviços OSINT

---

## Funcionamento

O script funciona com base em ficheiros de texto simples (`.txt`), garantindo simplicidade,
reprodutibilidade e facilidade de análise dos resultados.

### Ficheiro de Entrada
O utilizador deve fornecer um ficheiro `.txt` contendo uma lista de possíveis subdomínios
(prefixos), com um subdomínio por linha.

Exemplo de ficheiro de entrada:
```txt
www
mail
api
dev
test
```
## Execução

Durante a execução, o script:

 - Lê o ficheiro de entrada com os subdomínios;

 - Combina cada subdomínio com o domínio base fornecido;

 - Realiza consultas DNS (A, AAAA ou CNAME) para verificar a existência do subdomínio;

 - Identifica os subdomínios com resolução DNS válida.

 - Ficheiro de Saída

Os subdomínios considerados válidos são guardados num ficheiro de texto .txt,
permitindo a sua posterior análise ou reutilização.

Exemplo de ficheiro de saída:

`www.exemplo.com`
`mail.exemplo.com`
`api.exemplo.com`

O nome do ficheiro de saída pode ser definido pelo utilizador através do parâmetro `--output`.

---

## Requisitos
- Python 3.10 ou superior
- Dependências descritas no ficheiro `requirements.txt` (na raiz do repositório)

Instalação das dependências:
```bash
python -m pip install -r ../requirements.txt`
```

## Utilização

Exemplo de execução a partir da raiz do projeto:

` python scripts\subdomain_enum.py -i examples\subdomains_clean.txt -d google.com -o examples\subdomains_active.txt`


## Parâmetros principais:

--`input` ou `-i` : ficheiro de entrada com subdomínios (um por linha)

--`domain` ou `-d` : domínio base a analisar

--`output` ou `-o` : (opcional) ficheiro de saída

--`timeout` : (opcional) timeout das consultas DNS

--`delay` : (opcional) atraso entre consultas DNS

## Output

O script gera um ficheiro de texto contendo apenas os subdomínios que apresentaram
resolução DNS válida.

Exemplo de output:

`www.exemplo.com`
`mail.exemplo.com`
`api.exemplo.com`

## Ética e Limitações

O script utiliza exclusivamente fontes públicas (consultas DNS).

Deve ser executado apenas em domínios próprios ou com autorização explícita.

Não realiza recolha de informação privada, exploração ativa ou testes intrusivos.

Tem carácter académico e demonstrativo, não constituindo uma ferramenta de produção.

## Nota Final

Este script foi desenvolvido como apoio ao projeto académico e serve apenas para ilustrar
conceitos de automação em OSINT, não substituindo ferramentas profissionais nem processos
completos de análise de segurança.
