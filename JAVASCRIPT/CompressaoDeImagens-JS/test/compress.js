
    var comprimir = function comprimir(arrayDescomprimido){
        var arraySemAlpha = [];
        var arrayComprimido = [];

        var count = 0;
        for (var i = 0; i < arrayDescomprimido.length; i++) {
            if(count != 3){
                arraySemAlpha.push(arrayDescomprimido[i]);
                count++;
            }else{
                count = 0
            }
        };

        var elementoAnterior;
            count = 1;

        arraySemAlpha.forEach(function(element, index, self) {
            
            if(elementoAnterior == element){
                count++
                if(self.length -1 != index){
                    return;
                }
            }

            if(self.length -1 == index){
                if(count == 1){
                    arrayComprimido.push(elementoAnterior);
                    arrayComprimido.push(element);
                }else if(count == 3 || count == 2){
                    for (var j = 0; j < count; j++) {
                        arrayComprimido.push(elementoAnterior);   
                    }
                }else if(count > 3){
                    arrayComprimido.push("!");
                    arrayComprimido.push(count);
                    arrayComprimido.push(elementoAnterior);
                    if(elementoAnterior != element){
                        arrayComprimido.push(element);    
                    }
                }

            }else if( elementoAnterior != undefined && count >= 1 && count <= 3){
                for (var j = 0; j < count; j++) {
                    arrayComprimido.push(elementoAnterior);   
                }
            }else if(count > 3){
                arrayComprimido.push("!");
                arrayComprimido.push(count);
                arrayComprimido.push(elementoAnterior);
            }

            if(elementoAnterior != undefined ){
                count = 1;
            }
            elementoAnterior = element;
        });

        return arrayComprimido;
    }


    var descomprimir = function descomprimir(comprimido){
        var arrayOriginal = [],
            arrayOriginalAux = [],
            isFind = false,
            value,
            count = 0;

        comprimido.forEach(function(element, index, self) { 
            
            if(element == "!"){
                isFind = true;
                return;
            }

            if(isFind == true){
                value = element;
                isFind = false;
                return;
            }

            if(value){
                for (var i = 0; i < value; i++) {
                    arrayOriginalAux.push(element);
                };
                value = undefined;
                return;
            }
            arrayOriginalAux.push(element);
        });

        for (var j = 0; j < arrayOriginalAux.length; j++) {
            if(count == 2 || arrayOriginalAux.length-1 == j){
                arrayOriginal.push(arrayOriginalAux[j]);
                arrayOriginal.push(255);
                count = 0;
            }else{
                arrayOriginal.push(arrayOriginalAux[j]);
                count++;
            }
        };

        return arrayOriginal;
    };