import io
from enum import Enum, auto
from PIL import Image

from core_rc.provider.SkinProvider import SkinProvider


class SkinService:
    class RendererType(Enum):
        BODY = auto()
        TEMPLATE = auto()
        HEAD = auto()

    @staticmethod
    def __getBody(img_template, slim):
        img_head = img_template.crop((8, 8, 16, 16))
        img_body = img_template.crop((20, 20, 28, 33))
        img_arm_left = img_template.crop((44, 20, 48 - int(slim), 32))
        img_arm_right = img_template.crop((36, 52, 40 - int(slim), 64))
        img_leg_left = img_template.crop((4, 20, 8, 33))
        img_leg_right = img_template.crop((20, 52, 24, 64))

        img_skin = Image.new('RGBA', (16, 32), color=(0, 0, 0, 0))
        img_skin.paste(img_head, (4, 0))
        img_skin.paste(img_body, (4, 8))
        img_skin.paste(img_arm_left, (int(slim), 8))
        img_skin.paste(img_arm_right, (12, 8))
        img_skin.paste(img_leg_left, (4, 20))
        img_skin.paste(img_leg_right, (8, 20))

        return img_skin

    @staticmethod
    def __getOuter(img_template, slim):
        img_outer_head = img_template.crop((40, 8, 48, 16))
        img_outer_body = img_template.crop((20, 36, 28, 48))
        img_outer_arm_left = img_template.crop((44, 36, 48 - int(slim), 48))
        img_outer_arm_right =img_template.crop((52, 52, 56 - int(slim), 64))
        img_outer_leg_left = img_template.crop((4, 36, 8, 48))
        img_outer_leg_right = img_template.crop((4, 52, 8, 64))

        img_outer = Image.new('RGBA', (16, 32), color=(0, 0, 0, 0))
        img_outer.paste(img_outer_head, (4, 0))
        img_outer.paste(img_outer_body, (4, 8))
        img_outer.paste(img_outer_arm_left, (int(slim), 8))
        img_outer.paste(img_outer_arm_right, (12, 8))
        img_outer.paste(img_outer_leg_left, (4, 20))
        img_outer.paste(img_outer_leg_right, (8, 20))

        return img_outer

    @staticmethod
    def __toPng(img):
        b = io.BytesIO()
        img.save(b, 'PNG')
        return b.getvalue()

    @staticmethod
    def __render_template(img_template, is_slim, outer):
        return SkinService.__toPng(img_template)

    @staticmethod
    def __render_body(img_template, is_slim, outer):
        img_skin = SkinService.__getBody(img_template, is_slim)

        if outer:
            img_outer = SkinService.__getOuter(img_template, is_slim)
            img_skin.paste(img_outer, (0, 0), img_outer)

        return SkinService.__toPng(img_skin)

    @staticmethod
    def __render_head(img_template, is_slim, outer):
        img_head = img_template.crop((8, 8, 16, 16))
        if outer:
            img_outer = img_template.crop((40, 8, 48, 16))
            img_head.paste(img_outer, (0, 0), img_outer)
        return SkinService.__toPng(img_head)

    RENDERER_TYPE = {
        RendererType.BODY: __render_body,
        RendererType.TEMPLATE: __render_template,
        RendererType.HEAD: __render_head,
    }

    @staticmethod
    def render(ref, renderer_type, outer=True, size=16):
        img_template, is_slim = SkinProvider.get_data(ref)
        renderer = SkinService.RENDERER_TYPE[renderer_type]

        img = renderer(img_template, is_slim, outer)
        if size > 16: img = img.resize((size, size * 2), Image.NEAREST)
        return SkinService.__toPng(img)
