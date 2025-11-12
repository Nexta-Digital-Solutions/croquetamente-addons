.. image:: https://img.shields.io/badge/license-AGPL--3-blue.svg
    :alt: License: AGPL-3

Valued Delivery Slip
====================

Este módulo permite definir si el impreso del albarán (delivery slip) debe mostrar los precios de los productos o no.
Añade un campo booleano en el modelo `stock.picking` para controlar si el documento será **valorado** o **no valorado**.

**Características principales:**

- Nuevo campo *"Albarán valorado"* (`valued_picking`) en `stock.picking`.
- Si el campo está activado, el informe de albarán mostrará precios unitarios, subtotales y totales.
- Si el campo está desactivado, el informe se imprimirá sin valores monetarios.
- Comportamiento totalmente integrado en la acción de impresión estándar del albarán.

Esta funcionalidad es útil para empresas que necesitan entregar albaranes sin precios a clientes finales, pero con valores internos para control o facturación.

Installation
============

Este módulo requiere la instalación del módulo base de inventario:

- `stock`

Se instala como cualquier otro módulo estándar de Odoo.

Configuration
=============

No se requiere configuración adicional.
El campo *"Albarán valorado"* puede activarse o desactivarse manualmente en cada albarán, o establecerse mediante herencias o automatizaciones personalizadas según la necesidad.

Usage
=====

1. Ir a **Inventario → Operaciones → Albaranes**.
2. Abrir un albarán y localizar el nuevo campo **“Albarán valorado”**.
3. Activar o desactivar el check según si se desea imprimir el documento con o sin valores.
4. Imprimir el albarán desde la acción estándar.
   - Si está activado → se mostrarán precios.
   - Si no está activado → se ocultarán.

Known Issues / Roadmap
======================

- Añadir opción para configurar el comportamiento por defecto (valorado/no valorado) a nivel de cliente o tipo de operación.

Credits
=======

Contributors
------------

* Jaume Basiero <jbasiero@nextads.es>

Maintainer
----------

.. image:: https://nextads.es/wp-content/uploads/2021/02/Logotipo-Principal.png.webp
   :alt: NextaDS
   :target: https://www.nextads.es/

Este módulo es mantenido por **NextaDS**.
