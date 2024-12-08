-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | num         | varchar |
-- +-------------+---------+
-- In SQL, id is the primary key for this table.
-- id is an autoincrement column starting from 1.

 

-- Find all numbers that appear at least three times consecutively.

-- Return the result table in any order.

The result format is in the following example.


-- Write your PostgreSQL query statement below

WITH previous_value as (
    SELECT
        lag(num, 1) over () as previous,
        lead(num, 1) over () as thenext,
        lag(id, 1) over () as previous_id,
        lead(id, 1) over () as next_id,
        num,
        id
    from Logs
    order by id
), equal_to_previous_and_next as (
    SELECT 
        num,
        id,
        previous,
        thenext,
        previous_id,
        next_id
    from previous_value
    where (previous = num and num = thenext) or previous is null
), consecutive_nums as (
    SELECT
        distinct(num) as ConsecutiveNums
    from equal_to_previous_and_next
    where id - 1 = previous_id and id + 1 = next_id
)
SELECT 
    * 
FROM consecutive_nums
