## Task 2
Command Line:
```sql
CREATE DATABASE website;

CREATE TABLE member ( 
    id bigint PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID', 
    name varchar(255) NOT NULL COMMENT 'Name', 
    username varchar(255) NOT NULL COMMENT 'Username', 
    password varchar(255) NOT NULL COMMENT 'Password',
    follower_count int unsigned NOT NULL DEFAULT 0 COMMENT 'Follower Count',
    time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time' ) COMMENT 'Description';
```
![結果](/Users/becca/Desktop/Week5/task2.png)

## Task3

INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.
SELECT all rows from the member table.
```sql
INSERT INTO member (name, username, password)
VALUES ('test', 'test', 'test'),
       ('John', 'john123', 'password123'),
       ('Alice', 'alice456', 'password456'),
       ('Bob', 'bob789', 'password789'),
       ('Emily', 'emily012', 'password012');

SELECT * FROM member
```
![](/Users/becca/Desktop/Week5/t3.1.png)

SELECT all rows from the member table, in descending order of time.
```sql
SELECT * FROM member ORDER BY time DESC;
```
![](/Users/becca/Desktop/Week5/t3.3.png)

SELECT total 3 rows, second to fourth, from the member table, in descending order
of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
```sql
SELECT * FROM member 
ORDER BY time DESC
LIMIT 1, 3;
```
![](/Users/becca/Desktop/Week5/t3.4.png)

SELECT rows where username equals to test.
```sql
SELECT * FROM member WHERE username = "test";
```
![](/Users/becca/Desktop/Week5/t3.5.png)

SELECT rows where name includes the es keyword.
```sql
SELECT * FROM member WHERE username LIKE "%es%";
```
![](/Users/becca/Desktop/Week5/t3.6.png)

SELECT rows where both username and password equal to test.
```sql
SELECT * FROM member WHERE username = "test" and password = "test";
```
![](/Users/becca/Desktop/Week5/t3.7.png)

UPDATE data in name column to test2 where username equals to test.
```sql
UPDATE member
SET name = 'test2' WHERE username = 'test';
```
![](/Users/becca/Desktop/Week5/t3.8.png)

## Task4
SELECT how many rows from the member table.
```sql
select count(*) from member;
```
![](/Users/becca/Desktop/Week5/t4.1.png)


`插播：前面沒assign follower_count，在這新增`
```sql
UPDATE member
SET follower_count = floor(rand()*10);
```
![](/Users/becca/Desktop/Week5/t4.png)

SELECT the sum of follower_count of all the rows from the member table.  
```sql
select sum(follower_count) from member;
```
![](/Users/becca/Desktop/Week5/t4.2.png)

SELECT the average of follower_count of all the rows from the member table.
```sql
select avg(follower_count) from member;
```
![](/Users/becca/Desktop/Week5/t4.3.png)

SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
```sql
select avg(follower_count) from(
    select follower_count
    from member 
    order by follower_count desc 
    limit 2) as top_2 ;

```
![](/Users/becca/Desktop/Week5/t4.4.png)


## Task5
Create a new table named message, in the website database.
```sql
CREATE TABLE message ( 
    id bigint PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID', 
    member_id bigint NOT NULL COMMENT 'Member ID for Message Sender', 
    FOREIGN KEY (member_id) REFERENCES member(id),
    content varchar(255) NOT NULL COMMENT 'Content', 
    like_count int unsigned NOT NULL DEFAULT 0 COMMENT 'Like Count',
    time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time' ) COMMENT 'Publish Time';
```
![](/Users/becca/Desktop/Week5/t5.1.png)


SELECT all messages, including sender names. We have to JOIN the member table to get that.
```sql
INSERT INTO message (member_id, content, like_count)
VALUES (1, 'one two three', 4),
       (3, 'hello world', 10),
       (1, 'four five six', 12),
       (5, 'hi', 2),
       (5, 'bye', 5);

select message.*, member.name from message
left join member on message.member_id = member.id;
```
![](/Users/becca/Desktop/Week5/t5.2.png)

SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
```sql
select message.*, member.name from message
left join member on message.member_id = member.id
where member.name = 'test';
```
![](/Users/becca/Desktop/Week5/t5.3.png)

Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
```sql
select member.username, avg(message.like_count) as avg_like 
from message
left join member on message.member_id = member.id
where member.username = 'test';
```
![](/Users/becca/Desktop/Week5/t5.4.png)

Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
```sql
select member.username,avg(message.like_count) as avg_like 
from message
left join member on message.member_id = member.id
group by member.username;
```
![](/Users/becca/Desktop/Week5/t5.5.png)

