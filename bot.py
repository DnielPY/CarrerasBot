#   IMPORTACIONES
from telegram import (
    Poll,
    ParseMode,
    KeyboardButton,
    KeyboardButtonPollType,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
    update,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    PollAnswerHandler,
    PollHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    ConversationHandler,
)

from telegram.ext import MessageHandler, Filters

from io import open
import datetime

import threading

import time

#   TOKEN
updater = Updater(token='2061858626:AAEycOS042ydCsUvtXEPYYror_7zYg8-8LY')

#   DISTPATCHER
dispatcher = updater.dispatcher

#   LOGGIN
import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)


#   Contadores
mylista = []

mensajes = []

indiceList = []

indicReal = []


print("++ Bot ejecutado con exito ++" + str(datetime.datetime.now()) + "\n")



def info(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="⚙️ Bienvenido a Boletas Bot ⚙️ \n\nLa herramienta para ayudarte a llenar tu Boleta de Pre Universitario \n\n¿Para qué sirve? \nEste bot te ayudará a tener una idea de que carreras puedes elegir cuando termines 12 grado tomando como referencia una supuesta nota final brindada por ti\n\n¿Cómo funciona?\nBasta con presionar en el botón /start y a continuación escribir tu supuesto índice, luego el bot te preguntará que rama de carreras te gustan y listo! \n\n¿Qué pasa si aún no tengo mi Índice General? \nEs muy probable que si usas este bot aún estés en el pre y no tengas tú índice final. No importa, de eso se trata, de que pruebes varias veces con los posibles índices para ver que carrera podrías elegir \n\n++ IMPORTANTE ++ \n1 - Este bot NO constituye una herramienta oficial del MINED, por lo que no se debería tomar como la única alternativa para investigar acerca de las Carreras y sus cortes. \n2 - Los cortes de las carreras fueron tomados del curso 2019 - 2020 en la provincia La Habana. \n\n\nDesarrollado por @NoSoyDniel \n\nVersion 4.0") 
    context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

info_handler = CommandHandler('info', info)
dispatcher.add_handler(info_handler)


#   START
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="⚙️ Bienvenido a Boletas Bot ⚙️\n\n/info - Leer Tutorial \n\n🖇 Escribe tu indice utilizando puntos en vez de comas (ej 97.82): 🖇") 
    
    us = f'{update.effective_user.first_name}'
    oa = f'{update.effective_user.username}'
    mylista.append(1)
    c = mylista.count(1)
    b = datetime.datetime.now()
    abrir = open("RegistroConexiones.txt", "a")
    esc = "\n \nNueva Conexion Registrada \n" + "Usuario: " + str(us) + " -- " + (oa) + "\nConexion Numero " + str(c) + "\n\n"
    abrir.write(esc)
    abrir.close()
    print(esc)

    var1 = f'{update.effective_user.username}'
    var2 = str(var1)
    print(str(var2))

    #print(str(update))
    context.bot.send_message(chat_id= 740635631, text=str(esc)) 
        

    ad = update.message.text
    mensajes.append(str(ad))
    #print(str(mensajes))

    #time.sleep(5)

    indice(update, context)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


#   CienciasTecnicas
def CienciasTecnicas(update, context):

    titulo = "🧑🏼‍💻 CIENCIAS TÉCNICAS 🧑🏼‍💻"

    texto=update.message.text

    carreras=["Ing Bioinformática ", "TS en Explotacion y Mantenimiento del Transporte Automotor", "Ing Metalurgia y Materiales ", "Ing Geología ", "Ing Eléctrica ", "Ing Geofísica ", "Ing Ciberseguridad ", "Ing Mecánica ", "Ing Ciencias Informáticas UCI ", "Ing Hidráulica ", "Ing Informática CUJAE ", "Ing Biomédica ", "Ing Química ", "Ing Automática ", "Ing Civil ", "Ing Industrial ", "Ing Telecomunicaciones y Electrónica ", "Diseño De Comunicacion Visual", "Arquitectura y Urbanismo", "Diseño Insdrustrial"]
    notas=[73.54, 74.17, 75.41, 77.34, 77.57, 77.75, 78.96, 83.42, 83.84, 84.6, 89.2, 90.07, 90.45, 90.61, 93.14, 93.28, 93.72, 95.44, 96.36, 96.55]

    calcIndice = indicReal[-1]     

    indicefinal = float(calcIndice)

    if indicefinal < 73.54:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, necesitas al menos 73.54 de Indice General para optar por una carrera de esta rama") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 100:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, el Indice solo puede ser de 100 puntos como máximo") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 73.54:
        listaX = []

        i=0
        for item in notas:
            i+=1
            if item < indicefinal:  

                listaX.append(str(notas[i-1]) + " - " + carreras[i-1])

        if indicefinal > 73.54:         
            b = listaX[0]
        if indicefinal > 74.17:
            b = listaX[0] + " \n" + listaX[1]
        if indicefinal > 75.41:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2]
        if indicefinal > 77.34:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] 
        if indicefinal > 77.57:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4]       
        if indicefinal > 77.75:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5]
        if indicefinal > 78.96:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6]
        if indicefinal > 83.42:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7]
        if indicefinal > 83.84:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8]
        if indicefinal > 84.6:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9]
        if indicefinal > 89.2:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] 
        if indicefinal > 90.07:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] 
        if indicefinal > 90.45:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] + " \n" + listaX[12]  
        if indicefinal > 90.61:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] + " \n" + listaX[12] + " \n" + listaX[13] 
        if indicefinal > 93.14:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] + " \n" + listaX[12] + " \n" + listaX[13] + " \n" + listaX[14] 
        if indicefinal > 93.28:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] + " \n" + listaX[12] + " \n" + listaX[13] + " \n" + listaX[14] + " \n" + listaX[15] 
        if indicefinal > 93.72:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] + " \n" + listaX[12] + " \n" + listaX[13] + " \n" + listaX[14] + " \n" + listaX[15] + " \n" + listaX[16]  
        if indicefinal > 95.44:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] + " \n" + listaX[12] + " \n" + listaX[13] + " \n" + listaX[14] + " \n" + listaX[15] + " \n" + listaX[16] + " \n" + listaX[17]   
        if indicefinal > 96.36:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] + " \n" + listaX[12] + " \n" + listaX[13] + " \n" + listaX[14] + " \n" + listaX[15] + " \n" + listaX[16] + " \n" + listaX[17] + " \n" + listaX[18]  
        if indicefinal > 96.55:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] + " \n" + listaX[12] + " \n" + listaX[13] + " \n" + listaX[14] + " \n" + listaX[15] + " \n" + listaX[16] + " \n" + listaX[17] + " \n" + listaX[18] + " \n" + listaX[19] 

           
            
        textFinal = titulo + "\n\n" + str(b)

        context.bot.send_message(chat_id=update.effective_chat.id, text= textFinal) 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

CienciasTecnicas_handler = CommandHandler('Tecnicas', CienciasTecnicas)
dispatcher.add_handler(CienciasTecnicas_handler) 


#   CienciasNaturales
def CienciasNaturales(update, context):

    titulo = "👩🏼‍🔬 CIENCIAS NATURALES 👩🏼‍🔬"

    texto=update.message.text

    carreras=["Lic Fisica ", "Lic Matematicas ", "Ing Instalaciones Nucleares y Energia ", "Lic Geografia ", "Lic Quimica ", "Lic Radioquimica ", "Lic Ciencias Farmaceuticas ", "Lic Ciencias de la Computacion ", "Lic Ciencias Alimentarias ", "Lic Biologia ", "Lic Meteorologia ", "Lic Microbiologia ", "Lic Fisica Nuclear Aplicada ", "Lic Bioquimica y Biologia Molecular "]
    notas=[71.61, 79.31, 81.22, 82.1, 83.01, 83.3, 83.65, 84.79, 87.64, 90.48, 92.7, 93.18, 93.22, 95.16]
   
    calcIndice = indicReal[-1]

    indicefinal = float(calcIndice)

    if indicefinal < 71.61:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, necesitas al menos 71.61 de Indice General para optar por una carrera de esta rama") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 100:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, el Indice solo puede ser de 100 puntos como máximo") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 71.61:
        listaX = []

        i=0
        for item in notas:
            i+=1
            if item < indicefinal:  

                listaX.append(str(notas[i-1]) + " - " + carreras[i-1])

        if indicefinal > 71.61:         
            b = listaX[0]
        if indicefinal > 79.31:
            b = listaX[0] + " \n" + listaX[1]
        if indicefinal > 81.22:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2]
        if indicefinal > 82.1:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] 
        if indicefinal > 83.01:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4]       
        if indicefinal > 83.3:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5]
        if indicefinal > 83.65:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6]
        if indicefinal > 84.79:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7]
        if indicefinal > 87.64:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8]
        if indicefinal > 90.48:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9]
        if indicefinal > 92.7:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] 
        if indicefinal > 93.18:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] 
        if indicefinal > 93.22:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] + " \n" + listaX[12]  
        if indicefinal > 95.16:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] + " \n" + listaX[12] + " \n" + listaX[13]    
            
        textFinal = titulo + "\n\n" + str(b)

        context.bot.send_message(chat_id=update.effective_chat.id, text= textFinal) 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 


CienciasNaturales_handler = CommandHandler('Naturales', CienciasNaturales)
dispatcher.add_handler(CienciasNaturales_handler)


#   CienciasSociales
def CienciasSociales(update, context):

    titulo = "🧑🏻‍⚖️ CIENCIAS SOCIALES 🧑🏻‍⚖️"
    texto=update.message.text

    carreras=["Lic Filosofia ", "Lic Historia ", "Lic en Ciencias De La Informacion ", "Letras ", "Sociologia ", "Lic Historia del Arte ", "Lic Derecho ", "Lic Lengua Rusa ", "Lic Psicologia ", "Lic Lengua Francesa ", "Lic Lengua Alemana ", "Lic Comunicacion Social ", "Lic Lengua Inglesa "]
    notas=[79.76, 85.44, 88.95, 89.06, 91.77, 92.14, 92.7, 94.74, 94.81, 95.39, 95.51, 95.7, 96.52]

    calcIndice = indicReal[-1]

    indicefinal = float(calcIndice)

    if indicefinal < 79.76:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, necesitas al menos 79.76 de Indice General para optar por una carrera de esta rama") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 100:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, el Indice solo puede ser de 100 puntos como máximo") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 79.76:
        listaX = []

        i=0
        for item in notas:
            i+=1
            if item < indicefinal:  

               listaX.append(str(notas[i-1]) + " - " + carreras[i-1])        

        if indicefinal > 79.76:
            b = listaX[0]
        if indicefinal > 85.44:
            b = listaX[0] + " \n" + listaX[1]
        if indicefinal > 88.95:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] 
        if indicefinal > 89.06:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3]        
        if indicefinal > 91.77:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4]
        if indicefinal > 92.14:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] 
        if indicefinal > 92.7:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] 
        if indicefinal > 94.74:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7]
        if indicefinal > 94.81:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] 
        if indicefinal > 95.39:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9]
        if indicefinal > 95.51:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] 
        if indicefinal > 95.7:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] 
        if indicefinal > 96.52:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] + " \n" + listaX[12] 
           
            
        textFinal = titulo + "\n\n" + str(b)

        context.bot.send_message(chat_id=update.effective_chat.id, text= textFinal) 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 


CienciasSociales_handler = CommandHandler('Sociales', CienciasSociales)
dispatcher.add_handler(CienciasSociales_handler)


#   CienciasMedicas
def CienciasMedicas(update, context):

    titulo = "🧑🏾‍⚕️ CIENCIAS MÉDICAS 🧑🏾‍⚕️"
    texto=update.message.text

    carreras=["Dr Medicina ", "Lic Bioanalisis Clinico ", "Ts Electromedicina ", "Ts Nutricion y Dietetica ", "Ts Radiologia ", "Lic Igiene y Epidemiologia ", "Ts Analisis Clinico y Medicina Transfuncional ", "Lic Enfermeria ", "Lic Logofonoaudiologia ", "TS Neurofisiologia Clinica ", "Lic Sistema de Informacion de la Salud ", "Ts Protesis Estomatologoca ", "Lic Imageonologia y Radiofisica Medica ", "Lic Nutricion ", "Lic Estomatologia "]
    notas=[69.29, 70.89, 71.69, 73.73, 74.31, 75.61,  75.75, 75.87, 77.11, 77.14, 77.67, 81.07, 83.73, 85.48, 94.94]
    
    calcIndice = indicReal[-1]

    indicefinal = float(calcIndice)

    if indicefinal < 69.29:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, necesitas al menos 69.29 de Indice General para optar por una carrera de esta rama") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 100:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, el Indice solo puede ser de 100 puntos como máximo") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 69.29:
        listaX = []

        i=0
        for item in notas:
            i+=1
            if item < indicefinal:  

               listaX.append(str(notas[i-1]) + " - " + carreras[i-1])

        if indicefinal > 69.29:
            b = listaX[0]
        if indicefinal > 70.89:
            b = listaX[0] + " \n" + listaX[1]
        if indicefinal > 71.69:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] 
        if indicefinal > 73.73:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3]        
        if indicefinal > 74.31:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4]
        if indicefinal > 75.61:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] 
        if indicefinal > 75.75:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] 
        if indicefinal > 75.87:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7]
        if indicefinal > 77.11:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] 
        if indicefinal > 77.14:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9]
        if indicefinal > 77.67:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] 
        if indicefinal > 81.07:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] 
        if indicefinal > 83.73:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] + " \n" + listaX[12] 
        if indicefinal > 85.48:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] + " \n" + listaX[12] + " \n" + listaX[13] 
        if indicefinal > 94.94:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10] + " \n" + listaX[11] + " \n" + listaX[12] + " \n" + listaX[13] + " \n" + listaX[14]    
            
        textFinal = titulo + "\n\n" + str(b)

        context.bot.send_message(chat_id=update.effective_chat.id, text= textFinal) 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 


CienciasMedicas_handler = CommandHandler('Medicas', CienciasMedicas)
dispatcher.add_handler(CienciasMedicas_handler)


#   CienciasCulturaFisica
def CienciasCulturaFisica(update, context):

    titulo = "🏀 CULTURA FÍSICA 🏀"
    texto=update.message.text

    carreras=["Lic Cultura Fisica ", "T.S Entrenador Deportivo "]
    notas=[70.54, 87.95]

    calcIndice = indicReal[-1]

    indicefinal = float(calcIndice)

    if indicefinal < 70.54:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, necesitas al menos 70.54 de Indice General para optar por una carrera de esta rama") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 100:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, el Indice solo puede ser de 100 puntos como máximo") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 70.54:
        listaX = []

        i=0
        for item in notas:
            i+=1
            if item < indicefinal:  

                listaX.append(str(notas[i-1]) + " - " + carreras[i-1])

        if indicefinal > 70.54:
            b = listaX[0]
        if indicefinal > 87.95:
            b = listaX[0] + " \n" + listaX[1]
             
        textFinal = titulo + "\n\n" + str(b)

        context.bot.send_message(chat_id=update.effective_chat.id, text= textFinal) 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 


CienciasCulturaFisica_handler = CommandHandler('CFisica', CienciasCulturaFisica)
dispatcher.add_handler(CienciasCulturaFisica_handler)


#   CienciasAgropecuarias
def CienciasAgropecuarias(update, context):

    titulo = "👩🏻‍🌾 CIENCIAS AGROPECUARIAS 👩🏻‍🌾"
    texto=update.message.text

    carreras=[ "Ing Agricola ", "Ing Agronomia ", "Ing Forestal ", "Dr Medicina Veternaria y Zootecnia ",]
    notas=[74.11, 75.38, 82.76, 84.93]

    calcIndice = indicReal[-1]

    indicefinal = float(calcIndice)

    if indicefinal < 74.11:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, necesitas al menos 74.11 de Indice General para optar por una carrera de esta rama") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 100:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, el Indice solo puede ser de 100 puntos como máximo") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 74.11:
        listaX = []

        i=0
        for item in notas:
            i+=1
            if item < indicefinal:  

                listaX.append(str(notas[i-1]) + " - " + carreras[i-1])

        if indicefinal > 74.11:
            b = listaX[0]
        if indicefinal > 75.38:
            b = listaX[0] + " \n" + listaX[1]
        if indicefinal > 82.76:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] 
        if indicefinal > 84.93:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3]        

             
        textFinal = titulo + "\n\n" + str(b)

        context.bot.send_message(chat_id=update.effective_chat.id, text= textFinal) 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 


CienciasAgropecuarias_handler = CommandHandler('Agropecuarias', CienciasAgropecuarias)
dispatcher.add_handler(CienciasAgropecuarias_handler)


#   CienciasPedagogicas
def CienciasPedagogicas(update, context):

    titulo = "🧑🏼‍🏫 CIENCIAS PEDAGÓGICAS 🧑🏼‍🏫"
    texto=update.message.text

    carreras=["Lic Artistica ", "Lic Educ Marxismo Leninismo e Historia ", "Lic Educ Matematica ", "Lic Educ Españo Literatura ", "Lic Educ Pedagogía-Psicología ", "Lic Educ Economía ", "Lic Educ Logopedia ", "Lic Educ Especial ", "Lic Educ Len Extrangera ", "Lic Educ Biología ", "Lic Educ Química "] 
    notas=[75.72, 77.21, 78.81, 79.06, 79.42, 79.71, 80.7, 80.85, 81.37, 82.97, 85.26]
        
    calcIndice = indicReal[-1]

    indicefinal = float(calcIndice)

    if indicefinal < 75.72:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, necesitas al menos 75.72 de Indice General para optar por una carrera de esta rama") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 100:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, el Indice solo puede ser de 100 puntos como máximo") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 75.72:
        listaX = []

        #texta = " "

        i=0
        for item in notas:
            i+=1
            if item < indicefinal:  

                listaX.append(str(notas[i-1]) + " - " + carreras[i-1])

        if indicefinal > 75.22:         
            b = listaX[0]
        if indicefinal > 77.21:
            b = listaX[0] + " \n" + listaX[1]
        if indicefinal > 78.81:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2]
        if indicefinal > 79.06:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] 
        if indicefinal > 79.71:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4]       
        if indicefinal > 80.7:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5]
        if indicefinal > 80.85:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6]
        if indicefinal > 81.37:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7]
        if indicefinal > 82.97:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8]
        if indicefinal > 85.26:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6] + " \n" + listaX[7] + " \n" + listaX[8] + " \n" + listaX[9] + " \n" + listaX[10]
    
        textFinal = titulo + "\n\n" + str(b)

        context.bot.send_message(chat_id=update.effective_chat.id, text= textFinal) 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio")


CienciasPedagogicas_handler = CommandHandler('Pedagogicas', CienciasPedagogicas)
dispatcher.add_handler(CienciasPedagogicas_handler)


#   CienciasEconomicas
def CienciasEconomicas(update, context):

    titulo = "👨🏽‍💼 CIENCIAS ECONÓMICAS 👨🏽‍💼"
    texto=update.message.text

    carreras=["TS en Logística ", "TS en Auditoria ", "TS Comercio Sostenible ", "TS Asistencia Turístca ", "Lic Contabilidad y Finanzas ", "Lic Economia ", "Lic Turismo " ]
    notas=[74.32, 75.15, 75.8, 84.32, 85.53, 89.32, 96.89]
           
    calcIndice = indicReal[-1]

    indicefinal = float(calcIndice)

    if indicefinal < 74.32:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, necesitas al menos 74.32 de Indice General para optar por una carrera de esta rama") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 100:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, el Indice solo puede ser de 100 puntos como máximo") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 74.32:
        listaX = []

        i=0
        for item in notas:
            i+=1
            if item < indicefinal:  

                listaX.append(str(notas[i-1]) + " - " + carreras[i-1])

        if indicefinal > 74.32:         
            b = listaX[0]
        if indicefinal > 75.15:
            b = listaX[0] + " \n" + listaX[1]
        if indicefinal > 75.8:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2]
        if indicefinal > 84.32:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] 
        if indicefinal > 85.53:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4]       
        if indicefinal > 89.32:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5]
        if indicefinal > 96.89:
            b = listaX[0] + " \n" + listaX[1] + " \n" + listaX[2] + " \n" + listaX[3] + " \n" + listaX[4] + " \n" + listaX[5] + " \n" + listaX[6]

        textFinal = titulo + "\n\n" + str(b)

        context.bot.send_message(chat_id=update.effective_chat.id, text= textFinal) 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 


CienciasEconomicas_handler = CommandHandler('Economicas', CienciasEconomicas)
dispatcher.add_handler(CienciasEconomicas_handler)


#   Cadetes
def Cadetes(update, context):

    titulo = "👩🏼‍🚀 CADETES MININT 👩🏼‍🚀"
    texto=update.message.text

    carreras=["Carrera Cadetes Minit"]
    notas=[79.18]  

    calcIndice = indicReal[-1]

    indicefinal = float(calcIndice)

    if indicefinal < 79.18:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, necesitas al menos 79.18 de Indice General para optar por una carrera de esta rama") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 100:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo sentimos, el Indice solo puede ser de 100 puntos como máximo") 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    if indicefinal > 79.18:
        listaX = []

        i=0
        for item in notas:
            i+=1
            if item < indicefinal:  

                listaX.append(str(notas[i-1]) + " - " + carreras[i-1])

        if indicefinal > 79.18:         
            b = listaX[0]
       
        textFinal = titulo + "\n\n" + str(b)

        context.bot.send_message(chat_id=update.effective_chat.id, text= textFinal) 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 


Cadetes_handler = CommandHandler('Cadetes', Cadetes)
dispatcher.add_handler(Cadetes_handler)



#   RAMAS
def ramas(update, context):
    try:
        calcIndice = int(indicReal[-1])  
    except ValueError:
        print(" ")  
    try:
        if calcIndice > 60:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Seleccione la rama de carreras de su preferencia: \n\n/Tecnicas - C. Tecnicas 🧑🏼‍💻 \n/Naturales - C. Naturales 👩🏼‍🔬 \n/Sociales - C. Sociales 🧑🏻‍⚖️ \n/Medicas - C. Médicas 🧑🏾‍⚕️\n/CFisica - C. Cultura Física 🏀\n/Agropecuarias - C. Agropecuarias 👩🏻‍🌾\n/Pedagogicas - C. Pedagógicas 🧑🏼‍🏫\n/Economicas - C. Economicas 👨🏽‍💼\n/Cadetes - Cadetes MININT 👩🏼‍🚀") 
        if calcIndice < 60:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Necesitas un Indice General superior a 60 para poder optar por una Carrera Universitaria") 
            context.bot.send_message(chat_id=update.effective_chat.id, text="Presione /start para volver a inicio") 

    except UnboundLocalError:
        print(" ") 


ramas_handler = CommandHandler('ramas', ramas)
dispatcher.add_handler(ramas_handler) 



#   INDICE
def indice(update, context):
    i = 0
    texto = update.message.text

    if 1 or 2 or 3 in texto:
        indiceList.append(texto)
        #print(str(indiceList))
    try:
        if indiceList[1]:
            pasadera = float(indiceList[-1])
            indicReal.append(pasadera)
            #   Esta es la linea que tengo que repetir a la ora de calcular las carreras    
            indiceParaCalculos = indicReal[-1]
            #print("El indice es de " + str(indiceParaCalculos))

            ramas(update, context)
            #CienciasTecnicas(update, context)
    except IndexError:
        print(" ")

indiceNaturales_handler = MessageHandler(Filters.text, indice)
dispatcher.add_handler(indiceNaturales_handler)



#   RUN-BOT
if __name__ == '__main__':


    updater.start_polling()        
    updater.idle()
