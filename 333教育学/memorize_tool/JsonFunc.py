import json
import datetime


def get_book_name():
    main_data_json = json.load(open("data\\main_data.json", encoding='utf-8'))
    return main_data_json["book_name"]


def refresh_date():
    # 在进入程序的时候调用，将当前日期作为一个新的时间节点
    main_data_json = json.load(open("data\\main_data.json", encoding='utf-8'))
    today = str(datetime.date.today())
    if today in main_data_json["date_time_dict"]:
        return
    else:
        main_data_json["cur_time"] += 1
        main_data_json["date_time_dict"][today] = main_data_json["cur_time"]
        # print(main_data_json)
        # print(type(main_data_json))
        json.dump(main_data_json, open("data\\main_data.json", 'w', encoding='utf-8'), ensure_ascii=False)
        # ensure_ascii 默认为True，这样写入的就会是unicode码


def get_cur_time():
    main_data_json = json.load(open("data\\main_data.json", encoding='utf-8'))
    return main_data_json["cur_time"]


def get_book_blank_unit(book_name):
    f = open("data\\" + book_name + ".json",encoding='utf-8')
    book_json = json.load(f)
    return len(book_json["data"]) + 1


def add_data_to_json(book_name, time, unit, desc, data_lines):
    f = open("data\\" + book_name + ".json", encoding='utf-8')
    book_json = json.load(f)
    cur_dict = {"time": time, "unit": unit, "desc": desc, "data": data_lines}
    book_json["data"].append(cur_dict)
    json.dump(book_json, open("data\\" + book_name + ".json", 'w', encoding='utf-8'), ensure_ascii=False)


def get_memorize_data():
    main_data_json = json.load(open("data\\main_data.json", encoding='utf-8'))
    book_names = main_data_json["book_name"]
    repeat_intervals = main_data_json["repeat_interval"]
    ans_dict_list = []
    cur_time = get_cur_time()
    for repeat_interval in repeat_intervals:
        for book_name in book_names:
            f = open("data\\" + book_name + ".json", encoding='utf-8')
            book_json = json.load(f)
            for dict_item in book_json["data"]:
                if cur_time - repeat_interval == dict_item["time"]:
                    for data in dict_item["data"]:
                        ans_dict = {"book_name": book_name, "repeat_interval": repeat_interval,
                                    "unit": dict_item["unit"], "desc": dict_item["desc"], "data": data}
                        ans_dict_list.append(ans_dict)
    return ans_dict_list


def get_book_data(book_name):
    f = open("data\\" + book_name + ".json", encoding='utf-8')
    book_json = json.load(f)
    book_data_list = book_json["data"]
    book_data_list.sort(key=lambda item: item["unit"])
    ans_dict_list = []
    for data_dict in book_data_list:
        ans_dict = {"unit_info": "Unit " + str(data_dict["unit"]) + ':' + data_dict["desc"], "data": data_dict["data"]}
        ans_dict_list.append(ans_dict)
    return ans_dict_list


if __name__ == "__main__":
    # print(get_memorize_data())
    pass
