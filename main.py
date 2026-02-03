"""
МОЙ ПЕРВЫЙ ВЕБ-САЙТ НА PYTHON
Простой веб-сервер с HTML страницей
"""

# Импортируем необходимые модули
from http.server import HTTPServer, BaseHTTPRequestHandler
import webbrowser
import time

# Класс для обработки HTTP запросов
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Обрабатываем GET запросы (когда браузер заходит на сайт)"""
        
        # Отправляем успешный ответ (200 OK)
        self.send_response(200)
        
        # Указываем, что отправляем HTML
        self.send_header('Content-type', 'text/html; charset="utf-8" ')
        self.end_headers()
        
        # HTML страница, которую увидит пользователь
        html_content = """
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Мой первый сайт на Python!</title>
            <style>
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }
                
                body {
                    font-family: 'Arial', sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 20px;
                }
                
                .container {
                    background: white;
                    border-radius: 20px;
                    padding: 40px;
                    max-width: 800px;
                    width: 100%;
                    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                    text-align: center;
                }
                
                h1 {
                    color: #333;
                    margin-bottom: 20px;
                    font-size: 2.5em;
                }
                
                h2 {
                    color: #667eea;
                    margin: 30px 0 15px 0;
                    border-bottom: 2px solid #667eea;
                    padding-bottom: 10px;
                }
                
                p {
                    color: #666;
                    line-height: 1.6;
                    margin-bottom: 20px;
                    font-size: 1.1em;
                }
                
                .code-block {
                    background: #f5f5f5;
                    border-left: 4px solid #667eea;
                    padding: 15px;
                    margin: 20px 0;
                    text-align: left;
                    border-radius: 5px;
                    font-family: 'Courier New', monospace;
                    font-size: 1em;
                    overflow-x: auto;
                }
                
                .success {
                    background: #d4edda;
                    color: #155724;
                    border: 1px solid #c3e6cb;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 20px 0;
                    font-weight: bold;
                }
                
                .features { 
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 20px;
                    margin: 30px 0;
                }
                
                .feature {
                    background: #f8f9fa;
                    border-radius: 10px;
                    padding: 20px;
                    flex: 1;
                    min-width: 200px;
                    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                }
                
                .feature h3 {
                    color: #764ba2;
                    margin-bottom: 10px;
                }
                
                .buttons {
                    margin-top: 30px;
                }
                
                button {
                    background: #667eea;
                    color: white;
                    border: none;
                    padding: 12px 30px;
                    border-radius: 50px;
                    font-size: 1em;
                    cursor: pointer;
                    margin: 0 10px;
                    transition: all 0.3s ease;
                }
                
                button:hover {
                    background: #764ba2;
                    transform: translateY(-2px);
                    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
                }
                
                .footer {
                    margin-top: 40px;
                    color: #999;
                    font-size: 0.9em;
                }
                
                @media (max-width: 600px) {
                    .container {
                        padding: 20px;
                    }
                    
                    h1 {
                        font-size: 1.8em;
                    }
                    
                    button {
                        display: block;
                        width: 100%;
                        margin: 10px 0;
                    }
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🎉 Мой первый сайт на Python! 🎉</h1>
                
                <div class="success">
                    ✅ УРА! Вы только что запустили свой первый веб-сервер на Python!
                </div>
                
                <p>
                    Этот сайт полностью создан и запущен с помощью Python. 
                    Все, что вы видите — HTML и CSS, сгенерированные Python-скриптом.
                </p>
                
                <h2>📊 Что сейчас работает:</h2>
                
                <div class="features">
                    <div class="feature">
                        <h3>🌐 Веб-сервер</h3>
                        <p>Python обрабатывает HTTP запросы и отправляет HTML страницу</p>
                    </div>
                    <div class="feature">   --------------------------------------------------------------------------------
                        <h3>🎨 Стили CSS</h3>
                        <p>Красивый дизайн с градиентами и анимациями</p>
                    </div>
                    <div class="feature">
                        <h3>📱 Адаптивность</h3>
                        <p>Сайт выглядит отлично на всех устройствах</p>
                    </div>
                </div>