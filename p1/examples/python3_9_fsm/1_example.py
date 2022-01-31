# perform "pip install transitions", then:
# Original: https://github.com/pytransitions/transitions
from transitions import Machine

# На этот объект будем вешать состояния
class Matter(object):
    pass

lump = Matter()

# Полный список состояний
states=['solid', 'liquid', 'gas', 'plasma']

# Добавляем таблицу переходов — из какое в какое состояние мы можем попасть
transitions = [
    { 'trigger': 'melt', 'source': 'solid', 'dest': 'liquid' },
    { 'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas' },
    { 'trigger': 'sublimate', 'source': 'solid', 'dest': 'gas' },
    { 'trigger': 'ionize', 'source': 'gas', 'dest': 'plasma' }
]

# Инициализация машины
machine = Machine(lump, states=states, transitions=transitions, initial='liquid')

# Проверяем начальное состояние
lump.state
# >>> 'liquid'

# И пробуем изменить состояние триггерами перехода
lump.evaporate()
lump.state
# >>> 'gas'
lump.trigger('ionize')
lump.state
