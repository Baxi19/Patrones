# TensorFlow y Keras

# 💻 ¿Qué es Keras en comparación con TensorFlow y cuál es su propósito?

Tensorflow es la biblioteca más famosa utilizada en producción para modelos de aprendizaje profundo. Tiene una comunidad muy grande e impresionante. La cantidad de confirmaciones y la cantidad de ejemplos en el repositorio de Tensorflow en Github son suficientes para definir la amplia popularidad de TensorFlow. Sin embargo, TensorFlow no es tan fácil de usar. Por otro lado, Keras es una API de alto nivel construida sobre Tensorflow  además es más fácil de usar y fácil de usar en comparación con TensorFlow. Keras es una librería la cual se encuentra escrita en Python, es utilizada para machine learning, especialmente con las redes neuronales , cabe resaltar que esta librería es de código abierto y  tiene la posibilidad de conectarse con TensorFlow y otras librerías enfocadas en aprendizaje profundo, el propósito de Keras es facilitar el uso de los modelos de machine learning [1].

---

# 👩🏻💻  ¿Por qué TensorFlow usa grafos y cómo se crean manualmente?

TensorFlow utiliza grafos para representar las redes neuronales en una estructura de datos.

**Creando grafos en TensorFlow 2**

Para iniciar se muestra de ejemplo de la creación de un grafo en Python.

```python
def compute(a,b,c):
	d = a*b+c
	e = a*b*c
	return d,e
```

Asumiendo que a, b y c son matrices de Tensor, este código calcula dos nuevos valores: d y e. Usando la ejecución **aeger**, TensorFlow podría calcular el valor para d y después calcular el valor para e.

Usando la ejecución **lazy**, TensorFlow crearía un grafo de operaciones, antes de ejecutar el grafo para obtener el resultado, se ejecutaría un optimizador de grafos. Para evitar calcular a * b dos veces, el optimizador almacenaría en caché el resultado y lo reutilizaría cuando fuera necesario. Para operaciones más complejas, el optimizador podría permitir el paralelismo para acelerar los cálculos. Ambas técnicas son importantes al ejecutar modelos grandes y complejos [2].

---

# 💻¿Cuál es la diferencia entre el modo de ejecución "Eager" y el modo de ejecución "Lazy"?

El cambio principal en TensorFlow 2 es la ejecución **eager**. Históricamente, TensorFlow 1 siempre ha usado la ejecución **lazy** por defecto. Se llama perezoso porque el framework no ejecuta las operaciones hasta que se solicita específicamente.

En el capítulo "TensorFlow Basics and Trainning", se hace mención a un ejemplo que ilustra la diferencia entre la ejecución **lazy** y **eager,** sumando el valor de dos vectores:

```python
import tensorflow as tf

a = tf.constant([1,2,3])
b = tf.constant([0,0,1])
c = tf.add(a,b)`
```

Nótese que `tf.add(a. b)` se podría remplazar con a + b ya que TensorFlow sobre escribe muchos de los operadores de Python.

El resultado del código anterior depende de la versión de TensorFlow. Con TensorFlow 1 que usa la ejecución lazy por defecto, el resultado sería el siguiente:

```python
Tensor("Add:0, shape = (3, ), dtype=int32)
```

Usando TensorFlow 2, que implementa la ejecución eager por defecto, se podría tener la siguiente la siguiente salida:

```python
tf.Tensor([1 2 4]), shape = (3, ), dtype=int32)
```

En ambos casos, la salida es un Tensor. En el segundo caso, la operación ha sido ejecutada ansiosamente y podemos ver directamente que el Tensor contiene el resultado (`[1 2 3 ]`). En el primer caso, el Tensor contiene información de la operación suma (`Add : 0`), pero no el resultado de la operación.

---

# 🔎 ¿Cómo registra la información en TensorBoard y cómo la muestra?

TensorBoard es un componente de TensorFlow, registra la información de diferentes escalares, imágenes, histogramas, etc, en archivos con formato **`tf.summary`**, además cabe resaltar que para mostrar la información se puede graficar de diferentes maneras, ya sea en el momento de la ejecución, entrada o salida de imágenes, entre otros.

---

# 📚 ¿Cuáles son las principales diferencias entre TensorFlow 1 y TensorFlow 2?

En TensorFlow 1, se podría de necesitar más código para calcular el resultado de operaciones entre grafos, haciendo el proceso de desarrollo más complejo. La ejecución **aeger** implementada en TensorFlow 2 hace que el proceso de debug sea más sencillo, ya que los desarrolladores pueden alcanzar el punto máximo del valor del Tensor en cualquier momento, propiciando un desarrollo más fácil.

---

# 📜 Referencias Bibliográficas

[1] Nain, A. (2017, 13 mayo). TensorFlow or Keras? Which one should I learn? Recuperado 13 de octubre de 2020, de [https://medium.com/implodinggradients/tensorflow-or-keras-which-one-should-i-learn-5dd7fa3f9ca0](https://medium.com/implodinggradients/tensorflow-or-keras-which-one-should-i-learn-5dd7fa3f9ca0)

[2] Benjamin Planche & Eliot Andres, 30 may. 2019,Hands-On Computer Vision with TensorFlow 2: Leverage deep learning to create powerful image processing apps with TensorFlow 2.0 and Keras, Capítulo 2: TensorFlow basics and training model, páginas 50-73. extraído de [https://app.box.com/s/7d8z6ofzs9twin728k1cnc987ja0hmd7](https://app.box.com/s/7d8z6ofzs9twin728k1cnc987ja0hmd7)