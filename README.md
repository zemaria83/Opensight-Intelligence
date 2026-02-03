# OpenSight Intelligence — Projeto OSINT

Projeto académico de conceção e prototipagem de uma plataforma de serviços OSINT (Open Source Intelligence),
desenvolvida com foco na recolha, análise e reporting de informação proveniente de fontes abertas,
de forma ética e em conformidade com o Regulamento Geral sobre a Proteção de Dados (RGPD).

O projeto inclui um protótipo funcional desenvolvido em Uizard e uma prova de conceito (PoC) técnica
para demonstrar a viabilidade de automação de tarefas OSINT.

---

## Objetivos
- Diagnóstico de exposição digital
- Produção de relatórios OSINT e recomendações
- Prototipagem de dashboards e fluxos de utilização
- Prova de conceito (PoC) de automação: enumeração de subdomínios via DNS

---

## Estrutura do Repositório
- `docs/` — capítulos do relatório e anexos
- `design/` — wireframes e protótipo Uizard (assets e descrição)
- `diagrams/` — diagramas UML, fluxogramas e modelos de dados
- `scripts/` — provas de conceito (ex.: enumeração de subdomínios)
- `assets/` — imagens, screenshots e logótipos
- `examples/` — outputs de exemplo (sem dados sensíveis)

---
## Prova de Conceito (PoC)

O repositório inclui um script em Python para enumeração de subdomínios, utilizando exclusivamente
consultas DNS (fontes públicas). Esta PoC tem carácter académico e demonstrativo, não constituindo
um sistema completo nem uma ferramenta de exploração.

Execução (exemplo):

```bash
python scripts/subdomain_enum.py --input subdomains.txt --domain exemplo.com


## Ética e Limitações

Apenas são utilizadas fontes de informação públicas (OSINT).
A execução de scripts deve ser realizada apenas em domínios próprios ou com autorização explícita.
Não são realizadas atividades de intrusão, exploração ativa ou recolha de informação privada.
Dados de exemplo presentes no repositório são fictícios ou anonimizados.
O projeto encontra-se em fase de prototipagem académica e não representa um produto final em produção.

**## Estado do Projeto**

Projeto em fase de conceção, prototipagem e validação académica, desenvolvido no âmbito de uma unidade
curricular de cibersegurança.



---

## Requisitos
- Python 3.10 ou superior
- Dependências descritas no ficheiro `requirements.txt`

Instalação das dependências:
```bash
python -m pip install -r requirements.txt
