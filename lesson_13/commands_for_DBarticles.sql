select * from comment;
INSERT INTO article  VALUES (3, 1, 'doil book', 'character', 'watson');
INSERT INTO article  VALUES (4, 2, 'vii', 'philosoph', 'homa');
INSERT INTO comment  VALUES (9, 3, 'ezhik', 'no oke', '2');
INSERT INTO comment  VALUES (10, 3, 'polibn', 'normal', '8');
INSERT INTO comment  VALUES (11, 3, 'pux', 'superrrr', '10');
INSERT INTO comment  VALUES (12, 3, 'dupa', 'nice!', '9');
INSERT INTO comment  VALUES (13, 4, 'alex', 'xmmmm', '4');
INSERT INTO comment  VALUES (14, 4, 'bubad', 'no good', '3');
INSERT INTO comment  VALUES (15, 4, 'sopew', 'wonderfull', '7');
INSERT INTO comment  VALUES (16, 4, 'ds', 'buuuuu', '0');
select name, article.head from author inner join article on author.id=article.author_id;
select name, article.content from author inner join article on author.id=article.author_id;
select head, AVG(comment.rating) as article_rating from article join comment
on article.id=comment.article_id group by head;
