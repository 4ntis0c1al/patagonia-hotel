# ============================================================
#  validaciones.py
#  Funciones reutilizables para validar entradas del usuario
# ============================================================


def pedir_entero(mensaje, minimo=None, maximo=None):
    """
    Solicita un número entero al usuario.
    Repite hasta obtener un valor válido dentro del rango indicado.
    """
    while True:
        entrada = input(mensaje).strip()
        if not entrada.isdigit():
            print("  ✘ Ingrese un número entero válido.")
            continue
        valor = int(entrada)
        if minimo is not None and valor < minimo:
            print(f"  ✘ El valor mínimo permitido es {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"  ✘ El valor máximo permitido es {maximo}.")
            continue
        return valor


def pedir_texto(mensaje, min_largo=2, max_largo=50):
    """
    Solicita un texto no vacío al usuario.
    Repite hasta obtener uno dentro de los límites de longitud.
    """
    while True:
        entrada = input(mensaje).strip()
        if len(entrada) < min_largo:
            print(f"  ✘ El texto debe tener al menos {min_largo} caracteres.")
            continue
        if len(entrada) > max_largo:
            print(f"  ✘ El texto no puede superar los {max_largo} caracteres.")
            continue
        return entrada


def pedir_dni():
    """Solicita y valida un DNI (solo dígitos, entre 7 y 8 caracteres)."""
    while True:
        dni = input("  DNI (sin puntos)      : ").strip()
        if not dni.isdigit():
            print("  ✘ El DNI debe contener solo números.")
            continue
        if not (7 <= len(dni) <= 8):
            print("  ✘ El DNI debe tener 7 u 8 dígitos.")
            continue
        return dni


def pedir_telefono():
    """Solicita y valida un teléfono (solo dígitos, entre 8 y 15 caracteres)."""
    while True:
        tel = input("  Teléfono              : ").strip()
        if not tel.isdigit():
            print("  ✘ El teléfono debe contener solo números.")
            continue
        if not (8 <= len(tel) <= 15):
            print("  ✘ Ingrese un teléfono entre 8 y 15 dígitos.")
            continue
        return tel


def pedir_fecha(mensaje):
    """
    Solicita una fecha con formato DD/MM/AAAA.
    Valida formato básico y rango de valores.
    """
    while True:
        fecha = input(mensaje).strip()
        partes = fecha.split("/")
        if len(partes) != 3:
            print("  ✘ Use el formato DD/MM/AAAA (ej: 15/07/2025).")
            continue
        dia, mes, anio = partes
        if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
            print("  ✘ La fecha debe contener solo números y '/'.")
            continue
        dia, mes, anio = int(dia), int(mes), int(anio)
        if not (1 <= dia <= 31):
            print("  ✘ El día debe estar entre 1 y 31.")
            continue
        if not (1 <= mes <= 12):
            print("  ✘ El mes debe estar entre 1 y 12.")
            continue
        if anio < 2024:
            print("  ✘ El año debe ser 2024 o posterior.")
            continue
        return fecha


def pedir_tipo_habitacion():
    """Solicita y valida el tipo de habitación."""
    tipos_validos = ["simple", "doble", "suite"]
    while True:
        tipo = input("  Tipo (simple/doble/suite): ").strip().lower()
        if tipo in tipos_validos:
            return tipo
        print(f"  ✘ Tipo inválido. Opciones: {', '.join(tipos_validos)}.")


def confirmar(mensaje):
    """Pide confirmación S/N. Devuelve True si el usuario confirma."""
    while True:
        resp = input(f"  {mensaje} (S/N): ").strip().upper()
        if resp == "S":
            return True
        if resp == "N":
            return False
        print("  ✘ Ingrese S para sí o N para no.")
