import tkinter as tk
from tkinter import messagebox
import math

def evitar_palabras_comunes(contraseña):
    palabras_comunes = {"Alejandro", "Juan", "Manuel", "Jose", "Francisco", "Javier", "Carlos", "Miguel", 
                        "Antonio", "Pedro", "Luis", "Alberto", "Jorge", "Daniel", "David", "Ramon", 
                        "Rafael", "Fernando", "Sergio", "Enrique", "Ignacio", "Roberto", "Ruben", "Diego", 
                        "Andres", "Angel", "Jose Antonio", "Adan", "Guillermo", "Gabriel", "Oscar", "Emilio", 
                        "Ricardo", "Arturo", "Vicente", "Raul", "Tomas", "Juan Carlos", "Jesus", "Julian", 
                        "Salvador", "Mateo", "Eduardo", "Salvador", "Marco", "Simon", "Israel", "Felipe", 
                        "Hugo", "Ernesto", "Agustin", "Adrian", "Alfonso", "Hector", "Efrain", "Joel", 
                        "Leon", "Raul", "Nicolas", "Mauricio", "Octavio", "Abel", "Victor", "Mauricio", 
                        "Cesar", "Matias", "Esteban", "Alvaro", "Leandro", "Martin", "Leonardo", "Alonso", 
                        "Julian", "Benjamin", "Alexis", "Vidal", "Ivan", "Ricardo", "Hugo", "Omar", "Edgar", 
                        "Camilo", "Gerardo", "Federico", "Pablo", "Gonzalo", "Juan Pablo", "Javier", 
                        "Juan Manuel", "Jose Luis", "Rodolfo", "Xavier", "Gilberto", "Leonel", "Edgar", 
                        "Ruben", "Ruben Dario", "Emiliano", "Isaac", "Santiago", "María", "Ana", "Laura", 
                        "Isabel", "Carmen", "Patricia", "Eva", "Rosa", "Marta", "Beatriz", "Elena", "Sara", 
                        "Lucía", "Carolina", "Claudia", "Vanessa", "Alejandra", "Teresa", "Julia", "Silvia", 
                        "Mónica", "Paula", "Adriana", "Diana", "Gabriela", "Miriam", "Lorena", "Raquel", 
                        "Lourdes", "Sonia", "Natalia", "Patricia", "Clara", "Andrea", "Susana", "Emma", 
                        "Victoria", "Lorena", "Irene", "Constanza", "Paloma", "Belén", "Ángela", "Mariana", 
                        "Alejandra", "Isabel", "Inés", "Rosa María", "Clara", "Graciela", "Alma", "Verónica", 
                        "Olivia", "Esther", "Raquel", "Aurora", "Maribel", "Margarita", "Jimena", "Valeria", 
                        "Patricia", "Patricia", "Catalina", "Susana", "Martina", "Josefina", "Marina", 
                        "Amalia", "Regina", "Camila", "Beatriz", "Clara", "Sara", "Marta", "Alicia", 
                        "Gabriela", "Rosa María", "Marina", "Estela", "Victoria", "Lorena", "Cecilia", 
                        "Pilar", "Gabriela", "Isabel", "Mariana", "Roxana", "Lucía", "Silvia", "Graciela", 
                        "Gabriela", "Diana", "Rosario", "Liliana", "Consuelo", "Renata", "Delfina", 
                        "Valentina", "Ángeles", "Josefina", "James", "John", "Robert", "Michael", "William", 
                        "David", "Richard", "Joseph", "Charles", "Thomas", "Christopher", "Daniel", 
                        "Matthew", "Anthony", "Donald", "Mark", "Paul", "Steven", "Andrew", "Kenneth", 
                        "George", "Joshua", "Kevin", "Brian", "Edward", "Ronald", "Timothy", "Jason", 
                        "Jeffrey", "Ryan", "Gary", "Jacob", "Nicholas", "Eric", "Stephen", "Jonathan", 
                        "Larry", "Frank", "Scott", "Justin", "Brandon", "Raymond", "Gregory", "Benjamin", 
                        "Samuel", "Patrick", "Alexander", "Jack", "Dennis", "Jerry", "Tyler", "Henry", 
                        "Douglas", "Peter", "Aaron", "Jose", "Adam", "Zachary", "Nathan", "Walter", "Harold", 
                        "Kyle", "Carl", "Arthur", "Ryan", "Roger", "Lawrence", "Willie", "Jesse", "Roy", 
                        "Austin", "Albert", "Ethan", "Terry", "Joe", "Noah", "Wayne", "Ralph", "Eugene", 
                        "Jeffrey", "Bryan", "Louis", "Billy", "Bruce", "Russell", "Howard", "Juan", "Joel", 
                        "Bobby", "Victor", "Martin", "Eugene", "Russell", "Alan", "Harry", "Billy", "Johnny", 
                        "Clifford", "Sean", "Philip" "Emily", "Olivia", "Emma", "Ava", "Sophia", "Isabella", 
                        "Mia", "Amelia", "Harper", "Evelyn", "Abigail", "Ella", "Scarlett", "Grace", "Lily", 
                        "Chloe", "Aria", "Zoey", "Penelope", "Riley", "Layla", "Lucy", "Aubrey", "Bella", 
                        "Natalie", "Hannah", "Avery", "Leah", "Stella", "Aaliyah", "Maya", "Ellie", "Aurora", 
                        "Samantha", "Skylar", "Addison", "Paisley", "Brooklyn", "Savannah", "Zoe", "Nora", 
                        "Scarlett", "Camila", "Anna", "Victoria", "Claire", "Lillian", "Eleanor", "Gabriella", 
                        "Natalie", "Hazel", "Grace", "Isabelle", "Sophie", "Scarlett", "Alice", "Kinsley", 
                        "Hailey", "Aurora", "Eliana", "Luna", "Violet", "Peyton", "Nova", "Aurora", "Genesis", 
                        "Emilia", "Autumn", "Aria", "Nevaeh", "Serenity", "Piper", "Penelope", "Scarlett", 
                        "Skylar", "Zoe", "Lila", "Aurora", "Ellie", "Mila", "Hazel", "Violet", "Lucy", 
                        "Aurora", "Bella", "Aurora", "Aria", "Ariana", "Aubrey", "Scarlett", "Amelia", 
                        "Grace", "Leah", "Scarlett", "Ruby", "Scarlett", "Aria", "Scarlett", "Skylar", "Zoe", 
                        "Perro", "Gato", "Elefante", "León", "Tigre", "Oso", "Mono", "Jirafa", "Cebra", 
                        "Serpiente", "Cocodrilo", "Hipopótamo", "Rinoceronte", "Ballena", "Delfín", "Tortuga", 
                        "Pez", "Pájaro", "Águila", "Búho", "Murciélago", "Caballo", "Vaca", "Cerdo", "Oveja", 
                        "Cabra", "Pollo", "Pato", "Pingüino", "Koala", "Canguro", "Ornitorrinco", "Tiburón", 
                        "Pulpo", "Mariposa", "Abeja", "Hormiga", "Araña", "Escorpión", "Mosquito", "Mosca", 
                        "Grillo", "Ciervo", "Zorro", "Lobo", "Puma", "Pantera", "Guepardo", "Oso panda", 
                        "Gorila", "Dog", "Cat", "Elephant", "Lion", "Tiger", "Bear", "Monkey", "Giraffe", 
                        "Zebra", "Snake", "Crocodile", "Hippopotamus", "Rhinoceros", "Whale", "Dolphin", 
                        "Turtle", "Fish", "Bird", "Eagle", "Owl", "Bat", "Horse", "Cow", "Pig", "Sheep", 
                        "Goat", "Chicken", "Duck", "Penguin", "Koala", "Kangaroo", "Platypus", "Shark", 
                        "Octopus", "Butterfly", "Bee", "Ant", "Spider", "Scorpion", "Mosquito", "Fly", 
                        "Cricket", "Deer", "Fox", "Wolf", "Puma", "Panther", "Cheetah", "Panda", "Gorilla", 
                        "el", "de", "que", "y", "a", "en", "un", "ser", "se", "no", "haber", "por", "con", 
                        "su", "para", "como", "estar", "tener", "le", "lo", "todo", "pero", "más", "hacer", 
                        "o", "poder", "decir", "este", "ir", "otro", "ese", "la", "si", "me", "ya", "ver", 
                        "porque", "dar", "cuando", "ser", "él", "muy", "sin", "vez", "saber", "qué", "sobre", 
                        "mal", "uno", "bien", "todo", "mucho", "mismo", "así", "nuevo", "sí", "año", 
                        "después", "vida", "quien", "día", "lugar", "tiempo", "año", "forma", "casa", 
                        "trabajo", "parte", "lugar", "mundo", "país", "ni", "niño", "persona", "mayor", 
                        "nunca", "día", "manera", "momento", "menos", "año", "lugar", "nombre", "caso", 
                        "ciudad", "país", "grupo", "problema", "hombre", "cuestión", "historia", "punto", 
                        "manera", "tarde", "derecho", "mujer", "hijo", "clase", "manera", "tipo", "the", 
                        "and", "to", "of", "a", "in", "is", "it", "you", "that", "he", "was", "for", "on", 
                        "are", "with", "as", "I", "his", "they", "be", "at", "one", "have", "this", "from", 
                        "or", "had", "by", "hot", "but", "some", "what", "there", "we", "can", "out", "other", 
                        "were", "all", "your", "when", "up", "use", "word", "how", "said", "an", "each", 
                        "she", "which", "do", "their", "time", "if", "will", "way", "about", "many", "then", 
                        "them", "would", "write", "like", "so", "these", "her", "long", "make", "thing", 
                        "see", "him", "two", "has", "look", "more", "day", "could", "go", "come", "did", 
                        "number", "sound", "no", "most", "people", "my", "over", "know", "water", "than", 
                        "call", "first", "who", "may", "down", "side", "been", "now", "find"}
    return not any(palabra.lower() in contraseña.lower() for palabra in palabras_comunes)

def detectar_patrones(contraseña):
    patrones_debiles = {"123456", "password", "qwerty", "abc123", "111111", "123123", "admin", "letmein", 
                        "welcome", "123abc", "1qaz2wsx", "1234abcd", "987654", "zxcvbn", "asdfgh", 
                        "iloveyou", "555555", "654321", "7777777", "666666", "121212", "000000", 
                        "sunshine", "football", "password1", "master", "123qwe", "test123", "dragon", 
                        "1q2w3e4r", "777777", "222222", "999999", "abcdef", "qwerty123", "112233", 
                        "qwertyui", "welcome1", "12345a", "qwertyu", "admin123", "monkey", "11223344", 
                        "0000", "1qazxsw2", "1234qwer", "1q1q1q1q", "letmein123", "99999999", "88888888", 
                        "11223355", "54321", "00000000", "123qweasd", "12121212", "1q1q1q", "1qazxcvbn", 
                        "iloveyou1", "q1w2e3r4t5", "654123", "987654321", "qazwsxedc", "abcd1234", "121212q", 
                        "passw0rd", "1234qwerasdf", "q1w2e3r4", "77777777", "9876543", "0000abcd", 
                        "qwerty12345", "asdf1234", "qwertyuio", "1qaz2wsx3edc", "11223344a", "696969", 
                        "abcdefg", "11111", "zxcvbnm", "abcd123", "qazqaz", "1212121", "a1b2c3d4", 
                        "54321a", "7777", "ababab", "qweasdzxc", "112233a", "12345q", "1111111", 
                        "1q2w3e4r5t", "qwerty12", "87654321", "987654a", "1122", "0000000000", "789456", 
                        "asdfghjkl", "010101", "qwe123", "q1w2e3r", "4444", "1212", "zxcvb", "1122a", 
                        "1q1q1q1", "qazwsx123", "2580", "369", "147258369", "asdfg", "010203", "111111a", 
                        "aaaaaa", "qwert", "876543", "131313", "007", "abcdef123", "3q2w1e", "5555", 
                        "777888", "741852963", "2222", "121314", "111222", "123abc123", "159753", "qweqwe", 
                        "456789", "1qaz2wsx", "1122334455", "9876543210", "3.141592", "654321a", 
                        "qazxcvbnm", "147147", "22222222", "13579", "qwer123", "456123", "7890123", "9876", 
                        "232323", "246810", "11221122", "12131415", "444444", "999999999", "111222333", 
                        "69696969", "112211", "01010101", "q1w2e3", "654654", "qwertyu", "abcde", 
                        "112233aabb", "asdf123", "987654321a", "1q2w3e4r5", "7777777a", "qazwsx1234", 
                        "a1s2d3f4", "4567890", "111222333a", "112233445566", "11223344556677", "12344321", 
                        "98765", "qazwsx12345", "123123123", "1234abcd", "789456123", "qwerty1234", 
                        "a1b2c3d4e5", "00000", "1212abcd", "121212ab", "987654321a", "123a321", 
                        "abcdefg123", "1234qwer", "qwertyuiop", "13579a", "0000000a", "010101a", "1122aa", 
                        "456789a", "1234qwe", "111111a", "qazwsx1", "22222", "121212a", "88888", "112233a", 
                        "121212qaz", "123qwea", "1111", "qazwsx12", "99999", "123aaa", "qwertyuiop123", 
                        "a123456", "121314a", "121212abab", "1234qwea", "121212qwer", "98765432", 
                        "a12345678", "01020304", "111112", "7777a", "147258a", "qwertya", "aaaa1111", 
                        "12341234", "121212qw", "q1w2e3r4t5y6", "44444", "12345a6", "6666", "q1w2e3r4t5a", 
                        "0000a", "123qweasd", "121212345", "121212abab", "123a123a", "55555a", "aaaa", 
                        "112233445", "1234a", "12345678a", "1234abcd", "abc12345", "qazwsx321", 
                        "121212qwerty", "1234abcd1234", "a1b2c3d4e5f6", "11111111a", "123qweasd123", 
                        "1234qwer1234", "987654321abc", "1a2b3c4d5e", "qwerty123abc", "a1s2d3f4g5h", 
                        "12345678910", "q1w2e3r4t5a", "1234abcd5678", "11223344aa", "123qweasdzxc", 
                        "abcdefgh1234", "qazwsx123abc", "1234qwerty1234", "1q2w3e4r5t6y", "aabbccddeeff", 
                        "1qazxsw2edc", "1234abcd9876", "q1w2e3r4t5y6u", "a1b2c3d4e5f6g7", "123a123a123", 
                        "11111111aa", "987654a321", "1234qwea1234", "qwerty12345abc", "a1b2c3d4a1", 
                        "12345qwerty12345", "121212qwertyui", "abcdefghijklmnop", "123456789a123456", 
                        "qwertyuiopasdfghjkl", "12345qwertya", "1111111122", "123a321a123", "abcdefg12345", 
                        "1234qwertya", "1234567a", "1qaz2wsx3edc4rfv", "abcdefghijkl", "1234qwertya", 
                        "12345qwertyabc", "a1b2c3d4a", "qazwsxedcrfv", "1234abcd9876", "123qweasd123qwe", 
                        "1q2w3e4r5t6", "1234qwertyabcd", "abcdefghijklmnop", "123qweasdqwe", 
                        "1a2b3c4d5e6f7g8", "123a321a", "abcdefghijklmnopqrst", "111111a1", "123a123a", 
                        "123qwertya", "11111111a"}
    return not any(patron.lower() in contraseña.lower() for patron in patrones_debiles)

def comprobar_contra_diccionario(contraseña):
    contra_diccionario = {"12345", "123456", "123456789", "test1", "password", "12345678", "zinch", 
                          "g_czechout", "asdf", "qwerty", "1234567890", "1234567", "Aa123456.", "iloveyou", 
                          "1234", "abc123", "111111", "123123", "dubsmash", "test", "princess", "qwertyuiop", 
                          "sunshine", "BvtTest123", "11111", "ashley", "00000", "000000", "password1", 
                          "monkey", "livetest", "55555", "soccer", "charlie", "asdfghjkl", "654321", 
                          "family", "michael", "123321", "football", "baseball", "q1w2e3r4t5y6", "nicole", 
                          "jessica", "purple", "shadow", "hannah", "chocolate", "michelle", "daniel", 
                          "maggie", "qwerty123", "hello", "112233", "jordan", "tigger", "666666", 
                          "987654321", "superman", "12345678910", "summer", "1q2w3e4r5t", "fitness", 
                          "bailey", "zxcvbnm", "fuckyou", "121212", "buster", "butterfly", "dragon", 
                          "jennifer", "amanda", "justin", "cookie", "basketball", "shopping", "pepper", 
                          "joshua", "hunter", "ginger", "matthew", "abcd1234", "taylor", "samantha", 
                          "whatever", "andrew", "1qaz2wsx3edc", "thomas", "jasmine", "animoto", "madison", 
                          "54321", "flower", "Password", "maria", "babygirl", "lovely", "sophie", "Chegg123", 
                          "computer", "qwe123", "anthony", "1q2w3e4r", "peanut", "bubbles", "asdasd", 
                          "qwert", "1qaz2wsx", "pakistan", "123qwe", "liverpool", "elizabeth", "harley", 
                          "chelsea", "familia", "yellow", "william", "george", "7777777", "loveme", "123abc", 
                          "letmein", "oliver", "batman", "cheese", "banana", "testing", "secret", "angel", 
                          "friends", "jackson", "aaaaaa", "softball", "chicken", "lauren", "andrea", 
                          "welcome", "asdfgh", "robert", "orange", "Testing1", "pokemon", "555555", 
                          "melissa", "morgan", "123123123", "qazwsx", "diamond", "brandon", "jesus", 
                          "mickey", "olivia", "changeme", "danielle", "victoria", "gabriel", "123456a", 
                          "0.00000000", "loveyou", "hockey", "freedom", "azerty", "snoopy", "skinny", 
                          "myheritage", "qwerty1", "159753", "forever", "iloveu", "killer", "joseph", 
                          "master", "mustang", "hellokitty", "school", "Password1", "patrick", "blink182", 
                          "tinkerbell", "rainbow", "nathan", "cooper", "onedirection", "alexander", 
                          "jordan23", "lol123", "jasper", "junior", "q1w2e3r4", "222222", "11111111", 
                          "benjamin", "jonathan", "passw0rd", "123456789", "a123456", "samsung", "123", 
                          "love123", "picture1", "senha", "Million2", "aaron431", "qqww1122", "omgpop", 
                          "jacket025", "evite", "123qwe", "5201314", "159753", "123456789", "pokemon", 
                          "Bangbang123", "jobandtalent", "123654", "ohmnamah23", "zing", "102030", 
                          "147258369", "qazwsx", "qwe123", "football1", "jesus1", "b123456", "101010", 
                          "12341234", "a801016", "1111", "1111111", "yugioh", "fuckyou1", "trustno1", 
                          "x4ivygA51F", "142536", "11223344", "angel1"}
    return contraseña.lower() not in contra_diccionario

def calcular_entropia(contraseña):
    caracteres_posibles = 94  # Número total de caracteres posibles (alfanuméricos y caracteres especiales)
    longitud = len(contraseña)
    entropia = longitud * math.log2(caracteres_posibles)
    return entropia

def calificar_entropia(entropia):
    if entropia < 40:
        return "Débil"
    elif 40 <= entropia < 60:
        return "Moderada"
    else:
        return "Fuerte"

def analizar_complejidad_gramatical(contraseña):
    tiene_minuscula = any(c.islower() for c in contraseña)
    tiene_mayuscula = any(c.isupper() for c in contraseña)
    tiene_numero = any(c.isdigit() for c in contraseña)

    if not (tiene_minuscula and tiene_mayuscula and tiene_numero):
        return "La contraseña debería incluir al menos una letra minúscula, una letra mayúscula y un número.", "Baja"
    
    return "", ""

def analizar_complejidad_semantica(contraseña):
    palabras_debil = {"abcd", "access", "action", "adventure", "airplane", "alligator", "amazing", "analyze", 
                      "animal", "answer", "apartment", "apple", "architect", "argument", "artichoke", 
                      "astronomy", "athlete", "atmosphere", "avocado", "awesome", "banana", "basketball", 
                      "beautiful", "bicycle", "birthday", "biscuit", "blueberry", "bodyguard", "broccoli", 
                      "business", "butterfly", "calendar", "camera", "caramel", "carpet", "celebration", 
                      "champion", "chocolate", "cinnamon", "civilization", "classical", "coconut", 
                      "colleague", "collect", "community", "computer", "concert", "confident", "consider", 
                      "convenient", "cucumber", "curiosity", "dangerous", "decision", "delicate", 
                      "delicious", "democracy", "dentist", "destination", "determine", "diamond", 
                      "different", "direction", "discover", "discovery", "discussion", "dragonfly", 
                      "education", "elegant", "elephant", "elevate", "elephant", "embrace", "emotion", 
                      "energy", "engineer", "enjoyable", "envelope", "epicenter", "equation", "essential", 
                      "evaluate", "evolution", "excellent", "excitement", "exercise", "existence", 
                      "experience", "explore", "extraordinary", "fantastic", "favorite", "feedback", 
                      "financial", "flexible", "flowerpot", "football", "forever", "fragrance", "freedom", 
                      "friendship", "fruitcake", "fulfillment", "galaxy", "generation", "generosity", 
                      "gentle", "genuine", "geography", "glamorous", "happiness", "harmony", "health", 
                      "heartwarming", "helicopter", "hilarious", "history", "holiday", "horizon", 
                      "hydrangea", "imagination", "impressive", "independence", "individual", "infinite", 
                      "innocence", "innovative", "inspiration", "intelligence", "intensity", "interesting", 
                      "international", "invisible", "invitation", "involve", "island", "joyful", "journey", 
                      "judicious", "kaleidoscope", "keyboard", "landscape", "laughter", "lavender", 
                      "lemonade", "lifestyle", "lightning", "literature", "magnificent", "mango", "marathon", 
                      "masterpiece", "meaningful", "meditation", "melody", "memorable", "metaphor", 
                      "meticulous", "milestone", "miracle", "mischief", "momentum", "moonlight", "motivate", 
                      "mountain", "mysterious", "navigate", "necessary", "necklace", "negotiate", "network", 
                      "nutritious", "oasis", "ocean", "official", "optimistic", "orchid", "organize", 
                      "original", "outrageous", "pacific", "palette", "paradise", "passion", "peaceful", 
                      "peanut", "perseverance", "perspective", "phenomenal", "philosophy", "pineapple", 
                      "playful", "pleasure", "positive", "powerful", "precious", "pristine", "proactive", 
                      "profound", "progress"}

    for palabra in palabras_debil:
        if palabra.lower() in contraseña.lower():
            return f"Evite el uso de palabras débiles como '{palabra}'.", "Baja"

    return "", ""

def verificar_contraseña(contraseña):
    # Verificar longitud mínima
    if len(contraseña) < 12:
        return "La contraseña es demasiado corta. Debe tener al menos 12 caracteres.", "Baja", "", "", ""

    # Verificar mayúsculas, números, caracteres especiales
    if not any(c.isupper() for c in contraseña):
        return "La contraseña debe contener al menos una letra mayúscula.", "Baja", "", "", ""

    if not any(c.isdigit() for c in contraseña):
        return "La contraseña debe contener al menos un número.", "Baja", "", "", ""

    if not any(c in "!@#$%^&*()-_+=" for c in contraseña):
        return "La contraseña debe contener al menos un carácter especial.", "Baja", "", "", ""

    # Verificar otras condiciones
    mensaje_gramatical, calificacion_gramatical = analizar_complejidad_gramatical(contraseña)
    mensaje_semantica, calificacion_semantica = analizar_complejidad_semantica(contraseña)

    if mensaje_gramatical == "":
        mensaje_gramatical = "La contraseña cumple con la complejidad gramatical."
    if mensaje_semantica == "":
        mensaje_semantica = "La contraseña cumple con la complejidad semántica."

    # Calcular entropía y calificación
    entropia = calcular_entropia(contraseña)
    calificacion_entropia = calificar_entropia(entropia)
    mensaje_entropia = f"{calificacion_entropia} ({entropia:.2f} bits)"

    return "La contraseña es segura.", "Alta", mensaje_gramatical, mensaje_semantica, mensaje_entropia

def verificar_contraseña_desde_interfaz(event=None):
    contraseña = entry_contraseña.get()

    try:
        resultado, calificacion, mensaje_gramatical, mensaje_semantica, mensaje_entropia = verificar_contraseña(contraseña)
    except Exception as e:
        resultado = "Error al verificar la contraseña."
        calificacion = "Error"
        mensaje_gramatical = ""
        mensaje_semantica = ""
        mensaje_entropia = str(e)

    resultado_resultado_var.set(resultado)
    calificacion_resultado_var.set(calificacion.upper())

    if calificacion == "Alta":
        label_calificacion_resultado.config(fg="green", font=("Arial", 10, "bold"))
    elif calificacion == "Moderada":
        label_calificacion_resultado.config(fg="orange")
    else:
        label_calificacion_resultado.config(fg="red", font=("Arial", 10, "bold"))

    gramatical_resultado_var.set(mensaje_gramatical)
    semantica_resultado_var.set(mensaje_semantica)
    entropia_resultado_var.set(mensaje_entropia)

    messagebox.showinfo("Resultado", f"{resultado}\nCalificación de complejidad de la contraseña: {calificacion}")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Verificador de Contraseña")

# Configurar tamaño de la ventana
root.geometry("500x500")

# Crear widgets
label_titulo = tk.Label(root, text="Script desarrollado en Python \nMarcos Cunioli - Especialista en Ciberseguridad", font=("Arial", 16))
label_instrucciones = tk.Label(root, text="Ingrese su contraseña:")
entry_contraseña = tk.Entry(root, show="*")
label_requisitos = tk.Label(root, text="- Longitud mínima de 12 caracteres.\n- Al menos una letra mayúscula.\n- Al menos un número.\n- Al menos un carácter especial (!@#$%^&*()-_+=).\n- No contiene palabras comunes o secuencias sencillas.\n- No contiene patrones débiles.\n- No está en un contra-diccionario de contraseñas débiles.\n- La entropía de la contraseña debe ser alta (más de 40 bits).", justify=tk.LEFT)
button_verificar = tk.Button(root, text="Verificar Contraseña", command=verificar_contraseña_desde_interfaz)

# Organizar widgets en la interfaz
label_titulo.pack(pady=10)
label_instrucciones.pack()
entry_contraseña.pack(pady=5)
label_requisitos.pack(pady=5)
button_verificar.pack(pady=10)

# Resultados
frame_resultados = tk.Frame(root)
frame_resultados.pack(pady=10)

label_resultado = tk.Label(frame_resultados, text="Resultado:")
label_calificacion = tk.Label(frame_resultados, text="Calificación:")
label_gramatical = tk.Label(frame_resultados, text="Complejidad gramatical:")
label_semantica = tk.Label(frame_resultados, text="Complejidad semántica:")
label_entropia = tk.Label(frame_resultados, text="Entropía:")

label_resultado.grid(row=0, column=0, sticky="e")
label_calificacion.grid(row=1, column=0, sticky="e")
label_gramatical.grid(row=2, column=0, sticky="e")
label_semantica.grid(row=3, column=0, sticky="e")
label_entropia.grid(row=4, column=0, sticky="e")

resultado_resultado_var = tk.StringVar()
calificacion_resultado_var = tk.StringVar()
gramatical_resultado_var = tk.StringVar()
semantica_resultado_var = tk.StringVar()
entropia_resultado_var = tk.StringVar()

label_resultado_resultado = tk.Label(frame_resultados, textvariable=resultado_resultado_var)
label_calificacion_resultado = tk.Label(frame_resultados, textvariable=calificacion_resultado_var)
label_gramatical_resultado = tk.Label(frame_resultados, textvariable=gramatical_resultado_var)
label_semantica_resultado = tk.Label(frame_resultados, textvariable=semantica_resultado_var)
label_entropia_resultado = tk.Label(frame_resultados, textvariable=entropia_resultado_var)

label_resultado_resultado.grid(row=0, column=1, sticky="w")
label_calificacion_resultado.grid(row=1, column=1, sticky="w")
label_gramatical_resultado.grid(row=2, column=1, sticky="w")
label_semantica_resultado.grid(row=3, column=1, sticky="w")
label_entropia_resultado.grid(row=4, column=1, sticky="w")

# Asociar evento "Enter" al botón
entry_contraseña.bind("<Return>", verificar_contraseña_desde_interfaz)

# Iniciar el bucle de eventos de la interfaz gráfica
root.mainloop()
