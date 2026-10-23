<img src="marca/teleprompter.svg" width="64" alt="">

# Teleprompter

**por Javier Nieto** · una de [mis herramientas abiertas](https://javiernieto.net/profesional/recursos/)

Un teleprompter que **te escucha**: cuando hablas, el texto avanza contigo; cuando te detienes, se
espera. Lo hice para grabar mis videos y lo regalo. Es gratis y de código abierto (licencia MIT).

## Úsalo sin instalar nada

Ábrelo en Chrome o Edge: **https://javiernieto.net/teleprompter/**

Pega tu guion (o arrastra un `.txt`), toca **Seguir mi voz** y graba. Tu texto se queda en tu
navegador; no me llega nada.

## Lo que lo hace distinto

- **Sigue tu voz.** No tienes que acelerar para alcanzarlo ni quedarte callado mientras se va.
- **La velocidad es en palabras por minuto**, no en píxeles: la misma toma dura lo mismo con
  cualquier tamaño de letra.
- **El texto arranca cerca de la cámara** (en la línea naranja), no abajo, que es lo que delata que
  estás leyendo.
- **Lo ya leído se atenúa**: el ojo no tiene que buscar dónde iba.
- **Entiende tu guion** (abajo): tomas, pausas y apuntes que no se leen.
- **Cuenta regresiva** de 3 segundos al arrancar: silencio limpio para cortar en la edición.
- Se maneja con **un clicker de presentaciones** (avanza o regresa por párrafo).

## Cómo escribir tu guion para que se detenga donde quieres

| En tu texto | Qué hace |
|---|---|
| **3 líneas en blanco** | Separan una **toma** de otra. Cada una con su cronómetro; `N` / `P` cambian de toma |
| **1 línea en blanco** | Una **pausa** corta (0.6 s, ajustable) |
| `ARRANQUE` · `CIERRE` | Letrero naranja; lo que sigue se lee |
| `BLOQUES — esto NO se lee` | Lo que sigue va en **ámbar y más chico**: apuntes para platicar, no para leer |
| `1.` `2.` … dentro de `BLOQUES` | Con «Parar en cada bloque», **se detiene en cada uno**: platicas, y `Espacio` para seguir |

Toca **Ejemplo** en el panel para ver uno armado.

## «Seguir mi voz»: lo que hay que saber

- Funciona en **Chrome o Edge, en la computadora**. En Firefox no existe; en iPhone va limitado.
- **Chrome manda el audio a Google para reconocerlo** (así funciona el dictado de Chrome). Si no
  quieres eso, apágalo y usa la velocidad fija.
- Los números escritos con letra («ciento sesenta») Chrome los oye como «160». No se pierde: se
  ubica de nuevo con las palabras siguientes.
- Tu programa de grabación (OBS u otro) puede usar el mismo micrófono al mismo tiempo.

## Sin internet

Descarga este repo y abre `abrir_teleprompter.pyw` (Windows, con Python). Lo sirve en tu
computadora para que Chrome recuerde el permiso del micrófono. Abrir `index.html` con doble clic
también funciona, pero el micrófono te pide permiso a cada rato. Sin internet, «Seguir mi voz» no
funciona; la velocidad fija sí.

## Atajos

`Espacio` iniciar/pausar · `↓` `→` `AvPág` siguiente párrafo · `↑` `←` `RePág` anterior ·
`Shift+↑↓` velocidad · `N`/`P` toma · `R` desde el inicio · `V` voz · `+`/`-` tamaño ·
`H` panel · `F` pantalla completa · `M` espejo.

## Sin soporte

Se comparte tal cual. Si te sirvió, sígueme en Threads o Instagram (**@holajaviernieto**) y
cuéntame qué le mejorarías. Más herramientas gratis en
[javiernieto.net/profesional/recursos](https://javiernieto.net/profesional/recursos/).
