drop table if EXISTS page_content;
drop table if EXISTS url_uncrawl;

create TABLE page_content (
  url VARCHAR(100) not NULL UNIQUE ,
  content MEDIUMTEXT,
  crl_time timestamp NOT NULL default CURRENT_TIMESTAMP
)engine=MyISAM DEFAULT charset=utf8;

CREATE TABLE url_uncrawl (
  url VARCHAR(100) not NULL UNIQUE
)engine=MyISAM DEFAULT charset=utf8;

