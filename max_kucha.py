class max_kucha:
    def __init__(self):
        self.kucha = []
###########################################################
    def insert(self,*values):
        for value in values:
            self.kucha.append(value)
            cur_idx = len(self.kucha)
            while self.kucha[cur_idx-1] > self.kucha[(cur_idx//2)-1] and cur_idx!=1:
                self.kucha[cur_idx-1],self.kucha[(cur_idx//2)-1] = self.kucha[(cur_idx//2)-1],self.kucha[cur_idx-1]
                cur_idx = cur_idx//2
###########################################################
    def extract_max(self):
        max_i = self.kucha[0]
        self.kucha[0] = self.kucha[-1]
        self.kucha.pop(-1)
        cur_idx = 1
        c_left = cur_idx*2
        c_right = cur_idx*2+1
        while c_left <= len(self.kucha):
            # Если нет правого
            if c_right > len(self.kucha):
                if self.kucha[cur_idx - 1]>= self.kucha[c_left - 1]:
                    break
                self.kucha[cur_idx - 1], self.kucha[c_left - 1] = \
                    self.kucha[c_left - 1], self.kucha[cur_idx - 1]
                cur_idx = c_left
                c_left = cur_idx * 2
                c_right = cur_idx * 2 + 1

            # Если есть оба ребёнка
            else:
                # Левый больше или равен правому
                if self.kucha[c_left - 1] < self.kucha[c_right - 1]:
                    if self.kucha[cur_idx - 1] >= self.kucha[c_right - 1]:
                        break
                    self.kucha[cur_idx - 1], self.kucha[c_right - 1] = \
                        self.kucha[c_right - 1], self.kucha[cur_idx - 1]
                    cur_idx = c_right
                    c_left = cur_idx * 2
                    c_right = cur_idx * 2 + 1
                else:
                    if self.kucha[cur_idx - 1] >= self.kucha[c_left - 1]:
                        break
                    self.kucha[cur_idx - 1], self.kucha[c_left - 1] = \
                        self.kucha[c_left - 1], self.kucha[cur_idx - 1]
                    cur_idx = c_left
                    c_left = cur_idx * 2
                    c_right = cur_idx * 2 + 1
        return max_i
###########################################################
    def __str__(self):
        if not self.kucha:
            return "Куча пуста"
        lines = []
        level = 0
        i = 0
        size = len(self.kucha)
        while i < size:
            level_size = 2 ** level
            level_nodes = self.kucha[i:i + level_size]
            # Форматируем строку уровня
            indent = "  " * (max(0, 4 - level))  # отступ для красоты
            lines.append(f"{indent}Уровень {level}: {level_nodes}")
            i += level_size
            level += 1
        return "\n".join(lines)
###########################################################
if __name__ == '__main__':
    debug = False
    k = max_kucha()
    k.insert(200,10,5)
    print(str(k))
    for _ in range(3):
        max_el = k.extract_max()
        print(max_el)
        print(str(k))
