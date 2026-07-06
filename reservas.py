# ============================================================
#  reservas.py
#  Módulo encargado de gestionar reservas, check-in y check-out
# ============================================================

import habitaciones as hab_mod
import huespedes   as hue_mod

# Base de datos en memoria: lista de reservas activas y finalizadas
reservas = []

# Contador de reservas
_ultimo_id_reserva = 0


def _generar_id_reserva():
    global _ultimo_id_reserva
    _ultimo_id_reserva += 1
    return _ultimo_id_reserva


# ── VALIDACIONES ────────────────────────────────────────────

def _validar_fecha(texto_fecha):
    """
    Valida que la fecha tenga formato DD/MM/AAAA.
    Devuelve True si es válida, False si no.
    """
    partes = texto_fecha.strip().split("/")
    if len(partes) != 3:
        return False
    dia, mes, anio = partes
    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
        return False
    dia, mes, anio = int(dia), int(mes), int(anio)
    if not (1 <= dia <= 31 and 1 <= mes <= 12 and anio >= 2024):
        return False
    return True


def _calcular_noches(fecha_entrada, fecha_salida):
    """
    Calcula la cantidad de noches entre dos fechas DD/MM/AAAA.
    Devuelve un entero >= 1, o None si las fechas son inválidas.
    """
    def a_dias(f):
        d, m, a = [int(x) for x in f.split("/")]
        # Conversión simple a días totales (aproximación para el trabajo)
        return a * 365 + m * 30 + d

    noches = a_dias(fecha_salida) - a_dias(fecha_entrada)
    if noches < 1:
        return None
    return noches


# ── CHECK-IN ────────────────────────────────────────────────

def hacer_checkin(dni_huesped, numero_hab, fecha_entrada, fecha_salida):
    """
    Realiza el check-in de un huésped en una habitación.
    - Verifica que el huésped exista.
    - Verifica que la habitación esté disponible.
    - Valida las fechas.
    - Registra la reserva y cambia el estado de la habitación.
    """
    # 1. Buscar huésped
    huesped = hue_mod.buscar_por_dni(dni_huesped)
    if huesped is None:
        print("\n  ✘ No se encontró ningún huésped con ese DNI.")
        print("    Registre al huésped primero (opción 1 del menú).")
        return

    # 2. Buscar habitación
    habitacion = hab_mod.buscar_habitacion(numero_hab)
    if habitacion is None:
        print(f"\n  ✘ No existe la habitación N°{numero_hab}.")
        return

    if habitacion["estado"] != "disponible":
        print(f"\n  ✘ La habitación N°{numero_hab} ya está ocupada.")
        return

    # 3. Validar fechas
    if not _validar_fecha(fecha_entrada):
        print("\n  ✘ Fecha de entrada inválida. Use el formato DD/MM/AAAA.")
        return
    if not _validar_fecha(fecha_salida):
        print("\n  ✘ Fecha de salida inválida. Use el formato DD/MM/AAAA.")
        return

    noches = _calcular_noches(fecha_entrada, fecha_salida)
    if noches is None:
        print("\n  ✘ La fecha de salida debe ser posterior a la de entrada.")
        return

    # 4. Calcular costo total
    costo_total = noches * habitacion["precio"]

    # 5. Registrar reserva
    nueva_reserva = {
        "id":            _generar_id_reserva(),
        "huesped_id":    huesped["id"],
        "huesped_nombre": f"{huesped['nombre']} {huesped['apellido']}",
        "habitacion":    numero_hab,
        "tipo_hab":      habitacion["tipo"],
        "fecha_entrada": fecha_entrada.strip(),
        "fecha_salida":  fecha_salida.strip(),
        "noches":        noches,
        "precio_noche":  habitacion["precio"],
        "costo_total":   costo_total,
        "estado":        "activa",
    }
    reservas.append(nueva_reserva)

    # 6. Cambiar estado de la habitación
    hab_mod.cambiar_estado(numero_hab, "ocupada")

    # 7. Confirmar al usuario
    print("\n  ✔ CHECK-IN REALIZADO EXITOSAMENTE")
    print(f"  Reserva N°   : {nueva_reserva['id']}")
    print(f"  Huésped      : {nueva_reserva['huesped_nombre']}")
    print(f"  Habitación   : {numero_hab} ({habitacion['tipo'].capitalize()})")
    print(f"  Entrada      : {fecha_entrada}")
    print(f"  Salida       : {fecha_salida}")
    print(f"  Noches       : {noches}")
    print(f"  Precio/noche : ${habitacion['precio']:,.0f}")
    print(f"  TOTAL        : ${costo_total:,.0f}")
    print()


# ── CHECK-OUT ───────────────────────────────────────────────

def hacer_checkout(numero_hab):
    """
    Realiza el check-out de la habitación indicada.
    Muestra el resumen de la estadía y libera la habitación.
    """
    # Buscar reserva activa de esa habitación
    reserva = None
    for r in reservas:
        if r["habitacion"] == numero_hab and r["estado"] == "activa":
            reserva = r
            break

    if reserva is None:
        print(f"\n  ✘ No hay una reserva activa en la habitación N°{numero_hab}.")
        return

    # Finalizar reserva
    reserva["estado"] = "finalizada"
    hab_mod.cambiar_estado(numero_hab, "disponible")

    print("\n  ✔ CHECK-OUT REALIZADO EXITOSAMENTE")
    print(f"  Reserva N°   : {reserva['id']}")
    print(f"  Huésped      : {reserva['huesped_nombre']}")
    print(f"  Habitación   : {numero_hab} ({reserva['tipo_hab'].capitalize()})")
    print(f"  Entrada      : {reserva['fecha_entrada']}")
    print(f"  Salida       : {reserva['fecha_salida']}")
    print(f"  Noches       : {reserva['noches']}")
    print(f"  TOTAL COBRADO: ${reserva['costo_total']:,.0f}")
    print()


# ── LISTADOS ────────────────────────────────────────────────

def listar_reservas_activas():
    """Muestra todas las reservas con estado 'activa'."""
    activas = [r for r in reservas if r["estado"] == "activa"]
    if not activas:
        print("\n  No hay reservas activas en este momento.")
        return

    print(f"\n  {'N°':<5} {'HUÉSPED':<22} {'HAB':<5} {'ENTRADA':<12} {'SALIDA':<12} {'TOTAL'}")
    print(f"  {'-'*65}")
    for r in activas:
        print(f"  {r['id']:<5} {r['huesped_nombre']:<22} {r['habitacion']:<5} "
              f"{r['fecha_entrada']:<12} {r['fecha_salida']:<12} ${r['costo_total']:,.0f}")
    print()


def listar_historial():
    """Muestra todas las reservas (activas y finalizadas)."""
    if not reservas:
        print("\n  No hay reservas registradas.")
        return

    print(f"\n  {'N°':<5} {'HUÉSPED':<22} {'HAB':<5} {'ENTRADA':<12} {'SALIDA':<12} {'ESTADO':<12} {'TOTAL'}")
    print(f"  {'-'*80}")
    for r in reservas:
        print(f"  {r['id']:<5} {r['huesped_nombre']:<22} {r['habitacion']:<5} "
              f"{r['fecha_entrada']:<12} {r['fecha_salida']:<12} "
              f"{r['estado'].capitalize():<12} ${r['costo_total']:,.0f}")
    print()


def estadisticas_ingresos():
    """Muestra ingresos totales y por tipo de habitación."""
    finalizadas = [r for r in reservas if r["estado"] == "finalizada"]
    if not finalizadas:
        print("\n  Aún no hay reservas finalizadas para calcular ingresos.")
        return

    total_ingresos  = sum(r["costo_total"] for r in finalizadas)
    total_noches    = sum(r["noches"] for r in finalizadas)
    total_reservas  = len(finalizadas)

    print("\n  === ESTADÍSTICAS DE INGRESOS ===")
    print(f"  Reservas finalizadas : {total_reservas}")
    print(f"  Noches totales       : {total_noches}")
    print(f"  Ingresos totales     : ${total_ingresos:,.0f}")

    tipos = ["simple", "doble", "suite"]
    print("\n  Ingresos por tipo de habitación:")
    for t in tipos:
        ing_t = sum(r["costo_total"] for r in finalizadas if r["tipo_hab"] == t)
        res_t = sum(1 for r in finalizadas if r["tipo_hab"] == t)
        print(f"    {t.capitalize():<8}: ${ing_t:>10,.0f}  ({res_t} reservas)")
    print()
