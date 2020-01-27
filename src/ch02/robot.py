class Robot(object):
    def __init__(self,name):
        self.name = name
        self.height = 30
        self.weight = 5
        self.left_foot_from_earth = 0 #左脚距离地面0厘米
        self.right_foot_from_earth = 0  # 右脚距离地面0厘米
        self.left_hand_from_earth = 15  # 左手距离地面15厘米
        self.right_hand_from_earth = 15  # 右手距离地面15厘米

    def _adjust_movement(self,part,current_value,displacement):
        if part == 'foot':
            boundary = [0,15]
        elif part == 'hand':
            boundary = [15,40]
        else:
            print('未知的身体部位!')
            return

        new_value = current_value + displacement

        if new_value < boundary[0]:
            return boundary[0]
        elif new_value > boundary[1]:
            return boundary[1]
        else:
            return new_value

    def move_left_foot(self,displacement):
        left_foot_from_earth = self.left_foot_from_earth + displacement

        if left_foot_from_earth > 0 and self.right_foot_from_earth > 0:
            print('不能双脚同时落地，放弃移动左脚！')
            return

        self.left_foot_from_earth = self._adjust_movement('foot',self.left_foot_from_earth,displacement)

        self.announce()

    def move_right_foot(self,displacement):
        right_foot_from_earth = self.right_foot_from_earth + displacement

        if right_foot_from_earth > 0 and self.right_foot_from_earth > 0:
            print('不能双脚同时落地，放弃移动右脚！')
        else:
            self.right_foot_from_earth = self._adjust_movement('foot',self.right_foot_from_earth,displacement)
            self.announce()

    def move_left_hand(self,displacement):
        self.left_hand_from_earth = self._adjust_movement('hand',self.left_hand_from_earth,displacement)
        self.announce()

    def move_right_hand(self,displacement):
        self.right_hand_from_earth = self._adjust_movement('hand',self.right_hand_from_earth,displacement)
        self.announce()

    def announce(self):
        print('\n**********************')
        print('左手距离地面：{}厘米'.format(self.left_hand_from_earth))
        print('右手距离地面：{}厘米'.format(self.right_hand_from_earth))
        print('左脚距离地面：{}厘米'.format(self.left_foot_from_earth))
        print('右脚距离地面：{}厘米'.format(self.right_hand_from_earth))
        print('***********************\n')

    def dance(self):
        self.move_left_foot(14)
        self.move_right_foot(4)
        self.move_left_hand(20)
        self.move_right_hand(100)
        self.move_right_hand(-5)
        self.move_left_hand(-2)


#name__ == '__main__':
robot = Robot('瓦力')
robot.dance()



