# ============================================================
#  huespedes.py
#  Módulo encargado de gestionar el registro de huéspedes
# ============================================================

# Base de datos en memoria: lista de diccionarios
huespedes = []

# Contador para generar IDs únicos automáticamente
_ultimo_id = 0


def _generar_id():
    """Genera un ID único correlativo para cada huésped."""
    global _ultimo_id
    _ultimo_id += 1
    return _ultimo_id


def registrar_huesped(nombre, apellido, dni, telefono):
    """
    Registra un nuevo huésped y lo agrega a la lista.
    Devuelve el diccionario del huésped creado.
    """
    nuevo = {
        "id":       _generar_id(),
        "nombre":   nombre.strip().title(),
        "apellido": apellido.strip().title(),
        "dni":      dni.strip(),
        "telefono": telefono.strip(),
    }
    huespedes.append(nuevo)
    print(f"\n  ✔ Huésped registrado con ID #{nuevo['id']}: "
          f"{nuevo['nombre']} {nuevo['apellido']}")
    return nuevo


def buscar_por_dni(dni):
    """Devuelve el huésped con ese DNI, o None si no existe."""
    for h in huespedes:
        if h["dni"] == dni.strip():
            return h
    return None


def buscar_por_id(id_huesped):
    """Devuelve el huésped con ese ID, o None si no existe."""
    for h in huespedes:
        if h["id"] == id_huesped:
            return h
    return None


def listar_huespedes():
    """Muestra todos los huéspedes registrados."""
    if not huespedes:
        print("\n  No hay huéspedes registrados.")
        return

    print(f"\n  {'ID':<5} {'APELLIDO':<15} {'NOMBRE':<15} {'DNI':<12} {'TELÉFONO'}")
    print(f"  {'-'*58}")
    for h in huespedes:
        print(f"  {h['id']:<5} {h['apellido']:<15} {h['nombre']:<15} "
              f"{h['dni']:<12} {h['telefono']}")
    print()
