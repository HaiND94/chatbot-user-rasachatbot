# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from codecs import utf_8_decode
import json 

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


data_address = {
    'nghệ an': [
        {
            'name': "Bệnh Viện Sản Nhi Nghệ An",
            'tel': '0238 3844 129',
            'add': '19 Tôn Thất Tùng, Hưng Dũng, Thành phố Vinh, Nghệ An',
            'time': 'cả ngày'
        },

        {
            'name': "Bệnh Viện Đa Khoa Thành Phố Vinh",
            'tel': '0238 3844 626',
            'add': '178 Trần Phú, Hồng Sơn, Thành phố Vinh, Nghệ An',
            'time': 'cả ngày'
        },

        {
            'name': "Bệnh viện Hữu nghị Đa khoa Nghệ An",
            'tel': '0238 3844 528',
            'add': 'Km số 5, V.L Lê Nin, Thành phố Vinh, Nghệ An',
            'time': 'cả ngày'
        },

        {
            'name': "Bệnh Viện Đa Khoa 115 Nghệ An",
            'tel': '0238 3518 887',
            'add': 'Số 40 Đại lộ Xô Viết Nghệ, Nghi Phú, Thành phố Vinh, Nghệ An',
            'time': 'cả ngày'
        },

        {
            'name': "Bệnh viện đa khoa Cửa Đông",
            'tel': '0238 3569 888',
            'add': '143 Nguyễn Phong Sắc, Thành phố Vinh, Nghệ An',
            'time': 'cả ngày'
        }

    ],
    'hà nội': [
        {
            'name': "Khoa truyền nhiễm – Bệnh viện Nhi Trung ương",
            'tel': None,
            'add': 'số 18/879 La Thành, Đống Đa, Hà Nội.',
            'time': 'cả ngày'
        },
        
        {
            'name': "Bệnh viện Đa khoa quốc tế Vinmec",
            'tel': None,
            'add': '458 Phố Minh Khai, Vĩnh Tuy, Hai Bà Trưng, Hà Nội.',
            'time': 'cả ngày'
        },

        {
            'name': "Khoa Nhi tổng quát – Bệnh viện Đa khoa Xanh Pôn",
            'tel': None,
            'add': 'số 12 Chu Văn An, Ba Đình, Hà Nội.',
            'time': 'cả ngày'
        },

        {
            'name': "Khoa Nhi – Bệnh viện Thanh Nhàn",
            'tel': None,
            'add': 'số 42 Thanh Nhàn, Hai Bà Trưng, Hà Nội.',
            'time': 'cả ngày'
        },

        {
            'name': "Khoa Nhi – Bệnh viện Việt Pháp",
            'tel': None,
            'add': 'số 1 Phương Mai, Đống Đa, Hà Nội.',
            'time': 'cả ngày'
        },

        {
            'name': "Chuyên khoa nhi – PK số 1, Bệnh viện Đại học Y Hà Nội",
            'tel': None,
            'add': 'số 1 Tôn Thất Tùng, Đống Đa, Hà Nội.',
            'time': 'cả ngày'
        }
    ]
}

class FindHospital(Action):

    def name(self) -> Text:
        return "find_hospital"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        add = tracker.get_slot("address")

        if not add:
            dispatcher.utter_message(text="Tôi chưa nhận được dữ liệu từ bạn, làm ơn hãy nhập địa chỉ bạn vào")
        elif str(add).lower() in data_address.keys():
            text = 'Bạn có thể tham khảo một số bệnh viện sau:\n'
            province_hos = data_address.get(str(add).lower())

            str_array = [ f'Bệnh viện: {host["name"]}\n\
                ==> Điện thoại: {host["tel"]}\n\
                ==> Địa chỉ: {host["add"]}\n\
                ==> Thời gian hoạt động: {host["time"]}' for host in province_hos]

            mess = text + "\n".join(str_array)
            dispatcher.utter_message(text=mess)
        else:
            dispatcher.utter_message(text=f"Xin lỗi hệ thống của chúng tôi chưa cập nhật bệnh viện tại khu vực {add}")

        return []
