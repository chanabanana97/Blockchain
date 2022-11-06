import requests

GENESIS_BLOCK = 1231006505

def get_block_time(block_height):
    block_request = requests.get(f'https://blockchain.info/block-height/{block_height}?format=json')
    block = block_request.json()
    ts = block.get('blocks')[0].get('time')
    return ts

def latest_block():
    latest_block_req = requests.get('https://blockchain.info/latestblock')
    return latest_block_req.json()

def binary_search(search_value):
    low = 1
    high = latest_block().get('height')

    while low < high:
        mid = (high + low) // 2
        mid_time = get_block_time(mid)

        if mid_time <= search_value:
            low = mid + 1
        else:
            high = mid
    return low - 1


def check_timestamp(ts):
    # edge case - timestamp too small or too big
    if ts < GENESIS_BLOCK or ts > latest_block().get('time'):
        return False
    return True


if __name__ == '__main__':
    # timestamp = 1232103989
    try:
        timestamp = int(input("enter timestamp"))
        if check_timestamp(timestamp):
            latest_before_ts = binary_search(timestamp)
            print(latest_before_ts)
        else:
            print('invalid timestamp')
    except ValueError:
        print('invalid timestamp')

