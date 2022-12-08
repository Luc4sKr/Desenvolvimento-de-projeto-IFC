from scripts.constants import Constants as Const
from scripts.utils.draw_utils import Draw_util


class Game_utils:

    @staticmethod
    def dev_options(clock, screen):
        Draw_util.draw_text(screen, f"FPS: {clock.get_fps():.2f}", 12, Const.RED, 20, 100, topleft=True)

