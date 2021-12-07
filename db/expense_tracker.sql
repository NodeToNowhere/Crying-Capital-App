DROP TABLE transactions;
DROP TABLE tags;
DROP TABLE merchants;

CREATE TABLE merchants(
    id SERIAL PRIMARY KEY,
    merchant VARCHAR(63)
);
CREATE TABLE tags(id SERIAL PRIMARY KEY, tag VARCHAR(63));

CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    amount INT,
    date VARCHAR(31),
    description TEXT,
    merchant_id INT NULL REFERENCES merchants(id),
        tag_id INT NULL REFERENCES tags(id)
);