"""
UnionFind木の実装
inputで取り扱うことができるのは、int形式のみ。
strのデータは、加工して利用すること。

TODO:
    特にないし。
"""
from typing import List


class UnionFind:
    """
    UnionFindの実装
    引用元:https://note.nkmk.me/python-union-find/
    親の特定と要素数を同じリストで管理しているのはいけてないけど、外から見えないからいいかって感じ。
    でも頭がこんがらがる。意味合いが違う要素が同じリストでまとまっているのは違和感。
    """

    def __init__(self, element_num: int) -> None:
        """UnionFindのクラスを生成。
           要素の数だけ、親子関係を表現するリストを作成
           indexが要素の値。
           valueが要素の親子関係を管理。
           valueが負の場合は、その要素は親。要素の値の絶対値が要素数になる。（* -1したら要素数が求まる。）
           valueが正の場合は、その要素はvalueの値の子になる。（valueの値が親になる。）
        Args:
            element_num (int): 要素数を記載。
        """
        self.element_num = element_num + 1
        self.parents: List = [-1] * element_num + 1

    def union(self, element1: int, element2: int) -> None:
        """統合処理を行う。

        Args:
            element1 (int): 要素1
            element2 (int): 要素2
        """
        root_element1_index = self.find(element1)
        root_element2_index = self.find(element2)

        # 親が同じときには何も処理をしない。
        if root_element1_index == root_element2_index:
            return

        # 以下の処理は親の要素しかないため、root_element(1|2)は、正の値のしか持たない。
        # 要素の数が大きい方をroot_element1とする。（経路圧縮、ランクの処理）
        if self.parents[root_element1_index] > self.parents[root_element2_index]:
            root_element1_index, root_element2_index = (
                root_element2_index,
                root_element1_index,
            )

        # root_element1には、root_element2の要素数を足した数を要素数とする。
        # root_element1の配下にroot_element2が入るため。
        self.parents[root_element1_index] += self.parents[root_element2_index]
        self.parents[root_element2_index] = root_element1_index  # 親のindexを入れる。

    def find(self, element: int) -> int:
        """要素を含んでいる木のrootのindexを出力する。

        Args:
            element (str): 要素

        Returns:
            str: 要素のrootのindex出力
        """
        if self.parents[element] < 0:
            return element
        else:
            self.parents[element] = self.find(self.parents[element])
            return self.parents[element]

    def same(self, element1: int, element2: int) -> bool:
        """同じrootを持つ要素かどうかを判定する。

        Args:
            element1 (int): 要素の値
            element2 (int): 要素の値

        Returns:
            bool: bool
        """
        return self.find(element1) == self.find(element2)

    def menbers(self, element: int) -> List[int]:
        """指定した要素を含むグループの要素をlistで出力する。

        Args:
            element (int): 要素

        Returns:
            List[int]: 指定した要素を含むグループの要素をlist
        """
        root = self.find(element)
        res: List[int] = list()
        for idx in range(self.element_num):
            if self.find(idx) == root:
                res.append(idx)
        return res

    def roots(self) -> List[int]:
        """rootの要素を全て出力する。

        Returns:
            List[int]: _description_
        """
        res = []
        for menber in self.parents[1:]:
            if menber < 0:
                res.append(menber)
        return res
