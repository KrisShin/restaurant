### http request
# user module
# 用户不存在
USER_NOT_EXIST = 1001

# 用户已存在
USER_EXISTED = 1002

# 手机号格式错误
USER_WRONG_PHONE_FORMAT = 1003

# 用户密码错误
USER_WRONG_PASSWORD = 1004

# 没有邮箱
USER_EMAIL_NOT_EXIST = 1005

# 验证邮件已发送, 稍后再试
USER_CAPTCHA_SENDED = 1006

# 新密码不能与原密码相同
USER_SAME_PASSWORD = 1007

# 验证码错误
USER_WRONG_CAPTCHA = 1008

# 验证码已过期
USER_CAPTCHA_EXPIRED = 1009

# token过期
USER_TOKEN_EXPIRE = 10010

# token无效
USER_INVALID_TOKEN = 10011

# 确认密码与新密码不一致
USER_WRONG_CONFIRM_PASSWORD = 10012

# 用户不是管理员
USER_NOT_ADMIN = 10013

# addr module
# 地址数据有误(创建地址带上了id)
ADDR_DATA_ERROR = 1101

# 地址数据不完整
ADDR_LACK_DATA = 1102

# 地址不存在
ADDR_NOT_EXISIT = 1103

# order module
# 提交订单没有菜品
ORDER_EMPTY_CART = 1201
