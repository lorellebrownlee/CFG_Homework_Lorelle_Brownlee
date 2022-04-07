
CREATE DATABASE BookStore;

USE BookStore;

CREATE TABLE Authors (
    author_name VARCHAR(50) NOT NULL,
    book_name VARCHAR(50) NOT NULL
);

CREATE TABLE Books (
    book_name VARCHAR(50) NOT NULL,
    sold_copies INT NOT NULL
);

-- Now populating both tables
INSERT INTO Authors
(author_name, book_name)
VALUES
('author_1', 'book_1'),
('author_1', 'book_2'),
('author_2', 'book_3'),
('author_2', 'book_4'),
('author_2', 'book_5'),
('author_3', 'book_6'),
('author_4', 'book_6'),
('author_4', 'book_7'),
('author_4', 'book_8'),
('author_5', 'book_9'),
('author_999', 'book_743');

INSERT INTO Books
(book_name, sold_copies)
VALUES
('book_1', 1000),
('book_2', 1500),
('book_3', 34000),
('book_4', 29000),
('book_5', 40000),
('book_6', 4400),
('book_7', 500),
('book_8', 200),
('book_9', 250),
('book_743', 500);


select j.author_name as 'Author name', sum(j.sold_copies)  as 'Total sold'
from (SELECT a.author_name, b.book_name, b.sold_copies
FROM Authors a
INNER JOIN (SELECT book_name, sold_copies FROM books) b on a.book_name = b.book_name) as j
group by j.author_name
order by sum(sold_copies) desc
limit 3;