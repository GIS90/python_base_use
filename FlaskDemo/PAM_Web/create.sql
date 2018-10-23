drop table if exists UserInfo;

create table UserInfo (
  id integer primary key autoincrement,
  title string not null,
  text string not null
);