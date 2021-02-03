#!python3
try:
		from mysql import connector
except ModuleNotFoundError:
		print('MySQL Connector não instalado!')
else:
		print('MySQL Connector instalado e pronto!')

# python -m venv .venv
# pip install mysql-connector
# pip install --upgrade pip
# pip install --upgrade setuptools