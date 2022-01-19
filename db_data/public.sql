/*
 Navicat Premium Data Transfer

 Source Server         : myserver_postgres
 Source Server Type    : PostgreSQL
 Source Server Version : 130004
 Source Host           : 101.35.152.20:35432
 Source Catalog        : restaurant
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 130004
 File Encoding         : 65001

 Date: 19/01/2022 22:05:32
*/


-- ----------------------------
-- Type structure for rate_enum
-- ----------------------------
DROP TYPE IF EXISTS "public"."rate_enum";
CREATE TYPE "public"."rate_enum" AS ENUM (
  'good',
  'ok',
  'bad'
);
ALTER TYPE "public"."rate_enum" OWNER TO "restuser";

-- ----------------------------
-- Type structure for role_enum
-- ----------------------------
DROP TYPE IF EXISTS "public"."role_enum";
CREATE TYPE "public"."role_enum" AS ENUM (
  'user',
  'admin'
);
ALTER TYPE "public"."role_enum" OWNER TO "restuser";

-- ----------------------------
-- Sequence structure for tb_account_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tb_account_id_seq";
CREATE SEQUENCE "public"."tb_account_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tb_address_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tb_address_id_seq";
CREATE SEQUENCE "public"."tb_address_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tb_comment_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tb_comment_id_seq";
CREATE SEQUENCE "public"."tb_comment_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tb_discount_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tb_discount_id_seq";
CREATE SEQUENCE "public"."tb_discount_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tb_dish_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tb_dish_id_seq";
CREATE SEQUENCE "public"."tb_dish_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tb_dishimg_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tb_dishimg_id_seq";
CREATE SEQUENCE "public"."tb_dishimg_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tb_order_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tb_order_id_seq";
CREATE SEQUENCE "public"."tb_order_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tb_tag_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tb_tag_id_seq";
CREATE SEQUENCE "public"."tb_tag_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tb_user_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tb_user_id_seq";
CREATE SEQUENCE "public"."tb_user_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS "public"."alembic_version";
CREATE TABLE "public"."alembic_version" (
  "version_num" varchar(32) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO "public"."alembic_version" VALUES ('7beccd47c4a3');

-- ----------------------------
-- Table structure for rs_dish_order
-- ----------------------------
DROP TABLE IF EXISTS "public"."rs_dish_order";
CREATE TABLE "public"."rs_dish_order" (
  "dish_id" int4 NOT NULL,
  "order_id" int4 NOT NULL
)
;

-- ----------------------------
-- Records of rs_dish_order
-- ----------------------------

-- ----------------------------
-- Table structure for rs_dish_tag
-- ----------------------------
DROP TABLE IF EXISTS "public"."rs_dish_tag";
CREATE TABLE "public"."rs_dish_tag" (
  "dish_id" int4 NOT NULL,
  "tag_id" int4 NOT NULL
)
;

-- ----------------------------
-- Records of rs_dish_tag
-- ----------------------------
INSERT INTO "public"."rs_dish_tag" VALUES (1, 1);
INSERT INTO "public"."rs_dish_tag" VALUES (3, 4);
INSERT INTO "public"."rs_dish_tag" VALUES (2, 8);
INSERT INTO "public"."rs_dish_tag" VALUES (4, 5);
INSERT INTO "public"."rs_dish_tag" VALUES (2, 5);

-- ----------------------------
-- Table structure for rs_user_tag
-- ----------------------------
DROP TABLE IF EXISTS "public"."rs_user_tag";
CREATE TABLE "public"."rs_user_tag" (
  "user_id" int4 NOT NULL,
  "tag_id" int4 NOT NULL
)
;

-- ----------------------------
-- Records of rs_user_tag
-- ----------------------------

-- ----------------------------
-- Table structure for tb_account
-- ----------------------------
DROP TABLE IF EXISTS "public"."tb_account";
CREATE TABLE "public"."tb_account" (
  "id" int4 NOT NULL DEFAULT nextval('tb_account_id_seq'::regclass),
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "user_id" int4,
  "is_vip" bool,
  "start_time" timestamp(6),
  "end_time" timestamp(6),
  "balance" float8
)
;

-- ----------------------------
-- Records of tb_account
-- ----------------------------
INSERT INTO "public"."tb_account" VALUES (2, NULL, NULL, 1, NULL, NULL, NULL, 0);
INSERT INTO "public"."tb_account" VALUES (4, '2022-01-14 19:42:25.361314', NULL, 3, 'f', NULL, NULL, 0);
INSERT INTO "public"."tb_account" VALUES (5, '2022-01-16 21:23:21.54315', NULL, 4, 'f', NULL, NULL, 0);

-- ----------------------------
-- Table structure for tb_address
-- ----------------------------
DROP TABLE IF EXISTS "public"."tb_address";
CREATE TABLE "public"."tb_address" (
  "id" int4 NOT NULL DEFAULT nextval('tb_address_id_seq'::regclass),
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "name" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "phone" varchar(11) COLLATE "pg_catalog"."default" NOT NULL,
  "location" json NOT NULL,
  "is_default" bool,
  "user_id" int4
)
;

-- ----------------------------
-- Records of tb_address
-- ----------------------------

-- ----------------------------
-- Table structure for tb_comment
-- ----------------------------
DROP TABLE IF EXISTS "public"."tb_comment";
CREATE TABLE "public"."tb_comment" (
  "id" int4 NOT NULL DEFAULT nextval('tb_comment_id_seq'::regclass),
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "content" varchar(512) COLLATE "pg_catalog"."default",
  "user_id" int4,
  "order_id" int4,
  "rate" "public"."rate_enum"
)
;

-- ----------------------------
-- Records of tb_comment
-- ----------------------------

-- ----------------------------
-- Table structure for tb_discount
-- ----------------------------
DROP TABLE IF EXISTS "public"."tb_discount";
CREATE TABLE "public"."tb_discount" (
  "id" int4 NOT NULL DEFAULT nextval('tb_discount_id_seq'::regclass),
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "discount_type" int4 NOT NULL,
  "description" varchar(200) COLLATE "pg_catalog"."default" NOT NULL,
  "start_time" timestamp(6),
  "end_time" timestamp(6),
  "discount" float8
)
;

-- ----------------------------
-- Records of tb_discount
-- ----------------------------
INSERT INTO "public"."tb_discount" VALUES (1, '2022-01-19 22:00:56', NULL, 0, '无折扣', NULL, NULL, NULL);
INSERT INTO "public"."tb_discount" VALUES (2, '2022-01-19 22:00:56', NULL, 0, '无折扣', NULL, NULL, NULL);
INSERT INTO "public"."tb_discount" VALUES (3, '2022-01-19 22:00:56', NULL, 0, '无折扣', NULL, NULL, NULL);
INSERT INTO "public"."tb_discount" VALUES (4, '2022-01-19 22:00:56', NULL, 1, '95折', '2022-01-19 22:02:15', '2022-02-06 22:02:17', 0.95);

-- ----------------------------
-- Table structure for tb_dish
-- ----------------------------
DROP TABLE IF EXISTS "public"."tb_dish";
CREATE TABLE "public"."tb_dish" (
  "id" int4 NOT NULL DEFAULT nextval('tb_dish_id_seq'::regclass),
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "name" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "price" float8,
  "amount" int4,
  "description" varchar(256) COLLATE "pg_catalog"."default",
  "discount_id" int4
)
;

-- ----------------------------
-- Records of tb_dish
-- ----------------------------
INSERT INTO "public"."tb_dish" VALUES (1, '2022-01-14 19:31:44', NULL, '佛跳墙', 299, 100, '微辣，孜然味浓郁', 1);
INSERT INTO "public"."tb_dish" VALUES (4, '2022-01-14 22:48:51', NULL, '土豆丝', 35, 20, '青椒土豆丝', 4);
INSERT INTO "public"."tb_dish" VALUES (3, '2022-01-14 22:47:59', NULL, '鱼香茄子', 43.5, 10, '酸甜鱼香茄子, 又耙又糯', 2);
INSERT INTO "public"."tb_dish" VALUES (2, '2022-01-14 22:48:09', NULL, '回锅肉', 98.88, 59, '香辣不腻, 好吃的很', 3);

-- ----------------------------
-- Table structure for tb_dishimg
-- ----------------------------
DROP TABLE IF EXISTS "public"."tb_dishimg";
CREATE TABLE "public"."tb_dishimg" (
  "id" int4 NOT NULL DEFAULT nextval('tb_dishimg_id_seq'::regclass),
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "is_index" bool,
  "uri" varchar(512) COLLATE "pg_catalog"."default" NOT NULL,
  "dish_id" int4
)
;

-- ----------------------------
-- Records of tb_dishimg
-- ----------------------------
INSERT INTO "public"."tb_dishimg" VALUES (3, '2022-01-14 22:44:55', NULL, 't', '/static/dish/ftq.jpg', 1);
INSERT INTO "public"."tb_dishimg" VALUES (4, '2022-01-14 22:49:41', NULL, 't', '/static/dish/hgr.jpg', 2);
INSERT INTO "public"."tb_dishimg" VALUES (5, '2022-01-14 22:50:40', NULL, 't', '/static/dish/tds.jpg', 4);
INSERT INTO "public"."tb_dishimg" VALUES (6, '2022-01-14 22:51:15', NULL, 't', '/static/dish/yxqz.jpg', 3);
INSERT INTO "public"."tb_dishimg" VALUES (7, '2022-01-14 22:53:04', NULL, 'f', '/static/dish/yxqz2.jpg', 3);
INSERT INTO "public"."tb_dishimg" VALUES (8, '2022-01-14 22:53:25', NULL, 'f', '/static/dish/yxqz3.jpg', 3);
INSERT INTO "public"."tb_dishimg" VALUES (9, '2022-01-14 22:53:48', NULL, 'f', '/static/dish/yxqz4.jpg', 3);

-- ----------------------------
-- Table structure for tb_order
-- ----------------------------
DROP TABLE IF EXISTS "public"."tb_order";
CREATE TABLE "public"."tb_order" (
  "id" int4 NOT NULL DEFAULT nextval('tb_order_id_seq'::regclass),
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "money" float8,
  "status" int4,
  "note" varchar(256) COLLATE "pg_catalog"."default",
  "dish_amount" json NOT NULL,
  "user_id" int4,
  "address_id" int4
)
;

-- ----------------------------
-- Records of tb_order
-- ----------------------------

-- ----------------------------
-- Table structure for tb_tag
-- ----------------------------
DROP TABLE IF EXISTS "public"."tb_tag";
CREATE TABLE "public"."tb_tag" (
  "id" int4 NOT NULL DEFAULT nextval('tb_tag_id_seq'::regclass),
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "weight" int4,
  "name" varchar(32) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of tb_tag
-- ----------------------------
INSERT INTO "public"."tb_tag" VALUES (1, '2021-11-27 22:13:42.991576', NULL, 1, '蛋糕');
INSERT INTO "public"."tb_tag" VALUES (2, '2021-11-27 22:13:43.004755', NULL, 1, '奶茶');
INSERT INTO "public"."tb_tag" VALUES (3, '2021-11-27 22:13:43.010333', NULL, 1, '碳酸饮料');
INSERT INTO "public"."tb_tag" VALUES (4, '2021-11-27 22:13:43.014163', NULL, 1, '偏甜');
INSERT INTO "public"."tb_tag" VALUES (5, '2021-11-27 22:13:43.018164', NULL, 1, '咸香');
INSERT INTO "public"."tb_tag" VALUES (6, '2021-11-27 22:13:43.022146', NULL, 1, '香辣');
INSERT INTO "public"."tb_tag" VALUES (7, '2021-11-27 22:13:43.026788', NULL, 1, '麻辣');
INSERT INTO "public"."tb_tag" VALUES (8, '2021-11-27 22:13:43.030805', NULL, 1, '特辣');
INSERT INTO "public"."tb_tag" VALUES (9, '2021-11-27 22:13:43.035913', NULL, 1, '微辣');
INSERT INTO "public"."tb_tag" VALUES (10, '2021-11-27 22:13:43.040861', NULL, 1, '中辣');
INSERT INTO "public"."tb_tag" VALUES (11, '2021-11-27 22:13:43.046859', NULL, 1, '广东辣');
INSERT INTO "public"."tb_tag" VALUES (12, '2021-11-27 22:13:43.051077', NULL, 1, '少油');
INSERT INTO "public"."tb_tag" VALUES (13, '2021-11-27 22:13:43.055596', NULL, 1, '少盐');
INSERT INTO "public"."tb_tag" VALUES (14, '2021-11-27 22:13:43.059639', NULL, 1, '少糖');
INSERT INTO "public"."tb_tag" VALUES (15, '2021-11-27 22:13:43.063922', NULL, 1, '甜点');
INSERT INTO "public"."tb_tag" VALUES (16, '2021-11-27 22:13:43.068094', NULL, 1, '海鲜');
INSERT INTO "public"."tb_tag" VALUES (17, '2021-11-27 22:13:43.071835', NULL, 1, '生鲜');
INSERT INTO "public"."tb_tag" VALUES (18, '2021-11-27 22:13:43.076095', NULL, 1, '五香');
INSERT INTO "public"."tb_tag" VALUES (19, '2021-11-27 22:13:43.080005', NULL, 1, '糖醋');

-- ----------------------------
-- Table structure for tb_user
-- ----------------------------
DROP TABLE IF EXISTS "public"."tb_user";
CREATE TABLE "public"."tb_user" (
  "id" int4 NOT NULL DEFAULT nextval('tb_user_id_seq'::regclass),
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "nickname" varchar(128) COLLATE "pg_catalog"."default",
  "age" int4,
  "phone" varchar(11) COLLATE "pg_catalog"."default" NOT NULL,
  "avatar" varchar(512) COLLATE "pg_catalog"."default",
  "email" varchar(128) COLLATE "pg_catalog"."default",
  "password" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "gender" bool,
  "is_new" bool,
  "is_email_active" bool,
  "role" "public"."role_enum"
)
;

-- ----------------------------
-- Records of tb_user
-- ----------------------------
INSERT INTO "public"."tb_user" VALUES (3, '2022-01-14 19:42:25.349771', NULL, '隔壁大王', 120, '18228598311', '/static/avatar/default.jpg', 'liuyang@163.com', '95irFL94EdrlGa7DvayiEBoC30a1ninkTPZWb7xT2pY=
', 't', 't', 'f', 'user');
INSERT INTO "public"."tb_user" VALUES (1, NULL, '2021-12-19 15:59:29.467883', 'admin', 20, '13433334444', '/static/avatar/6ea1ebed100443f697d6921594d9f19a.jpeg', 'test@email.com', '95irFL94EdrlGa7DvayiEO0WqhTjGZlKM2hv5YuaI0I=
', 't', 't', 't', 'admin');
INSERT INTO "public"."tb_user" VALUES (4, '2022-01-16 21:23:21.526575', NULL, 'JQK', 23, '13533335555', '/static/avatar/default.jpg', 'email@test.com', '95irFL94EdrlGa7DvayiECG3DhN30wkNzDCGPXyVsXk=
', 'f', 't', 'f', 'user');

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tb_account_id_seq"
OWNED BY "public"."tb_account"."id";
SELECT setval('"public"."tb_account_id_seq"', 6, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tb_address_id_seq"
OWNED BY "public"."tb_address"."id";
SELECT setval('"public"."tb_address_id_seq"', 4, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tb_comment_id_seq"
OWNED BY "public"."tb_comment"."id";
SELECT setval('"public"."tb_comment_id_seq"', 4, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tb_discount_id_seq"
OWNED BY "public"."tb_discount"."id";
SELECT setval('"public"."tb_discount_id_seq"', 5, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tb_dish_id_seq"
OWNED BY "public"."tb_dish"."id";
SELECT setval('"public"."tb_dish_id_seq"', 5, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tb_dishimg_id_seq"
OWNED BY "public"."tb_dishimg"."id";
SELECT setval('"public"."tb_dishimg_id_seq"', 10, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tb_order_id_seq"
OWNED BY "public"."tb_order"."id";
SELECT setval('"public"."tb_order_id_seq"', 4, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tb_tag_id_seq"
OWNED BY "public"."tb_tag"."id";
SELECT setval('"public"."tb_tag_id_seq"', 4, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tb_user_id_seq"
OWNED BY "public"."tb_user"."id";
SELECT setval('"public"."tb_user_id_seq"', 5, true);

-- ----------------------------
-- Primary Key structure for table alembic_version
-- ----------------------------
ALTER TABLE "public"."alembic_version" ADD CONSTRAINT "alembic_version_pkc" PRIMARY KEY ("version_num");

-- ----------------------------
-- Primary Key structure for table rs_dish_order
-- ----------------------------
ALTER TABLE "public"."rs_dish_order" ADD CONSTRAINT "rs_dish_order_pkey" PRIMARY KEY ("dish_id", "order_id");

-- ----------------------------
-- Primary Key structure for table rs_dish_tag
-- ----------------------------
ALTER TABLE "public"."rs_dish_tag" ADD CONSTRAINT "rs_dish_tag_pkey" PRIMARY KEY ("dish_id", "tag_id");

-- ----------------------------
-- Primary Key structure for table rs_user_tag
-- ----------------------------
ALTER TABLE "public"."rs_user_tag" ADD CONSTRAINT "rs_user_tag_pkey" PRIMARY KEY ("user_id", "tag_id");

-- ----------------------------
-- Primary Key structure for table tb_account
-- ----------------------------
ALTER TABLE "public"."tb_account" ADD CONSTRAINT "tb_account_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tb_address
-- ----------------------------
ALTER TABLE "public"."tb_address" ADD CONSTRAINT "tb_address_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tb_comment
-- ----------------------------
ALTER TABLE "public"."tb_comment" ADD CONSTRAINT "tb_comment_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tb_discount
-- ----------------------------
ALTER TABLE "public"."tb_discount" ADD CONSTRAINT "tb_discount_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tb_dish
-- ----------------------------
ALTER TABLE "public"."tb_dish" ADD CONSTRAINT "tb_dish_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tb_dishimg
-- ----------------------------
ALTER TABLE "public"."tb_dishimg" ADD CONSTRAINT "tb_dishimg_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tb_order
-- ----------------------------
ALTER TABLE "public"."tb_order" ADD CONSTRAINT "tb_order_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table tb_tag
-- ----------------------------
ALTER TABLE "public"."tb_tag" ADD CONSTRAINT "tb_tag_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table tb_tag
-- ----------------------------
ALTER TABLE "public"."tb_tag" ADD CONSTRAINT "tb_tag_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table tb_user
-- ----------------------------
ALTER TABLE "public"."tb_user" ADD CONSTRAINT "tb_user_email_key" UNIQUE ("email");
ALTER TABLE "public"."tb_user" ADD CONSTRAINT "tb_user_phone_key" UNIQUE ("phone");

-- ----------------------------
-- Primary Key structure for table tb_user
-- ----------------------------
ALTER TABLE "public"."tb_user" ADD CONSTRAINT "tb_user_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table rs_dish_order
-- ----------------------------
ALTER TABLE "public"."rs_dish_order" ADD CONSTRAINT "rs_dish_order_dish_id_fkey" FOREIGN KEY ("dish_id") REFERENCES "public"."tb_dish" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."rs_dish_order" ADD CONSTRAINT "rs_dish_order_order_id_fkey" FOREIGN KEY ("order_id") REFERENCES "public"."tb_order" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table rs_dish_tag
-- ----------------------------
ALTER TABLE "public"."rs_dish_tag" ADD CONSTRAINT "rs_dish_tag_dish_id_fkey" FOREIGN KEY ("dish_id") REFERENCES "public"."tb_dish" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."rs_dish_tag" ADD CONSTRAINT "rs_dish_tag_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tb_tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table rs_user_tag
-- ----------------------------
ALTER TABLE "public"."rs_user_tag" ADD CONSTRAINT "rs_user_tag_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tb_tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."rs_user_tag" ADD CONSTRAINT "rs_user_tag_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."tb_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tb_account
-- ----------------------------
ALTER TABLE "public"."tb_account" ADD CONSTRAINT "tb_account_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."tb_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tb_address
-- ----------------------------
ALTER TABLE "public"."tb_address" ADD CONSTRAINT "tb_address_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."tb_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tb_comment
-- ----------------------------
ALTER TABLE "public"."tb_comment" ADD CONSTRAINT "tb_comment_order_id_fkey" FOREIGN KEY ("order_id") REFERENCES "public"."tb_order" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tb_comment" ADD CONSTRAINT "tb_comment_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."tb_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tb_dish
-- ----------------------------
ALTER TABLE "public"."tb_dish" ADD CONSTRAINT "tb_dish_discount_id_fkey" FOREIGN KEY ("discount_id") REFERENCES "public"."tb_discount" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tb_dishimg
-- ----------------------------
ALTER TABLE "public"."tb_dishimg" ADD CONSTRAINT "tb_dishimg_dish_id_fkey" FOREIGN KEY ("dish_id") REFERENCES "public"."tb_dish" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tb_order
-- ----------------------------
ALTER TABLE "public"."tb_order" ADD CONSTRAINT "tb_order_address_id_fkey" FOREIGN KEY ("address_id") REFERENCES "public"."tb_address" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tb_order" ADD CONSTRAINT "tb_order_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."tb_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
