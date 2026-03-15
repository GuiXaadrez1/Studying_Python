# Obtendo Janelas da Aplicação

Depois de iniciar ou conectar, precisamos acessar a janela principal. Existem duas formas principais.

- Método .window()

```python

    # acessando uma janela da aplicacao iniciada pelo nome do titulo
    janela = app.window(title="Untitled - Notepad")

    # retorna um objeto -> WindowSpecification
```

Esse objeto é uma referência a uma janela da aplicação.

- Acesso por índicie

Outra forma:

```python
    janela = app["Untitled - Notepad"]
```

Essa forma usa dicionário interno de janelas.

## Esperando a Janela Aparecer

Em automações reais a janela pode demorar para abrir. Por isso usamos .wait(). Exemplo:

```python
    janela.wait("visible")
```

Os possíveis estados da Janela (processo da exibicao da janela)...
Recomendo que veja sobre os estados de um processo, é bom saber:

| Estado  | Significado       |
| ------- | ----------------- |
| exists  | existe na memória |
| visible | está visível      |
| enabled | pode ser usada    |
| ready   | pronta            |

Exemplo:

```python
    janela.wait("ready")
```

## Listando Janelas Disponíveis

Para descobrir as janelas existentes:

```python
isExistsWindows = app.windows()
```

Exemplo:

```python
for janela in isExistsWindows:
    print(w.window_text())
```

Saída possível:

```bash
Untitled - Notepad
Save As
Find
```




