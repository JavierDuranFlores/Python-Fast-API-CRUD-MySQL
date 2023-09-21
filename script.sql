CREATE TABLE Libros (
    IDLibro INT PRIMARY KEY,
    Titulo VARCHAR(255),
    Autor VARCHAR(255),
    AnioPublicacion INT
);

CREATE TABLE Prestamos (
    IDPrestamo INT PRIMARY KEY,
    IDLibro INT,
    FechaPrestamo DATE,
    FechaDevolucion DATE,
    FOREIGN KEY (IDLibro) REFERENCES Libros(IDLibro)
);