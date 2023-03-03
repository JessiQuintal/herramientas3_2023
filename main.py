#JESSICA CRISTINA QUINTAL GIL
#PARCIAL 1
import streamlit as st
import pandas as pd
import accessApi as servicio
import json

#Agregamos el archivo csv y agregamos cada columna a una lista
#Con unique() me aseguro que sea únicamente un elemento sin repetirse
#Más adelante utilizaré esta lista para agregar las opciones a mi formulario y no hacerlo manualmente.
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

#Título, nombre y propósito del formulario
st.markdown("<h1 style='text-align: center; color: red;'>Herramientas 3</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: blue;'>Primer Parcial de Jessica Cristina Quintal Gil </h3>", unsafe_allow_html=True)
st.text('Formulario para consumir la API deployada en Microsoft Azure.')
st.write('El formulario consta de 16 campos, se deben llenar todos los campos y el resultado debe establecer si es o nó elegible para un crédito bancario')

#Empezamos con el forms, primero lo dividi en 3 columnas para poder visualizar mejor las opciones, después creamos el forulario y a los selects les agrego la lista de la columna
#correspondiente, de igual manera, a los slides les sacó su max y mínimo para que funcione correctamente
#Los campos de número únicamente guardan el valor en la variable
col1, col2, col3= st.columns(3)
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
      pdays = st.number_input("Pdays 0-999")
      previous = st.number_input("Previous 1-7")
   with col3:
      poutcome = st.selectbox('Poutcome', (listaPout))
      emp = st.slider('Emp.var.rate', min(listaEmp), max(listaEmp))
      cons_price = st.slider('Cons.price.idx', min(listaConsPrice), max(listaConsPrice))
      employed = st.slider('Nr.employed', min(listaEmployed), max(listaEmployed))

#Agregamos el submit button para enviar nuestro formulario
#Se envía el formulario con las variables de nuestro forms y en el accessApi se agregan a la función llamar servicio
   if st.form_submit_button("Submit"):
      servicio = servicio.llamarservicio(age,job, marital, education, default, housing, loan, contact, month, duration, campaign, pdays, previous, poutcome, emp, cons_price, employed)
      #Previamente importe json porque el resultado del servicio viene dentro de un arreglo, para poder devolver un mensaje con un formato adecuado
      #obtenemos el valor correspondiente del arreglo y realizamos una válidación para mandar el mensaje correspondiente a la respuesta
      resultado = json.loads(servicio.decode("utf-8"))
      arregloResultado = resultado["Results"][0]
      if arregloResultado == "yes":
         st.success('El usuario es elegible para un crédito bancario')
      else:
         st.warning('El usuario no es elegible para un crédito bancario')

