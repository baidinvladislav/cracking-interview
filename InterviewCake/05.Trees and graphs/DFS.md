<h2>Поиск в глубину и обход в глубину</h2>

Поиск в глубину это метод для изучения дерева или графа. В поиске в глубину вы идете так глубоко как можете вниз по одному
одному пути пока не отскочите назад и не начнете новый путь.

Поиск в глубину похож на выход из лабиринта. Вы исследуете один путь, доходите до конца, и затем пробуете новый путь.

Например обойдем такое дерево:
```
         1
   /     |     \
  2      3      4
 / \    / \    / \
5   6  7   8  9   10
|   |
11  12
```

1. Сначала посетим вершину 1 - это корень дерева
2. Затем 2,5,11 - посетим все вершины по первому пути от корня до самого конца дерева
3. Затем 2,6,12 - возьмем след. путь от корня
4. Затем 1,3,7 - возьмем след. путь от корня
5. Затем 1,3,8 - возьмем след. путь от корня
6. Затем 1,4,9 - возьмем след. путь от корня
7. Затем 1,4,10 - и наконец посетим последний путь от корня

Преимущества:
* Обход бинарного дерева в глубину обычно требует меньше памяти чем обход его в ширину
* Может быть легко реализован через рекурсию

Недостатки:
* Поиск в глубину не гарантирует поиск кратчайщего пути, когда обход в ширину находит крачтайщий путь между двумя вершинами.
