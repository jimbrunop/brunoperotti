'use strict';


describe('Comprir array:  ', function () {

	it('array deverá ser igual index 267', function () {
		var imgArray = [3,3,3,255,3,3,3,255,0,0,0,255,2,2,2,255,2,2,1,255];
		var arrayEsperado = ["!",6,3,0,0,0,'!',5,2,1];

		expect(comprimir(imgArray)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual index 69', function () {
		var imgArray = [6,6,6,255,0,0,0,255,1,1,1,255,1,1,1,255,2,2,2,255];
		var arrayEsperado = [6,6,6,0,0,0,'!',6,1,2,2,2];
		expect(comprimir(imgArray)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual tipo 1', function () {
		var imgArray = [1,1,1,255,1,2,3,255];
		var arrayEsperado = ["!",4, 1, 2, 3];

		expect(comprimir(imgArray)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual tipo 2', function () {
		var imgArray = [1,2,3,255,1,1,1,255];
		var arrayEsperado = [1,2,3,1,1,1];
		expect(comprimir(imgArray)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual tipo 3', function () {
		var imgArray = [1,2,3,255,1,1,1,255,1,3,3,255,3,3,3,255];
		var arrayEsperado = [1,2,3,'!',4,1,'!',5,3];
		expect(comprimir(imgArray)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual vazio', function () {
		var imgArray = [];
		var arrayEsperado = [];
		expect(comprimir(imgArray)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual tipo 4', function () {
		var imgArray = [121,121,121,255,121,121,121,255,5,5,5,255,5,5,5,255,120,120,120,255];
		var arrayEsperado = ['!',6,121,'!',6,5, 120, 120, 120];
		expect(comprimir(imgArray)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual tipo 5', function () {
		var imgArray = [1,1,1,255,1,2,2,255 ];
		var arrayEsperado = ['!',4,1,2,2];
		expect(comprimir(imgArray)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual tipo 6', function () {
		var imgArray = [1,1,1,255,1,2,2,255,1,1,1,255,1,2,2,255];
		var arrayEsperado = ['!',4,1,2,2,'!',4,1,2,2];
		expect(comprimir(imgArray)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual tipo 7', function () {
		var imgArray = [1,2,3,255,1,1,1,255,1,2,3,255,1,1,1,255];
		var arrayEsperado = [1,2,3,'!',4,1,2,3,1,1,1];
		expect(comprimir(imgArray)).toEqual(arrayEsperado);
	});

});

describe('Descomprir array:  ', function () {


	it('array deverá ser igual tipo 267', function () {
		var arrayEsperado = [3,3,3,255,3,3,3,255,0,0,0,255,2,2,2,255,2,2,1,255];
		var arrayComprimido = ["!",6,3,0,0,0,'!',5,2,1];
		expect(descomprimir(arrayComprimido)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual index 69', function () {
		var arrayEsperado = [6,6,6,255,0,0,0,255,1,1,1,255,1,1,1,255,2,2,2,255];
		var arrayComprimido = [6,6,6,0,0,0,'!',6,1,2,2,2];
		expect(descomprimir(arrayComprimido)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual tipo 1', function () {
		var arrayEsperado = [1,1,1,255,1,2,3,255];
		var arrayComprimido = ["!",4, 1, 2, 3];

		expect(descomprimir(arrayComprimido)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual tipo 2', function () {
		var arrayEsperado = [1,2,3,255,1,1,1,255];
		var arrayComprimido = [1,2,3,1,1,1];

		expect(descomprimir(arrayComprimido)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual tipo 3', function () {
		var arrayEsperado = [1,2,3,255,1,1,1,255,1,3,3,255,3,3,3,255];
		var arrayComprimido = [1,2,3,'!',4,1,'!',5,3];

		expect(descomprimir(arrayComprimido)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual vazio', function () {
		var arrayEsperado = [];
		var arrayComprimido = [];

		expect(descomprimir(arrayComprimido)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual tipo 4', function () {
		var arrayEsperado = [121,121,121,255,121,121,121,255,5,5,5,255,5,5,5,255,120,120,120,255];
		var arrayComprimido = ['!',6,121,'!',6,5, 120, 120, 120];

		expect(descomprimir(arrayComprimido)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual tipo 5', function () {
		var arrayEsperado = [1,1,1,255,1,2,2,255];
		var arrayComprimido = ['!',4,1,2,2];
		expect(descomprimir(arrayComprimido)).toEqual(arrayEsperado);
	});


	it('array deverá ser igual tipo 6', function () {
		var arrayEsperado = [1,1,1,255,1,2,2,255,1,1,1,255,1,2,2,255];
		var arrayComprimido = ['!',4,1,2,2,'!',4,1,2,2];
		expect(descomprimir(arrayComprimido)).toEqual(arrayEsperado);
	});

	it('array deverá ser igual tipo 7', function () {
		var arrayEsperado = [1,2,3,255,1,1,1,255,1,2,3,255,1,1,1,255];
		var arrayComprimido = [1,2,3,'!',4,1,2,3,1,1,1];
		expect(descomprimir(arrayComprimido)).toEqual(arrayEsperado);
	});

});
