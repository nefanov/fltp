# Generalized LL

 - Устранение левой рекурсии -- грамматика сильно меняется
 - Неоднозначность -- хотелось бы парсить и неоднозначные грамматики. Интуитивно понятно, что теперь деревом разбора будет не дерево, а более "общая" структура -- сжатый лес разбора (вспомним прошлое занятие). 
    
  (Проблема с неоднозначными -- хотим записать в одну ячейку несколько подходящих продукций)
    
Реализуем нисходящий анализ для произвольных КС-языков [4]

_Принципы_:

- По грамматике строим управляющую таблицу (позволим записывать в ячейку более одной продукции)
- Таблица и анализируемое слово поступает на вход абстрактному интерпретатору
- Для работы интерпретатор поддерживает вспомогательную структуру данных -- стек для LL (графоструктурированный). Работа сведется к <<ручному>> контролю стека*
- Один шаг работы состоит в том, чтобы рассмотреть текущую позицию в слове, все соответствующие ей правила из таблицы при возможности сдвинуть позицию разбора вправо.


_Идея_: разрешим параллельно обрабатывать все возможные продукции, оказавшиеся в ячейке, и при этом не сильно разрастаться (обойтись без копирования, как минимум)...

--------------------------------------------------------------------------------------------------------------------------
* важно, что процесс работы СА задается переходами между состояниями МП-автомата: (t:S)-->(t+1:S'), где S:<inp, stack_top, N, call_right>. 

* слот грамматики: позволим в правой части продукции выделять позицию -- ставить точку <<.>> . -- какую часть продукции мы уже обработали (слева от точки), а какую еще осталось (справа). Описанная пара продукция -- точка уже однозначно задает состояние синтаксического разбора. Слоты в грамматике соответствуют состояниям некоторого рекурсивного автомата.

_Графоструктурированный стек_

Добавим стек -- GSS [1-3] (Предложен Томитой для GLR [2], но идея обобщается на GLL).

Детали реализации GSS:

push -- добавим вершину, если нет ее. Иначе смещаем указатель на правильную вершину.

pop -- сдвиг указателя, удаления явно не происходит. Этим мы избежим повторные удаления элементов.

GSS эмулирует вызов функций из рекурсивного спуска. И при этом он вроде как похож на стек LL (мы складываем в LL-стек правую часть продукции, исследуя какой-то нетерминал). 

В RD у нас информация "вызвалась ф-я для разбора такого-то нетерминала". То есть "факты вызова такой-то функции".
Входным параметром для функции была позиция во входе (кусочек входа, номер символа) --> мы вызвали ф-ю обработки нетерминала N начиная со 100500-й позиции во входе --> результат -- разобралось / нет. Результат не зависит от того, где мы эту функцию вызвали (от контекста). Дополнительная информация нам не нужна. 

_Резюме_: у нас будут лежать там только пары <нетерминал, позиция во вх строке, с которой мы начали его распознавать>. Мы потеряли "адрес возврата" -- он содержится в слоте грамматики "." -- "в какой позиции мы находимся?". 

Информация об "адресах возврата" будет храниться на ребрах в виде слотов. Распознали нетерминал в текущей позиции -- проходим по всем исходящим из данной вершины ребрам (считываем адреса возврата) -- сдвигаем указатель головы стека на все-все-все позиции. 


_Дескрипторы_ грамматики

Будем называть пару состояние-стек -- слот-GSS _дескриптором_. 

_Дескриптор_ -- тройка (X, u , i), где X -- слот грамматики, i -- позиция в слове w, а u -- узел GSS. Можем, имея конкретный дескриптор, без дополнительных ухищрений возобновить процедуру СА из этого состояния.

Легко доказывается (а мы не будем), что дескрипторов -- конечное число (для любой конечной грамматики).




--------------------------------------------------------------------------------------------------------------------------
Заметки:

* В RD стек неявный. В LL мы его заводим, но операции привычны. В GLL с ним надо аккуратно поработать...

---------------------------------------------------------------------------------------------------------------------------

Литература:

1) GSS: https://en.wikipedia.org/wiki/Graph-structured_stack
2) Masaru Tomita. Graph-Structured Stack And Natural Language Parsing. Annual Meeting of the Association of Computational Linguistics, 1988.
3) "Простейшая" реализация GSS https://www.tutorialspoint.com/cplusplus-program-to-implement-graph-structured-stack
4) GLL: https://dotat.at/tmp/gll.pdf
5) https://hackage.haskell.org/package/gll-0.4.0.3/docs/GLL-Parser.html
6) GLL Graph generalization: http://iguana-parser.github.io/
