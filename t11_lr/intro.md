**LR(K)**

Как следует из названия, этот вариант анализатора просматривает входную последовательность слева направо, пытаясь применить продукцию к крайней правой части подстроки (то есть вывод -- правосторонний), предпросматриваются k символов вперёд от текущего.

Мы будем рассматривать LR(0) и LR(1) анализаторы, от LR(1) можно довольно просто сделать обобщение к LR(k).

Идея следующая: у нас есть стек и входной буфер. Понадобятся 2 операции -- перенос и свёртка.

Перенос: если у нас на вершине стека нетерминал, то сдвигаем указатель текущего символа, и кладём его содержимое на стек.

Анализ: пытаемся применить некоторую продукцию к содержимому стека + следующим k символам во входном потоке.

Свёртка: заменяем на стеке правую часть подходящей продукции левой.

Если выполнен перенос по $, и на стеке S, то мы разобрали слово и оно принимается.

При таком выводе дерево почти явно строится снизу-вверх: свёртка это, по сути, добавление поддерева высоты 1, дети которого -- символы правой части примененной продукции, а корень -- левая часть.