"""
`address_books` を使って、次のような出力をするコードを実装してください。
`address_books` は面倒なのでコピペしてください。

東京タワー 〒1050011 東京都港区芝公園４丁目２−８
スカイツリー 〒1310045 東京都墨田区押上１丁目１−２
通天閣タワー 〒5560002 大阪府大阪市浪速区恵美須東１丁目１８−６
"""


def main():
    address_books = [
        {'name': '東京タワー',
         'location': '東京都港区芝公園4丁目２－８',
         'zipcode': '105001'},
        {'name': 'スカイツリー',
         'location': '東京都墨田区1丁目1－2',
         'zipcode': '1310045'},
        {'name': '通天閣タワー',
         'location': '大阪府大阪市浪速区恵美須東１丁目１８−６',
         'zipcode': '5560002'},
    ]

    # 出力
    for i in range(3):
        adress = address_books
        print(f'{adress[i]["name"]} {adress[i]["zipcode"]} {adress[i]["location"]}')
    print("\n")
    for address_book in address_books:
        print(address_book)


if __name__ == '__main__':
    main()
