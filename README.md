# 📉 Análise Histórica da COVID-19 no Brasil

Este projeto realiza uma análise da evolução da pandemia de COVID-19 no Brasil com base nos dados do [Our World in Data (OWID)](https://ourworldindata.org/covid-cases). Os dados estão disponíveis até **agosto de 2024**, e foram utilizados para gerar gráficos claros e informativos, ideais para portfólios de ciência de dados.

---

## 📊 Gráficos gerados

Os arquivos são salvos na pasta `imgs/`:

- **Casos acumulados e mortes acumuladas**
- **Novos casos diários**
- **Novas mortes diárias**
- **Total de vacinas aplicadas**

---

## 🛠️ Como executar localmente

1. Baixe o arquivo de dados manualmente:

🔗 https://covid.ourworldindata.org/data/owid-covid-data.csv

Salve como:
```
owid-covid-data.csv
```

2. Instale os pacotes:

```bash
pip install pandas matplotlib
```
3. Execute o script:
```bash
python covid_historico.py
```

As imagens serão salvas em imgs/.

##**🧪 Dataset**
Fonte: OWID - COVID-19

País: Brasil

Última data do dataset: 2024-08-04

Dados incluem casos, mortes e vacinação.

✍️ Autor
- *Criado por Yuri Abuchaim · [rilufi.github.io](https://rilufi.github.io)*
- *Contato · 📧 [yuri.abuchaim@gmail.com](mailto:yuri.abuchaim@gmail.com)*

📌 Projeto complementar com dados atualizados automaticamente:
👉 github.com/rilufi/pythovid
