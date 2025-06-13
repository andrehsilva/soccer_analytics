
# ⚽ Brasileirão App - Análise de Dados do Campeonato Brasileiro (2013-2023)

Este é um projeto desenvolvido em **Streamlit** que permite explorar os dados do **Campeonato Brasileiro de Futebol (Série A)** entre os anos de **2013 e 2023**. Através de uma interface interativa, você pode visualizar informações dos campeões de cada ano, desempenho dos clubes, e também baixar a base de dados utilizada.

---

## 🔥 Funcionalidades

- 🏆 **Exibição do último campeão** (2023), com:
  - Nome do time
  - Pontuação total
  - Total de vitórias
  - Total de gols marcados

- 📅 **Análise por período:**  
  Filtre os dados entre qualquer intervalo de anos de 2013 a 2023 para visualizar os campeões e suas estatísticas.

- 🔍 **Consulta personalizada:**  
  Selecione seu time do coração e veja os dados detalhados sobre sua performance no período escolhido.

- ⬇️ **Download da base de dados:**  
  Exporte o dataset completo em CSV diretamente da aplicação.

---

## 🚀 Tecnologias utilizadas

- [Streamlit](https://streamlit.io/) — para criação da interface web interativa
- [Pandas](https://pandas.pydata.org/) — manipulação e análise de dados
- [NumPy](https://numpy.org/) — suporte a operações numéricas
- [Requests](https://docs.python-requests.org/en/latest/) — (preparado para futuras integrações)

---

## 📁 Organização dos arquivos

```
.
├── app.py               # Código principal do Streamlit
├── datasets/
│   └── db.csv           # Base de dados com os resultados do Brasileirão (2013-2023)
├── README.md            # Este arquivo
```

---

## 🛠️ Como executar o projeto

### ✅ 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/brasileirao-app.git
cd brasileirao-app
```

### ✅ 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### ✅ 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### ✅ 4. Execute o app

```bash
streamlit run app.py
```

### ✅ 5. Acesse no navegador

> O Streamlit abrirá automaticamente no navegador. Caso não abra, acesse:  
> 👉 `http://localhost:8501`

---

## 📦 Requisitos

### `requirements.txt` sugerido:

```
streamlit
pandas
numpy
requests
```

---

## ✨ Melhorias futuras

- 📈 Gráficos interativos sobre desempenho dos times
- 📊 Análises de artilharia, defesa e ataque
- 🌐 Dados atualizados automaticamente via API
- 🏟️ Informações sobre estádios, técnicos e jogadores

---

## 🤘 Autor

**André Rodrigues**  
🔗 [LinkedIn](https://www.linkedin.com/in/andrehrsilva/) 
