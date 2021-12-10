/*
 Navicat Premium Data Transfer

 Source Server         : test
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : test_interface

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 10/12/2021 10:59:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for case_interface
-- ----------------------------
DROP TABLE IF EXISTS `case_interface`;
CREATE TABLE `case_interface`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name_interface` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '接口名称',
  `exe_level` int(0) NULL DEFAULT NULL COMMENT '执行优先级，0代表BVT',
  `exe_mode` varchar(4) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '执行方式：POST、GET，默认是POST方式',
  `url_interface` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '接口地址：直接使用HTTP开头的详细地址',
  `header_interface` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '接口请求的头文件，有则使用，无则不用',
  `params_interface` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '接口请求的参数',
  `result_interface` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '接口返回结果',
  `code_to_compare` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '待比较的Code值，用户自定义比较值，例如ReturnCode和Code等，默认ReturnCode',
  `code_actual` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '接口实际Code返回值',
  `code_expect` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '接口预期Code返回值',
  `result_code_compare` int(0) NULL DEFAULT NULL COMMENT 'Code比较结果，1-pass，0-fail，2-无待比较参数，3-比较出错，4-返回包不合法，9-系统异常',
  `params_to_compare` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '接口比较参数集合，用于比较参数的完整性',
  `params_actual` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '接口实际返回参数',
  `result_params_compare` int(0) NULL DEFAULT NULL COMMENT '参数完整性比较结果，1-pass，0-fail，2-获取参数集错误，9-系统异常',
  `case_status` int(0) NULL DEFAULT 0 COMMENT '用例状态，1-有效，0-无效',
  `create_time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '接口用例表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of case_interface
-- ----------------------------
INSERT INTO `case_interface` VALUES (1, 'ipSearch', 0, 'GET', 'https://ip.taobao.com/ipSearch', '{\'Host\':\'ip.taobao.com\'}', 'ipAddr=63.223.108.4', 'http://www.w3.org/1999/xhtml', 'code', NULL, '0', NULL, '[\'code\',\'data\',\'country\']', NULL, NULL, 1, '2021-12-08 14:56:10', '2021-12-10 10:51:39');
INSERT INTO `case_interface` VALUES (2, 'getIpInfo.php', 0, 'GET', 'http://ip.taobao.com/service/getIpInfo.php', '{\'Host\':\'ip.taobao.com\'}', 'ip=63.223.108.4', NULL, 'code', NULL, '0', NULL, '[\'code\',\'data\',\'country\']', NULL, NULL, 1, '2021-12-08 14:56:32', '2021-12-08 14:56:32');

-- ----------------------------
-- Table structure for config_total
-- ----------------------------
DROP TABLE IF EXISTS `config_total`;
CREATE TABLE `config_total`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `key_config` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '关键字名称',
  `value_config` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '关键字值',
  `description` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '关键字解释信息',
  `status` int(0) NULL DEFAULT NULL COMMENT '配置文件状态，1-有效，0-无效',
  `create_time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 35 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '接口测试配置表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of config_total
-- ----------------------------
INSERT INTO `config_total` VALUES (1, 'test', 'value_test', '测试配置', 1, '2021-11-22 15:04:47', '2021-11-22 15:04:47');
INSERT INTO `config_total` VALUES (2, 'test', 'value_test', '测试配置', 1, '2021-11-22 15:06:54', '2021-11-22 15:06:54');
INSERT INTO `config_total` VALUES (3, '3', 'Tom', '1 year 1 class', 6, '2021-11-22 17:52:28', '2021-11-22 17:52:28');
INSERT INTO `config_total` VALUES (4, '3', 'Tom', '1 year 1 class', 6, '2021-11-22 17:52:28', '2021-11-22 17:52:28');
INSERT INTO `config_total` VALUES (5, '5', 'Tom', '1 year 1 class', 6, '2021-11-22 17:53:03', '2021-11-22 17:53:03');
INSERT INTO `config_total` VALUES (6, '6', 'Jimmy', '2 year 2 class', 8, '2021-11-22 17:53:03', '2021-11-22 17:53:03');
INSERT INTO `config_total` VALUES (7, '5', 'Tom', '1 year 1 class', 6, '2021-11-22 17:55:22', '2021-11-22 17:55:22');
INSERT INTO `config_total` VALUES (8, '6', 'Jimmy', '2 year 2 class', 8, '2021-11-22 17:55:22', '2021-11-22 17:55:22');
INSERT INTO `config_total` VALUES (9, '5', 'Tom', '1 year 1 class', 6, '2021-11-22 17:55:27', '2021-11-22 17:55:27');
INSERT INTO `config_total` VALUES (10, '6', 'Jimmy', '2 year 2 class', 8, '2021-11-22 17:55:27', '2021-11-22 17:55:27');
INSERT INTO `config_total` VALUES (11, '5', 'Tom', '1 year 1 class', 6, '2021-11-22 17:56:02', '2021-11-22 17:56:02');
INSERT INTO `config_total` VALUES (12, '6', 'Jimmy', '2 year 2 class', 8, '2021-11-22 17:56:02', '2021-11-22 17:56:02');
INSERT INTO `config_total` VALUES (13, '5', 'Tom', '1 year 1 class', 6, '2021-11-22 17:56:12', '2021-11-22 17:56:12');
INSERT INTO `config_total` VALUES (14, '6', 'Jimmy', '2 year 2 class', 8, '2021-11-22 17:56:12', '2021-11-22 17:56:12');
INSERT INTO `config_total` VALUES (15, '5', 'Tom', '1 year 1 class', 6, '2021-11-22 18:00:28', '2021-11-22 18:00:28');
INSERT INTO `config_total` VALUES (16, '6', 'Jimmy', '2 year 2 class', 8, '2021-11-22 18:00:28', '2021-11-22 18:00:28');
INSERT INTO `config_total` VALUES (17, '5', 'Tom', '1 year 1 class', 6, '2021-11-22 18:00:37', '2021-11-22 18:00:37');
INSERT INTO `config_total` VALUES (18, '6', 'Jimmy', '2 year 2 class', 8, '2021-11-22 18:00:37', '2021-11-22 18:00:37');
INSERT INTO `config_total` VALUES (19, '5', 'Tom', '1 year 1 class', 6, '2021-11-22 18:06:31', '2021-11-22 18:06:31');
INSERT INTO `config_total` VALUES (20, '6', 'Jimmy', '2 year 2 class', 8, '2021-11-22 18:06:31', '2021-11-22 18:06:31');
INSERT INTO `config_total` VALUES (21, '5', 'Tom', '1 year 1 class', 6, '2021-11-22 18:25:31', '2021-11-22 18:25:31');
INSERT INTO `config_total` VALUES (22, '6', 'Jimmy', '2 year 2 class', 8, '2021-11-22 18:25:31', '2021-11-22 18:25:31');
INSERT INTO `config_total` VALUES (23, '5', 'Tom', '1 year 1 class', 6, '2021-11-23 09:38:07', '2021-11-23 09:38:07');
INSERT INTO `config_total` VALUES (24, '6', 'Jimmy', '2 year 2 class', 8, '2021-11-23 09:38:07', '2021-11-23 09:38:07');
INSERT INTO `config_total` VALUES (25, '1', 'Tom', '1 year 1 class', 6, '2021-11-30 09:32:25', '2021-11-30 09:32:25');
INSERT INTO `config_total` VALUES (26, '2', 'Jimmy', '2 year 2 class', 8, '2021-11-30 09:32:25', '2021-11-30 09:32:25');
INSERT INTO `config_total` VALUES (27, '1', 'Tom', '1 year 1 class', 6, '2021-12-08 15:25:02', '2021-12-08 15:25:02');
INSERT INTO `config_total` VALUES (28, '2', 'Jimmy', '2 year 2 class', 8, '2021-12-08 15:25:02', '2021-12-08 15:25:02');
INSERT INTO `config_total` VALUES (29, '1', 'Tom', '1 year 1 class', 6, '2021-12-08 15:25:35', '2021-12-08 15:25:35');
INSERT INTO `config_total` VALUES (30, '2', 'Jimmy', '2 year 2 class', 8, '2021-12-08 15:25:35', '2021-12-08 15:25:35');
INSERT INTO `config_total` VALUES (31, '1', 'Tom', '1 year 1 class', 6, '2021-12-08 15:26:01', '2021-12-08 15:26:01');
INSERT INTO `config_total` VALUES (32, '2', 'Jimmy', '2 year 2 class', 8, '2021-12-08 15:26:01', '2021-12-08 15:26:01');
INSERT INTO `config_total` VALUES (33, '1', 'Tom', '1 year 1 class', 6, '2021-12-08 15:32:14', '2021-12-08 15:32:14');
INSERT INTO `config_total` VALUES (34, '2', 'Jimmy', '2 year 2 class', 8, '2021-12-08 15:32:14', '2021-12-08 15:32:14');

SET FOREIGN_KEY_CHECKS = 1;
