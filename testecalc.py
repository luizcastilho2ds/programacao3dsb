#!/usr/bin/env python3
"""Calculadora simples de linha de comando.

Suporta operações: +, -, *, /

Uso interativo: execute sem argumentos e digite expressões como:
  2 + 2

Para rodar testes automáticos (não interativo):
  python teste.py --selftest
"""
import sys


def add(a, b):
	return a + b


def sub(a, b):
	return a - b


def mul(a, b):
	return a * b


def div(a, b):
	if b == 0:
		raise ZeroDivisionError("divisão por zero")
	return a / b


def calculate(op, a, b):
	ops = {
		"+": add,
		"-": sub,
		"*": mul,
		"/": div,
	}
	if op not in ops:
		raise ValueError(f"Operação inválida: {op}")
	return ops[op](a, b)


def parse_expression(expr):
	"""Tenta extrair (a, op, b) de uma string como '2 + 3'."""
	for op in ('+', '-', '*', '/'):
		if op in expr:
			parts = expr.split(op)
			if len(parts) != 2:
				raise ValueError("Formato inválido. Use: <num> <op> <num>")
			a = float(parts[0].strip())
			b = float(parts[1].strip())
			return op, a, b
	raise ValueError("Operador não encontrado. Use +, -, * ou /")


def interactive():
	print("Calculadora simples — digite 'sair' para encerrar.")
	print("Digite um cálculo no formato: <número> <operador> <número> (ex.: 2 + 3). Operadores: + - * /")
	while True:
		try:
			expr = input("Digite o cálculo (ou 'sair'): ").strip()
			if not expr:
				continue
			if expr.lower() in ('sair', 'exit', 'quit', 'q'):
				break
			op, a, b = parse_expression(expr)
			res = calculate(op, a, b)
			print("=", res)
		except Exception as e:
			print("Erro:", e)
	print("Encerrando...")


def selftest():
	tests = [
		('+', 2, 3, 5),
		('-', 5, 3, 2),
		('*', 4, 2, 8),
		('/', 9, 3, 3),
	]
	for op, a, b, expected in tests:
		out = calculate(op, a, b)
		assert abs(out - expected) < 1e-9, f"{a}{op}{b} => {out}, esperado {expected}"

	# Teste divisão por zero
	try:
		calculate('/', 1, 0)
	except ZeroDivisionError:
		pass
	else:
		raise AssertionError('Divisão por zero não levantou erro')

	print('Self-test: OK')


if __name__ == '__main__':
	if '--selftest' in sys.argv:
		selftest()
	else:
		interactive()
