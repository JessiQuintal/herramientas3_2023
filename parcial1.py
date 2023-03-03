import streamlit as st
import pandas as pd
import accessApi as servicio
import json

df = pd.read_csv('Herramientas3_2023_banco.csv.csv')
listaJobs= df['job'].unique().tolist()
listaMarital= df['marital'].unique().tolist()
listaEdu= df['education'].unique().tolist()
listaHouse= df['housing'].unique().tolist()
listaLoan= df['loan'].unique().tolist()
listaContact= df['contact'].unique().tolist()
listaMonth= df['month'].unique().tolist()
listaPout= df['poutcome'].unique().tolist()
listaEmp = df['emp.var.rate'].unique().tolist()
listaConsPrice = df['cons.price.idx'].unique().tolist()
listaEmployed = df['nr.employed'].unique().tolist()

st.markdown("<h1 style='text-align: center; color: red;'>Herramientas 3</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: blue;'>Primer Parcial de Jessica Cristina Quintal Gil </h3>", unsafe_allow_html=True)
st.text('Formulario para consumir la API deployada en Microsoft Azure.')
st.write('El formulario consta de 16 campos, se deben llenar todos los campos y el resultado debe establecer si es o nó elegible para un crédito bancario')

col1, col2, col3 = st.columns(3)
with st.form("my_form", clear_on_submit=True):
   with col1:
      age= st.number_input("Edad")
      job = st.selectbox('Job:',(listaJobs))
      marital = st.selectbox('Estado civil:', (listaMarital))
      education = st.selectbox('Nivel de educación',(listaEdu))
      default= 'yes'
      housing = st.selectbox('Housing', (listaHouse))
      loan = st.selectbox('Loan',(listaLoan))
   with col2:
      contact = st.selectbox('Contact',(listaContact))
      month = st.selectbox('Month', ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
      duration = st.number_input("Duration 0-4918")
      campaign = st.number_input("Campaign 0-56")
      pdays= st.number_input("Pdays 0-999")
      previous = st.number_input("Previous 1-7")
   with col3:
      poutcome= st.selectbox('Poutcome',(listaPout))
      emp = st.slider('Emp.var.rate', min(listaEmp), max(listaEmp))
      cons_price = st.slider('Cons.price.idx', min(listaConsPrice), max(listaConsPrice))
      employed = st.slider('Nr.employed', min(listaEmployed), max(listaEmployed))

   if st.form_submit_button("Submit"):
      servicio = servicio.llamarservicio(age,job, marital, education, default, housing, loan, contact, month, duration, campaign, pdays, previous, poutcome, emp, cons_price, employed)
      resultado = json.loads(servicio.decode("utf-8"))
      arregloResultado = resultado["Results"][0]
      if arregloResultado == "yes":
         st.success('El usuario es elegible para un crédito bancario')
      else:
         st.warning('El usuario no es elegible para un crédito bancario')



