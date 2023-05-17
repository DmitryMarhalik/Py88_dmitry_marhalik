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
-- Name: eating; Type: TABLE; Schema: public; Owner: dm
--

CREATE TABLE public.eating (
    person_id integer,
    product_id integer,
    datetime timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.eating OWNER TO dm;

--
-- Name: person; Type: TABLE; Schema: public; Owner: dm
--

CREATE TABLE public.person (
    id integer NOT NULL,
    name text NOT NULL,
    CONSTRAINT person_id_check CHECK ((id > 0))
);


ALTER TABLE public.person OWNER TO dm;

--
-- Name: product; Type: TABLE; Schema: public; Owner: dm
--

CREATE TABLE public.product (
    id integer NOT NULL,
    title text NOT NULL,
    CONSTRAINT product_id_check CHECK ((id > 0))
);


ALTER TABLE public.product OWNER TO dm;

--
-- Data for Name: eating; Type: TABLE DATA; Schema: public; Owner: dm
--

COPY public.eating (person_id, product_id, datetime) FROM stdin;
1	1	2023-05-17 01:17:16.401846
1	2	2023-05-17 01:17:36.354417
1	3	2023-05-17 01:17:40.833996
1	4	2023-05-17 01:17:44.231417
2	1	2023-05-17 01:17:53.717578
2	2	2023-05-17 01:17:58.302396
2	3	2023-05-17 01:18:01.777008
2	4	2023-05-17 01:18:04.994216
3	1	2023-05-17 01:18:10.4459
3	2	2023-05-17 01:18:14.045922
3	3	2023-05-17 01:18:17.219606
3	4	2023-05-17 01:18:20.336465
4	1	2023-05-17 01:18:25.641366
4	2	2023-05-17 01:18:28.728998
4	3	2023-05-17 01:18:31.745482
4	4	2023-05-17 01:18:34.678904
\.


--
-- Data for Name: person; Type: TABLE DATA; Schema: public; Owner: dm
--

COPY public.person (id, name) FROM stdin;
1	Arkady
2	Violetta
3	Evlampiy
4	Ognezhka
\.


--
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: dm
--

COPY public.product (id, title) FROM stdin;
1	meat
2	spagetti
3	apple
4	potato
\.


--
-- Name: person person_pkey; Type: CONSTRAINT; Schema: public; Owner: dm
--

ALTER TABLE ONLY public.person
    ADD CONSTRAINT person_pkey PRIMARY KEY (id);


--
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: dm
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (id);


--
-- Name: eating eating_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dm
--

ALTER TABLE ONLY public.eating
    ADD CONSTRAINT eating_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.person(id);


--
-- Name: eating eating_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dm
--

ALTER TABLE ONLY public.eating
    ADD CONSTRAINT eating_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.product(id);


--
-- PostgreSQL database dump complete
--

