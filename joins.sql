-- DROP TABLE Rates;
-- DROP TABLE Continents;

CREATE TABLE Rates (
    FactDate date,
    Country varchar(255),
    MortgageRate float,
    BankLendingRate float 
);

INSERT INTO Rates (FactDate, Country, MortgageRate, BankLendingRate)
VALUES
    ('2021-01-01', 'Blueland', 5.1, 1.1),
    ('2021-02-01', 'Blueland', 5.5, 1.2),
    ('2021-03-01', 'Blueland', 6.1, 2.1),
    ('2021-04-01', 'Blueland', 5.9, 1.7),
    ('2021-01-01', 'Lavendaria', 7.2, 0.3),
    ('2021-02-01', 'Lavendaria', 5.6, 0.3),
    ('2021-03-01', 'Lavendaria', 6.8, 0.31),
    ('2021-04-01', 'Lavendaria', 9, 0.32),
    ('2021-01-01', 'Elfoa', 2.1, 2.05),
    ('2021-02-01', 'Elfoa', 2.1, 1.9),
    ('2021-03-01', 'Elfoa', 2.3, 1.8),
    ('2021-04-01', 'Elfoa', 2.31, 1.95);

CREATE TABLE Continents (
    Country varchar(255),
    Continent varchar(255)
)
INSERT INTO Continents (Country, Continent)
VALUES
    ('Blueland','Coloraven'),
    ('Lavendaria','Coloraven'),
    ('Elfoa','Disenchanta');

SELECT Continents.Continent, Rates.Country, MortgageRate 
FROM RATES
INNER JOIN Continents on Continents.Country=Rates.Country
WHERE FactDate='2021-01-01'
