# Estrutura Hierárquica da Interface

Interfaces Windows seguem uma hierarquia de elementos.

## Estrutura:

```bash

Application
   ↓
Window
   ↓
Control
   ↓
SubControl

```

Exemplo real:

```bash
Notepad
   ↓
MenuBar
   ↓
File
   ↓
Save
```

Representação no pywinauto:

```python

# Janela
app.window(...)

# Componente da janela
window.child_window(...)

# Evento Sobre a Janela
control.click()

```

## Inspecionando a Estrutura da Janela

**Método essencial:**

```python
    
    # Capta a Árvore de componentes da janela... 
    janela.print_control_identifiers()

```

Exemplo de Saida:

```txt
Control Identifiers:

Dialog - 'Calculadora'    (L929, T288, R1347, B923)
['CalculadoraDialog', 'Calculadora', 'Dialog', 'CalculadoraDialog0', 'CalculadoraDialog1', 'Calculadora0', 'Calculadora1', 'Dialog0', 'Dialog1']
child_window(title="Calculadora", control_type="Window")
   | 
   | Dialog - 'Calculadora'    (L1105, T289, R1338, B329)
   | ['CalculadoraDialog2', 'Calculadora2', 'Dialog2']
   | child_window(title="Calculadora", auto_id="TitleBar", control_type="Window")
   |    | 
   |    | Menu - 'Sistema'    (L0, T0, R0, B0)
   |    | ['Menu', 'SistemaMenu', 'Sistema', 'Sistema0', 'Sistema1']
   |    | child_window(title="Sistema", auto_id="SystemMenuBar", control_type="MenuBar")
   |    |    | 
   |    |    | MenuItem - 'Sistema'    (L0, T0, R0, B0)
   |    |    | ['MenuItem', 'SistemaMenuItem', 'Sistema2']
   |    |    | child_window(title="Sistema", control_type="MenuItem")
   |    | 
   |    | Button - 'Minimizar Calculadora'    (L1167, T289, R1224, B329)
   |    | ['Minimizar Calculadora', 'Minimizar CalculadoraButton', 'Button', 'Button0', 'Button1']
   |    | child_window(title="Minimizar Calculadora", auto_id="Minimize", control_type="Button")
   |    | 
   |    | Button - 'Maximizar Calculadora'    (L1224, T289, R1281, B329)
   |    | ['Maximizar Calculadora', 'Maximizar CalculadoraButton', 'Button2']
   |    | child_window(title="Maximizar Calculadora", auto_id="Maximize", control_type="Button")
   |    | 
   |    | Button - 'Fechar Calculadora'    (L1281, T289, R1338, B329)
   |    | ['Fechar Calculadora', 'Button3', 'Fechar CalculadoraButton']
   |    | child_window(title="Fechar Calculadora", auto_id="Close", control_type="Button")
   | 
   | Dialog - 'Calculadora'    (L938, T289, R1338, B914)
   | ['CalculadoraDialog3', 'Calculadora3', 'Dialog3']
   | child_window(title="Calculadora", control_type="Window")
   |    | 
   |    | Static - 'Calculadora'    (L998, T299, R1078, B319)
   |    | ['Static', 'Calculadora4', 'CalculadoraStatic', 'Static0', 'Static1']
   |    | child_window(title="Calculadora", auto_id="AppName", control_type="Text")
   |    | 
   |    | Custom - ''    (L938, T329, R1338, B914)
   |    | ['Custom', 'CalculadoraCustom']
   |    | child_window(auto_id="NavView", control_type="Custom")
   |    |    | 
   |    |    | Button - 'Abrir Navega��o'    (L943, T337, R993, B382)
   |    |    | ['Abrir Navega��oButton', 'Abrir Navega��o', 'Button4']
   |    |    | child_window(title="Abrir Navega��o", auto_id="TogglePaneButton", control_type="Button")
   |    |    |    | 
   |    |    |    | Static - ''    (L0, T0, R0, B0)
   |    |    |    | ['Static2']
   |    |    |    | child_window(auto_id="PaneTitleTextBlock", control_type="Text")
   |    |    | 
   |    |    | GroupBox - ''    (L938, T339, R1338, B909)
   |    |    | ['GroupBox', 'CalculadoraGroupBox', 'GroupBox0', 'GroupBox1']
   |    |    |    | 
   |    |    |    | Static - 'Expression � '    (L0, T0, R0, B0)
   |    |    |    | ['Static3', 'Expression � ', 'Expression � Static']
   |    |    |    | child_window(title="Expression � ", auto_id="CalculatorExpression", control_type="Text")
   |    |    |    | 
   |    |    |    | Static - 'A exibi��o � 0'    (L938, T414, R1338, B504)
   |    |    |    | ['A exibi��o � 0Static', 'Static4', 'A exibi��o � 0']
   |    |    |    | child_window(title="A exibi��o � 0", auto_id="CalculatorResults", control_type="Text")
   |    |    |    | 
   |    |    |    | Button - 'Abrir submenu de hist�rico'    (L1288, T339, R1328, B379)
   |    |    |    | ['Abrir submenu de hist�rico', 'Button5', 'Abrir submenu de hist�ricoButton']
   |    |    |    | child_window(title="Abrir submenu de hist�rico", auto_id="HistoryButton", control_type="Button")
   |    |    |    | 
   |    |    |    | GroupBox - 'Controles de mem�ria'    (L943, T505, R1334, B540)
   |    |    |    | ['Controles de mem�riaGroupBox', 'Controles de mem�ria', 'GroupBox2']
   |    |    |    | child_window(title="Controles de mem�ria", auto_id="MemoryPanel", control_type="Group")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Limpar toda a mem�ria'    (L943, T505, R1006, B540)
   |    |    |    |    | ['Limpar toda a mem�riaButton', 'Limpar toda a mem�ria', 'Button6']
   |    |    |    |    | child_window(title="Limpar toda a mem�ria", auto_id="ClearMemoryButton", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Rechamada de mem�ria'    (L1008, T505, R1071, B540)
   |    |    |    |    | ['Rechamada de mem�ria', 'Button7', 'Rechamada de mem�riaButton']
   |    |    |    |    | child_window(title="Rechamada de mem�ria", auto_id="MemRecall", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Adi��o de mem�ria'    (L1073, T505, R1136, B540)
   |    |    |    |    | ['Adi��o de mem�riaButton', 'Adi��o de mem�ria', 'Button8']
   |    |    |    |    | child_window(title="Adi��o de mem�ria", auto_id="MemPlus", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Subtra��o de mem�ria'    (L1139, T505, R1202, B540)
   |    |    |    |    | ['Subtra��o de mem�ria', 'Button9', 'Subtra��o de mem�riaButton']
   |    |    |    |    | child_window(title="Subtra��o de mem�ria", auto_id="MemMinus", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Armazenamento de mem�ria'    (L1205, T505, R1268, B540)
   |    |    |    |    | ['Armazenamento de mem�ria', 'Button10', 'Armazenamento de mem�riaButton']
   |    |    |    |    | child_window(title="Armazenamento de mem�ria", auto_id="memButton", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Abrir submenu de mem�ria'    (L1271, T505, R1334, B540)
   |    |    |    |    | ['Button11', 'Abrir submenu de mem�ria', 'Abrir submenu de mem�riaButton']
   |    |    |    |    | child_window(title="Abrir submenu de mem�ria", auto_id="MemoryButton", control_type="Button")
   |    |    |    | 
   |    |    |    | GroupBox - 'Controles de exibi��o'    (L943, T542, R1333, B600)
   |    |    |    | ['GroupBox3', 'Controles de exibi��oGroupBox', 'Controles de exibi��o']
   |    |    |    | child_window(title="Controles de exibi��o", auto_id="DisplayControls", control_type="Group")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Por cento'    (L943, T542, R1039, B600)
   |    |    |    |    | ['Button12', 'Por cento', 'Por centoButton']
   |    |    |    |    | child_window(title="Por cento", auto_id="percentButton", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Limpar entrada'    (L1040, T542, R1136, B600)
   |    |    |    |    | ['Limpar entrada', 'Limpar entradaButton', 'Button13']
   |    |    |    |    | child_window(title="Limpar entrada", auto_id="clearEntryButton", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Limpar'    (L1139, T542, R1235, B600)
   |    |    |    |    | ['LimparButton', 'Limpar', 'Button14']
   |    |    |    |    | child_window(title="Limpar", auto_id="clearButton", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Backspace'    (L1237, T542, R1333, B600)
   |    |    |    |    | ['Backspace', 'BackspaceButton', 'Button15']
   |    |    |    |    | child_window(title="Backspace", auto_id="backSpaceButton", control_type="Button")
   |    |    |    | 
   |    |    |    | GroupBox - 'Fun��es padr�o'    (L943, T604, R1235, B662)
   |    |    |    | ['GroupBox4', 'Fun��es padr�oGroupBox', 'Fun��es padr�o']
   |    |    |    | child_window(title="Fun��es padr�o", auto_id="StandardFunctions", control_type="Group")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Rec�proco'    (L943, T604, R1039, B662)
   |    |    |    |    | ['Rec�proco', 'Rec�procoButton', 'Button16']
   |    |    |    |    | child_window(title="Rec�proco", auto_id="invertButton", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Quadrado'    (L1040, T604, R1136, B662)
   |    |    |    |    | ['QuadradoButton', 'Button17', 'Quadrado']
   |    |    |    |    | child_window(title="Quadrado", auto_id="xpower2Button", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Raiz quadrada'    (L1139, T604, R1235, B662)
   |    |    |    |    | ['Raiz quadrada', 'Button18', 'Raiz quadradaButton']
   |    |    |    |    | child_window(title="Raiz quadrada", auto_id="squareRootButton", control_type="Button")
   |    |    |    | 
   |    |    |    | GroupBox - 'Operadores padr�o'    (L1237, T604, R1333, B909)
   |    |    |    | ['Operadores padr�o', 'Operadores padr�oGroupBox', 'GroupBox5']
   |    |    |    | child_window(title="Operadores padr�o", auto_id="StandardOperators", control_type="Group")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Dividir por'    (L1237, T604, R1333, B662)
   |    |    |    |    | ['Dividir por', 'Button19', 'Dividir porButton']
   |    |    |    |    | child_window(title="Dividir por", auto_id="divideButton", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Multiplicar por'    (L1237, T666, R1333, B725)
   |    |    |    |    | ['Multiplicar por', 'Multiplicar porButton', 'Button20']
   |    |    |    |    | child_window(title="Multiplicar por", auto_id="multiplyButton", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Menos'    (L1237, T727, R1333, B785)
   |    |    |    |    | ['MenosButton', 'Button21', 'Menos']
   |    |    |    |    | child_window(title="Menos", auto_id="minusButton", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Mais'    (L1237, T788, R1333, B847)
   |    |    |    |    | ['MaisButton', 'Mais', 'Button22']
   |    |    |    |    | child_window(title="Mais", auto_id="plusButton", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Igual a'    (L1237, T851, R1333, B909)
   |    |    |    |    | ['Button23', 'Igual aButton', 'Igual a']
   |    |    |    |    | child_window(title="Igual a", auto_id="equalButton", control_type="Button")
   |    |    |    | 
   |    |    |    | GroupBox - 'Teclado num�rico'    (L943, T665, R1235, B907)
   |    |    |    | ['GroupBox6', 'Teclado num�ricoGroupBox', 'Teclado num�rico']
   |    |    |    | child_window(title="Teclado num�rico", auto_id="NumberPad", control_type="Group")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Zero'    (L1040, T850, R1136, B908)
   |    |    |    |    | ['Button24', 'Zero', 'ZeroButton']
   |    |    |    |    | child_window(title="Zero", auto_id="num0Button", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Um'    (L943, T788, R1039, B847)
   |    |    |    |    | ['UmButton', 'Um', 'Button25']
   |    |    |    |    | child_window(title="Um", auto_id="num1Button", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Dois'    (L1040, T788, R1136, B847)
   |    |    |    |    | ['Button26', 'DoisButton', 'Dois']
   |    |    |    |    | child_window(title="Dois", auto_id="num2Button", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Tr�s'    (L1139, T788, R1235, B847)
   |    |    |    |    | ['Tr�sButton', 'Tr�s', 'Button27']
   |    |    |    |    | child_window(title="Tr�s", auto_id="num3Button", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Quatro'    (L943, T727, R1039, B785)
   |    |    |    |    | ['Quatro', 'QuatroButton', 'Button28']
   |    |    |    |    | child_window(title="Quatro", auto_id="num4Button", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Cinco'    (L1040, T727, R1136, B785)
   |    |    |    |    | ['Button29', 'CincoButton', 'Cinco']
   |    |    |    |    | child_window(title="Cinco", auto_id="num5Button", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Seis'    (L1139, T727, R1235, B785)
   |    |    |    |    | ['Seis', 'Button30', 'SeisButton']
   |    |    |    |    | child_window(title="Seis", auto_id="num6Button", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Sete'    (L943, T665, R1039, B723)
   |    |    |    |    | ['Sete', 'Button31', 'SeteButton']
   |    |    |    |    | child_window(title="Sete", auto_id="num7Button", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Oito'    (L1040, T665, R1136, B723)
   |    |    |    |    | ['Oito', 'Button32', 'OitoButton']
   |    |    |    |    | child_window(title="Oito", auto_id="num8Button", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Nove'    (L1139, T665, R1235, B723)
   |    |    |    |    | ['Button33', 'Nove', 'NoveButton']
   |    |    |    |    | child_window(title="Nove", auto_id="num9Button", control_type="Button")
   |    |    |    |    | 
   |    |    |    |    | Button - 'Separador decimal'    (L1139, T850, R1235, B908)
   |    |    |    |    | ['Separador decimal', 'Separador decimalButton', 'Button34']
   |    |    |    |    | child_window(title="Separador decimal", auto_id="decimalSeparatorButton", control_type="Button")
   |    |    |    | 
   |    |    |    | Button - 'Positivo negativo'    (L943, T850, R1039, B908)
   |    |    |    | ['Positivo negativoButton', 'Button35', 'Positivo negativo']
   |    |    |    | child_window(title="Positivo negativo", auto_id="negateButton", control_type="Button")
   |    |    | 
   |    |    | Static - 'Padr�o'    (L998, T340, R1078, B374)
   |    |    | ['Padr�oStatic', 'Static5', 'Padr�o']
   |    |    | child_window(title="Padr�o", auto_id="Header", control_type="Text")
   |    |    | 
   |    |    | Button - 'Manter na parte superior'    (L1091, T339, R1131, B379)
   |    |    | ['Manter na parte superior', 'Manter na parte superiorButton', 'Button36']
   |    |    | child_window(title="Manter na parte superior", auto_id="NormalAlwaysOnTopButton", control_type="Button")
   | 
   | Pane - ''    (L938, T329, R1338, B914)
   | ['CalculadoraPane', 'Pane']

```

Isso revela todos os controles acessíveis.

Esse método é fundamental para engenharia de automação.


