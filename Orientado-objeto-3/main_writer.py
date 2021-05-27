from classes_writer import Writer
from classes_writer import Pen
from classes_writer import TypingMachine

escritor = Writer('João Lisboa')
caneta = Pen('Bic')
maquina = TypingMachine()

escritor.tool = caneta
escritor.tool.write()
