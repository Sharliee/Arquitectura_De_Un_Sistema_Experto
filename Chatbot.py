import sqlite3

# Función para crear la tabla si no existe
def crear_tabla():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS respuestas (pregunta TEXT PRIMARY KEY, respuesta TEXT)")
    conn.commit()
    conn.close()

# Función para obtener una respuesta de la base de datos
def obtener_respuesta(pregunta):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT respuesta FROM respuestas WHERE pregunta=?", (pregunta,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else None

# Función para agregar una nueva respuesta a la base de datos
def agregar_respuesta(pregunta, respuesta):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO respuestas (pregunta, respuesta) VALUES (?, ?)", (pregunta, respuesta))
    conn.commit()
    conn.close()

# Función principal del chat
def chat():
    crear_tabla()
    print("¡Hola! Soy un chatbot. Puedes escribir 'Salir' en cualquier momento para terminar la conversación.")
    print(" ")
    while True:
        entrada = input("Usuario: ")
        if entrada.lower() == "salir":
            print(" ")
            print("Chatbot: Hasta luego. ¡Adiós!")
            print(" ")
            break
        respuesta = obtener_respuesta(entrada.lower())
        if respuesta is not None:
            print("Chatbot:", respuesta)
        else:
            print(" ")
            print("Lo siento, no tengo una respuesta predefinida para esa pregunta.")
            nueva_respuesta = input("Por favor, ingresa una respuesta para esta pregunta: ")
            agregar_respuesta(entrada.lower(), nueva_respuesta)
            print(" ")
            print("Chatbot: Gracias por agregar nuevo conocimiento a la base de datos.")
            print(" ")

# Iniciar el chat
if __name__ == "__main__":
    chat()
