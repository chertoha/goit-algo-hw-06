## Висновки до завдання 2

Шляхи DFS від Central Station до Airport:
['Central Station', 'South District', 'Intermediary 2', 'Intermediary 4', 'Airport']
['Central Station', 'North District', 'Intermediary 1', 'Intermediary 3', 'Airport']

Шляхи BFS від Central Station до Airport:
['Central Station', 'North District', 'Intermediary 1', 'Intermediary 3', 'Airport']
['Central Station', 'South District', 'Intermediary 2', 'Intermediary 4', 'Airport']

Порівняння:
DFS досліджує шляхи вглиб, перш ніж досліджувати сусідів, тому може спочатку знаходити довші шляхи.
BFS досліджує всіх сусідів на поточному рівні, перш ніж переходити на наступний рівень, що гарантує знаходження найкоротшого шляху.
DFS та BFS знайшли різні шляхи через їхні різні стратегії пошуку.
DFS зазвичай знаходить шлях: ['Central Station', 'South District', 'Intermediary 2', 'Intermediary 4', 'Airport']
BFS завжди знаходить найкоротший шлях: ['Central Station', 'North District', 'Intermediary 1', 'Intermediary 3', 'Airport']
