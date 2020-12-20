import os

import yadisk


class Yandex:
    def __init__(self, token: str) -> None:
        self.token = token

    def load(self):
        y = yadisk.YaDisk(token=self.token)
        Dir_tupe = os.walk('C:\DiplomAPI\Dir')
        Dir_list = list(Dir_tupe)
        for element in Dir_list:
            for el in element:
                for e in el:
                    if len(e) > 1:
                        with open(f"Dir/{e}", "rb") as f:
                            y.upload(f, f"{e}")
