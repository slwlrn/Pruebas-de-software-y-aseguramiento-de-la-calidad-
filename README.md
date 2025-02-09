
### **📌 Proyecto: Cálculo de Ventas en Python**

Este proyecto contiene un programa en Python que calcula el total de ventas a partir de archivos JSON que contienen información de productos y registros de ventas. Se manejan errores en los datos de entrada y se generan reportes con los resultados.

---

## **📂 Estructura del Proyecto**
```
📂 project
 ├── 📂 TC1  # Casos de prueba 1
 │   ├── TC1.ProductList.json
 │   ├── TC1.Sales.json
 ├── 📂 TC2  # Casos de prueba 2
 │   ├── TC2.Sales.json
 ├── 📂 TC3  # Casos de prueba 3
 │   ├── TC3.Sales.json
 ├── compute_sales.py  # Script principal
 ├── SalesResults.txt  # Archivo de salida con los resultados
 ├── README.md  # Este documento
```

---

## **🔹 Requerimientos Previos**
Para ejecutar el programa, necesitas:
- **Python 3.8 o superior** instalado.
- Instalar `flake8` y `pylint` para verificar el código:

```sh
pip install flake8 pylint
```

---

## **🚀 Cómo Ejecutar el Programa**
### **📊 Cálculo de Ventas**
📍 **Ubicación:** `compute_sales.py`  
🔹 **Funcionalidad:**
Este programa toma dos archivos JSON como entrada:
- **Archivo de productos:** Contiene una lista de productos con sus precios.
- **Archivo de ventas:** Registra la cantidad vendida de cada producto.

El programa calcula el **total de ventas** de los productos vendidos, considerando errores en los datos y generando un reporte en `SalesResults.txt`.

✅ **Ejemplo de Ejecución:**
```sh
python compute_sales.py TC1/TC1.ProductList.json TC1/TC1.Sales.json
```

📤 **Salida esperada (en `SalesResults.txt`):**
```
======== SALES REPORT ========
Total Sales (excluding negatives): $2,481.86
Total Sales (including negatives): $2,481.86
Execution Time: 0.0010 seconds
================================
```
---

## **✅ Validación de Estilo con `flake8` y `pylint`**
Para verificar que el código cumple con los estándares PEP 8, ejecutar:

```sh
flake8 compute_sales.py --max-line-length=100
pylint compute_sales.py
```

Un puntaje de **10/10** en `pylint` indica que el código está correctamente estructurado.

---

## **⚠ Notas Importantes**
- **`SalesResults.txt`** ahora guarda los resultados de **todas las ejecuciones**, en lugar de sobrescribirse en cada ejecución.
- **Errores detectados** en los archivos de entrada se mostrarán en la terminal y en el archivo de salida.
- Se manejan **cantidades negativas en las ventas**, mostrando resultados **con y sin ellas**.
- **Si un producto en ventas no existe en la lista de productos**, se genera una advertencia en los resultados.

---
