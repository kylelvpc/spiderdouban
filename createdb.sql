
drop table dianying;
create table dianying (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  img_url VARCHAR(100) NOT NULL COMMENT 'ͼƬ����',
  title VARCHAR(100) NOT NULL COMMENT '��Ӱ����',
  actor VARCHAR(100) NOT NULL COMMENT '����',
  type_ VARCHAR(100) NOT NULL COMMENT '��Ӱ����',
  score VARCHAR(100) NOT NULL COMMENT '�÷�',
  quote_ VARCHAR(100) NOT NULL COMMENT '����',
  PRIMARY KEY (id))
COLLATE='utf8_general_ci'
ENGINE=MyISAM
