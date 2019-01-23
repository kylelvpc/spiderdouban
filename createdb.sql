
drop table dianying;
create table dianying (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  img_url VARCHAR(100) NOT NULL COMMENT '图片链接',
  title VARCHAR(100) NOT NULL COMMENT '电影标题',
  actor VARCHAR(100) NOT NULL COMMENT '导演',
  type_ VARCHAR(100) NOT NULL COMMENT '电影类型',
  score VARCHAR(100) NOT NULL COMMENT '得分',
  quote_ VARCHAR(100) NOT NULL COMMENT '评论',
  PRIMARY KEY (id))
COLLATE='utf8_general_ci'
ENGINE=MyISAM
