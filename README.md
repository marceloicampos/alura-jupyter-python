# instalando o Jupyter Notebook no GNU / Linux

sudo apt install python3

python3 --version

sudo apt install python3-pip

python3 -m pip --version

---

python3 -m ensurepip --default-pip

python3 -m pip install --upgrade pip setuptools wheel

---

python3 -m venv tutorial_env
source default_env/bin/activate

NOTA: os comandos acima são servem para CRIAR opcionalmente um ambiente virtual

Isso criará um novo ambiente virtual no default_env subdiretório e configurará o shell atual para usá-lo como o python ambiente padrão.

Os “Ambientes Virtuais” do Python permitem que os pacotes do Python sejam instalados em um local isolado para um aplicativo específico, em vez de serem instalados globalmente.

---

python3 -m pip install "SomeProject Like 'jupyter'"

python3 -m pip install --upgrade "SomeProject Like 'jupyter'"

python3 -m pip install --user "SomeProject Like 'jupyter'"

---

alura-jupyter-python
