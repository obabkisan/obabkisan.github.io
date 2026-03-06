## Вычисления и анализ данных с использованием NumPy

## Цель работы 

Освоить базовые возможности библиотеки NumPy для работы с массивами и матрицами, научиться:
- выполнять векторные и матричные операции без использования циклов.
- проводить статистический анализ данных с помощью функций NumPy.
- визуализировать результаты с использованием `matplotlib` и `seaborn`.
- загружать и обрабатывать табличные данные из CSV-файлов через `pandas`.

---

## Задание
Создать виртуальное окружение и установить необходимые зависимости (numpy, matplotlib, seaborn, pandas, pytest).
Реализовать все функции, чтобы они проходили тесты.

---

## Код и команды
### Подготовка к работе
```
# Создание виртуального окружения:
python -m venv numpy_env
   
# Активация виртуального окружения:
source numpy_env/bin/activate 
   
# Установка зависимостей:
pip install numpy matplotlib seaborn pandas pytest
```
Структура проекта
```
numpy_lab/
├── main.py
├── test.py
├── data/
│   └── students_scores.csv
└── plots/
```
Содержимое файла students_scores.csv в папке data:
```
math,physics,informatics
78,81,90
85,89,88
92,94,95
70,75,72
88,84,91
95,99,98
60,65,70
73,70,68
84,86,85
90,93,92
```
### Реализация функций в main.py
Создание и обработка массивов 

```
def create_vector() -> np.ndarray:
    """
    Создает массив от 0 до 9.

    Returns:
        numpy.ndarray: Массив чисел от 0 до 9 включительно
    """
    return np.arange(10)


def create_matrix() -> np.ndarray:
    """
    Создает матрицу 5x5 со случайными числами [0,1].

    Returns:
        numpy.ndarray: Матрица 5x5 со случайными значениями от 0 до 1
    """
    return np.random.rand(5, 5)


def reshape_vector(vec: np.ndarray) -> np.ndarray:
    """
    Преобразовывает (10,) -> (2,5)

    Args:
        vec (numpy.ndarray): Входной массив формы (10,)

    Returns:
        numpy.ndarray: Преобразованный массив формы (2, 5)
    """
    return vec.reshape(2,5)



def transpose_matrix(mat: np.ndarray) -> np.ndarray:
    """
    Производит транспонирование матрицы.

    Args:
        mat (numpy.ndarray): Входная матрица

    Returns:
        numpy.ndarray: Транспонированная матрица
    """
    return np.transpose(mat) # mat.T
```
Векторные операции
```
def vector_add(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Складывает вектора одинаковой длины (векторизация без циклов).

    Args:
        a (numpy.ndarray): Первый вектор
        b (numpy.ndarray): Второй вектор

    Returns:
        numpy.ndarray: Результат поэлементного сложения
    """
    return a + b


def scalar_multiply(vec: np.ndarray, scalar: float | int) -> np.ndarray:
    """
    Умножает вектора на число.

    Args:
        vec (numpy.ndarray): Входной вектор
        scalar (float/int): Число для умножения

    Returns:
        numpy.ndarray: Результат умножения вектора на скаляр
    """
    return vec * scalar


def elementwise_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Поэлементно умножает.

    Args:
        a (numpy.ndarray): Первый вектор/матрица
        b (numpy.ndarray): Второй вектор/матрица

    Returns:
        numpy.ndarray: Результат поэлементного умножения
    """
    # Подсказка: используйте оператор *
    return a * b


def dot_product(a: np.ndarray, b: np.ndarray) -> float:
    """
    Вычисляет скалярное произведение.

    Args:
        a (numpy.ndarray): Первый вектор
        b (numpy.ndarray): Второй вектор

    Returns:
        float: Скалярное произведение векторов
    """
    return np.dot(a, b)
```
Матричные операции 
```
def matrix_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Умножает матрицы.

    Args:
        a (numpy.ndarray): Первая матрица
        b (numpy.ndarray): Вторая матрица

    Returns:
        numpy.ndarray: Результат умножения матриц
    """
    return np.matmul(a, b) # a @ b


def matrix_determinant(a: np.ndarray) -> float:
    """
    Вычисляет определитель матрицы.

    Args:
        a (numpy.ndarray): Квадратная матрица

    Returns:
        float: Определитель матрицы
    """
    return np.linalg.det(a)


def matrix_inverse(a: np.ndarray) -> np.ndarray:
    """
    Вычисляет обратную матрицу.

    Args:
        a (numpy.ndarray): Квадратная матрица

    Returns:
        numpy.ndarray: Обратная матрица
    """
    return np.linalg.inv(a)


def solve_linear_system(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Решает систему линейных уравнений Ax = b

    Args:
        a (numpy.ndarray): Матрица коэффициентов A
        b (numpy.ndarray): Вектор свободных членов b

    Returns:
        numpy.ndarray: Решение системы x
    """
    return np.linalg.solve(a, b)
```
Статический анализ
```
def load_dataset(path="data/students_scores.csv") -> np.ndarray:
    """
    Загружает CSV и возвращает NumPy массив.

    Args:
        path (str): Путь к CSV файлу

    Returns:
        numpy.ndarray: Загруженные данные в виде массива
    """
    return pd.read_csv(path).to_numpy()


def statistical_analysis(data: np.ndarray) -> dict[str, float]:
    """
    Выполняет статистический анализ одномерного массива данных.
    Представьте, что данные — это результаты экзамена по математике.

    Вычисляет: средний балл, медиану, стандартное отклонение,
    минимум, максимум, 25 и 75 перцентили.

    Args:
        data (numpy.ndarray): Одномерный массив данных

    Returns:
        dict: Словарь со статистическими показателями
    """
    return {
        "mean": np.mean(data),
        "median": np.median(data),
        "std": np.std(data),
        "min": np.min(data),
        "max": np.max(data),
        "percentile_25": np.percentile(data, 25),
        "percentile_75": np.percentile(data, 75),
    }


def normalize_data(data: np.ndarray) -> np.ndarray:
    """
    Выполняет Min-Max нормализацию.

    Формула: (x - min) / (max - min)

    Args:
        data (numpy.ndarray): Входной массив данных

    Returns:
        numpy.ndarray: Нормализованный массив данных в диапазоне [0, 1]
    """
    min_val = np.min(data)
    max_val = np.max(data)
    if max_val - min_val == 0:
        return np.zeros_like(data, dtype=float)
    return (data - min_val) / (max_val - min_val)
```
Визуализация
```
def plot_histogram(data: np.ndarray) -> None:
    """
    Строит гистограмму распределения оценок по математике.

    Args:
        data (numpy.ndarray): Данные для гистограммы
    """
    os.makedirs("plots", exist_ok=True)
    plt.figure()
    plt.hist(data, bins=10, edgecolor="black")
    plt.title("Histogram of Scores")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.savefig("plots/histogram.png")
    plt.close()


def plot_heatmap(matrix: np.ndarray) -> None:
    """
    Строит тепловую карту корреляции предметов.

    Args:
        matrix (numpy.ndarray): Матрица корреляции
    """
    os.makedirs("plots", exist_ok=True)
    plt.figure()
    sns.heatmap(matrix, annot=True, cmap="coolwarm")
    plt.title("Heatmap")
    plt.savefig("plots/heatmap.png")
    plt.close()


def plot_line(x: np.ndarray, y: np.ndarray) -> None:
    """
    Строит график зависимости: студент -> оценка по математике.

    Args:
        x (numpy.ndarray): Номера студентов
        y (numpy.ndarray): Оценки студентов
    """
    os.makedirs("plots", exist_ok=True)
    plt.figure()
    plt.plot(x, y, marker="o")
    plt.title("Student Scores")
    plt.xlabel("Student ID")
    plt.ylabel("Score")
    plt.savefig("plots/line.png")
    plt.close()
```
### Запуск тестов
```
python -m pytest test.py -v
```
Пример одного из тестов 
```
# Тест вычисления определителя марицы
def test_matrix_determinant() -> None:
    A = np.array([[1, 2], [3, 4]])
    assert round(matrix_determinant(A), 5) == -2.0
```
Результаты выполнения тестов
```
collected 17 items                                                                                             

test.py::test_create_vector PASSED                                                                       [  5%]
test.py::test_create_matrix PASSED                                                                       [ 11%]
test.py::test_reshape_vector PASSED                                                                      [ 17%]
test.py::test_vector_add PASSED                                                                          [ 23%]
test.py::test_scalar_multiply PASSED                                                                     [ 29%]
test.py::test_elementwise_multiply PASSED                                                                [ 35%]
test.py::test_dot_product PASSED                                                                         [ 41%]
test.py::test_matrix_multiply PASSED                                                                     [ 47%]
test.py::test_matrix_determinant PASSED                                                                  [ 52%]
test.py::test_matrix_inverse PASSED                                                                      [ 58%]
test.py::test_solve_linear_system PASSED                                                                 [ 64%]
test.py::test_load_dataset PASSED                                                                        [ 70%]
test.py::test_statistical_analysis PASSED                                                                [ 76%]
test.py::test_normalization PASSED                                                                       [ 82%]
test.py::test_plot_histogram PASSED                                                                      [ 88%]
test.py::test_plot_heatmap PASSED                                                                        [ 94%]
test.py::test_plot_line PASSED                                                                           [100%]

============================================= 17 passed in 13.38s ==============================================
```
### Нюансы и особенности решения 

При работе с матричными операциями важно учитывать погрешность вычислений с плавающей точкой, поэтому в тестах используется `round()` или `np.allclose()` вместо прямого сравнения. Функции визуализации должны создавать папку `plots/`, если её нет, и сохранять графики через `plt.savefig()`, иначе тесты не найдут файлы. Все операции нужно выполнять векторизованно (через методы NumPy), без циклов. Запускать тесты нужно из той папки, где лежит `test.py`, иначе `pytest` не увидит файлы.

---

## Вывод
В ходе работы я освоила базовые возможности NumPy: создание и преобразование массивов, векторные и матричные операции, статистический анализ и нормализацию данных. Научилась визуализировать результаты через matplotlib и seaborn, а также проверять корректность кода с помощью pytest. Поняла, что векторизация делает код эффективнее, а изоляция зависимостей в виртуальном окружении помогает избегать конфликтов между проектами. Эти навыки пригодятся для дальнейшего изучения анализа данных и машинного обучения.