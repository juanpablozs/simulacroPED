enunciados:
	git web--browse www/index.html

all:
	@echo "Compilacion / ejecucion del ejercicio"

clean:
	@echo "Limpiando..."

servidor:
	python3 servidor.py

cliente:
	python3 cliente.py

test:
	python3 -m unittest discover -v