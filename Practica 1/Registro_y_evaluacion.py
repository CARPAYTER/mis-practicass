def mostrar_encabezado_escuelas():
    print("Universidad Tecnologica utxj")
    print("Carrera")

def nota_minima(nota_mini):
    if nota_mini > 6:
        return "minima"
    return "muy baja"

def evaluar_rendimiento(nota_final):
    if nota_final < 7.0:
        return "Reprobado"
    elif 7.0 <= nota_final < 9.0:
        return "Aprobado"
    elif 9.0 <= nota_final <= 10.0:
        return "Excelente"
    return "Desconocido"

def obtener_nota_minima_aprobatoria(exam1, tara1):
    promedio = (exam1 * 0.7) + (tara1 * 0.3)
    return round(promedio, 1)

print("--- 1. Encabezado ---")
mostrar_encabezado_escuelas()

print("\n--- 2. Evaluación de Rendimiento ---")
print("Nota 8.5:", evaluar_rendimiento(8.5))
print("Nota 9.5:", evaluar_rendimiento(9.5))

print("\n--- 3. Promedio Ponderado ---")
resultado_promedio = obtener_nota_minima_aprobatoria(9.0, 8.0)
print(f"El promedio ponderado es: {resultado_promedio}")
    

    