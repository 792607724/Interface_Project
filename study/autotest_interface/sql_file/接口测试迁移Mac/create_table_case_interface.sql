CREATE TABLE case_interface (
id INT ( 2 ) NOT NULL AUTO_INCREMENT,
name_interface VARCHAR ( 128 ) NOT NULL COMMENT '接口名称',
exe_level INT ( 2 ) DEFAULT NULL COMMENT '执行优先级，0代表BVT',
exe_mode VARCHAR ( 4 ) DEFAULT NULL COMMENT '执行方式：POST、GET，默认是POST方式',
url_interface VARCHAR ( 128 ) DEFAULT NULL COMMENT '接口地址：直接使用HTTP开头的详细地址',
header_interface text COMMENT '接口请求的头文件，有则使用，无则不用',
params_interface VARCHAR ( 256 ) DEFAULT NULL COMMENT '接口请求的参数',
result_interface text COMMENT '接口返回结果',
code_to_compare VARCHAR ( 16 ) DEFAULT NULL COMMENT '待比较的Code值，用户自定义比较值，例如ReturnCode和Code等，默认ReturnCode',
code_actual VARCHAR ( 16 ) DEFAULT NULL COMMENT '接口实际Code返回值',
code_expect VARCHAR ( 16 ) DEFAULT NULL COMMENT '接口预期Code返回值',
result_code_compare INT ( 2 ) DEFAULT NULL COMMENT 'Code比较结果，1-pass，0-fail，2-无待比较参数，3-比较出错，4-返回包不合法，9-系统异常',
params_to_compare VARCHAR ( 256 ) DEFAULT NULL COMMENT '接口比较参数集合，用于比较参数的完整性',
params_actual text COMMENT '接口实际返回参数',
result_params_compare INT ( 2 ) DEFAULT NULL COMMENT '参数完整性比较结果，1-pass，0-fail，2-获取参数集错误，9-系统异常',
case_status INT ( 2 ) DEFAULT 0 COMMENT '用例状态，1-有效，0-无效',
create_time TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
update_time TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
PRIMARY KEY ( id ) 
) ENGINE = INNODB auto_increment = 1 DEFAULT charset = utf8 COMMENT = '接口用例表';
INSERT INTO case_interface ( name_interface, exe_level, exe_mode, url_interface, header_interface, params_interface, code_to_compare, code_expect, params_to_compare, case_status, create_time, update_time )
VALUES
	(
	'getIpInfo.php',
	0,
	'GET',
	'https://ip.taobao.com/ipSearch',
	'{\'Host\':\'ip.taobao.com\'}',
	'ipAddr=63.223.108.4',
	'code',
	'0',
	'[\'code\',\'data\',\'country\']',
	1,
	NOW( ),
	NOW( ) 
	);