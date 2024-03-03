from block import Block
import random

COLORS = ['white', 'yellow', 'green', 'blue', 'red', 'brown', 'orange', 'pink']

class BlockManager():

    def __init__(self, screen_width, screen_heigth, rows, blocks_per_row):
        super().__init__()
        self.all_blocks = []
        self.block_width = screen_width / blocks_per_row
        self.block_height = screen_heigth / 15
        self.row_y_positions = [(screen_heigth/2 - self.block_height * i) - screen_heigth/6 for i in range(rows)]
        self.x_positions = [(screen_width / blocks_per_row * i) - (screen_width / 2) + self.block_width/2 for i in range(blocks_per_row)]
        self.create_blocks()

    def create_random_colors(self):
        # return random hexadecimal color code
        return [f'#{random.randrange(256 ** 3):06x}' for num in range(len(self.row_y_positions))]


    def create_blocks(self):
        block_id = 0
        for color, y_pos in zip(self.create_random_colors(), self.row_y_positions):
            for x_pos in self.x_positions:
                new_block = Block(color, x_pos, y_pos, self.block_width, self.block_height, block_id)
                block_id += 1
                self.all_blocks.append(new_block)

    def delete_block(self, found_block):
        # filter destroyed block by id
        self.all_blocks = [block for block in self.all_blocks if found_block.id != block.id]
