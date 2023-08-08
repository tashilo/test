from datetime import datetime

"робимо бекап якихось даних"

def make_backup(data):
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    with open(f'backup_{current_time}.txt', 'w') as fh:
        fh.write(data)

if __name__ == '__main__':
    data = '11111'
    make_backup(data)        