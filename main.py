# ============================================================
#  main.py
#  Punto de entrada del sistema de Gestión de Hotel
#  Ejecutar con: python main.py
# ============================================================

import habitaciones as hab_mod
import huespedes   as hue_mod
import reservas    as res_mod
import validaciones as val

NOMBRE_HOTEL = "Patagonia Hotel"
SEPARADOR    = "=" * 52


def encabezado():
    """Imprime el encabezado del sistema."""
    print(f"\n{SEPARADOR}")
    print(f"   🏨  {NOMBRE_HOTEL}  —  Sistema de Gestión")
    print(SEPARADOR)


def menu_principal():
    """Muestra el menú principal y devuelve la opción elegida."""
    print("\n  ── MENÚ PRINCIPAL ──────────────────────────")
    print("  1. Gestión de Huéspedes")
    print("  2. Gestión de Habitaciones")
    print("  3. Check-in")
    print("  4. Check-out")
    print("  5. Reservas activas")
    print("  6. Historial de reservas")
    print("  7. Estadísticas")
    print("  0. Salir")
    print("  ─────────────────────────────────────────────")
    return val.pedir_entero("  Opción: ", minimo=0, maximo=7)


# ── SUBMENÚ: HUÉSPEDES ──────────────────────────────────────

def menu_huespedes():
    while True:
        print("\n  ── HUÉSPEDES ───────────────────────────────")
        print("  1. Registrar nuevo huésped")
        print("  2. Buscar huésped por DNI")
        print("  3. Listar todos los huéspedes")
        print("  0. Volver al menú principal")
        print("  ─────────────────────────────────────────────")
        opcion = val.pedir_entero("  Opción: ", minimo=0, maximo=3)

        if opcion == 1:
            print("\n  -- REGISTRAR HUÉSPED --")
            nombre   = val.pedir_texto("  Nombre                : ")
            apellido = val.pedir_texto("  Apellido              : ")
            dni      = val.pedir_dni()

            # Verificar que no exista ya ese DNI
            if hue_mod.buscar_por_dni(dni):
                print("  ✘ Ya existe un huésped registrado con ese DNI.")
            else:
                telefono = val.pedir_telefono()
                hue_mod.registrar_huesped(nombre, apellido, dni, telefono)

        elif opcion == 2:
            print("\n  -- BUSCAR HUÉSPED --")
            dni = val.pedir_dni()
            h = hue_mod.buscar_por_dni(dni)
            if h:
                print(f"\n  ✔ Huésped encontrado:")
                print(f"    ID       : {h['id']}")
                print(f"    Nombre   : {h['nombre']} {h['apellido']}")
                print(f"    DNI      : {h['dni']}")
                print(f"    Teléfono : {h['telefono']}")
            else:
                print("  ✘ No se encontró ningún huésped con ese DNI.")

        elif opcion == 3:
            hue_mod.listar_huespedes()

        elif opcion == 0:
            break


# ── SUBMENÚ: HABITACIONES ───────────────────────────────────

def menu_habitaciones():
    while True:
        print("\n  ── HABITACIONES ────────────────────────────")
        print("  1. Ver todas las habitaciones")
        print("  2. Ver solo las disponibles")
        print("  3. Ver disponibles por tipo")
        print("  0. Volver al menú principal")
        print("  ─────────────────────────────────────────────")
        opcion = val.pedir_entero("  Opción: ", minimo=0, maximo=3)

        if opcion == 1:
            hab_mod.listar_habitaciones()
        elif opcion == 2:
            hab_mod.listar_disponibles()
        elif opcion == 3:
            tipo = val.pedir_tipo_habitacion()
            hab_mod.listar_disponibles(tipo)
        elif opcion == 0:
            break


# ── CHECK-IN ────────────────────────────────────────────────

def flujo_checkin():
    print("\n  -- CHECK-IN ──────────────────────────────────")
    print("  (El huésped debe estar registrado previamente)")

    # Mostrar habitaciones disponibles para ayudar al usuario
    hab_mod.listar_disponibles()

    dni        = val.pedir_dni()
    numero_hab = val.pedir_entero("  N° de habitación     : ", minimo=100, maximo=999)
    f_entrada  = val.pedir_fecha( "  Fecha de entrada (DD/MM/AAAA): ")
    f_salida   = val.pedir_fecha( "  Fecha de salida  (DD/MM/AAAA): ")

    if val.confirmar("¿Confirmar check-in?"):
        res_mod.hacer_checkin(dni, numero_hab, f_entrada, f_salida)
    else:
        print("  Check-in cancelado.")


# ── CHECK-OUT ───────────────────────────────────────────────

def flujo_checkout():
    print("\n  -- CHECK-OUT ─────────────────────────────────")
    res_mod.listar_reservas_activas()
    numero_hab = val.pedir_entero("  N° de habitación a liberar: ", minimo=100, maximo=999)

    if val.confirmar("¿Confirmar check-out?"):
        res_mod.hacer_checkout(numero_hab)
    else:
        print("  Check-out cancelado.")


# ── ESTADÍSTICAS ────────────────────────────────────────────

def menu_estadisticas():
    while True:
        print("\n  ── ESTADÍSTICAS ────────────────────────────")
        print("  1. Ocupación de habitaciones")
        print("  2. Ingresos por reservas")
        print("  0. Volver al menú principal")
        print("  ─────────────────────────────────────────────")
        opcion = val.pedir_entero("  Opción: ", minimo=0, maximo=2)

        if opcion == 1:
            hab_mod.estadisticas_ocupacion()
        elif opcion == 2:
            res_mod.estadisticas_ingresos()
        elif opcion == 0:
            break


# ── PROGRAMA PRINCIPAL ──────────────────────────────────────

def main():
    encabezado()
    print(f"  Bienvenido/a al sistema de gestión del {NOMBRE_HOTEL}.")

    continuar = True
    while continuar:
        opcion = menu_principal()

        if opcion == 1:
            menu_huespedes()
        elif opcion == 2:
            menu_habitaciones()
        elif opcion == 3:
            flujo_checkin()
        elif opcion == 4:
            flujo_checkout()
        elif opcion == 5:
            res_mod.listar_reservas_activas()
        elif opcion == 6:
            res_mod.listar_historial()
        elif opcion == 7:
            menu_estadisticas()
        elif opcion == 0:
            if val.confirmar("¿Seguro que desea salir del sistema?"):
                print(f"\n  Hasta pronto. ¡Gracias por usar el sistema del {NOMBRE_HOTEL}!\n")
                continuar = False


# Punto de entrada
if __name__ == "__main__":
    main()
