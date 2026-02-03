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

## Requisitos
- Python 3.10 ou superior
- Dependências descritas no ficheiro `requirements.txt`

Instalação das dependências:
```bash
python -m pip install -r requirements.txt

