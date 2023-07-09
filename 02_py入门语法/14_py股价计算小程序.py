
# 公司名称
name = "传智播客"

# 股票价格
stock_price = 19.99
# 股票代码
stock_code = "23467"
# 每日增长系数
stock_price_daily_growth_factor = 1.2
# 增长的天数
growth_day = 7

# 计算经过growth_day天的增长后，股价达到了多少钱
# 使用字符串格式化输出，浮点数的精度要求为2位

# 因为是每天，所有是幂等
result = stock_price_daily_growth_factor ** growth_day

# 方式1
print(f"""公司：{name},股票代码：{stock_code}, 当前股价:{stock_price}
每日增长系数为%.2f ,经过 %d 天的增长后，股价达到 %.2f
      """ % (stock_price_daily_growth_factor, growth_day, result))
# 方式2
print(f"公司：{name},股票代码：{stock_code}, 当前股价:{stock_price}")
print("每日增长系数为%.1f ,经过 %d 天的增长后，股价达到 %.2f" % (stock_price_daily_growth_factor, growth_day, result))




