# Importamos las librerías necesarias
import pandas as pd
import plotly.express as px
import streamlit as st

# Cargamos el DataSet del cual vamos obtener la información
df = pd.read_csv('vehicles_us.csv')

# Encabezado
st.markdown("#<h1 style='text-align: center; color: white;'>Bienvenido a un vistazo al carrazo...🚗</h1>", unsafe_allow_html=True)

st.markdown("<p style='font-size:18px; color:gray;'>Aquí podrás ver una mestra de lo que se puede hacer con Python y la librería de Streamlit</p>", unsafe_allow_html=True)

st.markdown("📊 **Analiza los datos de manera interactiva**")

# Botón Histograma
hist_button = st.button('Histograma')

if hist_button:
    #Mensaje
    st.write('Creación de un histograma para el conjunto de datos de precios de venta de coches')
    
    #Crea el histograma
    hist_fig = px.histogram(df, x="price", title='Histograma del precio de los vehículos en cartera') # crear un histograma
    
    #Mostrar Gráfico interactivo
    st.plotly_chart(hist_fig, use_container_width=True)
    
# Boton dispersión
disp_button = st.button('Dispersión')

if disp_button:
    #Mensaje
    st.write('Creación de una gráfica de disperción para el conjunto de datos de precios de venta de coches')
    
    # crear un gráfico de dispersión
    disp_fig = px.scatter(df, x="model_year", y="price", title='Disperción del modelo de los coches en cartera') 
    
    #Mostrar Gráfico interactivo
    st.plotly_chart(disp_fig, use_container_width=True)

# Agrupamos los tipos de autos
all_type = df['type'].unique() 
selected_type = st.multiselect("Selecciona los típos de autos que quieres analizar:", all_type)

# Boton dispersión
bar_button = st.button('Barras')

if bar_button:
    # Filtramos los típos de autos
    filtered_df = df[df['type'].isin(selected_type)]
    type_counts = filtered_df['condition'].value_counts().reset_index(name='count')

    # Gráfico de barras
    fig = px.bar(type_counts, x='condition', y='count',
                    title=f"Condición de autos para tipos seleccionados: {', '.join(selected_type)}",
                    labels={'condition': 'Condición del auto', 'count': 'Cantidad'},
                    color='condition')
    st.plotly_chart(fig, use_container_width=True)
    
# Texto normal con estilo en negritas o cursivas
st.markdown("**Realizado por**   _Aldo Ca_")
