# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from random import randint
from actions.video import get_random_video
from swiplserver import PrologMQI, PrologThread
from pathlib import Path
import os
import json



class ConsultarProlog():
    
    @staticmethod
    def consultar(consulta):
        with PrologMQI() as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query_async(r"consult('D:\\Proyectos_Programacion\\Python\\Yorobot\\actions\\prolog\\yo.pl')", find_all=False)
                consulta = prolog_thread.query(consulta)
                return consulta
            
                
class OperarArchivo():

    @staticmethod
    def guardar(AGuardar):
        with open(".\\actions\\datos","w") as archivo_descarga:
            json.dump(AGuardar, archivo_descarga, indent=4)
        archivo_descarga.close()

    @staticmethod
    def cargarArchivo(): 
        if os.path.isfile(".\\actions\\datos"):
            with open(".\\actions\\datos","r") as archivo_carga:
                retorno=json.load(archivo_carga)
                archivo_carga.close()
        else:
            retorno={}
        return retorno


class ActionQueHacias(Action):

    def name(self) -> Text:
        return "action_que_hacias"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        eleccion = randint(0, 2)
        if eleccion == 0:
            dispatcher.utter_message(text="Estaba programando en mi nuevo proyecto")
            dispatcher.utter_message(json_message={"sticker": "https://i.ibb.co/VqDfkYW/e9cfa1b5-f10c-4d99-8086-6dd71a736350.webp"})
        elif eleccion == 1:
            dispatcher.utter_message(text="Estaba haciendo un chatbot para Programacion Exploratoria sobre mi")
        elif eleccion == 2:
            info = get_random_video()
            text = f"Estaba viendo un video de mi youtuber favorito, DotCSV."
            dispatcher.utter_message(text=text)
            dispatcher.utter_message(f" El video se llama: {info['title']}.")
            dispatcher.utter_message(f" Aca te paso el link por si te interesa... {info['url']}")
        return []


class ActionGreet(Action):
    
    def name(self) -> Text:
        return "action_saludo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Veo si el numero que me hablo por telegram lo tengo agendado en mi .json
        # Si no esta agendado, le pregunto como se llama y lo agendo
        # Si esta agendado, le saludo por su nombre
        
        # Obtengo los metadatos del mensaje
        sender = tracker.latest_message["metadata"]["message"]["from"]
        contactos = OperarArchivo.cargarArchivo()
        if sender["id"] in contactos:
            # Mando mensaje y seteo el slot con el nombre del contacto
            random = randint(0, 2)
            if random == 0:
                msg = f"Hola {contactos[sender['id']]['nombre']}! Como va todo?"
            elif random == 1:
                msg = f"Como vaa {contactos[sender['id']]['nombre']}"
            elif random == 2:
                msg = f"Que onda {contactos[sender['id']]['nombre']}, como estas?"
            dispatcher.utter_message(text=msg)
            return [SlotSet("nombre",contactos[id]['nombre'])]
        else:
            dispatcher.utter_message(text="Hola! No te tengo agendado, quien sos?")
        return []

class ActionGuardarContacto(Action):
    
    def name (self) -> Text:
        return "action_guardar_contacto"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        sender = tracker.latest_message["metadata"]["message"]["from"]
        nombre = next(tracker.get_latest_entity_values("nombre"), None)
        contactos = OperarArchivo.cargarArchivo()
        contactos[sender["id"]] = {}
        contactos[sender["id"]]["nombre"] = nombre
        OperarArchivo.guardar(contactos)
        dispatcher.utter_message(text=f"Ahh si!!! Como estas {nombre}?")
        return []
    
class ActionNotBot(Action):
    
    def name(self) -> Text:
        return "action_not_bot"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        random = randint(0, 2)
        msg = f"https://github.com/igorriti/myBot/raw/main/audios/{random}.ogg"        
        dispatcher.utter_message(json_message={"voice": msg})
        return []      

class ActionLenguajes(Action):
    
    def name(self) -> Text:
        return "action_lenguajes"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #Consulta en el archivo de prolog si el lenguaje que le pasaron por la entidad es true o no
        lenguaje = tracker.get_slot("lenguaje")
        print(lenguaje)
        lenguaje = lenguaje.title()
        consulta = ConsultarProlog.consultar(f'programa("{lenguaje}").')
        
        if consulta:
            dispatcher.utter_message(text=f"Si, se programar en {lenguaje}!")
        else:
            dispatcher.utter_message(text=f"No, no se programar en {lenguaje}")

            

        return []

class ActionIntegrantes(Action):
    
    def name(self) -> Text:
        return "action_integrantes"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #Consulta en el archivo de prolog si el integrante que le pasaron por la entidad es true o no
        integrante = tracker.get_slot("nombre_grupo")
        integrante = integrante.title()

        consulta = ConsultarProlog.consultar(f'es_amigo("{integrante}").')
        
        if consulta:
            dispatcher.utter_message(text=f"Si!!! Me encantaria hacer grupo con {integrante}. Es mi amigo!")
        else:
            dispatcher.utter_message(text=f"No conozco a {integrante}. Prefiero a otra persona") 
        
        return []

            
class ActionGrupoInteres(Action):
    
    def name(self) -> Text:
        return "action_grupo_interes"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        grupo = tracker.get_slot("grupo")
        consulta = ConsultarProlog.consultar(f"grupo_de_amigos(X).")
        mes = "Me gustaria hacer grupo con "
        
        for a in consulta[0]['X']:
            if a == consulta[0]['X'][-2]:
                mes += a + " y "
            elif a == consulta[0]['X'][-1]:
                mes += a + "."
            else:
                mes += a + ", "
            
        dispatcher.utter_message(mes)
        return []
    
class ActionTodosLenguajes(Action):
    
    def name(self) -> Text:
        return "action_todos_lenguajes"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        consulta = ConsultarProlog.consultar(f"lenguajes_que_programo(X).")
        print(consulta)

        mes = "Se programar en "
        
        for a in consulta[0]['X']:
            if a == consulta[0]['X'][-2]:
                mes += a + " y "
            elif a == consulta[0]['X'][-1]:
                mes += a + "."
            else:
                mes += a + ", "

    
            
        dispatcher.utter_message(mes)
        return []
    
class ActionMateriasCursadas(Action):
    
    def name(self) -> Text:
        return "action_materias_cursadas"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        consulta = ConsultarProlog.consultar(f"materias_cursadas(X).")
        mes = "Hasta ahora curse "
        for a in consulta[0]['X']:
            if a == consulta[0]['X'][-2]:
                mes += a + " y "
            elif a == consulta[0]['X'][-1]:
                mes += a + "."
            else:
                mes += a + ", "
            
        dispatcher.utter_message(mes)
        return []

class ActionMateriasCursa(Action):

    def name(self) -> Text:
        return "action_materias_cursa"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        consulta = ConsultarProlog.consultar(f"materias_cursando(X).")
        mes = "Estoy cursando "
        dispatcher.utter_message(mes)
        
        for a in consulta[0]['X']:
            if a == consulta[0]['X'][-1]:
                dispatcher.utter_message(f"Y tambien {a}")
            else:
                dispatcher.utter_message(a)
        return []
    
class ActionFinalesPendientes(Action):
    
    def name(self) -> Text:
        return "action_finales_pendientes"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        consulta = ConsultarProlog.consultar(f"materias_finales_pendientes(X).")
        mes = "Todavia me quedan rendir un par de finales... "
        dispatcher.utter_message(mes)

            
        for a in consulta[0]['X']:
            if a == consulta[0]['X'][-1]:
                dispatcher.utter_message(f"Y {a}")
            else:
                dispatcher.utter_message(a)
            
        return []
    
class ActionMateriasCursaDia(Action):
    
    def name(self) -> Text:
        return "action_materias_cursa_dia"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dia = tracker.get_slot("dia")
        consulta = ConsultarProlog.consultar(f"materias_cursa_dia({dia},X).")
        
        
        if consulta[0]['X'] != []:
            mes = f"El {dia} curso: "
            
            for a in consulta[0]['X']:
                if len(consulta[0]['X'])>=2 and a == consulta[0]['X'][-2]:
                    mes += a + " y "
                elif a == consulta[0]['X'][-1]:
                    mes += a + "."
                else:
                    mes += a + ", "
                
        else:
            mes = f"No curso ninguna materia los {dia}"

        dispatcher.utter_message(mes)
        return []
    
class ActionHorariosMateria(Action):
    
    def name(self) -> Text:
        return "action_horarios_materias"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        materia = tracker.get_slot("materia")
        materia = materia.title()
        print(materia)
        consulta = ConsultarProlog.consultar(f'cursa_horarios("{materia}",X,Y,Z).')
        
        if consulta:
            # X = dia, Y = hora de inicio, Z = hora fin
                mes = f"Curso {materia} los {consulta[0]['X']} de {consulta[0]['Y']} a {consulta[0]['Z']}"
        else:
            mes = f"No estoy cursando {materia}"

        
        dispatcher.utter_message(mes)
        return []
          
