(function(){
    var img = document.getElementById("image01"),
        arrayFinalComprimido = [],
        arrayFinalDescomprimido = [];

    var comprimir = function comprimir(arrayDescomprimido){
        var arraySemAlpha = [];
        var arrayComprimido = [];

        var count = 0;
        for (var i = 0; i < arrayDescomprimido.length; i++) {
            //tira o alpha
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

  

       var jqInfoComprimido = $('#infoCanvasComprimido');
           jqInfoComprimido.find('#canvasComprimido').text(arrayComprimido.length);
           jqInfoComprimido.find('#percentualCompressao').text( (-100 * arrayComprimido.length)/arrayDescomprimido.length + 100);
        return arrayComprimido;
    }

    var descomprimir = function descomprimir(comprimido){
        var arrayOriginal = [],
            arrayOriginalAux = [],
            isFind = false,
            value,
            count = 0;

        comprimido.forEach(function(element, index, self) { 
            //se encontrar o simbolo volta com ins fine true
            if(element == "!"){
                isFind = true;
                return;
            }
            //atribui o elemento ao valor
            if(isFind == true){
                value = element;
                isFind = false;
                return;
            }
            //como agora tem um valor definido, ele pega ele elemento e popula a quantidade de vezes até o valor do contador
            if(value){
                for (var i = 0; i < value; i++) {
                    arrayOriginalAux.push(element);
                };
                value = undefined;
                return;
            }
            arrayOriginalAux.push(element);
        });

        //com o array populado, aqui é colocado o alpha, coloca o o valor 3x e depois o alpha
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

    //pega as dimensões da imagem
    var resizeCanvas = function(canvas, img, callback){
        var widthImg = img.getAttribute('width'),
            heightImg = img.getAttribute('height');
        
        canvas.setAttribute('width', widthImg);
        canvas.setAttribute('height',heightImg);
        
        if(callback){
            callback(canvas, img);
        }
    };

    //segundo canvas - descomprimido
    var fillCanvasWithImgData = function(imgDataArray, canvas){
        var widthImg = img.getAttribute('width'),
            heightImg = img.getAttribute('height'),
            context;
        
        canvas.setAttribute('width', widthImg);
        canvas.setAttribute('height',heightImg);

        context = canvas.getContext("2d");

        var imgData = context.createImageData(widthImg, heightImg);
        
        //contrução da imagem no segundo canvas
        for (var i= 0; i < imgData.data.length;i+=4) {
            imgData.data[i+0]=imgDataArray[i+0];
            imgData.data[i+1]=imgDataArray[i+1];
            imgData.data[i+2]=imgDataArray[i+2];
            imgData.data[i+3]=imgDataArray[i+3];
        }
        context.putImageData(imgData,0,0);
    }

    //seta os tamanhos da imagem no primeiro canvas, imprime para o usuário os valores
    var fillCanvasImg = function(canvas, img){
        var  context;
        
        context = canvas.getContext("2d");
        context.drawImage(img, 0, 0);

        var jqInfoDiv = $('#infoCanvasa');
        jqInfoDiv.find('#imgInfoWidth').text(canvas.width);
        jqInfoDiv.find('#imgInfoHeight').text(canvas.height);
        jqInfoDiv.find('#img-size').text((canvas.width * canvas.height) *4);
    };

    //função de click que chama a função para pegar os valores da imagem (resize)
    var eventTransporImg = function(){

        $('#btnMostrar').click(function(){
            var canvas = document.getElementById('canvasa');
                
            resizeCanvas(canvas, img, fillCanvasImg);
        });
    };

    var eventComprimir = function(){
        $('#btnComprimir').click(function(){
            var canvas = document.getElementById('canvasa'),
                context = canvas.getContext('2d'),
                imgData = context.getImageData(0,0, canvas.width,canvas.height);

            arrayFinalComprimido =  comprimir(imgData.data);
        });
    };

    var eventDescomprimir = function(){
        $('#btnDescomprimir').click(function(){
            var canvas = document.getElementById('canvasb');
            
            var arrayFinalDescomprimido = descomprimir(arrayFinalComprimido);   
                fillCanvasWithImgData(arrayFinalDescomprimido, canvas);
        });
    };

    eventTransporImg();
    eventComprimir();
    eventDescomprimir();

})();