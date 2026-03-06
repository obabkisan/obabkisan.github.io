import os
import numpy as np
from main import (
    create_vector, create_matrix, reshape_vector,
    vector_add, scalar_multiply, elementwise_multiply, dot_product,
    matrix_multiply, matrix_determinant, matrix_inverse, solve_linear_system,
    load_dataset, statistical_analysis, normalize_data,
    plot_histogram, plot_heatmap, plot_line
)

# ============================================================
# ТЕСТЫ
# ============================================================

# Тест создания вектора от 0 до 9
def test_create_vector() -> None:
    v = create_vector()
    assert isinstance(v, np.ndarray)
    assert v.shape == (10,)
    assert np.array_equal(v, np.arange(10))

# Тест создания матрицы 5x5 со случайными числами
def test_create_matrix() -> None:
    m = create_matrix()
    assert isinstance(m, np.ndarray)
    assert m.shape == (5, 5)
    assert np.all((m >= 0) & (m < 1))

# Тест преобразования вектора из формы (10,) в (2, 5)
def test_reshape_vector() -> None:
    v = np.arange(10)
    reshaped = reshape_vector(v)
    assert reshaped.shape == (2, 5)
    assert reshaped[0, 0] == 0
    assert reshaped[1, 4] == 9

# Тест сложения векторов
def test_vector_add() -> None:
    assert np.array_equal(
        vector_add(np.array([1, 2, 3]), np.array([4, 5, 6])),
        np.array([5, 7, 9]),
    )
    assert np.array_equal(
        vector_add(np.array([0, 1]), np.array([1, 1])),
        np.array([1, 2]),
    )

# Тест умножения вектора на скаляр
def test_scalar_multiply() -> None:
    assert np.array_equal(
        scalar_multiply(np.array([1, 2, 3]), 2),
        np.array([2, 4, 6]),
    )

# Тест поэлементного умножения векторов
def test_elementwise_multiply() -> None:
    assert np.array_equal(
        elementwise_multiply(np.array([1, 2, 3]), np.array([4, 5, 6])),
        np.array([4, 10, 18]),
    )

# Тест скалярного произведения векторов
def test_dot_product() -> None:
    assert dot_product(np.array([1, 2, 3]), np.array([4, 5, 6])) == 32
    assert dot_product(np.array([2, 0]), np.array([3, 5])) == 6

# Тест умножения матриц
def test_matrix_multiply() -> None:
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[2, 0], [1, 2]])
    assert np.array_equal(matrix_multiply(A, B), A @ B)

# Тест вычисления определителя марицы
def test_matrix_determinant() -> None:
    A = np.array([[1, 2], [3, 4]])
    assert round(matrix_determinant(A), 5) == -2.0

# Тест вычисления обратной матрицы
def test_matrix_inverse() -> None:
    A = np.array([[1, 2], [3, 4]])
    inv_a = matrix_inverse(A)
    assert np.allclose(A @ inv_a, np.eye(2))

# Тест решения системы линейных уравнений
def test_solve_linear_system() -> None:
    A = np.array([[2, 1], [1, 3]])
    b = np.array([1, 2])
    x = solve_linear_system(A, b)
    assert np.allclose(A @ x, b)

# Тест загрузки данных из CSV файла
def test_load_dataset() -> None:
    # Для теста создадим временный файл
    test_data = "math,physics,informatics\n78,81,90\n85,89,88"
    filename = "test_data.csv"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(test_data)
    try:
        data = load_dataset(filename)
        assert data.shape == (2, 3)
        assert np.array_equal(data[0], [78, 81, 90])
    finally:
        if os.path.exists(filename):
            os.remove(filename)

# Тест статического анализа данных
def test_statistical_analysis() -> None:
    data = np.array([10, 20, 30])
    result = statistical_analysis(data)
    assert result["mean"] == 20
    assert result["min"] == 10
    assert result["max"] == 30

# Тест Min-Max нормализации данных
def test_normalization() -> None:
    data = np.array([0, 5, 10])
    norm = normalize_data(data)
    assert np.allclose(norm, np.array([0, 0.5, 1]))

# Тест построения гистограммы
def test_plot_histogram() -> None:
    # просто проверяем, что функция не падает
    data = np.array([1, 2, 3, 4, 5])
    plot_histogram(data)

# Тест построения тепловой карты
def test_plot_heatmap() -> None:
    matrix = np.array([[1, 0.5], [0.5, 1]])
    plot_heatmap(matrix)

# Тест построения линейного графика
def test_plot_line() -> None:
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    plot_line(x, y)

if __name__ == "__main__":
    print("Запустите python -m pytest main.py -v для проверки лабораторной работы.")