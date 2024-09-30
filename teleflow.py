import os
import telebot
import plotly.io as pio # type: ignore
import plotly.graph_objects as go # type: ignore
from IPython.display import display
from dotenv import load_dotenv
class Bot:
    '''
    Этот класс представляет Telegram бота, который может взаимодействовать с пользователями, отправляя сообщения, фотографии и файлы, а также может генерировать и обновлять графики с помощью Plotly.

    Методы:
    - __init__(self, dotenv=False): Инициализирует класс Bot, настраивая токен и ID пользователя для Telegram бота.
    - init_graph(self) -> go.FigureWidget: Создает и возвращает пустой график с заданными параметрами осей и разметкой.
    - plot_graph(self, accuracy: list = None, loss: list = None, title: str = 'Learning', epoch: int = None, fig: go.FigureWidget = None): Обновляет данные графика переданными списками точности и потерь.
    - send_text(self, text): Отправляет текстовое сообщение в Telegram.
    - send_file(self, file): Отправляет файл в Telegram.
    - send_results(self, text: str, image: str, file: str): Отправляет изображение и файл с сообщением в Telegram.
    '''

    def __init__(self, dotenv=False):
        '''
        Инициализирует класс Bot, настраивая токен и ID пользователя для Telegram бота.
        
        Параметры:
        - dotenv (bool): Загружать ли переменные окружения из файла .env. Default is False.
        '''
        if dotenv:
            load_dotenv()
        self.token = os.environ.get('TG_TOKEN')
        self.user_id = int(os.environ.get('TG_USER_ID'))
        self.bot = telebot.TeleBot(self.token)

    def init_graph(self) -> go.FigureWidget:
        '''
        Создает и возвращает пустой график с заданными параметрами осей и разметкой.
        
        Возвращает:
        - go.FigureWidget: Объект Plotly FigureWidget с пустым графиком, имеющим заданные заголовки осей и поля.
        '''
        fig = go.FigureWidget()
        fig.update_layout(
            xaxis_title='Epoch',
            yaxis_title='Value',
            margin=dict(l=20, r=20, t=20, b=20)
        )
        fig.add_trace(go.Scatter(y=[], mode='lines', name='Accuracy'))
        return fig

    def plot_graph(self, accuracy: list = None, loss: list = None, title: str = 'Learning', epoch: int = None, fig: go.FigureWidget = None):
        '''
        Обновляет данные графика переданными списками точности и потерь.
        
        Параметры:
        - accuracy (list, optional): Список значений точности для построения графика. Default is None.
        - loss (list, optional): Список значений потерь для построения графика. Default is None.
        - title (str, optional): Заголовок графика. Default is 'Learning'.
        - epoch (int, optional): Текущий номер эпохи. Default is None.
        - fig (go.FigureWidget, optional): Объект Plotly FigureWidget для обновления. Default is None.
        '''
        if accuracy: fig.data[0].y = accuracy
        if loss: fig.data[1].y = loss

    def send_text(self, text):
        '''
        Отправляет текстовое сообщение в Telegram.
        
        Параметры:
        - text (str): Текст сообщения для отправки.
        '''
        self.bot.send_message(self.user_id, text)

    def send_file(self, file):
        '''
        Отправляет файл в Telegram.
        
        Параметры:
        - file (str): Путь к файлу для отправки.
        '''
        self.bot.send_document(self.user_id, file)

    def send_results(self, text: str, image: str, file: str):
        '''
        Отправляет изображение и файл с сообщением в Telegram.
        
        Параметры:
        - text (str): Текст сообщения для отправки с изображением и файлом.
        - image (str): Путь к изображению для отправки.
        - file (str): Путь к файлу для отправки.
        '''
        with open(image, 'rb') as f:
            self.bot.send_photo(self.user_id, f, text)
        with open(file, 'rb') as f:
            self.bot.send_document(self.user_id, f)