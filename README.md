# Теория алгоритмов

Курс для студентов 3-го года программы [Фундаментальная и компьютерная лингвистика](https://www.hse.ru/ba/ling/)

* [Оценки за задания](https://docs.google.com/spreadsheets/d/1Lwz38H7USB2HzAwjWA8EarTZ6FIvJI_kNmKAMUbJTaA/pubhtml)
* Как отправлять задания: [инструкция](meta/git_workflow.md), [видео](https://youtu.be/dpHrqlhC_NE)
* [О подозрениях в списывании](meta/cheating.md)
* [Визуализатор алгоритмов](http://algo-visualizer.jasonpark.me)

# Литература

* **CLRS:** Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein *Introduction to Algorithms*, 3rd edition, 2009
  (*Алгоритмы: построение и анализ*, 3-е издание, 2013)
* Steven Skiena *Algorithm Design Manual* (2nd edition, 2008)

# Программа курса

## Модуль 3

1. Анализ алгоритмов. Асимптотическое оценки вычислительной сложности.
  ([семинар](https://mkuznets.com/hse/2017-alg/seminar01.pdf), [листок](https://mkuznets.com/hse/2017-alg/problems01.pdf), [решения](https://mkuznets.com/hse/2017-alg/solutions01.pdf))
	* Вычислительная модель компьютера с памятью с произвольным доступом
	* Операторы и выражения Python в терминах процессорных команд
	* Классы O, Ω, Θ
	* Оценка времени и памяти в лучшем, худшем и среднем случаях. Амортизационная сложность.
	* Сравнение темпов роста функций. Типичные для анализа алгоритмов асимптотические классы.
	* Примеры: возведение в целую степень, числа Фибоначчи, умножение Карацубы.
2. Типы и структуры данных
   ([лекция](https://mkuznets.com/hse/2017-alg/lecture02.pdf), [листок](problems/02))
	* Список и его реализации: массив, связный список (одно- и двусвязный), динамический массив. Бинарный поиск в массиве. `list` в Python.
	* Стек, очередь, двухсторонняя очередь. Их реализация через динамический массив и двусвязный список. `deque` в Python.
	* Коллекции с быстрыми добавлением, удалением и поиском.
		* Словарь. Реализация через хэш-таблицы.
		* Разрешение коллизий: цепочки, открытая адресация (линейное пробирование).
		* Множество. Реализация через хэш-таблицу.
	* Частные случаи, задачи
		* Алгоритмы без дополнительной памяти (in-place)
		* Многомерные массивы
		* Цикл в связном списке
		* Применения стека: поддержка рекурсии, скобочные выражения
		* LRU-кэш
3. Алгоритмы сортировки ([конспект](http://nbviewer.jupyter.org/github/mkuznets/hse-ling-algorithms/blob/master/lecture_notes/03_sorting.ipynb), [листок](problems/03), [решения](https://github.com/mkuznets/hse-ling-algorithms/blob/master/problems/03/solutions.ipynb))
	* Задача сортировки. Сортировки основанные на сравнениях (Comparison sort).
	* Сортировка вставками (Insertion sort)
	* Парадигма «разделяй и властвуй» (divide and conquer). Сортировка слиянием (Mergesort). Master theorem и её применение для оценки сложности.
	* Нижняя граница сложности сортировки, основанной на сравнениях.
	* Quicksort. Поиск порядковых статистик (Selection problem).
	* Selection sort (как приквел к Heapsort)
	* Двоичная куча (Binary heap)
	* Heapsort
4. Двоичные деревья 
	* Определения, реализация, операции поиска ([конспект](http://nbviewer.jupyter.org/github/mkuznets/hse-ling-algorithms/blob/master/lecture_notes/04_1_bst.ipynb))
		* Поиск элемента
		* Поиск минимума/максимума
		* Обходы дерева: в глубину (pre-, in-, post-order), в ширину
		* Поиск следующего и предыдущего значений
	* Динамические деревья поиска (CLRS 12.3, 13 и 18; [лекция в MIT](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/video-lectures/lecture-10-red-black-trees-rotations-insertions-deletions/))
		* Добавление и удаление элементов
		* Сбалансированные деревья поиска (Balanced BST)
			* Красно-чёрное дерево (Red-Black Tree): свойства, вращения, добавление элементов (без удаления).
5. Деревья в приложениях
	* Индексы в базах данных
		* Общие свойства алгоритмов для внешней памяти (external memory)
		* B-Tree: основная идея структуры данных и алгоритмов поиска/добавления элементов
	* Суффиксные и префиксные деревья (tries)
	* **Материалы:**
		* Внешняя память и B-Tree (CLRS 18)
		* [Trie](https://en.wikipedia.org/wiki/Trie)
			* [Про переносы слов в TeX](http://tex.stackexchange.com/a/262595) и его простая [реализация на Python](https://nedbatchelder.com/code/modules/hyphenate.py)
		* [Suffix tree](https://en.wikipedia.org/wiki/Suffix_tree)
			* Skiena, Section 12.3
			* Построение за линейное время: Ukkonen's algorithm (для самостоятельного изучения)
				* [Fast String Searching With Suffix Trees](http://marknelson.us/1996/08/01/suffix-trees/)
				* D. Gusfield. *Algorithms on Strings, Trees, and Sequences: Computer Science and Computational Biology.* (1997)
			* [Поиск всех вхождений подстроки](http://www.geeksforgeeks.org/suffix-tree-application-2-searching-all-patterns/)

## Контрольная

* [Вариант 1](https://mkuznets.com/hse/2017-alg/exam_01_v01.pdf) ([ответы](https://mkuznets.com/hse/2017-alg/solutions_01_v01.pdf))
* [Вариант 2](https://mkuznets.com/hse/2017-alg/exam_01_v02.pdf) ([ответы](https://mkuznets.com/hse/2017-alg/solutions_01_v02.pdf))

## Модуль 4
(программа уточняется)

1. Парадигмы построения алгоритмов
	* Динамическое программирование (dynamic programming) *# лекция 7.04.2017*
		* Задача о разрезании стержня (CLRS 15.1)
		* Числа Фибоначчи как задача динамического программирования (Skiena 8.1)
	* Жадные алгоритмы (greedy) *# лекция 21.04.2017*
		* Задача о выборе процессов (CLRS 16.1)
		* Оптимальность жадного решения на примере fractional vs 0-1 knapsack problem (CLRS 16.2, [доказательство оптимальности](http://www.cs.ust.hk/mjg_lib/Classes/COMP3711H_Fall14/lectures/Greedy_Knapsack_Slides.pdf) для fractional)
	* Приложения: *# семинар 28.04.2017*
		* Приближённое сравнение строк
		* Выравнивание текста
		* Нахождение максимальной общей подпоследовательности
2. Графы
	* Основные определения и виды графов
	* Структуры данных: матрица смежности (adjacency matrix), списки смежных вершин (adjacency lists)
	* Поиск: в ширину, в глубину (depth-/breadth-first search)
	* Ориентированные ациклические графы (directed acyclic graphs, DAG). Топологическая сортировка (topological sort).
	* Поиск связных и сильносвязных компонент
3. Графы (продолжение)
	* Задачи на взвешенных графах:
		* Поиск кратчайших путей: от одной вершины (алгоритмы Дейкстры и Беллмана-Форда), между всеми вершинами (алгоритм Флойда-Уоршелла)
		* Минимальное покрывающее дерево (minimum spanning tree, MST)
		* Задача о максимальном потоке (maximum flow)
4. Алгоритмы на строках
	* Поиск подстроки в строке (обзорно)
		* Регулярные выражения
		* Кнут-Моррис-Пратт
		* Рабин-Карп
		* Бойер-Мур
	* Скрытые марковские модели. Алгоритм Витерби