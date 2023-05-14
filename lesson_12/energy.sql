--
-- PostgreSQL database dump
--

-- Dumped from database version 14.7 (Ubuntu 14.7-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.7 (Ubuntu 14.7-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product (
    id integer NOT NULL,
    name character varying(255),
    protein smallint,
    fat smallint,
    carbohydrate smallint,
    calorie smallint
);


ALTER TABLE public.product OWNER TO postgres;

--
-- Name: product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_id_seq OWNER TO postgres;

--
-- Name: product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.product_id_seq OWNED BY public.product.id;


--
-- Name: usage_datatime; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usage_datatime (
    product_id integer,
    datatime timestamp without time zone
);


ALTER TABLE public.usage_datatime OWNER TO postgres;

--
-- Name: product id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product ALTER COLUMN id SET DEFAULT nextval('public.product_id_seq'::regclass);


--
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.product (id, name, protein, fat, carbohydrate, calorie) FROM stdin;
1	avocado	2	23	7	223
2	green been	22	2	55	309
3	beef	18	12	0	187
4	milk	3	3	5	58
5	cheese	25	32	0	396
6	honey	1	8	80	308
7	egg	13	12	1	157
\.


--
-- Data for Name: usage_datatime; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usage_datatime (product_id, datatime) FROM stdin;
1	2023-05-02 00:27:00.765293
2	2023-05-01 00:27:00.765293
3	2023-05-03 02:27:00.765293
4	2023-05-05 12:27:00.765293
5	2023-05-21 14:27:00.743293
3	2023-05-25 11:27:00.743293
4	2023-05-26 17:27:00.743293
3	2023-05-25 11:27:00.743293
1	2023-05-29 11:27:00.143293
2	2023-05-29 01:27:00.143293
2	2023-05-29 01:37:00.144293
2	2023-06-29 11:37:50.144293
\.


--
-- Name: product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.product_id_seq', 1, false);


--
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (id);


--
-- Name: usage_datatime usage_datatime_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usage_datatime
    ADD CONSTRAINT usage_datatime_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.product(id);


--
-- PostgreSQL database dump complete
--

