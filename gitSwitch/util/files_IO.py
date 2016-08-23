from StringIO import StringIO


def get_file_object_like(file_path):
    return StringIO('\n'.join(line.strip() for line in open(file_path)))
