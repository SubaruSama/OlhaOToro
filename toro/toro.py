import urllib3
import discord
from config import api_key_openweather

class ToroBot(discord.Client):
    """
    Classe do Bot.
    Esta classe herda a classe Client. Esta classe contém
    métodos e atributos que facilitam na hora de interagir
    com o WebSockets e API do Discord
    """
    bot_name = 'Toro'
    version = 0.1
    author = 'r0se / SubaruSama'

    def __init__(self, city: str, state: str, country: str) -> None:
        """Construtor."""
        # TODO: deixar que ele receba estes valores de city, state e country via mensagem do Discord
        self.city = city
        self.state = state
        self.country = country
        self.url = f'https://api.openweathermap.org/data/2.5/weather?q={self.city},{self.state},{self.country}&units=metric&appid={api_key_openweather}'
        super().__init__()

    # Discord stuff
    async def on_message(self, message):
        """
        Método herdado da classe discord.Client
        Será chamado quando um model Message é criado e enviado.
        """
        if message.content.startswith('$tempo'): # TODO: Existe o discord.ext.commands, decorators que ajudam no parse. Utilizar depois
            await message.channel.send('Nao sei')

    async def on_ready(self) -> None:
        """
        No momento em que o bot é iniciado, printa no terminal com qual usuário está logado.
        Para debug apenas.
        """
        print(f'Logado como {self.user}')

    def notify_all(self):
        """
        Método para enviar um @everyone avisando para não esquecer o
        guarda chuva.
        """
        pass

    # OpeanWeather stuff
    def it_will_rain(self, contents: str) -> None:
        """
        Método que decide se irá chover ou não. Caso true, chama notify_all(). Caso false, faz nada.
        """
        if contents["weather"][0]["main"] != "Clear":
            self.notify_all()
        else:
            pass

    def get_weather(self) -> None:
        """
        Método que pega os dados do OpenWeather e envia para o parse_weather
        """
        http = urllib3.PoolManager()
        get = http.request('GET', self.url)
        self.it_will_rain(get)
