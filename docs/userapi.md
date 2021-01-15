# 1. 用户注册

**url: /user/register　**

**方法：POST**

**数据格式：JSON**

**编码：UTF-8**

**请求参数：**

```json
{
	"nickname": nickname,
	"gender": true/false, // true-男/flase-女
	"age":18,
	"phone": "13433334444",
	"password": "password"
}

```


**响应参数**

```json
{
  	"success": true,
    "info": "OK",
    "data":{
        "phone":"13433334444"
    }
}
```



# 2. 用户登录

**url: /user/login　**

**方法：POST**

**数据格式：JSON**

**编码：UTF-8**

**请求参数：**

```json
{
	"phone": "13433334444",
	"password": "password"
}

```


**响应参数**

```json
{
  	"success": true,
  	"info": "OK",
    "data": {
        "user_id": user_id,
        "nickname": nickname,
        "is_vip": true/false,
        "is_active": true/false,
        "is_new": true/false,
        "gender": true/false,
        "balance": 0.00,
        // 下面的内容完善中, 暂时会写死或者返回空值
        "tags":["微辣", "甜点", "奶茶", "小龙虾"],
        "push_dishes":[
            {
                "name":"鱼香肉丝",
                "img":"dish_img_url", 
                "tag":["微辣","酸甜"],
                "price":23.78, 
                "amount":18 // 累计销量
            },
        ]
    }
}
```



# 3. 修改密码

**url: /user/change_pwd　**

**方法：POST**

**数据格式：JSON**

**编码：UTF-8**

**说明: 点击修改密码提示确认, 点击确认就会给他发送验证邮件(后面可能会修改为短信验证码形式) **

**请求参数：**

```json
{
    "user_id": user_id,
	"capcha": "邮箱验证码",
	"old_password": "password",
	"new_password": "password",
}

```


**响应参数**

```json
{
	"success": true,
	"info": "OK",
	"data": {
        "nickname": nickname,
        "is_vip": true/false,
        "is_active": true/false,
        "is_new": true/false,
        "gender": true/false,
        ""
    }
}
```



# 4. 查看信息

**url: /user/profile　**

**方法：GET **

**数据格式：JSON**

**编码：UTF-8**

**请求参数：**

```json
{
    "user_id": user_id
}

```


**响应参数**

```json
{
	"success": true,
	"info": "OK",
	"data": {
        "nickname": "nickname",
        "is_vip": true/false,
        "is_active": true/false,
        "is_new": true/false,
        "gender": true/false,
        "email": "123@123.com",
        "avatar": "http://192.168.8.17:9999/static/avatar/default.jpg",
        "balance": 499.38,
        "phone": "1234123456",
        "age": 18
    }
}
```



# 5. 编辑信息

**url: /user/edit_profile　**

**方法：POST **

**数据格式：JSON**

**编码：UTF-8**

**请求参数：**

```json
{
    "user_id": user_id,
    "avatar": "http://192.168.8.17:9999/static/avatar/default.jpg",
    "age": 18
    "tags": ["汽水", "鸡蛋", "牛排", "变态辣"]
}

```


**响应参数**

```json
{
	"success": true,
	"info": "OK",
}
```



# 6. 修改邮箱

**url: /user/profile　**

**方法：POST **

**数据格式：JSON**

**编码：UTF-8**

**说明: 点击修改邮箱提示确认, 点击确认就会给他发送验证邮件(后面可能会修改为短信验证码形式) **

**请求参数：**

```json
{
    "user_id": user_id,
    "captcha": "邮箱验证码",
    "new_email": "123123@321.com"
}

```


**响应参数**

```json
{
	"success": true,
	"info": "OK",
}
```

# 7. 请求验证邮件

**url: /user/email_captcha **

**方法：POST **

**数据格式：JSON**

**编码：UTF-8**

**说明: 点击修改邮箱提示确认, 点击确认就会给他发送验证邮件(后面可能会修改为短信验证码形式) **

**请求参数：**

```json
{
    "email": "123123@321.com"
}

```


**响应参数**

```json
{
	"success": true,
	"info": "OK",
}
```

# 8. 退出登录

**url: /user/logout **

**方法：POST **

**数据格式：JSON**

**编码：UTF-8**

**请求参数：**

```json
{
    "user_id": user_id,
}

```

**响应参数**

```json
{
	"success": true,
	"info": "OK",
}
```
