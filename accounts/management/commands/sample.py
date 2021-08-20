from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'ユーザー情報を表示するコマンドです'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='名前')  # 第一引数
        parser.add_argument('age', type=int)  # 第二引数
        parser.add_argument('--birthday', default='2020-01-01')  # オプション引数
        parser.add_argument('three_words', nargs=3)
        parser.add_argument('--active', action='store_true')
        parser.add_argument('--color', choices=['Blue', 'Red', 'Yellow'])

    def handle(self, *args, **options):
        name = options['name']
        age = options['age']
        birthday = options['birthday']
        three_words = options['three_words']
        active = options['active']
        color = options['color']

        print(f'name = {name}  age = {age}  birthday = {birthday}, three_words={three_words}')
        print(active)
        if color == 'Blue':
            print('Go')
        elif color == 'Red':
            print('Stop')
        elif color == 'Yellow':
            print('Warning')
