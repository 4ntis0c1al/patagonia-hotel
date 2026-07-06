# ============================================================
#  habitaciones.py
#  Módulo encargado de gestionar las habitaciones del hotel
# ============================================================

# Base de datos en memoria: lista de diccionarios
# Cada habitación tiene: número, tipo, precio por noche y estado
habitaciones = [
    {"numero": 101, "tipo": "simple",   "precio": 78.000,  "estado": "disponible"},
    {"numero": 102, "tipo": "simple",   "precio": 78.000,  "estado": "disponible"},
    {"numero": 103, "tipo": "simple",   "precio": 78.000,  "estado": "disponible"},
    {"numero": 201, "tipo": "doble",    "precio": 96.000,  "estado": "disponible"},
    {"numero": 202, "tipo": "doble",    "precio": 96.000,  "estado": "disponible"},
    {"numero": 203, "tipo": "doble",    "precio": 106.000,  "estado": "disponible"},
    {"numero": 301, "tipo": "suite",    "precio": 144.000, "estado": "disponible"},
    {"numero": 302, "tipo": "suite",    "precio": 144.000, "estado": "disponible"},
]


def buscar_habitacion(numero):
    """Devuelve el diccionario de la habitación con ese número, o None si no existe."""
    for hab in habitaciones:
        if hab["numero"] == numero:
            return hab
    return None


def listar_habitaciones():
    """Muestra todas las habitaciones con su estado actual."""
    print("\n{'='*50}")
    print(f"  {'N°':<6} {'TIPO':<10} {'PRECIO/NOCHE':<15} {'ESTADO'}")
    print(f"  {'-'*46}")
    for hab in habitaciones:
        print(f"  {hab['numero']:<6} {hab['tipo'].capitalize():<10} "
              f"${hab['precio']:<14,.0f} {hab['estado'].capitalize()}")
    print()


def listar_disponibles(tipo=None):
    """
    Muestra solo las habitaciones disponibles.
    Si se indica tipo ('simple', 'doble', 'suite'), filtra por ese tipo.
    """
    disponibles = [h for h in habitaciones if h["estado"] == "disponible"]
    if tipo:
        disponibles = [h for h in disponibles if h["tipo"] == tipo]

    if not disponibles:
        print("\n  No hay habitaciones disponibles" +
              (f" de tipo '{tipo}'." if tipo else "."))
        return

    print("\n  Habitaciones disponibles" + (f" ({tipo})" if tipo else "") + ":")
    print(f"  {'N°':<6} {'TIPO':<10} {'PRECIO/NOCHE'}")
    print(f"  {'-'*32}")
    for hab in disponibles:
        print(f"  {hab['numero']:<6} {hab['tipo'].capitalize():<10} ${hab['precio']:,.0f}")
    print()


def cambiar_estado(numero, nuevo_estado):
    """Cambia el estado de una habitación. Estados válidos: disponible / ocupada."""
    hab = buscar_habitacion(numero)
    if hab:
        hab["estado"] = nuevo_estado
        return True
    return False


def estadisticas_ocupacion():
    """Muestra un resumen de ocupación del hotel."""
    total     = len(habitaciones)
    ocupadas  = sum(1 for h in habitaciones if h["estado"] == "ocupada")
    libres    = total - ocupadas
    porcentaje = (ocupadas / total * 100) if total > 0 else 0

    print("\n  === ESTADÍSTICAS DE OCUPACIÓN ===")
    print(f"  Total de habitaciones : {total}")
    print(f"  Ocupadas              : {ocupadas}")
    print(f"  Disponibles           : {libres}")
    print(f"  Porcentaje de ocupación: {porcentaje:.1f}%")

    # Desglose por tipo
    tipos = ["simple", "doble", "suite"]
    print("\n  Desglose por tipo:")
    for t in tipos:
        tot_t = sum(1 for h in habitaciones if h["tipo"] == t)
        ocu_t = sum(1 for h in habitaciones if h["tipo"] == t and h["estado"] == "ocupada")
        print(f"    {t.capitalize():<8}: {ocu_t}/{tot_t} ocupadas")
    print()
