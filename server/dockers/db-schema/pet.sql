CREATE DATABASE pets;

USE pets;

CREATE TABLE dogs(
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(200) NOT NULL, 
    PRIMARY KEY (id), 
    INDEX (name)
    );

CREATE TABLE cats( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(200) NOT NULL, 
    PRIMARY KEY (id), 
    INDEX (name)
    );