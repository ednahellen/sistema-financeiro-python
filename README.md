# Sistema Financeiro — Portfólio com dados 100% fictícios

Projeto demonstrativo de análise financeira, classificação de despesas, comparativos 2025 × 2026 e relatórios HTML. **Todas as transações, nomes, descrições e valores neste pacote são sintéticos.**

## Conteúdo
- `Faturas_DEMO.xlsx`: estrutura ilustrativa de faturas, histórico e cadastro de categorias (432 transações fictícias).
- `despesas-casa-AAAA-MM.csv`: 24 exemplos de despesas domésticas, 12 meses de 2025 e 12 de 2026.
- `Contas_DEMO_GitHub.ipynb`: notebook independente para gerar os relatórios a partir de `dados_ficticios_2025_2026.json`.
- `build_demo.py`: gerador local dos relatórios demonstrativos.
- `relatorio_completo_2026_DEMO.html`: relatório financeiro demonstrativo.
- `relatorio_comparativo_2025_2026_DEMO.html`: relatório analítico com ranking, médias, evolução e picos por categoria, e bloco de contas da casa.

## Como executar
Execute `python build_demo.py` na pasta do projeto ou abra `Contas_DEMO_GitHub.ipynb` no Colab. Os relatórios do gerador utilizam a base JSON sintética; **a planilha e os CSVs são exemplos independentes de formato**, não são lidos automaticamente pelo gerador demonstrativo.

## Privacidade
Não publique as planilhas, os CSVs ou os notebooks de produção. Os arquivos originais enviados pelo usuário não fazem parte deste pacote. Os estabelecimentos, portadores, datas e valores dos arquivos demonstrativos foram criados artificialmente.
