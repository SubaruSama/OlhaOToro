import urllib3
import discord
import config

class ToroBot(discord.Client):
    """Classe do Bot.
    Esta classe herda a classe Client. Esta classe contém
    métodos e atributos que facilitam na hora de interagir
    com o WebSockets e API do Discord"""
    bot_name = 'Toro'
    version = 0.1
    author = 'r0se / SubaruSama'

    def __init__(self, city: str, state: str, country: str) -> None:
        self.api_key = config.api_key_discord
        # TODO: deixar que ele receba estes valores de city, state e country via mensagem do Discord
        self.city = city
        self.state = state
        self.country = country
        self.url = f'https://api.openweathermap.org/data/2.5/weather?q={self.city},{self.state},{self.country}&units=metric&appid={config.api_key_openweather}'

    # Discord stuff
    async def on_message(self, message):
        """
        Método herdado da classe discord.Client
        Será chamado quando um model Message é criado e enviado.
        """
        if message.content.startswith('$vai_chover'):
            await message.channel.send('Nao sei')

    async def on_ready(self) -> None:
        print(f'Logado como {self.user}')

    def notify_all(self):
        """
        Método para enviar um @everyone avisando para não esquecer o
        guarda chuva.
        """
        pass

    # OpeanWeather stuff
    def get_weather(self) -> None:
        """
        Método que retorna dados a partir do OpenWeather.
        """
        http = urllib3.PoolManager()
        get = http.request('GET', self.url)
        self.it_will_rain(get)

    def it_will_rain(self, contents) -> bool:
        """
        Método que decide se irá chover ou não. Caso true, chama notify_all(). Caso false, faz nada.
        Precisa realizar um parse do json vindo do método get_weather().
        """
        pass
