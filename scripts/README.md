
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
O script recebe como entrada:
- um ficheiro de texto contendo possíveis subdomínios (prefixos),
- um domínio base autorizado.

Para cada subdomínio, é realizada uma consulta DNS (A, AAAA ou CNAME).
Os subdomínios válidos são guardados num ficheiro de saída para posterior análise.

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

`python scripts/subdomain_enum.py --input examples/subdomains.txt --domain exemplo.com`


## Parâmetros principais:

--`input` : ficheiro de entrada com subdomínios (um por linha)

--`domain` : domínio base a analisar

--`output` : (opcional) ficheiro de saída

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
