function atualizarContador(event) {
    const tipoCristal = event.detail.tipo;
    console.log(`Missão: Cristal de energia "${tipoCristal}" coletado!`);
    
    const contadorElement = document.getElementById('contador-cristais');
    let contador = parseInt(contadorElement.textContent);
    contador++;
    contadorElement.textContent = contador;

    if (contador >= 5) {
        console.log("Missão Concluída: Todas as energias arcanas foram coletadas!");
    }
}

const NOME_EVENTO = 'cristalColetado';

document.addEventListener(NOME_EVENTO, atualizarContador);

function simularColeta(tipo) {
    console.log(`Simulação: Nave encontrou um cristal ${tipo}. Disparando evento...`);

    const eventoCustomizado = new CustomEvent(NOME_EVENTO, {
        detail: { tipo: tipo, timestamp: Date.now() }
    });
    
    document.dispatchEvent(eventoCustomizado);
}
