CREATE SEQUENCE materiau_id_seq;

CREATE TABLE materiau (
                id INTEGER NOT NULL DEFAULT nextval('materiau_id_seq'),
                nom VARCHAR NOT NULL,
                reference VARCHAR NOT NULL,
                e1 DOUBLE PRECISION NOT NULL,
                e2 DOUBLE PRECISION,
                g12 DOUBLE PRECISION,
                v12 DOUBLE PRECISION,
                s11_t DOUBLE PRECISION,
                s22_t DOUBLE PRECISION,
                s11_c DOUBLE PRECISION,
                s22_c DOUBLE PRECISION,
                s12 DOUBLE PRECISION,
                CONSTRAINT materiau_pk PRIMARY KEY (id)
);


ALTER SEQUENCE materiau_id_seq OWNED BY materiau.id;
