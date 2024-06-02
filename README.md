
INSTALL
------------
Run requirements::

    $ virtualenv --python=python3.12 .venv
	$ source .venv/bin/activate 
    $ pip3 install -r requirements.txt

RUN
------------
    $ python3 task_1.py
	$ python3 task_2.py
	$ python3 task_3.py


# Порівняння результатів DFS та BFS алгоритмів

## Результати DFS алгоритму
```h f a b c d e g```

## Результати BFS алгоритму
```h f c a g e b d```

## Пояснення різниці в отриманих результатах

### DFS (Depth-First Search) алгоритм
DFS працює за принципом "глибокого" проходження графа. Він обирає один з сусідів поточного вузла і глибоко проводить аналіз кожної гілки до тих пір, поки не досягне кінцевого вузла або не знайде вузол, який вже був відвіданий. Результати можуть бути не впорядковані за "короткістю" шляхів, і можуть залежати від порядку обходу.

### BFS (Breadth-First Search) алгоритм
BFS працює за принципом "широкого" проходження графа. Він обирає всіх сусідів поточного вузла і вивчає їх перед переходом до наступного рівня вузлів. Це забезпечує знаходження найкоротших шляхів від початкового вузла до всіх інших вузлів.

## Висновки
1. DFS може виводити шляхи в довільному порядку, в залежності від того, як обираються сусіди на кожному етапі.
2. BFS гарантує знаходження найкоротших шляхів, оскільки він розглядає всі можливі варіанти на одному рівні перед переходом на наступний рівень.
3. У випадку, коли граф є деревом або не має циклів, обидва алгоритми повинні виводити однакові результати щодо шляхів.

Вибір між DFS і BFS залежить від конкретних вимог задачі. Якщо необхідно знайти найкоротший шлях, BFS може бути кращим вибором. У випадках, коли важливий сам факт досягнення певного вузла, DFS може бути ефективним.