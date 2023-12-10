
#include <iostream>
#include <vector>

class Matrix {
    public:
        Matrix(const int &crows, const int &ccolumns);

        void print();
        std::vector<std::vector<int>> summation(Matrix matr2);
        int getItem(const int &i, const int &j) { return matrix[i][j]; };
        void putItem(const int &i, const int &j, int item) { matrix[i][j] = item; };    

    private:
        int rows;
        int columns;
        std::vector<std::vector<int>> matrix;
        
        void initialize(const int &crows, const int &ccolumns);
};


Matrix::Matrix(const int &crows, const int &ccolumns) {
    rows = crows;
    columns = ccolumns;
    initialize(rows, columns);
}    

void Matrix::initialize(const int &crows, const int &ccolumns) {
        matrix.resize(crows);
        for (int i = 0; i < crows; i++) {
            matrix.at(i).resize(ccolumns);
        }
}

void Matrix::print() {
    std::cout << "-----------MATRIX-----------" << std::endl;
    for (int i = 0; i < rows; i++) {
        std::cout << "         [ ";
        for (int j = 0; j < columns; j++) {
            std::cout << matrix[i][j] << ' ';
        }
        std::cout << ']' << std::endl;
    }
    std::cout << "----------------------------";
}

std::vector<std::vector<int>> Matrix::summation(Matrix matr2) {
    std::vector<std::vector<int>> resultMatrix;
    resultMatrix.resize(rows);
    for (int i = 0; i < rows; i++) {
        resultMatrix.at(i).resize(columns);
    }
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            resultMatrix[i][j] = matr2.getItem(i, j) + matrix[i][j];
        }
    }
    return resultMatrix;
}

int main() {
    Matrix a = Matrix(3, 3);
    Matrix b = Matrix(3, 3);
    b.putItem(1, 1, 5);
    

    std::vector<std::vector<int>> c = a.summation(b);
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            std::cout << c[i][j];
        }
    }
    return 0;
}
