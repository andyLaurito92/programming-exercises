-- The most consecutive 20 pts seasons

-- select column_name, data_type from information_schema.columns where table_name = 'player_seasons'

with players_with_20pts as (
	select player_name, pts, season from player_seasons ps 
	where pts >= 20.0
	order by player_name, season
), 
players_with_prev_seasons as (
	select 
		*,
		lag(season, 1) over (partition by player_name) as prev_season
	from players_with_20pts
),
consecutive_seasons as (
	select *
	from players_with_prev_seasons
	where season = prev_season + 1 or prev_season is null
), 
rank_consecutive_seasons as (
	select 
		*,
		rank() over (partition by player_name order by season) as consecutive_seasons
	from consecutive_seasons
),
max_consecutive_seasons_with_20_pts as (
	select 
		player_name,
		season,
		pts,
		consecutive_seasons as max_consecutive_seasons
	from rank_consecutive_seasons as rc1
	where consecutive_seasons = (
		select 
			max(consecutive_seasons) 
			from rank_consecutive_seasons rc2 
		where rc2.player_name = rc1.player_name)
	order by max_consecutive_seasons desc
)

 select * from max_consecutive_seasons_with_20_pts limit 20;