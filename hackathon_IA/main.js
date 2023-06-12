// Obtener referencias a elementos HTML
const inputText = document.getElementById('input-text');
const analyzeButton = document.getElementById('analyze-button');
const resultContainer = document.getElementById('result-container');

// Función para mostrar mensaje de resultado
function mostrarMensaje(mensaje) {
  const mensajeElement = document.createElement('p');
  mensajeElement.textContent = mensaje;
  resultContainer.appendChild(mensajeElement);
}

// Cargar el modelo de Spacy.js
spacy.load('es_core_news_sm').then((nlp) => {
  // Agregar evento click al botón de análisis
  analyzeButton.addEventListener('click', () => {
    // Obtener el texto de entrada
    const texto = inputText.value;

    

// Obtener referencia al botón de análisis
const analyzeButton = document.getElementById('analyze-button');

// Agregar evento click al botón de análisis
analyzeButton.addEventListener('click', () => {
  // Obtener el texto de entrada
  const texto = document.getElementById('input-text').value;

  // Llamar a la función de análisis y obtener los resultados
  const resultados = analizarTexto(texto);

  // Mostrar los resultados en la página
  mostrarResultados(resultados);
});

// Función para analizar el texto
function analizarTexto(texto) {
  // Analizar el texto
  const docInput = nlp(texto);

  // Lista de palabras ofensivas y suicidas
  const docOfensivo = ["gordo", "zorra", "perra", "gato", "maricon", "negro", "matate", "imbecil", "idiota", "boludo", "pelotudo", "pobre", "turro", "rata", "cagon", "retrasado", "mogolico", "gil", "gorreado", "pajero", "croto", "atorrante", "subnormal"];
  const docSuicida = ["cortar", "ahorcar", "morirme", "morir", "suicidio", "venas", "vena", "tiro", "arma", "depresion", "deprimido", "deprimida", "flagelar", "sobredosis", "apuñalar", "apuñalen", "inyectar", "ahogar", "cuello", "pegar", "tirar"];

  // Variables de resultado
  const contenido_ofensivo = [];
  const lista_suicida = [];
  let potencial_suicida = false;
  let ofensivo = false;

  // Verificar palabras ofensivas
  for (let palabra of docInput) {
    palabra = String(palabra);
    for (let palabra_ofensivo of docOfensivo) {
      if (palabra === palabra_ofensivo) {
        ofensivo = true;
        contenido_ofensivo.push(palabra);
      }
    }
  }

  // Mostrar palabras ofensivas encontradas
  if (ofensivo) {
    mostrarMensaje('Este usuario ha sido ofensivo en su comentario');
    mostrarMensaje('Palabras ofensivas encontradas:');
    for (let palabra of contenido_ofensivo) {
      mostrarMensaje('- ' + palabra);
    }
  }

  // Verificar palabras suicidas
  for (let palabra of docInput) {
    palabra = String(palabra);
    for (let palabra_suicida of docSuicida) {
      if (palabra === 'cortar') {
        for (let suicida of docSuicida) {
          if (suicida === 'venas' || suicida === 'vena') {
            potencial_suicida = true;
            lista_suicida.push(palabra);
          }
          if (suicida === 'cuello') {
            potencial_suicida = true;
            lista_suicida.push(palabra);
          }
        }
      }
      if (palabra_suicida === 'pegar') {
        for (let suicida of docSuicida) {
          if (suicida === 'tiro' || suicida === 'tiros') {
            potencial_suicida = true;
            lista_suicida.push(palabra);
          }
        }
      } else if (palabra_suicida === palabra) {
        potencial_suicida = true;
        lista_suicida.push(palabra);
      }
    }
  }

  // Mostrar palabras suicidas encontradas
  if (potencial_suicida) {
    mostrarMensaje('Mensaje suicida');
    mostrarMensaje('Palabras suicidas encontradas:');
    for (let palabra of lista_suicida) {
      mostrarMensaje('- ' + palabra);
    }
  }


  return resultados;
}

// Función para mostrar los resultados en la página
function mostrarResultados(resultados) {
  // Obtener referencia al contenedor de resultados
  const resultContainer = document.getElementById('result-container');

  // Limpiar el contenedor de resultados
  resultContainer.innerHTML = '';

  // Mostrar mensaje de ofensivo si corresponde
  if (resultados.ofensivo) {
    const mensajeOfensivo = document.createElement('p');
    mensajeOfensivo.textContent = 'Este usuario ha sido ofensivo en su comentario';
    resultContainer.appendChild(mensajeOfensivo);

    // Mostrar las palabras ofensivas encontradas
    const palabrasOfensivas = document.createElement('p');
    palabrasOfensivas.textContent = 'Palabras ofensivas encontradas: ' + resultados.palabrasOfensivas.join(', ');
    resultContainer.appendChild(palabrasOfensivas);
  }

  // Mostrar mensaje de suicida si corresponde
  if (resultados.suicida) {
    const mensajeSuicida = document.createElement('p');
    mensajeSuicida.textContent = 'Mensaje suicida';
    resultContainer.appendChild(mensajeSuicida);

    // Mostrar las palabras suicidas encontradas
    const palabrasSuicidas = document.createElement('p');
    palabrasSuicidas.textContent = 'Palabras suicidas encontradas: ' + resultados.palabrasSuicidas.join(', ');
    resultContainer.appendChild(palabrasSuicidas);
  }
}
});