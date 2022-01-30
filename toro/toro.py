import requests
import discord
from config import api_key_openweather

class ToroBot(discord.Client):
    """
    Classe do Bot.
    Esta classe herda a classe Client. Esta classe contém
    métodos e atributos que facilitam na hora de interagir
    com o WebSockets e API do Discord
    """
    bot_name = 'Toró'
    version = 0.1
    author = 'r0se / SubaruSama'

    def __init__(self, city: str, state: str, country: str) -> None:
        """Construtor."""
        # TODO: deixar que ele receba estes valores de city, state e country via mensagem do Discord
        super().__init__()
        self.city = city
        self.state = state
        self.country = country
        self.url = f'https://api.openweathermap.org/data/2.5/weather?q={self.city},{self.state},{self.country}&units=metric&appid={api_key_openweather}'

    # Discord stuff
    async def on_message(self, message):
        """
        Método herdado da classe discord.Client
        Será chamado quando um model Message é criado e enviado.
        """
        if message.content.startswith('$tempo'): # TODO: Existe o discord.ext.commands, decorators que ajudam no parse. Utilizar depois.
            await message.channel.send(self.get_weather())

    async def on_ready(self) -> None:
        """
        No momento em que o bot é iniciado, printa no terminal com qual usuário está logado.
        Para debug apenas.
        """
        print(f'Logado como {self.user}')
        print(f'Nome do bot: {self.bot_name}')
        print(f'Versão: {self.version}')
        print(f'Desenvolvido por: {self.author}')

    def notify_all(self):
        """
        Método para enviar um @everyone avisando para não esquecer o
        guarda chuva.
        """
        pass

    # OpeanWeather stuff
    def it_will_rain_automatic(self, contents: str) -> None:
        """
        Método que decide se irá chover ou não. Caso true, chama notify_all(). Caso false, faz nada.
        """
        if contents["weather"][0]["main"] != "Clear":
            self.notify_all()
        else:
            pass

    def get_weather(self) -> any:
        """
        Método que pega os dados do OpenWeather.
        Este método possui duas funções:
            Enviar o response para o it_will_rain_automatic, responsável por avisar se vai chover e chamar o notify_all().\n
            Preencher as variáveis com os valores recebidos do json e envia para o it_will_rain, método que responde quando o comando é enviado.
        """
        response = requests.request('GET', self.url).json()
        # self.it_will_rain_automatic(response)
        
        temp = response["main"]["temp"]
        temp_max = response["main"]["temp_max"]
        temp_min = response["main"]["temp_min"]
        feels_like = response["main"]["feels_like"]
        humidity = response["main"]["humidity"]
        weather_main = response["weather"][0]["main"]
        weather_description = response["weather"][0]["description"]
        payload = f'Temperatura atual: {temp} °C\nTemperatura máxima: {temp_max} °C\nTemperatura mínima: {temp_min} °C\n' \
            f'Sensação térmica: {feels_like} °C\nUmidade: {humidity}%\n' \
            f'Tempo: {weather_main}\nDescrição do tempo: {weather_description}'

        return payload
