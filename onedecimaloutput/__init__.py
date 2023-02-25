import sys

class OneDecimalOutput:
    def __init__(self, stream):
        self.stream = stream
    
    def write(self, data):
        if isinstance(data, str):
            lines = data.split('\n')
            formatted_lines = [self._format_line(line) for line in lines]
            formatted_data = '\n'.join(formatted_lines)
            self.stream.write(formatted_data)
        else:
            self.stream.write(data)
    
    def _format_line(self, line):
        words = line.split()
        formatted_words = []
        for word in words:
            try:
                float_val = float(word)
                formatted_val = "{:.1f}".format(float_val)
                formatted_words.append(formatted_val)
            except ValueError:
                formatted_words.append(word)
        return ' '.join(formatted_words)

sys.stdout = OneDecimalOutput(sys.stdout)
sys.stderr = OneDecimalOutput(sys.stderr)
