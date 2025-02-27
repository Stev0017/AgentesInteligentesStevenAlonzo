def sistema_experto():
    print("Bienvenido al sistema experto de diagnóstico básico de la universidad Mariano Galvez.")
    print("Por favor, ingresa los síntomas que estás experimentando (ingresalos por favor separados por ,):")
    
    # Solicitar síntomas al usuario
    sintomas = input("Síntomas: ").strip().lower().split(',')
    
    # Limpiar los síntomas (eliminar espacios en blanco)
    sintomas = [s.strip() for s in sintomas]
    
    # Reglas de diagnóstico
    if "fiebre" in sintomas and "tos" in sintomas and "dolor de garganta" in sintomas:
        print("--Diagnóstico: Podrías tener gripe o resfriado común.")
    elif "dolor de cabeza" in sintomas and "nauseas" in sintomas and "sensibilidad a la luz" in sintomas:
        print("--Diagnóstico: Podrías estar experimentando migraña.")
    elif "dolor en el pecho" in sintomas and "respiracion rapida" in sintomas and "sudoración" in sintomas:
        print("--Diagnóstico: Podrías estar experimentando un problema cardíaco. Busca atención médica inmediata.")
    elif "dolor abdominal" in sintomas and "nauseas" in sintomas and "vómitos" in sintomas:
        print("--Diagnóstico: Podrías tener una intoxicación alimentaria o gastritis.")
    elif "fatiga" in sintomas and "pérdida de peso" in sintomas and "aumento del apetito" in sintomas:
        print("--Diagnóstico: Podrías tener hipertiroidismo. Consulta a un médico.")
    else:
        print("--Diagnóstico: Hola en mi BD no encuentro una enfermedad asociada a tus sintomas, por favor. Consulta a un médico para una evaluacin y que te pueda recetar algun medicamento.")

# Ejecutar el sistema experto
sistema_experto()