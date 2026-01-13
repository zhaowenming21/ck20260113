from datetime import datetime
from typing import Dict, List, Optional, Any

import dashscope
import requests
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 配置 API Keys
dashscope.api_key = "sk-101efc3d4dfd468f8777e29bb72d8023"
WEATHER_API_KEY = "2b54ee02282f48c7a827d6c1252fa906"


class WeatherService:
    """天气查询服务类"""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or WEATHER_API_KEY
        # self.base_url = "http://api.weatherapi.com/v1"  # 使用 WeatherAPI.com
        # 或者使用和风天气：https://dev.qweather.com/
        self.base_url = "https://np2tupa6bw.re.qweatherapi.com"

    def get_current_weather(self, city: str) -> Dict[str, Any]:
        """获取当前天气"""
        try:
            params = {
                'key': self.api_key,
                'q': city,
                'aqi': 'no'
            }

            # 如果使用的是和风天气API，请使用以下代码：
            # response = requests.get(f"https://devapi.qweather.com/v7/weather/now", params={
            #     'key': self.api_key,
            #     'location': city
            # })

            response = requests.get(f"{self.base_url}/current.json", params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            # 解析数据
            weather_data = {
                'city': data['location']['name'],
                'region': data['location']['region'],
                'country': data['location']['country'],
                'temperature': data['current']['temp_c'],
                'condition': data['current']['condition']['text'],
                'humidity': data['current']['humidity'],
                'wind_speed': data['current']['wind_kph'],
                'wind_dir': data['current']['wind_dir'],
                'feels_like': data['current']['feelslike_c'],
                'uv_index': data['current']['uv'],
                'last_updated': data['current']['last_updated']
            }

            return {
                'success': True,
                'data': weather_data,
                'raw_data': data
            }

        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': f"网络请求失败: {str(e)}"
            }
        except KeyError as e:
            return {
                'success': False,
                'error': f"数据解析失败: {str(e)}"
            }
        except Exception as e:
            return {
                'success': False,
                'error': f"未知错误: {str(e)}"
            }

    def get_forecast(self, city: str, days: int = 3) -> Dict[str, Any]:
        """获取天气预报"""
        try:
            params = {
                'key': self.api_key,
                'q': city,
                'days': days,
                'aqi': 'no',
                'alerts': 'no'
            }

            response = requests.get(f"{self.base_url}/forecast.json", params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            forecast_data = {
                'city': data['location']['name'],
                'forecast_days': []
            }

            for day in data['forecast']['forecastday']:
                forecast_data['forecast_days'].append({
                    'date': day['date'],
                    'max_temp': day['day']['maxtemp_c'],
                    'min_temp': day['day']['mintemp_c'],
                    'avg_temp': day['day']['avgtemp_c'],
                    'condition': day['day']['condition']['text'],
                    'chance_of_rain': day['day']['daily_chance_of_rain'],
                    'uv_index': day['day']['uv']
                })

            return {
                'success': True,
                'data': forecast_data
            }

        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }


class WeatherAgent:
    """天气查询Agent"""

    def __init__(self, model: str = "qwen-turbo"):
        self.model = model
        self.weather_service = WeatherService()
        self.conversation_history = []

        # 系统提示词
        self.system_prompt = """你是一个专业的天气助手。你的职责是：
        1. 理解用户关于天气的查询
        2. 调用天气查询工具获取准确数据
        3. 以友好、专业的方式呈现天气信息
        4. 根据天气情况提供适当的建议

        你可以：
        - 查询当前天气
        - 查询未来几天天气预报
        - 回答与天气相关的问题

        请确保在回答中：
        1. 准确引用天气数据
        2. 提供温度、天气状况、湿度、风速等关键信息
        3. 根据天气情况给出穿衣、出行等建议
        4. 保持友好和专业的语气"""

    def extract_city_from_query(self, query: str) -> Optional[str]:
        """从用户查询中提取城市名"""
        # 简单的城市名提取逻辑
        # 在实际应用中可以使用NER模型来改进
        cities = ['北京', '上海', '广州', '深圳', '杭州', '成都', '武汉', '南京',
                  '西安', '重庆', '天津', '苏州', '郑州', '长沙', '沈阳', '青岛',
                  'beijing', 'shanghai', 'guangzhou', 'shenzhen', 'hangzhou']

        query_lower = query.lower()
        for city in cities:
            if city.lower() in query_lower:
                return city
        return None

    def format_weather_response(self, weather_data: Dict) -> str:
        """格式化天气响应"""
        if not weather_data['success']:
            return f"抱歉，获取天气信息失败：{weather_data.get('error', '未知错误')}"

        data = weather_data['data']
        response = f"📍 {data['city']} ({data['region']}, {data['country']})\n\n"
        response += f"🌡️ 当前温度：{data['temperature']}°C (体感 {data['feels_like']}°C)\n"
        response += f"🌤️ 天气状况：{data['condition']}\n"
        response += f"💧 湿度：{data['humidity']}%\n"
        response += f"🌬️ 风速：{data['wind_speed']} km/h，风向：{data['wind_dir']}\n"
        response += f"☀️ 紫外线指数：{data['uv_index']}\n"
        response += f"🕐 数据更新时间：{data['last_updated']}\n\n"

        # 添加建议
        response += self._generate_suggestions(data)

        return response

    def _generate_suggestions(self, weather_data: Dict) -> str:
        """根据天气生成建议"""
        suggestions = "💡 生活建议：\n"

        temp = weather_data['temperature']
        condition = weather_data['condition'].lower()
        uv = weather_data['uv_index']

        if temp < 10:
            suggestions += "- 天气寒冷，建议穿厚外套、毛衣、围巾等保暖衣物\n"
        elif temp < 20:
            suggestions += "- 天气较凉，建议穿外套或薄毛衣\n"
        elif temp < 30:
            suggestions += "- 天气舒适，适合穿长袖或短袖\n"
        else:
            suggestions += "- 天气炎热，建议穿轻薄透气的衣物\n"

        if '雨' in condition:
            suggestions += "- 有降雨，建议携带雨具\n"
        elif '雪' in condition:
            suggestions += "- 有降雪，请注意防滑保暖\n"
        elif '晴' in condition:
            suggestions += "- 天气晴朗，适合户外活动\n"

        if uv > 7:
            suggestions += "- 紫外线较强，建议做好防晒措施\n"
        elif uv > 4:
            suggestions += "- 紫外线中等，建议适当防晒\n"

        if weather_data['wind_speed'] > 20:
            suggestions += "- 风较大，请注意防风\n"

        return suggestions

    def query_weather(self, city: str = None, query_type: str = "current") -> str:
        """查询天气"""
        if not city:
            return "请告诉我您要查询哪个城市的天气？"

        if query_type == "current":
            result = self.weather_service.get_current_weather(city)
            return self.format_weather_response(result)
        elif query_type == "forecast":
            result = self.weather_service.get_forecast(city, days=3)
            if result['success']:
                data = result['data']
                response = f"📅 {data['city']}未来3天天气预报：\n\n"
                for day in data['forecast_days']:
                    response += f"{day['date']}：\n"
                    response += f"  🌡️ 温度：{day['min_temp']}°C ~ {day['max_temp']}°C\n"
                    response += f"  🌤️ 天气：{day['condition']}\n"
                    response += f"  🌧️ 降水概率：{day['chance_of_rain']}%\n"
                    response += f"  ☀️ 紫外线：{day['uv_index']}\n\n"
                return response
            else:
                return f"获取天气预报失败：{result.get('error', '未知错误')}"
        else:
            return "不支持的查询类型"

    def chat_with_llm(self, user_input: str, context: List[Dict] = None) -> str:
        """与LLM对话"""
        messages = [
            {"role": "system", "content": self.system_prompt}
        ]

        # 添加上下文
        if context:
            messages.extend(context)

        # 添加用户输入
        messages.append({"role": "user", "content": user_input})

        try:
            from dashscope import Generation

            response = Generation.call(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )

            if response.status_code == 200:
                return response.output.text
            else:
                return f"调用模型失败：{response.message}"

        except Exception as e:
            return f"发生错误：{str(e)}"

    def process_query(self, user_input: str) -> str:
        """处理用户查询"""
        # 更新对话历史
        self.conversation_history.append({"role": "user", "content": user_input})

        # 判断是否需要查询天气
        weather_keywords = ['天气', '气温', '温度', '下雨', '下雪', '晴天', '阴天',
                            'weather', 'temperature', 'forecast', 'rain', 'snow']

        is_weather_query = any(keyword in user_input.lower() for keyword in weather_keywords)

        if is_weather_query:
            # 提取城市名
            city = self.extract_city_from_query(user_input)

            if city:
                # 判断查询类型
                forecast_keywords = ['预报', '未来', '明天', '后天', '下周', 'forecast']
                is_forecast = any(keyword in user_input for keyword in forecast_keywords)

                query_type = "forecast" if is_forecast else "current"

                # 查询天气
                weather_response = self.query_weather(city, query_type)

                # 将天气信息整合到上下文中，让LLM生成更自然的回复
                context = self.conversation_history[-5:]  # 最近5条对话
                enhanced_input = f"用户询问：{user_input}\n\n天气数据：{weather_response}\n\n请基于以上天气数据，用友好自然的方式回复用户，可以适当补充建议。"

                final_response = self.chat_with_llm(enhanced_input, context)
            else:
                # 没有识别到城市，让用户确认
                final_response = self.chat_with_llm(
                    f"用户想查询天气，但没有明确指定城市。用户输入是：{user_input}。请询问用户要查询哪个城市的天气。"
                )
        else:
            # 非天气查询，直接使用LLM
            final_response = self.chat_with_llm(user_input, self.conversation_history[-5:])

        # 保存助手回复
        self.conversation_history.append({"role": "assistant", "content": final_response})

        return final_response

    def clear_history(self):
        """清空对话历史"""
        self.conversation_history = []


class InteractiveCLI:
    """交互式命令行界面"""

    def __init__(self, agent: WeatherAgent):
        self.agent = agent
        self.running = False

    def print_welcome(self):
        """打印欢迎信息"""
        print("\n" + "=" * 60)
        print("🤖 天气查询助手 Agent Demo")
        print("=" * 60)
        print("功能：")
        print("  • 查询当前天气（如：北京天气怎么样？）")
        print("  • 查询天气预报（如：上海未来几天天气？）")
        print("  • 天气相关建议（如：今天应该穿什么？）")
        print("  • 普通对话")
        print("\n命令：")
        print("  • /clear  - 清空对话历史")
        print("  • /exit   - 退出程序")
        print("  • /help   - 显示帮助")
        print("=" * 60 + "\n")

    def run(self):
        """运行CLI"""
        self.running = True
        self.print_welcome()

        while self.running:
            try:
                # 获取用户输入
                user_input = input("\n👤 你：").strip()

                # 处理命令
                if user_input.lower() == '/exit':
                    print("👋 再见！")
                    self.running = False
                    continue
                elif user_input.lower() == '/clear':
                    self.agent.clear_history()
                    print("✅ 对话历史已清空")
                    continue
                elif user_input.lower() == '/help':
                    self.print_welcome()
                    continue
                elif not user_input:
                    continue

                # 显示正在思考
                print("🤔 AI思考中...", end='', flush=True)

                # 处理查询
                response = self.agent.process_query(user_input)

                # 打印回复
                print(f"\r{' ' * 50}", end='')  # 清除"思考中"提示
                print(f"\r🤖 助手：{response}")

            except KeyboardInterrupt:
                print("\n\n👋 再见！")
                self.running = False
            except Exception as e:
                print(f"\n❌ 发生错误：{str(e)}")


def main():
    """主函数"""

    # 检查API密钥
    if dashscope.api_key == 'your-dashscope-api-key':
        print("⚠️  警告：请设置你的 Dashscope API Key")
        print("1. 创建 .env 文件")
        print("2. 添加：DASHSCOPE_API_KEY=你的API密钥")
        print("3. 获取 WeatherAPI 密钥：https://www.weatherapi.com/")
        print("4. 添加：WEATHER_API_KEY=你的天气API密钥")

        # 询问是否继续
        choice = input("\n是否使用演示模式继续？(y/n): ")
        if choice.lower() != 'y':
            return

        # 演示模式 - 使用模拟数据
        demo_mode = True
        print("🔶 进入演示模式，使用模拟天气数据")
    else:
        demo_mode = False

    # 创建Agent
    agent = WeatherAgent(model="qwen-turbo")

    # 如果是演示模式，使用模拟天气服务
    if demo_mode:
        # 创建模拟天气服务
        class MockWeatherService:
            def get_current_weather(self, city):
                return {
                    'success': True,
                    'data': {
                        'city': city,
                        'region': '示例地区',
                        'country': '中国',
                        'temperature': 22.5,
                        'condition': '晴天',
                        'humidity': 65,
                        'wind_speed': 12.3,
                        'wind_dir': '东北风',
                        'feels_like': 23.1,
                        'uv_index': 6,
                        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M')
                    }
                }

            def get_forecast(self, city, days=3):
                return {
                    'success': True,
                    'data': {
                        'city': city,
                        'forecast_days': [
                            {
                                'date': (datetime.now()).strftime('%Y-%m-%d'),
                                'max_temp': 24,
                                'min_temp': 18,
                                'avg_temp': 21,
                                'condition': '晴天',
                                'chance_of_rain': 10,
                                'uv_index': 6
                            },
                            {
                                'date': (datetime.now()).strftime('%Y-%m-%d'),
                                'max_temp': 23,
                                'min_temp': 17,
                                'avg_temp': 20,
                                'condition': '多云',
                                'chance_of_rain': 20,
                                'uv_index': 5
                            }
                        ]
                    }
                }

        agent.weather_service = MockWeatherService()

    # 创建并运行CLI
    cli = InteractiveCLI(agent)
    cli.run()


if __name__ == "__main__":
    main()
