
import streamlit as st
import pytube
from pytube import YouTube
import os

st.title('YOUTUBE DOWLOADER')
escolha = st.selectbox(

    'Digite o formato para baixar',

    ('MP3','MP4'))

if escolha == 'MP3':
    # URL
    url = st.text_input(str('Digite a URL'))
    yt = YouTube(url)
    
    #Extraindo audio
    video = yt.streams.filter(only_audio=True).first()

    #destino para salvar
    destino =  st.text_input(str(input('Digite o caminho para salvar')))
    
    #Baixando 
    arquivo_externo = video.download(output_path=destino)

    #Salvando
    base, ext = os.path.splitext(arquivo_externo)
    novo_arquivo = base + '.mp3'
    os.rename(arquivo_externo, novo_arquivo)

    #resultado do sucesso


elif escolha == 'MP4':
    # URL
    url = st.text_input('Digite a URL')
    yt = YouTube(str(url))
    

    #Extraindo audio
    video = yt.streams.get_highest_resolution()

    #destino para salvar
    destino =  st.text_input(str(input('Digite o caminho para salvar')))

    #Baixando 
    arquivo_externo = video.download(output_path=destino)

    #Salvando
    base, ext = os.path.splitext(arquivo_externo)
    novo_arquivo = base + '.mp4'
    os.rename(arquivo_externo, novo_arquivo)

        #resultado do sucesso