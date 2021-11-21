/*
 Navicat Premium Data Transfer

 Source Server         : WSL_postgresql
 Source Server Type    : PostgreSQL
 Source Server Version : 140000
 Source Host           : localhost:35432
 Source Catalog        : restaurant
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 140000
 File Encoding         : 65001

 Date: 21/11/2021 13:25:34
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
-- Sequence structure for account_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."account_id_seq";
CREATE SEQUENCE "public"."account_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for address_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."address_id_seq";
CREATE SEQUENCE "public"."address_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for comment_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."comment_id_seq";
CREATE SEQUENCE "public"."comment_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for discount_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."discount_id_seq";
CREATE SEQUENCE "public"."discount_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for dish_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."dish_id_seq";
CREATE SEQUENCE "public"."dish_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for dishimg_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."dishimg_id_seq";
CREATE SEQUENCE "public"."dishimg_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for order_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."order_id_seq";
CREATE SEQUENCE "public"."order_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tag_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tag_id_seq";
CREATE SEQUENCE "public"."tag_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for user_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."user_id_seq";
CREATE SEQUENCE "public"."user_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Table structure for account
-- ----------------------------
DROP TABLE IF EXISTS "public"."account";
CREATE TABLE "public"."account" (
  "id" int4 NOT NULL DEFAULT nextval('account_id_seq'::regclass),
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
-- Records of account
-- ----------------------------

-- ----------------------------
-- Table structure for address
-- ----------------------------
DROP TABLE IF EXISTS "public"."address";
CREATE TABLE "public"."address" (
  "id" int4 NOT NULL DEFAULT nextval('address_id_seq'::regclass),
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
-- Records of address
-- ----------------------------

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
INSERT INTO "public"."alembic_version" VALUES ('a07c914f8d20');

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS "public"."comment";
CREATE TABLE "public"."comment" (
  "id" int4 NOT NULL DEFAULT nextval('comment_id_seq'::regclass),
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "content" varchar(512) COLLATE "pg_catalog"."default",
  "user_id" int4,
  "order_id" int4,
  "rate" "public"."rate_enum"
)
;

-- ----------------------------
-- Records of comment
-- ----------------------------

-- ----------------------------
-- Table structure for discount
-- ----------------------------
DROP TABLE IF EXISTS "public"."discount";
CREATE TABLE "public"."discount" (
  "id" int4 NOT NULL DEFAULT nextval('discount_id_seq'::regclass),
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
-- Records of discount
-- ----------------------------

-- ----------------------------
-- Table structure for dish
-- ----------------------------
DROP TABLE IF EXISTS "public"."dish";
CREATE TABLE "public"."dish" (
  "id" int4 NOT NULL DEFAULT nextval('dish_id_seq'::regclass),
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
-- Records of dish
-- ----------------------------

-- ----------------------------
-- Table structure for dishimg
-- ----------------------------
DROP TABLE IF EXISTS "public"."dishimg";
CREATE TABLE "public"."dishimg" (
  "id" int4 NOT NULL DEFAULT nextval('dishimg_id_seq'::regclass),
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "is_index" bool,
  "uri" varchar(512) COLLATE "pg_catalog"."default" NOT NULL,
  "dish_id" int4
)
;

-- ----------------------------
-- Records of dishimg
-- ----------------------------

-- ----------------------------
-- Table structure for order
-- ----------------------------
DROP TABLE IF EXISTS "public"."order";
CREATE TABLE "public"."order" (
  "id" int4 NOT NULL DEFAULT nextval('order_id_seq'::regclass),
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
-- Records of order
-- ----------------------------

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
-- Table structure for tag
-- ----------------------------
DROP TABLE IF EXISTS "public"."tag";
CREATE TABLE "public"."tag" (
  "id" int4 NOT NULL DEFAULT nextval('tag_id_seq'::regclass),
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "weight" int4,
  "name" varchar(32) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of tag
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS "public"."user";
CREATE TABLE "public"."user" (
  "id" int4 NOT NULL DEFAULT nextval('user_id_seq'::regclass),
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
-- Records of user
-- ----------------------------
INSERT INTO "public"."user" VALUES (1, NULL, '2021-11-21 13:07:17.758135', 'admin', 20, '13433334444', NULL, '2855829886@qq.com', '7RaqFOMZmUozaG/li5ojQg==
', 't', 't', 't', 'admin');

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."account_id_seq"
OWNED BY "public"."account"."id";
SELECT setval('"public"."account_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."address_id_seq"
OWNED BY "public"."address"."id";
SELECT setval('"public"."address_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."comment_id_seq"
OWNED BY "public"."comment"."id";
SELECT setval('"public"."comment_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."discount_id_seq"
OWNED BY "public"."discount"."id";
SELECT setval('"public"."discount_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."dish_id_seq"
OWNED BY "public"."dish"."id";
SELECT setval('"public"."dish_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."dishimg_id_seq"
OWNED BY "public"."dishimg"."id";
SELECT setval('"public"."dishimg_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."order_id_seq"
OWNED BY "public"."order"."id";
SELECT setval('"public"."order_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tag_id_seq"
OWNED BY "public"."tag"."id";
SELECT setval('"public"."tag_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."user_id_seq"
OWNED BY "public"."user"."id";
SELECT setval('"public"."user_id_seq"', 2, true);

-- ----------------------------
-- Primary Key structure for table account
-- ----------------------------
ALTER TABLE "public"."account" ADD CONSTRAINT "account_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table address
-- ----------------------------
ALTER TABLE "public"."address" ADD CONSTRAINT "address_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table alembic_version
-- ----------------------------
ALTER TABLE "public"."alembic_version" ADD CONSTRAINT "alembic_version_pkc" PRIMARY KEY ("version_num");

-- ----------------------------
-- Primary Key structure for table comment
-- ----------------------------
ALTER TABLE "public"."comment" ADD CONSTRAINT "comment_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table discount
-- ----------------------------
ALTER TABLE "public"."discount" ADD CONSTRAINT "discount_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table dish
-- ----------------------------
ALTER TABLE "public"."dish" ADD CONSTRAINT "dish_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table dishimg
-- ----------------------------
ALTER TABLE "public"."dishimg" ADD CONSTRAINT "dishimg_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table order
-- ----------------------------
ALTER TABLE "public"."order" ADD CONSTRAINT "order_pkey" PRIMARY KEY ("id");

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
-- Uniques structure for table tag
-- ----------------------------
ALTER TABLE "public"."tag" ADD CONSTRAINT "tag_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table tag
-- ----------------------------
ALTER TABLE "public"."tag" ADD CONSTRAINT "tag_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table user
-- ----------------------------
ALTER TABLE "public"."user" ADD CONSTRAINT "user_email_key" UNIQUE ("email");
ALTER TABLE "public"."user" ADD CONSTRAINT "user_phone_key" UNIQUE ("phone");

-- ----------------------------
-- Primary Key structure for table user
-- ----------------------------
ALTER TABLE "public"."user" ADD CONSTRAINT "user_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table account
-- ----------------------------
ALTER TABLE "public"."account" ADD CONSTRAINT "account_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table address
-- ----------------------------
ALTER TABLE "public"."address" ADD CONSTRAINT "address_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table comment
-- ----------------------------
ALTER TABLE "public"."comment" ADD CONSTRAINT "comment_order_id_fkey" FOREIGN KEY ("order_id") REFERENCES "public"."order" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."comment" ADD CONSTRAINT "comment_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table dish
-- ----------------------------
ALTER TABLE "public"."dish" ADD CONSTRAINT "dish_discount_id_fkey" FOREIGN KEY ("discount_id") REFERENCES "public"."discount" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table dishimg
-- ----------------------------
ALTER TABLE "public"."dishimg" ADD CONSTRAINT "dishimg_dish_id_fkey" FOREIGN KEY ("dish_id") REFERENCES "public"."dish" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table order
-- ----------------------------
ALTER TABLE "public"."order" ADD CONSTRAINT "order_address_id_fkey" FOREIGN KEY ("address_id") REFERENCES "public"."address" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."order" ADD CONSTRAINT "order_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table rs_dish_order
-- ----------------------------
ALTER TABLE "public"."rs_dish_order" ADD CONSTRAINT "rs_dish_order_dish_id_fkey" FOREIGN KEY ("dish_id") REFERENCES "public"."dish" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."rs_dish_order" ADD CONSTRAINT "rs_dish_order_order_id_fkey" FOREIGN KEY ("order_id") REFERENCES "public"."order" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table rs_dish_tag
-- ----------------------------
ALTER TABLE "public"."rs_dish_tag" ADD CONSTRAINT "rs_dish_tag_dish_id_fkey" FOREIGN KEY ("dish_id") REFERENCES "public"."dish" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."rs_dish_tag" ADD CONSTRAINT "rs_dish_tag_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table rs_user_tag
-- ----------------------------
ALTER TABLE "public"."rs_user_tag" ADD CONSTRAINT "rs_user_tag_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."rs_user_tag" ADD CONSTRAINT "rs_user_tag_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
