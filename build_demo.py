import json, random, html, calendar
from pathlib import Path
from datetime import datetime
R=Path(__file__).parent
random.seed(2026)
months=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
groups=['Mercado','Farmácia','Combustível','Almoço SENAC','Casa','Monk / Nina','Estacionamento','Perfumaria','Seguro do carro','Vestuário','Bilhete Único','Mecânico / Carro','Táxi','Alimentação','Saúde / Dentista','Outros']
bases=[1050,370,430,310,190,210,165,130,145,170,95,280,75,350,290,180]
records=[]
for year in (2025,2026):
 for m in range(1,13):
  for g,base in zip(groups,bases):
   factor=(1.075 if year==2026 else 1)*random.uniform(.67,1.37)
   if g=='Mecânico / Carro' and m in (3,9):factor*=2.1
   if g=='Saúde / Dentista' and m in (5,11):factor*=1.6
   records.append({'ano':year,'mes':m,'categoria':g,'valor':round(base*factor,2),'origem':'Cartão'})
  for g,base in [('Aluguel',1700),('Condomínio',510),('Energia',190),('Água',85),('Internet',110)]:
   records.append({'ano':year,'mes':m,'categoria':g,'valor':round(base*(1.06 if year==2026 else 1)*random.uniform(.95,1.05),2),'origem':'Casa'})
# Demonstration-only reimbursement records: included in card total, excluded from personal ranking
for year in (2025,2026):
 for m in (4,8):
  records.append({'ano':year,'mes':m,'categoria':'VIAGEM TRABALHO REEMBOLSO','valor':round(170*random.uniform(.8,1.2),2),'origem':'Cartão'})

def money(v):return 'R$ '+f'{v:,.2f}'.replace(',','X').replace('.',',').replace('X','.')
def sumdata(year,mes=None,group=None,origin=None):return round(sum(r['valor'] for r in records if r['ano']==year and (mes is None or r['mes']==mes) and (group is None or r['categoria']==group) and (origin is None or r['origem']==origin)),2)
def esc(s):return html.escape(str(s))
css='''*{box-sizing:border-box}body{font-family:Segoe UI,Arial,sans-serif;background:#f0f2f5;color:#202b39;margin:0;padding:20px}.container{max-width:1280px;margin:auto;background:white;padding:28px;border-radius:15px;box-shadow:0 6px 26px #0001}h1{border-bottom:3px solid #2E86AB;padding-bottom:14px;font-size:27px}h2{background:#f8f9fa;border-left:4px solid #2E86AB;padding:12px;margin-top:30px;font-size:20px}h3{color:#2E86AB}table{width:100%;border-collapse:collapse;margin:12px 0 25px}th{background:#2E86AB;color:white;text-align:left}td,th{padding:10px;border-bottom:1px solid #e7ecf0}tr:nth-child(even){background:#f8fafc}.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px}.card{background:#e8f3fb;border-radius:10px;padding:16px}.card strong{display:block;font-size:23px;margin-top:6px}.muted{color:#697887;font-size:13px}.notice{background:#fff8e8;padding:13px;border-left:4px solid #e8aa30;margin:16px 0}.bar{height:13px;background:#e6edf3;border-radius:8px;overflow:hidden}.bar>span{display:block;height:100%;background:#2E86AB}.bar .peak{background:#27ae60}.rowbar{margin:13px 0}.rowhead{display:flex;justify-content:space-between;gap:12px;margin-bottom:5px}.monthly{display:grid;grid-template-columns:repeat(12,minmax(58px,1fr));gap:5px;overflow-x:auto}.monthly .m{text-align:center;font-size:11px}.monthly .m b{display:block;margin-top:3px}.monthly .m .bar{height:12px}.group{border:1px solid #e7ecf0;border-radius:10px;padding:15px;margin:15px 0}.footer{margin-top:35px;background:#f8f9fa;padding:15px;text-align:center;color:#687888;font-size:12px}@media(max-width:700px){.container{padding:14px}.monthly{grid-template-columns:repeat(6,1fr)}}'''
def shell(title):return f'<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} — Demonstração</title><style>{css}</style></head><body><main class="container"><h1>{esc(title)}</h1><div class="notice"><strong>DEMONSTRAÇÃO — DADOS 100% FICTÍCIOS.</strong> Valores e lançamentos simulados para portfólio no GitHub. Não representam despesas reais.</div>'
def end():return '<footer class="footer">Projeto demonstrativo • Dados sintéticos • 2025–2026</footer></main></body></html>'
def cards(items):return '<div class="cards">'+''.join(f'<div class="card">{esc(k)}<strong>{money(v)}</strong></div>' for k,v in items)+'</div>'
def table(headers,rows):return '<div style="overflow-x:auto"><table><thead><tr>'+''.join(f'<th>{esc(h)}</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{v}</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table></div>'

def main_report():
 y=2026;s=shell('RELATÓRIO FINANCEIRO 2026')
 s+='<p class="muted">Período: janeiro a dezembro de 2026 | Exemplo de 12 faturas mensais simuladas</p>'
 s+=cards([('Total gasto 2026',sumdata(y)),('Cartão 2026',sumdata(y,origin='Cartão')),('Despesas da casa 2026',sumdata(y,origin='Casa')),('Reembolso informativo',sumdata(y,group='VIAGEM TRABALHO REEMBOLSO'))])
 s+='<h2>RESUMO DE PARCELAS 2026</h2><p>Exemplo demonstrativo: 24 parcelas cobradas, 8 parcelas futuras. Os valores desta seção são apenas ilustrativos e não alteram os totais simulados.</p>'
 s+='<h2>GASTOS MENSAIS CONSOLIDADOS 2026</h2>'
 s+=table(['Mês','Cartão','Casa','Total'],[[months[m-1],money(sumdata(y,m,origin='Cartão')),money(sumdata(y,m,origin='Casa')),f'<b>{money(sumdata(y,m))}</b>'] for m in range(1,13)])
 s+='<h2>CATEGORIAS POR MÊS 2026</h2>'
 for m in range(1,13):
  cat=sorted([(g,sumdata(y,m,group=g)) for g in groups+['VIAGEM TRABALHO REEMBOLSO']],key=lambda x:-x[1]);s+=f'<h3>{months[m-1]}</h3>'
  s+=table(['Categoria','Valor'],[[esc(g),money(v)] for g,v in cat[:8]]+[['Outras categorias',money(sum(v for g,v in cat[8:]))]])
 s+='<h2>PARCELAS FUTURAS — EXEMPLO</h2><p class="muted">Não são incluídas novamente no total mensal; demonstração de estrutura do relatório.</p>'
 s+='<h2>INSIGHTS AUTOMÁTICOS</h2><p>Maior mês: <b>'+months[max(range(1,13),key=lambda m:sumdata(y,m))-1]+'</b>. Menor mês: <b>'+months[min(range(1,13),key=lambda m:sumdata(y,m))-1]+'</b>.</p>'
 s+='<h2>LEGENDA — ENTENDENDO OS VALORES</h2><p>Valores positivos são despesas. Reembolsos de trabalho continuam no total do cartão, mas são separados na análise de gastos pessoais. Pagamentos de fatura e estornos não foram simulados.</p>'
 return s+end()

def comparison():
 s=shell('RELATÓRIO COMPARATIVO 2025 vs 2026')
 s+=cards([('Total 2025',sumdata(2025)),('Total 2026',sumdata(2026)),('Média mensal 2025',sumdata(2025)/12),('Média mensal 2026',sumdata(2026)/12)])
 s+='<h2>COMPARATIVO MENSAL — 2025 vs 2026</h2>'
 rows=[]
 for m in range(1,13):
  a=sumdata(2025,m);b=sumdata(2026,m);d=b-a;rows.append([months[m-1],money(a),money(b),money(d),f'{100*d/a:+.1f}%' if a else '—','Realizado (simulado)'])
 s+=table(['Mês','2025','2026','Diferença','Variação','Status'],rows)
 s+='<h2>ANÁLISE DE PROJEÇÃO</h2><p>Esta demonstração apresenta 12 meses simulados em ambos os anos; não há projeções pendentes.</p>'
 s+='<h2>INSIGHTS COMPARATIVOS</h2><p>Variação anual simulada: <b>'+f'{100*(sumdata(2026)/sumdata(2025)-1):+.1f}%</b>.</p>'
 s+='<h2>ANÁLISE DAS DESPESAS ESSENCIAIS — 2026</h2><p class="muted">Ranking por total anual e média mensal. Despesas de trabalho reembolsáveis ficam fora do ranking pessoal. Contas da casa formam um bloco exclusivo.</p>'
 def group_total(g,m=None):
  if g=='Contas da casa':return round(sum(sumdata(2026,m,group=x) for x in ['Aluguel','Condomínio','Energia','Água','Internet']),2)
  return sumdata(2026,m,group=g)
 main=sorted([(g,group_total(g)) for g in groups],key=lambda x:-x[1]);mx=max(v for g,v in main)
 s+='<h3>Ranking anual e média mensal</h3>'
 for g,v in main:
  s+=f'<div class="rowbar"><div class="rowhead"><b>{esc(g)}</b><span>{money(v)} | média {money(v/12)}/mês</span></div><div class="bar"><span style="width:{100*v/mx:.1f}%"></span></div></div>'
 s+='<h3>Em que mês cada categoria teve seu maior gasto?</h3>'
 for g,v in main:
  vals=[group_total(g,m) for m in range(1,13)];peak=max(vals);peakm=months[vals.index(peak)]
  s+=f'<section class="group"><b>{esc(g)}</b> <span class="muted">— maior gasto em {peakm}: {money(peak)}</span><div class="monthly">'
  for m,val in enumerate(vals):s+=f'<div class="m">{months[m][:3]}<div class="bar"><span class="{"peak" if val==peak else ""}" style="width:{100*val/peak if peak else 0:.1f}%"></span></div><b>{money(val)}</b></div>'
  s+='</div></section>'
 s+='<h2>CONTAS DA CASA — BLOCO EXCLUSIVO</h2>'
 s+=table(['Conta','Total anual','Média mensal'],[[g,money(sumdata(2026,group=g)),money(sumdata(2026,group=g)/12)] for g in ['Aluguel','Condomínio','Energia','Água','Internet']]+[['<b>TOTAL</b>',f'<b>{money(group_total("Contas da casa"))}</b>',f'<b>{money(group_total("Contas da casa")/12)}</b>']])
 s+='<h2>LEGENDA</h2><p>Azul: gastos mensais. Verde: mês de maior gasto por categoria. Outros: categorias de menor relevância. Contas da casa são mostradas separadamente, sem duplicação no ranking principal.</p>'
 return s+end()

def generate():
 (R/'relatorio_completo_2026_DEMO.html').write_text(main_report(),encoding='utf-8')
 (R/'relatorio_comparativo_2025_2026_DEMO.html').write_text(comparison(),encoding='utf-8')
 (R/'dados_ficticios_2025_2026.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__':generate()
