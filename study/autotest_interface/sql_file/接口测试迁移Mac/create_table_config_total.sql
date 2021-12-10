CREATE TABLE config_total (
id INT ( 2 ) NOT NULL AUTO_INCREMENT,
key_config VARCHAR ( 128 ) DEFAULT NULL COMMENT '关键字名称',
value_config text COMMENT '关键字值',
description VARCHAR ( 128 ) DEFAULT NULL COMMENT '关键字解释信息',
STATUS INT ( 2 ) DEFAULT NULL COMMENT '配置文件状态，1-有效，0-无效',
create_time TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
update_time TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
PRIMARY KEY ( id ) 
) ENGINE = INNODB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8 COMMENT = '接口测试配置表';

INSERT INTO config_total ( key_config, value_config, description, status )
VALUES
	( 'test', 'value_test', '测试配置', '1' );