from .base_classes import BaseCommand


class Canvas(BaseCommand):
    def create(self, w, h):
        """
        Create a new canvas of width w and height h.
        :param w: width (positive int)
        :param h: height (positive int)
        :return: list of str, that was added to the file in this step
        """
        template = []

        template.append('-'*(w+2))
        for height in range(h):
            template.append('|' + ' '*w + '|')
        template.append('-'*(w+2))

        self.file.write('\n'.join(template) + '\n')

        return template
