CREATE DATABASE IF NOT EXISTS master_python; --Creame una base de dato si esque no existe;
use master_python; -- Para usar la base de datos;

CREATE TABLE usuarios( -- Para crear la primera tabla;
                        --se auto incrementa solo y este campo no puede estar vacio;  
    id           int (25) auto_increment not null, -- Identifica a cada usuario;
    nombre       varchar(100), -- Puede tener mas de 100 carecteres;
    apellidos    varchar(100), -- Puede tener mas de 100 carecteres;
    email        varchar(255) not null, -- Todos los usuarios tiene que tener uno;
    password     varchar(255) not null, -- Todos los usuarios tiene que tener uno;
    fecha        date not null,  -- Para guardar la fecha de cada usuairo registrado;
    -- Restricciones que teine mi tabla;
    -- Clave primaria
    CONSTRAINT   pk_usuarios PRIMARY KEY(id), -- La clave primaria es pk_usuarios, 
    --el campo identificador va a hacer la clave primaria;
    -- Campo unico
    CONSTRAINT   uq_email UNIQUE(email) -- el email no puede repetirse
 -- Va a mantener la relacion entre  diferentes tablas
)ENGINE=InnoDb;

CREATE TABLE notas(
    id          int (25) auto_increment not null, -- Identifica a cada usuario;
    usuario_id  int (25) not null, -- Esta guardadno el id del usuario que a creado una nota en concreto;
    titulo      varchar(225) not null, --Va guardar el titulo de la nota
    descripcion MEDIUMTEXT, --permite tener muchos datos adentro
    fecha       date not null, 
    -- Restricciones 
    CONSTRAINT  pk_notas PRIMARY KEY(id), -- ;
    CONSTRAINT  fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id) -- Relaciona el campo usuario_id con la tabla usario y el campo
    -- id, dentro del usuario_id voy a guardar el id de la tabla usuario ;
    
)ENGINE=InnoDb;
